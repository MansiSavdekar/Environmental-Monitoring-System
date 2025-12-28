from django.urls import path
from .views import dashboard, fetch_air, air_api, water_api

urlpatterns = [
    path('', dashboard),
    path('fetch-air/', fetch_air),
    path('api/air/', air_api),
    path('api/water/', water_api),
]
