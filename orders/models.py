from django.db import models

from users.models import CarpetCleaning, User


class OrderStatus(models.IntegerChoices):
    waiting_for_response = 0, ("منتظر تایید قالیشویی")
    approved = 1, ("تایید شده")
    declined = 2, ("رد شده")
    received_from_client = 3, ("دریافت شده از مشتری")
    washing = 4, ("در حال شست و شو")
    delivering_to_client = 5, ("در حال تحویل به مشتری")
    delivered = 6, ("تحویل داده شده")


class Order(models.Model):
    customer = models.ForeignKey(
        null=True, blank=False, to=User, on_delete=models.CASCADE, related_name="orders"
    )

    carpet_cleaning = models.ForeignKey(
        null=True,
        blank=False,
        to=CarpetCleaning,
        on_delete=models.CASCADE,
        related_name="orders",
    )

    status = models.IntegerField(
        blank=False,
        null=False,
        choices=OrderStatus.choices,
        default=OrderStatus.waiting_for_response,
    )

    created_at = models.DateTimeField(blank=False, null=False, auto_now=True)

    carpet_count = models.IntegerField(blank=False, null=False, default=1)

    recieved_at = models.DateTimeField(
        null=True, blank=True
    )  # Recieved by carpet cleaning
    delivered_at = models.DateTimeField(null=True, blank=True)  # delivered to customer

    address = models.TextField(blank=False, null=False, default="no-address")
