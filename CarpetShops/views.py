from datetime import datetime

from django.db.models import Q
from django.shortcuts import render

from CarpetShops.models import CarpetCleaning


def getCarpetCleanings(request):
    current_time = datetime.now().time()
    carpets = None
    open_status = request.GET.get('open_status', 'none')
    if open_status == "none":
        carpets = CarpetCleaning.objects.all()
    elif open_status == "open":
        carpets = CarpetCleaning.objects.filter(opens_at__lte=current_time, closes_at__gte=current_time)
    elif open_status == "close":
        carpets = CarpetCleaning.objects.filter(Q(opens_at__gt=current_time) | Q(closes_at__lt=current_time))

    name_filter = request.GET.get('name', '')
    if name_filter:
        carpets = carpets.filter(name__contains=name_filter)

    context = {"carpetcleanings": carpets, 'name_filter': name_filter, 'open_status': open_status}
    return render(request, "CarpetShops/carpetcleanings.html", context)
