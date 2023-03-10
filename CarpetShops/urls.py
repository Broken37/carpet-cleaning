from django.urls import path
from .views import CarpetCleaningAllReviews, shop_page_view, AddShopFormView, getCarpetCleanings, comment, makeComment

urlpatterns = [
    path("carpet_cleaning/list", getCarpetCleanings, name="get-carpet-cleanings"),
    path("carpet_cleaning/add-shop", AddShopFormView.as_view(), name="add-shop"),
    path("carpet_cleaning/<int:carpet_cleaning_id>/shop_page", shop_page_view, name="shop_page"),
    path("carpet_cleaning/<int:carpet_cleaning_id>/reviews", CarpetCleaningAllReviews.as_view(), name="review"),
    path("carpet_cleaning/<int:carpet_cleaning_id>/comment", comment, name="comment"),
    path("carpet_cleaning/<int:carpet_cleaning_id>/make_comment", makeComment, name="make_comment"),
]
