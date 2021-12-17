from django.contrib import admin

from CarpetShops.models import CarpetCleaning


class CarpetCleaningAdmin(admin.ModelAdmin):
    """
    A class used for django admin representation of CarpetCleaning model
    """

    list_display = ("id", "name", "owner", "opens_at", "closes_at")
    list_display_links = ("id", "name")
    search_fields = ("name",)


admin.site.register(CarpetCleaning, CarpetCleaningAdmin)
