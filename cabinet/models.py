from django.db import models
from django.contrib.auth.models import AbstractUser


class Person(AbstractUser):
    avatar = models.ImageField(upload_to='avatar/%Y-%m-%d/')
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=30, editable=False, unique=True)
    email = models.EmailField(max_length=50, blank=True)
    password = models.CharField(max_length=30)
    birth_date = models.DateField(default=None, blank=True, null=True)
    description = models.TextField(default='')
    city = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    is_premium = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
