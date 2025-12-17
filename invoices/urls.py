

from django.urls import path
from .views import (
    InvoiceCreateView,
    InvoiceDeleteView,
    InvoiceDetailView,
    InvoiceSelectView
)

urlpatterns = [
    path("invoice-create", InvoiceCreateView.as_view(), name="create-invoice"),
    path("invoice-delete", InvoiceDeleteView.as_view(), name="delete-invoice"),
    path("invoice-details", InvoiceDetailView.as_view(), name="detials-invoice"),
    path("invoice-select", InvoiceSelectView.as_view(), name="select-invoice")
    
]


