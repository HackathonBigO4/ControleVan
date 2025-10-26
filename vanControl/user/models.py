from django.db import models
from django.contrib.auth.models import User, Group

# Create your models here.
class PersonalInfo(models.Model):
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    cpf = models.CharField(max_length=14, blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True,blank=True)