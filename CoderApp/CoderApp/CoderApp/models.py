from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    contraseña = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class BusquedaUsuario(models.Model):
    nombre_busqueda = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_busqueda


class InicioSesion(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Inicio de sesión de {self.usuario.nombre}"