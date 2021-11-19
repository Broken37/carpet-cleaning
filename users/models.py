from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


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
