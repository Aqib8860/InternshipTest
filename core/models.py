from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from .managers import UserManager

# Create your models here.



GENDER = (
    ("Male", "Male"),
    ("Female", "Female"),
    ("Other", "Other"),
)


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=10, null=True, blank=True)
    email = models.EmailField(unique=True)
    fullname = models.CharField(max_length=60, null=True)
    state = models.TextField(max_length=200, null=True)
    country = models.CharField(max_length=100, null=True)
    pincode = models.IntegerField(null=True)
    gender = models.CharField(max_length=12, choices=GENDER)
    is_staff = models.BooleanField(default=False)
    objects = UserManager()

    USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['first_name', 'last_name']
