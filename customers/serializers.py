

from .models import Customer
from rest_framework import serializers



class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = [
            "name",
            "email",
            "mobile",
            "created_at",
            "updated_at",
        ]


class CustomerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = [
            "id",
            "name",
            "email",
            "mobile"
        ]

        read_only_fields = ["id"]