# views.py

from django.shortcuts import render, redirect
from .models import Usuario
from .forms import UsuarioForm, BusquedaUsuarioForm
from django.http import HttpResponse

def registro_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = UsuarioForm()
    
    return render(request, 'CoderApp_templates/registro_usuario.html', {'form': form})

def buscar_usuario(request):
    if request.method == 'POST':
        form = BusquedaUsuarioForm(request.POST)
        if form.is_valid():
            nombre_busqueda = form.cleaned_data['nombre_busqueda']
            usuarios = Usuario.objects.filter(nombre__icontains=nombre_busqueda)
            return render(request, 'CoderApp_templates/buscar_usuario.html', {'form': form, 'usuarios': usuarios})
    else:
        form = BusquedaUsuarioForm()
    
    return render(request, 'CoderApp_templates/buscar_usuario.html', {'form': form})
