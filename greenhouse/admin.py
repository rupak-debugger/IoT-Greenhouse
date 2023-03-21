from django.contrib import admin

from greenhouse.models import SensorData

# Register your models here.


@admin.register(SensorData)
class SensorDataAdmin(admin.ModelAdmin):
    list_display = ['id', 'temperature', 'humidity']
