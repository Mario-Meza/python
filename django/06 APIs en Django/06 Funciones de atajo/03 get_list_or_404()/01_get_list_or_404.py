# app/views.py
from django.shortcuts import get_list_or_404
from django.http import HttpResponse
from .models import Producto

def productos(request):
    productos = get_list_or_404(Producto)
    return HttpResponse(productos)

# borrar registros en shell para probar 404
from holamundo.models import Producto
Producto.objects.all().delete()