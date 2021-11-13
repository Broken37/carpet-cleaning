from django.contrib import admin

from users.models import CarpetCleaning, User

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "id", "phone_number", "user_type")
    list_display_links = ("id", "phone_number", "last_name", "first_name")
    search_fields = ("phone_number", "first_name", "last_name")


class CarpetCleaningAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "owner", "opens_at", "closes_at")
    list_display_links = ("id", "name")
    search_fields = ("name", )


admin.site.register(User, UserAdmin)
admin.site.register(CarpetCleaning, CarpetCleaningAdmin)