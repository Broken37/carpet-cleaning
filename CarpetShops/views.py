from datetime import datetime

from django.shortcuts import render

from CarpetShops.models import CarpetCleaning


# Create your views here.
def getCarpetCleanings(request):
    carpets = CarpetCleaning.objects.all()

    name_filter = request.GET.get('name', '')
    if name_filter:
        carpets = carpets.filter(name__contains=name_filter)

    context = {"carpetcleanings": carpets, 'name_filter': name_filter}
    return render(request, "CarpetShops/carpetcleanings.html", context)
