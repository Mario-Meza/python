from django.http import HttpResponse

def bienvenida():
    return HttpResponse('¡Bienvenid@ a mi aplicación web construida con Django!')