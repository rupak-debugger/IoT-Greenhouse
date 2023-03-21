from greenhouse.models import SensorData
from rest_framework import serializers


class SensorDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorData
        fields = ['temperature', 'humidity']
