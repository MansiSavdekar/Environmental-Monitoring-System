from .models import AirQuality, WaterQuality
from .services import fetch_air_quality, fetch_water_quality
from .alerts import send_air_email, send_air_sms

def update_air(city="Delhi"):
    aqi = fetch_air_quality(city)
    if aqi:
        AirQuality.objects.create(city=city, aqi=aqi)
        send_air_email(aqi, city)
        send_air_sms(aqi, city)

def update_water(location="River Ganga"):
    ph = fetch_water_quality()
    WaterQuality.objects.create(location=location, ph_level=ph)
