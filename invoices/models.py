from django.db import models
from customers.models import Customer
from products.models import Product

# Create your models here.

"""
Invoice model for the inventory system.
    "total":"100",
    "discount":"10",
    "vat":"10",
    "payable":"100",
    "customer_id":"2",
    "products":[
        {"product_id":6,"qty":1,"sale_price":"300"},
        {"product_id":6,"qty":1,"sale_price":"300"}
    ]
"""


class Invoice(models.Model):
    total = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2)
    vat = models.DecimalField(max_digits=10, decimal_places=2)
    payable = models.DecimalField(max_digits=10, decimal_places=2)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='InvoiceProduct')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class InvoiceProduct(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    sale_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.product.name} - {self.quantity} @ {self.sale_price}"