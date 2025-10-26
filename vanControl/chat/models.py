from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Message(models.Model):
    content = models.TextField()
    sender = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    receiver = models.ForeignKey(User, on_delete=models.SET_NULL,related_name='received_messages', null=True, blank=True)
    send_date = models.DateTimeField(auto_now_add=True)