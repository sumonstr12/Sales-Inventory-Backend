

from rest_framework import serializers
from .models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'user', 'name', 'created_at', 'updated_at']
        read_only_fields = ['id', 'user', 'created_at', 'updated_at']