# holamundo/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('producto/<int:pk>/', views.producto),
]

# holamundo/views.py
from django.http import HttpResponse
from .models import Producto

# visita producto/1
def producto(request, pk):
    producto = Producto.objects.get(pk=pk)
    return HttpResponse(producto.cantidad)