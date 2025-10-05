from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()  # This will use the custom User model defined in users/models.py


class Customer(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE
    )
    name = models.CharField(max_length=255)
    email = models.EmailField()
    mobile = models.CharField(max_length=20, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.name} ({self.email})"