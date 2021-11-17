from django.contrib import admin

from orders.models import Order, OrderStatus
from users.models import CarpetCleaning, UserType


class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "customer", "carpet_cleaning", "status")
    list_display_links = ("id",)
    list_filter = ("status",)
    actions = ["approve_status"]

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if not self.has_view_or_change_permission(request):
            queryset = queryset.none()
        if request.user.user_type == UserType.carpet_cleaning_owner:
            # current user's carpet cleaning
            carpet_cleaning = CarpetCleaning.objects.filter(owner=request.user)
            queryset = queryset.filter(carpet_cleaning__id__in=carpet_cleaning)

        return queryset
    
    @admin.action(description=f'Mark selected orders as {OrderStatus.labels[OrderStatus.approved]}')
    def approve_status(self, request, queryset):
        queryset.update(status=OrderStatus.approved)
    


admin.site.register(Order, OrderAdmin)
