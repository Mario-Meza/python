# app/views.py
from django.shortcuts import render

def get_usuario(request):

    usuario = {
        'nombre': 'Gustavo',
        'apellido': 'Ulloa',
        'email': 'guga@example.com',
        'perfil': {
            'edad': 30,
            'ciudad': 'Sangolquí'
        }
    }

    return render(request, 'usuario.html', {'usuario': usuario})

# app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('usuario/', views.get_usuario)
]