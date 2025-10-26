from chat.models import Message
from rest_framework import serializers

class MessageSerializer(serializers.ModelSerializer):

    class Meta :
        model = Message
        fields = [
            'id',
            'content',
            'sender',
            'receiver',
            'send_date',
        ]
        read_only_fields = ['id', 'send_date']
