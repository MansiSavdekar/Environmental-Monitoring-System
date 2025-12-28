from django.db import models

class AirQuality(models.Model):
    city = models.CharField(max_length=100)
    aqi = models.IntegerField()
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.city} - {self.aqi}"

class WaterQuality(models.Model):
    location = models.CharField(max_length=100)
    ph_level = models.FloatField()
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.location} - {self.ph_level}"
