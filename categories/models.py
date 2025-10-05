from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()  # This will use the custom User model defined in users/models.py

# Create your models here.

class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.RESTRICT)
    name = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name