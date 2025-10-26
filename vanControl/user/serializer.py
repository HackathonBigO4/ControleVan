from django.contrib.auth.models import Group
from rest_framework import serializers
from user.models import User

class UserRouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
        ]
class UserSerializer(serializers.ModelSerializer):
    
    class Meta :
        model = User
        fields = [
            'id',
            'username',
            'cpf',
            'password',
            'email',
            'groups',
            'phone_number',
        ]
        extra_kwargs = {'password': {'write_only': True}}
    

class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = [
            'id',
            'name'
        ]