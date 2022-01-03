from django.urls import path

from . import views

urlpatterns = [
    path("list/", views.getCarpetCleanings, name="get-carpet-cleanings"),
    path("add-shop/", views.AddShopFormView.as_view(), name="add-shop"),
    path("shop-page/<str:carpet_cleaning_id>", views.shop_page_view, name="shop_page")
]
