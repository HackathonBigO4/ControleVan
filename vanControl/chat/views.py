from rest_framework import permissions, viewsets
from chat.serializer import MessageSerializer
from chat.models import Message

# Create your views here.

class MessageViewSet(viewsets.ModelViewSet) :
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [permissions.AllowAny]