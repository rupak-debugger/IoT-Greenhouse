from greenhouse.models import SensorData, RelayControl
from rest_framework import serializers


class SensorDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorData
        fields = ['temperature', 'humidity']


class RelayControlSerializer(serializers.ModelSerializer):
    class Meta:
        model = RelayControl
        fields = ['relay1', 'relay2']
