# views.py

from django.shortcuts import render, redirect
from .models import Usuario
from .forms import UsuarioForm, BusquedaUsuarioForm
from django.http import HttpResponse
from django.contrib import messages


from django.shortcuts import render
from .forms import UsuarioForm

def registro_usuario(request):
    mensaje = None
    
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            mensaje = "Usuario creado correctamente"
            form = UsuarioForm()  # Limpiar los campos del formulario
    else:
        form = UsuarioForm()
    
    return render(request, 'CoderApp_templates/registro_usuario.html', {'form': form, 'mensaje': mensaje})


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

def inicio_sesion(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        contrasena = request.POST.get('contrasena')
        
        try:
            usuario = Usuario.objects.get(nombre=nombre, contrasena=contrasena)
            # Realizar acciones necesarias para el inicio de sesión exitoso
            messages.success(request, 'Inicio de sesión exitoso')
            return redirect('inicio')  # Redirigir a la página de inicio después del inicio de sesión exitoso
        except Usuario.DoesNotExist:
            # Usuario no encontrado en la base de datos o credenciales inválidas
            messages.error(request, 'Nombre de usuario o contraseña incorrectos')
    
    return render(request, 'CoderApp_templates/inicio_sesion.html')