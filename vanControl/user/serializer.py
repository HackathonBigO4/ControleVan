from django.contrib.auth.models import Group, User
from rest_framework import serializers
from user.models import PersonalInfo

class UserRouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
        ]

class PersonalInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalInfo
        fields = [
            'phone_number',
            'cpf',
            'user',
        ]
class UserSerializer(serializers.ModelSerializer):
    
    class Meta :
        model = User
        fields = [
            'id',
            'username',
            'email',
            'groups',
            'password',
        ]
        extra_kwargs = {'password': {'write_only': True}}
    

class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = [
            'id',
            'name'
        ]