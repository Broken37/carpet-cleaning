from django.urls import path
from . import views

urlpatterns = [
    path("order/<str:carpet_cleaning_id>",
         views.order_view, name="register_page")
]
