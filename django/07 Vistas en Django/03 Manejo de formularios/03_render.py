# app/views.py
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .forms import NombreForm

@csrf_exempt
def obtener_nombre(request):
    if request.method == 'POST':

        form = NombreForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            email = form.cleaned_data['email']
            mensaje = form.cleaned_data['mensaje']
            # Hacer algo con la información recopilada
            print(nombre, email, mensaje)
            return HttpResponse('Recibido!')
    else:
        form = NombreForm()

    return render(request, 'nombre.html', {'form': form})

# app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('nombre/', views.obtener_nombre)
]