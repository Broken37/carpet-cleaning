from django.contrib import admin

from users.models import CarpetCleaning, User, UserType
from django.contrib.auth.models import Group, Permission

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "id", "phone_number", "user_type")
    list_display_links = ("id", "phone_number", "last_name", "first_name")
    search_fields = ("phone_number", "first_name", "last_name")

    def save_model(self, request, obj, form, change) -> None:
        if obj.user_type == UserType.carpet_cleaning_owner:
            obj.is_staff = True
            group = Group.objects.filter(name="CarpetOwners")
            if len(group) == 0:
                group = UserAdmin.createCarpetOwnersGroup()
            else:
                group = group.first()

        return super().save_model(request, obj, form, change)

    @staticmethod
    def createCarpetOwnersGroup():
        permissions = Permission.objects.filter(content_type__model__contains="order")
        group = Group.objects.create(name="CarpetOwners")
        group.permissions.set(permissions)
        return group


class CarpetCleaningAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "owner", "opens_at", "closes_at")
    list_display_links = ("id", "name")
    search_fields = ("name",)


admin.site.register(User, UserAdmin)
admin.site.register(CarpetCleaning, CarpetCleaningAdmin)
