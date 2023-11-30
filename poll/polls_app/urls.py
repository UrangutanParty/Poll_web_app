""" Fisierul urls.py trebuie creat pentru fiecare aplicatie nou
creata pentu a crea rutele => mapezi view-ul pe un URL pentru 
ai putea face call """

from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index') # 2 argumente obligatorii ruta si view-ul
    
]

