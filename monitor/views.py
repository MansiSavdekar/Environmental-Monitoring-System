from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import AirQuality, WaterQuality
from .serializers import AirQualitySerializer, WaterQualitySerializer
from .tasks import update_air

def dashboard(request):
    air = AirQuality.objects.all().order_by('-date_time')[:10]
    water = WaterQuality.objects.all().order_by('-date_time')[:10]

    return render(request, 'dashboard.html', {
        'air_data': air,
        'air_labels': [a.date_time.strftime('%H:%M') for a in air][::-1],
        'air_values': [a.aqi for a in air][::-1],
        'water_labels': [w.date_time.strftime('%H:%M') for w in water][::-1],
        'water_values': [w.ph_level for w in water][::-1],
    })

def fetch_air(request):
    update_air()
    return JsonResponse({"status": "updated"})

@api_view(['GET'])
def air_api(request):
    return Response(AirQualitySerializer(AirQuality.objects.all(), many=True).data)

@api_view(['GET'])
def water_api(request):
    return Response(WaterQualitySerializer(WaterQuality.objects.all(), many=True).data)
