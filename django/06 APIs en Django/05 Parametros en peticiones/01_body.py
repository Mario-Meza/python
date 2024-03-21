# app/views.py
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def ver_usuario(request, nombre):
    datos = json.loads(request.body)
    edad = datos.get('edad')
    return HttpResponse(f'Estás viendo el usuario {nombre} con edad {edad} años.')

# app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('usuario/<slug:nombre>', views.ver_usuario)
]