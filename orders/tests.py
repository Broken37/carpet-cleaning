from django.test import TestCase
from CarpetShops.models import CarpetCleaning
from orders.models import Order

from users.models import User
from django.urls import reverse
import random


# TODO: Change this test after implementation of authentication
class OrderTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create()
        self.carpet_cleaning = CarpetCleaning.objects.create()

    def test_create_order(self):
        url = reverse(
            "register_page", kwargs={"carpet_cleaning_id": self.carpet_cleaning.id}
        )

        carpet_count = random.randint(1, 20)
        addr = "Tehran, Sharif, ..."
        self.client.post(
            url,
            data={
                "number": carpet_count,
                "address": addr,
            },
        )

        order = Order.objects.first()
        self.assertEqual(order.carpet_count, carpet_count)
        self.assertEqual(order.address, addr)
