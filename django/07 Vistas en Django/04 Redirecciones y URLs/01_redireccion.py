# urls.py
from django.views.generic import RedirectView
from django.urls import path

urlpatterns = [
    path('ruta_antigua/', RedirectView.as_view(url='https://www.djangoproject.com/'))
]