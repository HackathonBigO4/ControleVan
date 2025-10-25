from django.shortcuts import render
from rest_framework import permissions, viewsets
from user.serializer import GroupSerializer, UserSerializer
from django.contrib.auth.models import User, Group 

# Create your views here.

class UserViewSet(viewsets.ModelViewSet) :
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]
    


class GroupViewSet(viewsets.ModelViewSet) :
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.AllowAny]
