from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from user import views 

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'group', views.GroupViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)), 
]

