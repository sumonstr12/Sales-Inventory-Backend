


from rest_framework import serializers
from .models import Invoice, InvoiceProduct
from customers.serializers import CustomerSerializer
from products.serializers import ProductSerializer
from products.models import Product
from customers.models import Customer
from .models import InvoiceProduct


class InvoiceItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(
        source='product', queryset=Product.objects.all(), write_only=True
    )

    class Meta:
        model = Invoice
