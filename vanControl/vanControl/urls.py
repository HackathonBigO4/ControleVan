from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from user import views 
from chat.views import MessageViewSet
from map.views import RouteViewSet

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'messages', MessageViewSet)
router.register(r'routes', RouteViewSet)
router.register(r'personalinfo', views.PersonalInfoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)), 
]

