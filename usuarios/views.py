from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "home.html")


def registro(request):
    return render(request, "registro.html")


def login(request):
    return render(request, "login.html")


def perfil(request):
    return render(request, "perfil.html")


def editar_perfil(request):
    return render(request, "editar_perfil.html")


def cambiar_contraseña(request):
    return render(request, "cambiar_contraseña.html")


def eliminar_cuenta(request):
    return render(request, "eliminar_cuenta.html")


def notificaciones(request):
    return render(request, "notificaciones.html")