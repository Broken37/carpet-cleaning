from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Order



def example_view(request):
    template = loader.get_template("orders/example.html")
    context = {
        "test_list": list(range(5)),
    }
    return HttpResponse(template.render(context, request))
def register_page(request, carpet_cleaning_id):
    if request.method == "POST":
        number = request.POST.get("number")
        address = request.POST.get("address")
        print(number, address, carpet_cleaning_id)
        Order.objects.create(
            
        )
    return render(request, "orders/create.html", {})