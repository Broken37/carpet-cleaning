from django.urls import path, re_path
from . import views

urlpatterns = [
    path("list/", views.getCarpetCleanings, name="get-carpet-cleanings"),
    re_path(r"add-shop/", views.AddShopFormView.as_view(), name="add-shop"),
]
