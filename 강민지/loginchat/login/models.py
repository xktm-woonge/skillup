from django.db import models
from django.contrib.auth.models import AbstractUser

class Users(AbstractUser):
    name = models.CharField(max_length=30)