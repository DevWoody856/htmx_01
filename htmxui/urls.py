from django.contrib import admin
from django.urls import path, include
import uiapp

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('uiapp.urls')),
]
