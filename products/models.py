from django.db import models
from categories.models import Category
from django.contrib.auth import get_user_model


# Create your models here.


"""
Product model for the inventory system.
    "name": "Demo",
    "price": "Demo",
    "unit": "Demo",
    "img_url": "uploads/1-1734351321-system_desing.png",
    "category_id": "1",
    "user_id": "1",
    "updated_at": "2024-12-16T12:15:21.000000Z",
    "created_at": "2024-12-16T12:15:21.000000Z",
    "id": 54
"""


User = get_user_model()  # This will use the custom User model defined in users/models.py


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.CharField(max_length=100)
    img_url = models.ImageField(upload_to="uploads/")
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name