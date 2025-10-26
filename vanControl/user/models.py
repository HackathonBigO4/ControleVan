from django.db import models
from django.contrib.auth.models import AbstractUser, Group

# Create your models here.
class User(AbstractUser):
    cpf = models.CharField(max_length=14, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)