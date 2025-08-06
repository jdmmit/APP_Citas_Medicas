from django.db import models
from django.contrib.auth.models import User
from usuarios.models import Usuarios

# Ejemplo de uso del modelo para probar las sugerencias de código
def ejemplo_uso_modelo():
    # Crear un nuevo usuario
    nuevo_usuario = Usuarios(
        nombre="Juan",
        apellido="Pérez",
        email="juan.perez@email.com",
        telefono="123456789",
        fecha_nacimiento="1990-01-01",
        cedula="12345678",
        direccion="Calle 123"
    )
    
    # Guardar el usuario
    nuevo_usuario.save()
    
    # Buscar usuarios
    usuarios_activos = Usuarios.objects.filter(activo=True)
    
    # Obtener un usuario por email
    try:
        usuario = Usuarios.objects.get(email="juan.perez@email.com")
        print(f"Usuario encontrado: {usuario.get_full_name()}")
    except Usuarios.DoesNotExist:
        print("Usuario no encontrado")
    
    # Actualizar un usuario
    Usuarios.objects.filter(email="juan.perez@email.com").update(
        telefono="987654321"
    )
    
    return usuarios_activos