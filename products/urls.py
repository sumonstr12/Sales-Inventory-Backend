
from django.urls import path
from .views import (
    ProductsCreateView,
    ProductUpdateView,
    ProductDeleteView,
    ProductListIDView,
    ProductListView,
)



urlpatterns = [
    path("create-product", ProductsCreateView.as_view(), name="product-create"),
    path("update-product", ProductUpdateView.as_view(), name="product-update"),
    path("delete-product", ProductDeleteView.as_view(), name="product-delete"),
    path("product-by-id", ProductListIDView.as_view(), name="product-by-id"),
    path("list-product", ProductListView.as_view(), name="product-list"),
]

