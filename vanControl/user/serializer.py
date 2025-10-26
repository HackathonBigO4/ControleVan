from django.contrib.auth.models import Group, User
from rest_framework import serializers
from user.models import PersonalInfo

class UserSerializer(serializers.ModelSerializer):
    personal_info = serializers.SerializerMethodField()

    def get_personal_info(self, obj):
        personal_info = PersonalInfo.objects.filter(user=obj).first()
        return personal_info if personal_info else None
    
    class Meta :
        model = User
        fields = [
            'id',
            'username',
            'email',
            'groups',
            'password',
            'personal_info', 
        ]
        extra_kwargs = {'password': {'write_only': True}}
      

        

class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = [
            'id',
            'name'
        ]