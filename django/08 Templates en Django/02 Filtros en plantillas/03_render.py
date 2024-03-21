# app/views.py
from django.shortcuts import render

def get_texto(request):
    return render(request, 'texto.html', { 'mi_texto': 'python'})

# app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('texto/', views.get_texto)
]