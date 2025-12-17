from rest_framework import serializers
from .models import Invoice, InvoiceItem
from customers.serializers import CustomerSerializer
from products.serializers import ProductSerializer
from products.models import Product
from customers.models import Customer
from users.models import User
from decimal import Decimal
class InvoiceItemSerializer(serializers.ModelSerializer):
    product_id = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), source='product')
   
    class Meta:
        model = InvoiceItem
        fields = ['product_id', 'quantity', 'sale_price'] 

class InvoiceItemReadSerializer(serializers.ModelSerializer):
    products = ProductSerializer(read_only=True)
    class Meta:
        model = InvoiceItem
        fields = "__all__"
class InvoiceSerializer(serializers.ModelSerializer):
    products = serializers.ListField(
        child=InvoiceItemSerializer(many=False),
        write_only=True  
    )

    customer_id = serializers.PrimaryKeyRelatedField(queryset=Customer.objects.all(), source='customer')

    class Meta:
        model = Invoice
        fields = ['total', 'discount', 'vat', 'payable', 'customer_id', 'products']
        read_only_fields = [ 'created_at', 'updated_at'] 
    
    def create(self, validated_data):
        # print("Validated data", validated_data) 
        
        products_data = validated_data.pop('products')
        invoice = Invoice.objects.create(**validated_data)
        
        for product_dict in products_data:
            # print("Product", product_dict) 
            item_data = {
                **product_dict,  
                'invoice': invoice,
            }
            print("Item data after add:", item_data) 
            InvoiceItem.objects.create(**item_data)
        
        return invoice

    def validate(self, data):
        total = data.get('total', Decimal('0'))
        discount = data.get('discount', Decimal('0'))
        vat = data.get('vat', Decimal('0'))
        expected_payable = total - discount + vat
        if data.get('payable') != expected_payable:
            raise serializers.ValidationError("Payable must be total - discount + vat")
        return data
    

class InvoiceDetailSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(read_only=True)
    product = InvoiceItemReadSerializer(
        source="invoice_items",
        read_only=True,
        many=True
    )

    class Meta:
        model = Invoice
        fields = "__all__"


class InvoiceSelectSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(read_only=True)
    class Meta:
        model = Invoice
        fields = [
            "id",
            "total",
            "discount",
            "vat",
            "payable",
            "customer_id",
            "customer"
        ]