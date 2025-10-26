from django.contrib import admin
from .models import Route, AttendanceList


class AttendanceListInline(admin.TabularInline):
    model = AttendanceList
    extra = 1
    autocomplete_fields = ['passenger']
    readonly_fields = []


@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'driver_id',
        'starting_time',
        'final_time',
        'total_time',
    )
    list_filter = ('driver_id', 'starting_time', 'final_time')
    search_fields = ('driver_id__username',)
    inlines = [AttendanceListInline]

    readonly_fields = ('starting_time',)  # <-- ✅ impede edição, mas exibe o valor

    fieldsets = (
        ('Motorista', {'fields': ('driver_id',)}),
        ('Pontos da Rota', {
            'fields': (
                ('starting_latitude', 'starting_longitude'),
                ('final_latitude', 'final_longitude'),
            )
        }),
        ('Horários', {
            'fields': ('starting_time', 'final_time', 'total_time')
        }),
    )


@admin.register(AttendanceList)
class AttendanceListAdmin(admin.ModelAdmin):
    list_display = ('id', 'route', 'passenger', 'attended')
    list_filter = ('attended', 'route')
    search_fields = ('passenger__username', 'route__driver_id__username')
