

from django.urls import path
from .views import (
    CustomerCreateView,
    CustomerUpdateView,
    CustomerDeleteView,
    CustomerListView
)

urlpatterns = [
    path("create-customer", CustomerCreateView.as_view(), name="customer-create"),
    path("update-customer", CustomerUpdateView.as_view(), name="customer-update"),
    path("delete-customer", CustomerDeleteView.as_view(), name="customer-delete"),
    path("list-customer", CustomerListView.as_view(), name="customer-list"),
]