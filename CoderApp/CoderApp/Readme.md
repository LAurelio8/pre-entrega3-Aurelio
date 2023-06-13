CoderApp
Este proyecto es una aplicación web desarrollada en Django que permite registrar usuarios, buscar usuarios y realizar inicio de sesión.

Estructura de archivos
views.py: Este archivo contiene las funciones que se utilizan en la aplicación.
registro_usuario: Vista para registrar un nuevo usuario.
buscar_usuario: Vista para buscar usuarios en base a un nombre de búsqueda.
inicio_sesion: Vista para realizar inicio de sesión.
models.py: Este archivo contiene las definiciones de los modelos de datos utilizados en la aplicación.
urls.py: Este archivo contiene las URL (rutas) de la aplicación.

/registro_usuario/: URL para acceder a la vista de registro de usuario.
/buscar_usuario/: URL para acceder a la vista de búsqueda de usuario.
/inicio_sesion/: URL para acceder a la vista de inicio de sesión.

Archivos HTML: Estos archivos contienen las plantillas HTML utilizadas para renderizar las vistas.

registro_usuario.html: Plantilla para la vista de registro de usuario.
buscar_usuario.html: Plantilla para la vista de búsqueda de usuario.
inicio_sesion.html: Plantilla para la vista de inicio de sesión.

Al registrar un usuario en la vista registro_usuario, se muestra un mensaje de confirmación si el registro es exitoso.

En la vista buscar_usuario, se muestra una lista de usuarios que coinciden con el nombre de búsqueda introducido.

En la vista inicio_sesion, se verifica si las credenciales ingresadas coinciden con algún usuario registrado en la base de datos.
