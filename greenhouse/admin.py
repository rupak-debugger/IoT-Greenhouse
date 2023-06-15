from django.contrib import admin

from greenhouse.models import SensorData, RelayControl

# Register your models here.


@admin.register(SensorData)
class SensorDataAdmin(admin.ModelAdmin):
    list_display = ['id', 'temperature', 'humidity', 'date_posted']


@admin.register(RelayControl)
class SensorDataAdmin(admin.ModelAdmin):
    list_display = ['id', 'relay1', 'relay2']
