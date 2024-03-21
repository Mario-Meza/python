# holamundo/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('articulo/<int:id_articulo>/', views.ver_articulo),
    path('usuario/<slug:nombre>/', views.ver_usuario),
    path('empleado/<str:nombre>/', views.ver_empleado),
    path('producto/<uuid:identificador>/', views.ver_producto),
    path('ruta/<path:parametro>/', views.mi_vista),
]

# holamundo/views.py
from django.http import HttpResponse

# visita articulo/2
def ver_articulo(request, id_articulo):
    return HttpResponse(f'Estás viendo el artículo {id_articulo}')

# visita usuario/marcos
def ver_usuario(request, nombre):
    return HttpResponse(f'Estás viendo el usuario {nombre}')

# visita empleado/marcos perez
def ver_empleado(request, nombre):
    return HttpResponse(f'Estás viendo el empleado {nombre}')

# visita producto/550e8400-e29b-41d4-a716-446655440000
def ver_producto(request, identificador):
    return HttpResponse(f'Estás viendo el producto {identificador}')

# visita ruta/cualquier_ruta
def mi_vista(request, parametro):
    return HttpResponse(f'Estás viendo la ruta con el parámetro: {parametro}')