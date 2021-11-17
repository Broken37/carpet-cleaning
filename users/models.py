from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
from django.core.validators import RegexValidator
import datetime


class UserType(models.IntegerChoices):
    admin = 0, ("مدیر")
    customer = 1, ("مشتری")
    carpet_cleaning_owner = 2, ("صاحب قالیشویی")


class User(AbstractUser):
    phone_regex = RegexValidator(
        regex=r"^(09)\d{9}$",
        message="phone_number format: 09xxxxxxxxx",
    )
    phone_number = models.CharField(
        validators=[phone_regex], max_length=11, null=False, blank=False, unique=True
    )
    user_type = models.IntegerField(
        blank=False, choices=UserType.choices, default=UserType.admin
    )


class CarpetCleaning(models.Model):
    name = models.CharField(null=False, blank=False, max_length=50, default="No name")

    owner = models.ForeignKey(
        null=True,
        blank=False,
        to=User,
        on_delete=models.CASCADE,
        related_name="carpet_cleaning",
    )

    opens_at = models.TimeField(
        blank=False, null=False, default=datetime.time(12, 0, 0)
    )
    closes_at = models.TimeField(
        blank=False, null=False, default=datetime.time(23, 59, 59)
    )

    address = models.CharField(max_length=255, default="No address")

    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)

    delivery_cost = models.IntegerField(default=0, null=False, blank=False)

    def __str__(self) -> str:
        return self.name
