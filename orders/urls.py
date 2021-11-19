from django.urls import path
from . import views

urlpatterns = [
    path("order/<str:carpet_cleaning_id>", views.register_page, name="register_page")
]
