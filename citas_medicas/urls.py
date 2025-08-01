"""
URL configuration for citas_medicas project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from usuarios import views  # Importamos las vistas de la aplicación usuarios

# Definición de las rutas URL de la aplicación
urlpatterns = [
    # Ruta para el panel de administración de Django
    path('admin/', admin.site.urls),
    # Ruta para la página de inicio
    path('', views.home, name='home'),
    # Ruta para la página de registro de usuarios
    path('registro/', views.registro, name='registro'),
    # Ruta para la página de inicio de sesión
    path('login/', views.login, name='login'),
    # Ruta para la página de perfil de usuario
    path('perfil/', views.perfil, name='perfil'),
    # Ruta para la página de edición de perfil
    path('editar_perfil/', views.editar_perfil, name='editar_perfil'),
    # Ruta para la página de cambio de contraseña
    path('cambiar_contraseña/', views.cambiar_contraseña, name='cambiar_contraseña'),
    # Ruta para la página de eliminación de cuenta
    path('eliminar_cuenta/', views.eliminar_cuenta, name='eliminar_cuenta'),
    # Ruta para la página de notificaciones
    path('notificaciones/', views.notificaciones, name='notificaciones'),
]
