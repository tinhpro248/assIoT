from django.http import HttpResponse, JsonResponse
from .models import Humidity, Temperature


def index(request):
    return HttpResponse("Đây là server ass IoT nhóm 2")

def setTemperature(request):
    t = Temperature.objects.get(id=1)
    min = request.GET['min']
    max = request.GET['max']
    t.min = float(min)
    t.max = float(max)
    t.save()
    return HttpResponse(t, content_type='application/json')

def getTemperature(request):
    t = Temperature.objects.get(id=1)
    return JsonResponse(t.get())

def setHumidity(request):
    t = Humidity.objects.get(id=1)
    min = request.GET['min']
    max = request.GET['max']
    t.min = float(min)
    t.max = float(max)
    t.save()
    return HttpResponse(t, content_type='application/json')

def getHumidity(request):
    t = Humidity.objects.get(id=1)
    return JsonResponse(t.get())


