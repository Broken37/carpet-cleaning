from django.contrib import admin

from orders.models import Order

# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "customer", "carpet_cleaning", "status")
    list_display_links = ("id", )
    search_fields = ("status", )


admin.site.register(Order, OrderAdmin)