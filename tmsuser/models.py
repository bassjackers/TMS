from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class Account(AbstractBaseUser):
    username = models.CharField(max_length=30, default="", unique=True)
    email = models.EmailField(max_length=255, default="", unique=True)
    password = models.CharField(max_length=64)
    created_dttm = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email
