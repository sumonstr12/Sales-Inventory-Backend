from django.contrib.auth.models import (
    AbstractBaseUser, 
    BaseUserManager,
    PermissionsMixin
)
from django.db import models

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            return ValueError("The Email Field must be set.")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        if extra_fields.get("is_staff") is not True:
            return  ValueError("SuperUser must here is_staff=True")
        if extra_fields.get("is_superuser") is not True:
            return  ValueError("SuperUser must here is_superuser=True")
        
        return self.create_user(email, password, **extra_fields)
        

    


class User(AbstractBaseUser, PermissionsMixin):
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    id = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=20)
    password = models.CharField(
        max_length=255
    ) # this field store Hashed password
    otp = models.CharField(max_length=6, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

