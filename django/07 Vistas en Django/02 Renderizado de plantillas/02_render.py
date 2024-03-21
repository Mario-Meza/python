# app/views.py
from django.shortcuts import render

def bienvenida(request):
    return render(request, 'index.html', {'nombre': 'colega'})

# app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('bienvenida/', views.bienvenida)
]
