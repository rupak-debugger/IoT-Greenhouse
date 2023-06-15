from django.db import models

# Create your models here.


class SensorData(models.Model):
    temperature = models.FloatField(blank=False)
    humidity = models.FloatField(blank=False)
    date_posted = models.DateTimeField(
        verbose_name='Posted On', auto_now_add=True)

    def save(self, *args, **kwargs):
        self.temperature = round(self.temperature, 2)
        self.humidity = round(self.humidity, 2)
        super(SensorData, self).save(*args, **kwargs)


class RelayControl(models.Model):
    relay1 = models.BooleanField(default=False)
    relay2 = models.BooleanField(default=False)
