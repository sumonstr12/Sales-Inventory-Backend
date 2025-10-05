

from rest_framework import serializers
from .models import Product



class ProductSerializer(serializers.ModelSerializer):
    user_name = serializers.SerializerMethodField()
    category_name = serializers.CharField(source='category.name', read_only=True)
    user_id = serializers.IntegerField(source='category.user.id', read_only=True)

    class Meta:
        model = Product
        fields = [
            "id",
            "category",
            "name",
            "price",
            "unit",
            "img_url",
            "created_at",
            "updated_at",
            "user_id",
            "user_name",
            "category_name",
        ]
        read_only_fields = ["id", "user", "created_at", "updated_at"]

    
    def get_user_name(self, obj):
        user = obj.category.user
        return f"{user.firstName} {user.lastName}" if user else "Unknown User"