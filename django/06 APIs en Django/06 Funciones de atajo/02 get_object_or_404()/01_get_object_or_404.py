# app/views.py
from django.shortcuts import redirect, get_object_or_404
from django.http import HttpResponse
from .models import Producto

def detalle_producto(request, pk):
    if pk == 1:
        return redirect('/admin/')
    producto = get_object_or_404(Producto.objects.filter(pk=pk))
    return HttpResponse(producto.cantidad)