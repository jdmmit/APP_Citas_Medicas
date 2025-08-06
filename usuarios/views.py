from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import IntegrityError
from .forms import RegistroUsuarioForm
from .models import Usuarios

# Vistas para la aplicación de usuarios
# Estas vistas renderizan las plantillas HTML correspondientes

def home(request):
    """Vista para la página de inicio.
    
    Renderiza la plantilla home.html que muestra información general de la aplicación.
    
    Args:
        request: Objeto HttpRequest con los datos de la petición.
        
    Returns:
        HttpResponse con la plantilla renderizada.
    """
    return render(request, "home.html")


def registro(request):
    """Vista para la página de registro de usuarios.
    
    Maneja tanto la visualización del formulario como el procesamiento del registro.
    Crea tanto el usuario de Django como el perfil personalizado en el modelo Usuarios.
    
    Args:
        request: Objeto HttpRequest con los datos de la petición.
        
    Returns:
        HttpResponse con la plantilla renderizada o redirección tras registro exitoso.
    """
    
    if request.method == 'GET':
        # Mostrar formulario de registro vacío
        return render(request, 'registro.html', {
            'form': RegistroUsuarioForm()
        })
    
    elif request.method == 'POST':
        # Procesar datos del formulario
        form = RegistroUsuarioForm(request.POST)
        
        if form.is_valid():
            try:
                # Guardar usuario y perfil
                user, usuario_perfil = form.save()
                
                # Iniciar sesión automáticamente
                login(request, user)
                
                # Mensaje de éxito
                messages.success(
                    request, 
                    f'¡Bienvenido {usuario_perfil.get_full_name()}! Tu cuenta ha sido creada exitosamente.'
                )
                
                # Redirigir al perfil o página principal
                return redirect('perfil')  # Cambia por la URL que prefieras
                
            except IntegrityError as e:
                # Error de integridad en la base de datos
                messages.error(
                    request, 
                    'Error al crear la cuenta. Algunos datos ya están registrados.'
                )
                return render(request, 'registro.html', {'form': form})
            
            except Exception as e:
                # Otros errores
                messages.error(
                    request, 
                    'Error inesperado al crear la cuenta. Por favor, inténtalo de nuevo.'
                )
                return render(request, 'registro.html', {'form': form})
        
        else:
            # Formulario con errores
            return render(request, 'registro.html', {'form': form})


def login_view(request):
    """Vista para la página de inicio de sesión.
    
    Maneja la autenticación de usuarios registrados.
    
    Args:
        request: Objeto HttpRequest con los datos de la petición.
        
    Returns:
        HttpResponse con la plantilla renderizada o redirección tras login exitoso.
    """
    
    if request.method == 'GET':
        return render(request, 'login.html', {
            'form': AuthenticationForm()
        })
    
    elif request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)
                messages.success(request, f'¡Bienvenido de nuevo, {user.first_name}!')
                return redirect('perfil')  # Redirigir a donde prefieras
            else:
                messages.error(request, 'Credenciales inválidas.')
        
        return render(request, 'login.html', {'form': form})


@login_required
def perfil(request):
    """Vista para la página de perfil del usuario.
    
    Muestra la información del perfil del usuario autenticado.
    
    Args:
        request: Objeto HttpRequest con los datos de la petición.
        
    Returns:
        HttpResponse con la plantilla renderizada.
    """
    try:
        # Obtener el perfil del usuario
        usuario_perfil = Usuarios.objects.get(email=request.user.email)
        
        return render(request, 'perfil.html', {
            'usuario': usuario_perfil
        })
    
    except Usuarios.DoesNotExist:
        messages.error(request, 'No se encontró el perfil del usuario.')
        return redirect('home')


@login_required
def editar_perfil(request):
    """Vista para editar el perfil del usuario.
    
    Permite al usuario modificar su información personal.
    
    Args:
        request: Objeto HttpRequest con los datos de la petición.
        
    Returns:
        HttpResponse con la plantilla renderizada.
    """
    # Implementar lógica de edición de perfil
    return render(request, 'editar_perfil.html')


@login_required
def cambiar_contraseña(request):
    """Vista para cambiar la contraseña del usuario.
    
    Permite al usuario cambiar su contraseña actual.
    
    Args:
        request: Objeto HttpRequest con los datos de la petición.
        
    Returns:
        HttpResponse con la plantilla renderizada.
    """
    # Implementar lógica de cambio de contraseña
    return render(request, 'cambiar_contraseña.html')


@login_required
def eliminar_cuenta(request):
    """Vista para eliminar la cuenta del usuario.
    
    Permite al usuario eliminar permanentemente su cuenta.
    
    Args:
        request: Objeto HttpRequest con los datos de la petición.
        
    Returns:
        HttpResponse con la plantilla renderizada.
    """
    # Implementar lógica de eliminación de cuenta
    return render(request, 'eliminar_cuenta.html')


@login_required
def notificaciones(request):
    """Vista para mostrar las notificaciones del usuario.
    
    Muestra las notificaciones y alertas del usuario.
    
    Args:
        request: Objeto HttpRequest con los datos de la petición.
        
    Returns:
        HttpResponse con la plantilla renderizada.
    """
    # Implementar lógica de notificaciones
    return render(request, 'notificaciones.html')


def logout_view(request):
    """Vista para cerrar sesión.
    
    Cierra la sesión del usuario actual.
    
    Args:
        request: Objeto HttpRequest con los datos de la petición.
        
    Returns:
        Redirección a la página de inicio.
    """
    logout(request)
    messages.success(request, 'Has cerrado sesión exitosamente.')
    return redirect('home')