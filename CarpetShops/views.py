from datetime import datetime

from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.generic.edit import FormView

from CarpetShops.forms import *
from CarpetShops.models import CarpetCleaning
from users.models import User, UserType


def getCarpetCleanings(request, **kwargs):
    current_time = datetime.now().time()
    carpets = None
    open_status = request.GET.get('open_status', 'none')
    if open_status == "none":
        carpets = CarpetCleaning.objects.all()
    elif open_status == "open":
        carpets = CarpetCleaning.objects.filter(
            opens_at__lte=current_time, closes_at__gte=current_time)
    elif open_status == "close":
        carpets = CarpetCleaning.objects.filter(
            Q(opens_at__gt=current_time) | Q(closes_at__lt=current_time))

    name_filter = request.GET.get('name', '')
    if name_filter:
        carpets = carpets.filter(name__contains=name_filter)

    context = {"carpetcleanings": carpets,
               'name_filter': name_filter, 'open_status': open_status}
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
