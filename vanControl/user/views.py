from django.shortcuts import render
from rest_framework import permissions, viewsets
from user.serializer import GroupSerializer, UserSerializer, PersonalInfoSerializer
from django.contrib.auth.models import User, Group 
from user.models import User, PersonalInfo
# Create your views here.

class UserViewSet(viewsets.ModelViewSet) :
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]
    
class PersonalInfoViewSet(viewsets.ModelViewSet) :
    queryset = PersonalInfo.objects.all()
    serializer_class = PersonalInfoSerializer
    permission_classes = [permissions.AllowAny]


class GroupViewSet(viewsets.ModelViewSet) :
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.AllowAny]
