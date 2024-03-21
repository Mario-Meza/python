# app/views.py
from django.shortcuts import render

def imagen(request):
    return render(request, 'imagen.html')

# app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('imagen/', views.imagen)
]