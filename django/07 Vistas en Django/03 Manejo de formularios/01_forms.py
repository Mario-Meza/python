# app/forms.py
from django import forms

class NombreForm(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=50)
    email = forms.EmailField(label='Email', max_length=100)
    mensaje = forms.CharField(label='Mensaje', widget=forms.Textarea)