from django.shortcuts import render

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
    
    Renderiza la plantilla registro.html que contiene el formulario de registro.
    
    Args:
        request: Objeto HttpRequest con los datos de la petición.
        
    Returns:
        HttpResponse con la plantilla renderizada.
    """
    return render(request, "registro.html")


def login(request):
    """Vista para la página de inicio de sesión.
    
    Renderiza la plantilla login.html que contiene el formulario de inicio de sesión.
    
    Args:
        request: Objeto HttpRequest con los datos de la petición.
        
    Returns:
        HttpResponse con la plantilla renderizada.
    """
    return render(request, "login.html")


def perfil(request):
    """Vista para la página de perfil de usuario.
    
    Renderiza la plantilla perfil.html que muestra la información del perfil del usuario.
    
    Args:
        request: Objeto HttpRequest con los datos de la petición.
        
    Returns:
        HttpResponse con la plantilla renderizada.
    """
    return render(request, "perfil.html")


def editar_perfil(request):
    """Vista para la página de edición de perfil.
    
    Renderiza la plantilla editar_perfil.html que contiene el formulario para actualizar
    la información del perfil del usuario.
    
    Args:
        request: Objeto HttpRequest con los datos de la petición.
        
    Returns:
        HttpResponse con la plantilla renderizada.
    """
    return render(request, "editar_perfil.html")


def cambiar_contraseña(request):
    """Vista para la página de cambio de contraseña.
    
    Renderiza la plantilla cambiar_contraseña.html que contiene el formulario
    para actualizar la contraseña del usuario.
    
    Args:
        request: Objeto HttpRequest con los datos de la petición.
        
    Returns:
        HttpResponse con la plantilla renderizada.
    """
    return render(request, "cambiar_contraseña.html")


def eliminar_cuenta(request):
    """Vista para la página de eliminación de cuenta.
    
    Renderiza la plantilla eliminar_cuenta.html que contiene la confirmación
    para eliminar la cuenta del usuario.
    
    Args:
        request: Objeto HttpRequest con los datos de la petición.
        
    Returns:
        HttpResponse con la plantilla renderizada.
    """
    return render(request, "eliminar_cuenta.html")


def notificaciones(request):
    """Vista para la página de notificaciones.
    
    Renderiza la plantilla notificaciones.html que muestra las notificaciones
    del usuario.
    
    Args:
        request: Objeto HttpRequest con los datos de la petición.
        
    Returns:
        HttpResponse con la plantilla renderizada.
    """
    return render(request, "notificaciones.html")