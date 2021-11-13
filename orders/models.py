from django.db import models


class OrderStatus(models.IntegerChoices):
    waiting_for_response = 0, ("منتظر تایید قالیشویی")
    approved = 1, ("تایید شده")
    declined = 2, ("رد شده")
    received_from_client = 3, ("دریافت شده از مشتری")
    washing = 4, ("در حال شست و شو")
    delivering_to_client = 5, ("در حال تحویل به مشتری")
    delivered = 6, ("تحویل داده شده")


class Order(models.Model):
    pass
