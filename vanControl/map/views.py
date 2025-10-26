from rest_framework import permissions, viewsets
from map.serializer import RouteSerializer
from map.models import Route

# Create your views here.

class RouteViewSet(viewsets.ModelViewSet) :
    queryset = Route.objects.all()
    serializer_class = RouteSerializer
    permission_classes = [permissions.AllowAny]