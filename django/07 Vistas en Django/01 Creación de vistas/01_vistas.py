# app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('bienvenida/', views.bienvenida)
]

# app/views.py
from django.http import HttpResponse

def bienvenida(request):
    return HttpResponse('¡Hola, bienvenid@ a mi sitio web!')