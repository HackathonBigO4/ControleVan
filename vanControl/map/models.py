from django.db import models
from user.models import User

# Create your models here.

class Route(models.Model):
    driver_id = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    attendance_list = models.ManyToManyField(User,related_name='attendance_list',through='AttendanceList',blank=True)
    starting_latitude = models.FloatField(null=True,blank=True)
    starting_longitude = models.FloatField(null=True,blank=True)
    final_latitude = models.FloatField(null=True,blank=True)
    final_longitude = models.FloatField(null=True,blank=True)
    starting_time = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    final_time = models.DateTimeField(null=True,blank=True)
    total_time = models.DurationField(null=True,blank=True)

class AttendanceList(models.Model):
    route = models.ForeignKey(Route, on_delete=models.SET_NULL,null=True,blank=True)
    passenger = models.ForeignKey(User, on_delete=models.SET_NULL,null=True,blank=True)
    attended = models.BooleanField(default=False)

# VIAGEM
# id motorista

# array id attendance_list(array de passengers) - Anterior ao inicio
# array id attended_passengers(array de passengers) - Durante

# Lat inicial - Inicial
# Long inicial - Inicial

# Lat Final - Final
# Long Final - Final

# hora_inicio - Inicial
# hora_fim - Final
# tempo_total - Final