# app/views.py
from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>Hola mundo!</h1>')

# app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index)
]

# urls.py
from django.urls import include, path

urlpatterns = [
    path('app/', include('app.urls'))
]