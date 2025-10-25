from django.db import models
from django.contrib.auth.models import Group, User 


class User(models.Model) :

    role = models.TextField(null=True, blank=True)
    password = models.TextField()
    name = models.TextField()
    email = models.TextField()

    def __str__(self):
        return f"{self.name}"