from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('assIoT/', include('assIoT.urls')),
    path('admin/', admin.site.urls),
]
