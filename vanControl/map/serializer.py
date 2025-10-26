from rest_framework import serializers
from map.models import Route, AttendanceList
from user.serializer import UserSerializer
from user.models import User


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
    driver = UserSerializer(source='driver_id', read_only=True)  # Para GET
    driver_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),  # Para POST/PUT/PATCH
        write_only=True,
        required=False
    )
    attendance_list = AttendanceListSerializer(
        source='attendancelist_set', many=True, required=False
    )

    class Meta:
        model = Route
        fields = [
            'id',
            'driver',
            'driver_id',
            'attendance_list',
            'starting_latitude',
            'starting_longitude',
            'final_latitude',
            'final_longitude',
            'starting_time',
            'final_time',
            'total_time',
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

    def update(self, instance, validated_data):
        # Atualiza o driver
        driver = validated_data.pop('driver_id', None)
        if driver is not None:
            instance.driver_id = driver

        # Atualiza campos simples do Route
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        # Atualiza lista de passageiros (AttendanceList)
        attendance_data = validated_data.pop('attendancelist_set', None)
        if attendance_data is not None:
            # Remove registros antigos não enviados
            existing_ids = [item['passenger'].id for item in attendance_data if item.get('passenger')]
            AttendanceList.objects.filter(route=instance).exclude(passenger__id__in=existing_ids).delete()

            # Cria ou atualiza os passageiros enviados
            for item in attendance_data:
                passenger = item.get('passenger')
                attended = item.get('attended', False)
                if passenger:
                    obj, created = AttendanceList.objects.update_or_create(
                        route=instance,
                        passenger=passenger,
                        defaults={'attended': attended}
                    )

        return instance
