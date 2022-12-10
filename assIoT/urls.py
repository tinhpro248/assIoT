from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('setTemp/<str:min>/<str:max>', views.setTemperature, name='setTemp'),
    path('getTemp', views.getTemperature, name='getTemp'),
    path('setHumi/<str:min>/<str:max>', views.setHumidity, name='setHumi'),
    path('getHumi', views.getHumidity, name='getHumi')
]