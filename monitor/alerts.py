from django.core.mail import send_mail
from twilio.rest import Client

def send_air_email(aqi, city):
    if aqi > 100:
        send_mail(
            "Air Quality Alert",
            f"AQI in {city} is {aqi}",
            None,
            ["your_email@gmail.com"],
            fail_silently=True
        )

def send_air_sms(aqi, city):
    if aqi > 100:
        client = Client("SID", "TOKEN")
        client.messages.create(
            body=f"AQI Alert: {city} AQI {aqi}",
            from_="+1234567890",
            to="+91XXXXXXXXXX"
        )
