from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Order
from users.models import User
from users.models import CarpetCleaning

def register_page(request, carpet_cleaning_id):
    if request.method == "POST":
        number = request.POST.get("number")
        address = request.POST.get("address")
        Order.objects.create(
            carpet_count = number,
            address = address,
            customer = User.objects.first(),
            carpet_cleaning = CarpetCleaning.objects.get(pk = carpet_cleaning_id)
        )
    return render(request, "orders/create.html", {})
