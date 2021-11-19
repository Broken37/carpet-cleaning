from django.urls import path
from . import views

urlpatterns = [
    path("carpetCleanings/", views.getCarpetCleanings, name="get-carpet-cleanings"),
]
