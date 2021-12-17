from django.urls import path

from . import views

urlpatterns = [
    path("register/", views.RegisterFormView.as_view(), name="get-register-page"),
]
