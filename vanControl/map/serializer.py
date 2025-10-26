from map.models import Route, AttendanceList
from user.models import User
from rest_framework import serializers
from user.serializer import UserSerializer


class AttendanceListSerializer(serializers.ModelSerializer):
    passenger = UserSerializer(read_only=True)
    passenger_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        source='passenger',
        write_only=True
    )

    class Meta:
        model = AttendanceList
        fields = ['id', 'passenger', 'passenger_id', 'attended']


class RouteSerializer(serializers.ModelSerializer):
    driver = UserSerializer(source='driver_id', read_only=True)
    attendance_list_detail = AttendanceListSerializer(
        source='attendancelist_set', many=True,)
    attendance_list = AttendanceListSerializer(
        source='attendancelist_set', many=True)

    class Meta:
        model = Route
        fields = [
            'id',
            'driver',
            'starting_latitude',
            'starting_longitude',
            'final_latitude',
            'final_longitude',
            'starting_time',
            'final_time',
            'total_time',
            'attendance_list',          # para enviar dados
            'attendance_list_detail',   # para ler dados completos
        ]
        read_only_fields = ['id', 'starting_time']

    def create(self, validated_data):
        attendance_data = validated_data.pop('attendancelist_set', [])
        route = Route.objects.create(**validated_data)

        for item in attendance_data:
            passenger = item.get('passenger')
            attended = item.get('attended', False)
            AttendanceList.objects.create(route=route, passenger=passenger, attended=attended)
        return route
