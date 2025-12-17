from invoices.models import (
    Customer, Invoice, InvoiceItem, Product, User
)
from rest_framework import serializers


class RecentInvoiceSerializer(serializers.ModelSerializer):
    customer_name = serializers.CharField(source="customer.name")
    class Meta:
        model = Invoice
        fields = ["id", "customer_name", "payable", "created_at"]


class TopProductSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    product_name = serializers.CharField()
    sold_quantity = serializers.IntegerField()
    revenue = serializers.DecimalField(max_digits=12, decimal_places=2)


class SalesByCategorySerializer(serializers.Serializer):
    category_name = serializers.CharField()
    sales_count = serializers.IntegerField()
    total_amount = serializers.DecimalField(max_digits=12, decimal_places=2)

