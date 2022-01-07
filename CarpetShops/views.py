from datetime import datetime

from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from CarpetShops.forms import *
from CarpetShops.models import CarpetCleaning, Review
from CarpetShops.serializers import ReviewSerializer
from users.models import User, UserType
from orders.models import Order, OrderStatus


def getCarpetCleanings(request, **kwargs):
    current_time = datetime.now().time()
    open_status = request.GET.get('open_status')
    if open_status == "open":
        carpets = CarpetCleaning.objects.filter(
            opens_at__lte=current_time, closes_at__gte=current_time)
    elif open_status == "close":
        carpets = CarpetCleaning.objects.filter(
            Q(opens_at__gt=current_time) | Q(closes_at__lt=current_time))
    else:
        carpets = CarpetCleaning.objects.all()

    name_filter = request.GET.get('name', '')
    if name_filter:
        carpets = carpets.filter(name__contains=name_filter)

    sort_by = request.GET.get('sort_by')
    if sort_by == 'rating':
        carpets = carpets.order_by('-rating')
    elif sort_by == 'name':
        carpets = carpets.order_by('name')

    context = {"carpetcleanings": carpets,
               'name_filter': name_filter, 'open_status': open_status, 'sort_by':sort_by}
    context.update(**kwargs)
    return render(request, "CarpetShops/carpetcleanings.html", context)


class AddShopFormView(FormView):
    template_name = 'CarpetShops/addShop.html'
    form_class = RegisterForm
    success_url = 'CarpetShops/carpetcleanings.html'

    def form_valid(self, form):
        owner_username = form.cleaned_data['owner_username']
        name = form.cleaned_data['name']
        opens_at = form.cleaned_data['opens_at']
        closes_at = form.cleaned_data['closes_at']
        address = form.cleaned_data['address']
        latitude = form.cleaned_data['latitude']
        longitude = form.cleaned_data['longitude']
        delivery_cost = form.cleaned_data['delivery_cost']
        owner = User.objects.filter(username=owner_username)

        if not owner:
            return render(self.request, self.template_name, {"message": "please register first!"})
        elif owner[0].user_type != UserType.carpet_cleaning_owner:
            return render(self.request, self.template_name, {"message": "only carpet owners can add a shop!"})

        shops = CarpetCleaning.objects.filter(owner=owner[0])
        if shops:
            return redirect("get-carpet-cleanings")
        else:
            shop = CarpetCleaning(name=name, opens_at=opens_at, closes_at=closes_at, address=address,
                                  latitude=latitude, longitude=longitude, delivery_cost=delivery_cost,
                                  owner=owner[0])
            shop.save()
            return redirect("get-carpet-cleanings")


def shop_page_view(request, carpet_cleaning_id):
    carpet_cleaning = CarpetCleaning.objects.get(pk=carpet_cleaning_id)
    context = {'shop': carpet_cleaning}
    if request.user.is_authenticated:
        username = request.user.username
        customer_previous_orders = Order.objects.filter(carpet_cleaning_id=carpet_cleaning_id,
                                                        customer__username=username,
                                                        status=OrderStatus.delivered)
        if customer_previous_orders:
            context["user_has_ordered_from_this_shop"] = True
    return render(request, "CarpetShops/shopPage.html", context)


def comment(request, carpet_cleaning_id):
    if request.user.is_authenticated:
        username = request.user.username
        customer_previous_orders = Order.objects.filter(carpet_cleaning_id=carpet_cleaning_id,
                                                        customer__username=username,
                                                        status=OrderStatus.delivered)
    if customer_previous_orders:
        carpet_cleaning = CarpetCleaning.objects.get(pk=carpet_cleaning_id)
        context = {"shop": carpet_cleaning,}

        return render(request, "CarpetShops/comment.html",context)

    else :
        return redirect('shop_page', carpet_cleaning_id = carpet_cleaning_id)


def makeComment(request, carpet_cleaning_id):
    carpet_cleaning = CarpetCleaning.objects.get(pk=carpet_cleaning_id)
    if request.user.is_authenticated:
        username = request.user.username
        customer_previous_orders = Order.objects.filter(carpet_cleaning_id=carpet_cleaning_id,
                                                        customer__username=username,
                                                        status=OrderStatus.delivered)
    if customer_previous_orders:
        print(request.POST)
        rate = float(request.POST['rate'])
        text = request.POST['text']
        carpet_cleaning.rating = (carpet_cleaning.rating * carpet_cleaning.number_of_voters + rate) / (carpet_cleaning.number_of_voters + 1) 
        carpet_cleaning.number_of_voters = carpet_cleaning.number_of_voters + 1 
        new_comment = Review(user = request.user, carpet_cleaning = carpet_cleaning, rate = rate, comment = text, created_at = datetime.now())
        new_comment.save()
        carpet_cleaning.save()
    return redirect('shop_page', carpet_cleaning_id = carpet_cleaning_id)



class ReviewsPagination(PageNumberPagination):
    page_size = 10
    result_key = 'comments'

    def get_paginated_response(self, data, **kwargs):
        return Response({
            self.result_key: data,
            'pagination': {
                'page': self.page.number,
                'next_page': self.page.number + 1 if self.page.has_next() else None,
                'prev_page': self.page.number - 1 if self.page.has_previous() else None,
                'total_pages': self.page.paginator.num_pages,
                'page_size': self.page.paginator.per_page,
            },
            **kwargs,
        })


class CarpetCleaningAllReviews(ListAPIView):
    pagination_class = ReviewsPagination

    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.filter(carpet_cleaning=self.carpet_cleaning, comment__isnull=False)

    def list(self, request, carpet_cleaning_id, *args, **kwargs):
        self.carpet_cleaning = CarpetCleaning.objects.get(pk=carpet_cleaning_id)
        return super().list(request, carpet_cleaning_id, *args, **kwargs)
