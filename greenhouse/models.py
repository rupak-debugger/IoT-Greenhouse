from django.db import models

# Create your models here.


class SensorData(models.Model):
    temperature = models.FloatField(blank=False)
    humidity = models.FloatField(blank=False)
