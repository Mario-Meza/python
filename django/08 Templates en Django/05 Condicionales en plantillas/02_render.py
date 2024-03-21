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
        },
        'autenticado': True,
        'admin': False,
        'super': True
    }

    return render(request, 'usuario.html', {'usuario': usuario})
