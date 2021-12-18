from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path("register/", views.RegisterFormView.as_view(), name="get-register-page"),
]
