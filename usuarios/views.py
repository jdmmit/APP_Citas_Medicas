from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

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
    # Vista para el registro de nuevos usuarios

    if request.method == "GET":
        # Si la petición es GET, muestra el formulario de registro vacío
        return render(request, "registro.html",
                      {
                          "form": UserCreationForm
                      })
    else:
        # Si la petición es POST, procesa los datos enviados por el usuario
        if request.POST["password1"] == request.POST["password2"]:
            # Verifica que las contraseñas coincidan
            try:
                user = User.objects.create_user(
                    username=request.POST["username"],
                    password=request.POST["password1"],

                )
                user.save()
                # Inicia sesión automáticamente al registrarse
                login(request, user)
                return redirect("perfil")  # Redirige a la página de tareas
            except IntegrityError:
                # Si las contraseñas no coinciden, muestra un mensaje de error
                render(
                    request,
                    "registro.html",
                    {
                        "form": UserCreationForm,
                        "error": "El nombre de usuario ya está en uso"
                    })
        return render(
            request,
            "registro.html",
            {
                "form": UserCreationForm,
                "error": "La contraseña no coincide"
            })



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