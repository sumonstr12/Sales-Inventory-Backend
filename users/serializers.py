
from rest_framework import serializers
from .models import User


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "firstName",
            "lastName",
            "email",
            "password",
            "mobile",
        ]

    def create(self, validated_data):

        # way -1 
        user = User(
            firstName = validated_data["firstName"],
            lastName = validated_data["lastName"],
            email = validated_data["email"],
            mobile = validated_data["mobile"],
        )
        user.set_password(validated_data["password"])
        user.save()


        # # way -2
        # user = User.objects.create_user(
        #     firstName = validated_data["fisrtName"],
        #     lastName = validated_data["lastName"],
        #     email = validated_data["email"],
        #     mobile = validated_data["mobile"],
        #     password = validated_data["password"],
        # )


        # way -3
        # (May be it has some problem)
        # user = User.objects.create_user(**validated_data)

        return user
    

class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["firstName", "lastName", "email", "mobile", "password"]
        extra_kwargs = {
            'password': {'write_only': True, 'required': False}  # Make password optional
        }

    def update(self, instance, validated_data):
        # Update regular fields
        instance.firstName = validated_data.get('firstName', instance.firstName)
        instance.lastName = validated_data.get('lastName', instance.lastName)
        instance.email = validated_data.get('email', instance.email)
        instance.mobile = validated_data.get('mobile', instance.mobile)

        # Handle password separately if provided
        password = validated_data.get('password')
        if password:
            instance.set_password(password)

        instance.save()
        return instance
    

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["firstName", "lastName", "email", "mobile"]
        read_only_fields = ["email"]
    