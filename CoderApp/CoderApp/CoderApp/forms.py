# forms.py

from django import forms
from .models import Usuario, BusquedaUsuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ('nombre', 'contraseña')


class BusquedaUsuarioForm(forms.ModelForm):
    class Meta:
        model = BusquedaUsuario
        fields = ('nombre_busqueda',)
