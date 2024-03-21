# app/views.py
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import Producto

def detalle_producto(request, pk):
    if pk == 1:
        return redirect('/admin/')
    producto = Producto.objects.get(pk=pk)
    return HttpResponse(producto.cantidad)