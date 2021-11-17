from django.contrib import admin

from orders.models import Order, OrderStatus
from users.models import CarpetCleaning, UserType


class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "customer", "carpet_cleaning", "status")
    list_display_links = ("id",)
    list_filter = ("status",)
    actions = ["wait_for_response_status", "approve_status", "decline_status", "received_from_client_status"]

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if not self.has_view_or_change_permission(request):
            queryset = queryset.none()
        if request.user.user_type == UserType.carpet_cleaning_owner:
            # current user's carpet cleaning
            carpet_cleaning = CarpetCleaning.objects.filter(owner=request.user)
            queryset = queryset.filter(carpet_cleaning__id__in=carpet_cleaning)

        return queryset
    
    @admin.action(description=f'Mark selected orders as {OrderStatus.labels[OrderStatus.waiting_for_response]}')
    def wait_for_response_status(self, request, queryset):
        queryset.update(status=OrderStatus.waiting_for_response)
    
    @admin.action(description=f'Mark selected orders as {OrderStatus.labels[OrderStatus.approved]}')
    def approve_status(self, request, queryset):
        queryset.update(status=OrderStatus.approved)
    
    @admin.action(description=f'Mark selected orders as {OrderStatus.labels[OrderStatus.declined]}')
    def decline_status(self, request, queryset):
        queryset.update(status=OrderStatus.declined)

    @admin.action(description=f'Mark selected orders as {OrderStatus.labels[OrderStatus.received_from_client]}')
    def received_from_client_status(self, request, queryset):
        queryset.update(status=OrderStatus.received_from_client)
    

    


admin.site.register(Order, OrderAdmin)
