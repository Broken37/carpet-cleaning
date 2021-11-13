from django.contrib import admin

from users.models import User

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "id", "phone_number")
    list_display_links = ("id", "phone_number", "last_name")
    search_fields = ("phone_number", "first_name", "last_name")


admin.site.register(User, UserAdmin)
