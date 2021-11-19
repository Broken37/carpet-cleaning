from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
from django.core.validators import RegexValidator
import datetime


class UserType(models.IntegerChoices):
    """
    A class used to represent user types in system (admin, customer, carpet_cleaning_owner)

    """

    admin = 0, ("مدیر")
    customer = 1, ("مشتری")
    carpet_cleaning_owner = 2, ("صاحب قالیشویی")


class User(AbstractUser):
    """
    A class used for representing different users in system

    Parameters
    -------
    phone_regex: String
        regex to validate user's phone number
    phone_number: String
        user's phone number
    user_type: UserType
    """

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
    """
    A class for Representing a Carpet cleaning entity of the system

    Parameters
    -------
    name: String
        the name of the carpet cleaning
    owner: User
        the owner of the carpet cleaning (user of type carpet_cleaning_owner)
    opens_at: Date
        the time when the carpet cleaning opens in day
    closes_at: Date
        the time when the carpet cleaning closes in day
    address: String
        the address of the carpet cleaning
    latitude: float
    longitude: float
    delivery_cost: Int
        cost of delivering carpets to carpet cleaning (Toman)
    """

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
