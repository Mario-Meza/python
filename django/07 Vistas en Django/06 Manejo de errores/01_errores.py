# app/views.py
from django.http import HttpResponse

def bienvenida(request):
    try:
        print('Ejecutar código')
        raise ValueError('¡Algo salió mal!')
        
    except ValueError as e:
        return HttpResponse('Ocurrió un error', status=404)
    
    except Exception as e:
        return HttpResponse('Ocurrió un error inesperado', status=402)
    

    return HttpResponse('¡La vista se ejecutó correctamente!')

# app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('bienvenida/', views.bienvenida)
]