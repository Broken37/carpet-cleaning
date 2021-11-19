from django.shortcuts import render

from CarpetShops.models import CarpetCleaning
from .models import Order
from users.models import User


def order_view(request, carpet_cleaning_id):
    """
    View to handle creating orders

        Parameters
        ----------
        carpet_cleaning_id : Int
            id of the carpet cleaning for which order should be created

    """

    if request.method == "POST":
        number = request.POST.get("number")
        address = request.POST.get("address")
        # TODO: error handling when carpet cleaning is not present
        Order.objects.create(
            carpet_count=number,
            address=address,
            customer=User.objects.first(),
            carpet_cleaning=CarpetCleaning.objects.get(pk=carpet_cleaning_id),
        )
        return render(request, "orders/createOrder.html", {"done": True})
    return render(request, "orders/createOrder.html", {"done": False})
