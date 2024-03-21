# app/views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Autor

@csrf_exempt
def mi_api(request):
    if request.method == 'GET':
        data = list(Autor.objects.values())
        return JsonResponse(data, safe=False)

# app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('api', views.mi_api, name='mi_api'),
]

# urls.py
from django.urls import include, path

urlpatterns = [
    path('blog/', include('blog.urls'))
]