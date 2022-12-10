from django.http import HttpResponse, JsonResponse
from .models import Humidity, Temperature, Notification


def index(request):
    return HttpResponse("Đây là server ass IoT nhóm 2")

def setTemperature(request, min, max):
    t = Temperature.objects.get(id=1)
    t.min = float(min)
    t.max = float(max)
    t.save()
    return HttpResponse(t, content_type='application/json')

def getTemperature(request):
    t = Temperature.objects.get(id=1)
    return JsonResponse(t.get())

def setHumidity(request, min, max):
    t = Humidity.objects.get(id=1)
    t.min = float(min)
    t.max = float(max)
    t.save()
    return HttpResponse(t, content_type='application/json')

def getHumidity(request):
    t = Humidity.objects.get(id=1)
    return JsonResponse(t.get())


