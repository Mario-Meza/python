# app/views.py
from django.http import HttpResponse
from django.core import serializers
from .models import Autor

# json
@csrf_exempt
def mi_api(request):
    if request.method == 'GET':
        datos = [Autor.objects.get(nombre='Juan')]
        json = serializers.serialize('json', datos)
        return HttpResponse(json, content_type='application/json')
    

# xml
@csrf_exempt
def mi_api(request):
    if request.method == 'GET':
        datos = [Autor.objects.get(nombre='Juan')]
        xml = serializers.serialize('xml', datos, fields=['email'])
        return HttpResponse(xml, content_type='application/xml')