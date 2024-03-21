# app/views.py
from django.shortcuts import render

def plantilla(request):
    return render(request, 'plantilla.html', { 'lista': ['html', 'css', 'javascript']})

# app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('plantilla/', views.plantilla)
]