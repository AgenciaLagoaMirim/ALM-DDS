from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from spd.models import DataParameter, Station


# Create your views here.
@csrf_exempt
@require_POST
def new_reading(request):
    station_id = request.POST.get("id")
    station_token = request.POST.get("token")
    station_value = request.POST.get("values")
    station = Station.objects.get(id=station_id)
    if station_token == station.access_token:
        print(station_id)
        print(station_token)
        print(station_value)
