import datetime

from django.db import models

from users.models import User


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

    name = models.CharField(null=False, blank=False,
                            max_length=50, default="No name")

    owner = models.OneToOneField(
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
