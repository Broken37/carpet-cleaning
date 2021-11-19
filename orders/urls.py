from django.urls import path
from . import views

urlpatterns = [
    path("test/", views.example_view, name="example_view"),
    path("register/", views.register_page, name="register_page")
]
