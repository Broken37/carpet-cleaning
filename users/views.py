from django.shortcuts import render
from .models import CarpetCleaning

# Create your views here.
def getCarpetCleanings(request):
    carpets = CarpetCleaning.objects.all()
    context = {"carpetcleanings": carpets}
    return render(request, "users/carpetcleanings.html", context)