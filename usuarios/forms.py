from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Usuarios
import re
from datetime import date, timedelta


class RegistroUsuarioForm(UserCreationForm):
    """
    Formulario personalizado para el registro de usuarios en la aplicación de citas médicas.
    Extiende UserCreationForm para incluir campos adicionales específicos del modelo Usuarios.
    """
    
    # Campos adicionales del modelo Usuarios
    nombre = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese su nombre',
            'required': True
        }),
        label='Nombre'
    )
    
    apellido = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese su apellido',
            'required': True
        }),
        label='Apellido'
    )
    
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'ejemplo@correo.com',
            'required': True
        }),
        label='Correo Electrónico'
    )
    
    telefono = forms.CharField(
        max_length=15,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ej: +57 300 123 4567',
            'required': True
        }),
        label='Teléfono'
    )
    
    cedula = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Número de identificación',
            'required': True
        }),
        label='Cédula/Identificación'
    )
    
    fecha_nacimiento = forms.DateField(
        widget=forms.DateInput(attrs={
            'class': 'form-control',
            'type': 'date',
            'required': True
        }),
        label='Fecha de Nacimiento'
    )
    
    direccion = forms.CharField(
        max_length=500,
        required=False,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Dirección completa (opcional)',
            'rows': 3
        }),
        label='Dirección'
    )
    
    # Campos de términos y condiciones
    acepta_terminos = forms.BooleanField(
        required=True,
        widget=forms.CheckboxInput(attrs={
            'class': 'form-check-input'
        }),
        label='Acepto los términos y condiciones'
    )
    
    acepta_politicas = forms.BooleanField(
        required=True,
        widget=forms.CheckboxInput(attrs={
            'class': 'form-check-input'
        }),
        label='Acepto las políticas de privacidad y tratamiento de datos'
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Personalizar campos heredados de UserCreationForm
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Nombre de usuario'
        })
        self.fields['username'].label = 'Nombre de Usuario'
        
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Contraseña'
        })
        self.fields['password1'].label = 'Contraseña'
        
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Confirmar contraseña'
        })
        self.fields['password2'].label = 'Confirmar Contraseña'

    def clean_email(self):
        """Validar que el email no esté ya registrado"""
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Este correo electrónico ya está registrado.")
        if Usuarios.objects.filter(email=email).exists():
            raise forms.ValidationError("Este correo electrónico ya está registrado.")
        return email

    def clean_cedula(self):
        """Validar formato de cédula y que no esté duplicada"""
        cedula = self.cleaned_data.get('cedula')
        
        # Validar que solo contenga números
        if not re.match(r'^\d+$', cedula):
            raise forms.ValidationError("La cédula debe contener solo números.")
        
        # Validar longitud mínima
        if len(cedula) < 6:
            raise forms.ValidationError("La cédula debe tener al menos 6 dígitos.")
        
        # Validar que no esté duplicada
        if Usuarios.objects.filter(cedula=cedula).exists():
            raise forms.ValidationError("Esta cédula ya está registrada.")
        
        return cedula

    def clean_telefono(self):
        """Validar formato de teléfono"""
        telefono = self.cleaned_data.get('telefono')
        
        # Remover espacios y caracteres especiales para validación
        telefono_limpio = re.sub(r'[^\d+]', '', telefono)
        
        # Validar formato básico
        if not re.match(r'^(\+\d{1,3})?\d{7,14}$', telefono_limpio):
            raise forms.ValidationError("Formato de teléfono inválido. Use formato: +57 300 123 4567")
        
        return telefono

    def clean_fecha_nacimiento(self):
        """Validar fecha de nacimiento"""
        fecha_nacimiento = self.cleaned_data.get('fecha_nacimiento')
        
        if fecha_nacimiento:
            # Validar que no sea fecha futura
            if fecha_nacimiento > date.today():
                raise forms.ValidationError("La fecha de nacimiento no puede ser futura.")
            
            # Validar edad mínima (por ejemplo, 16 años)
            edad_minima = date.today() - timedelta(days=16*365)
            if fecha_nacimiento > edad_minima:
                raise forms.ValidationError("Debe ser mayor de 16 años para registrarse.")
            
            # Validar edad máxima razonable (por ejemplo, 120 años)
            edad_maxima = date.today() - timedelta(days=120*365)
            if fecha_nacimiento < edad_maxima:
                raise forms.ValidationError("Fecha de nacimiento no válida.")
        
        return fecha_nacimiento

    def clean_nombre(self):
        """Validar nombre"""
        nombre = self.cleaned_data.get('nombre')
        
        # Validar que solo contenga letras y espacios
        if not re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$', nombre):
            raise forms.ValidationError("El nombre solo debe contener letras.")
        
        # Validar longitud mínima
        if len(nombre.strip()) < 2:
            raise forms.ValidationError("El nombre debe tener al menos 2 caracteres.")
        
        return nombre.title()  # Capitalizar primera letra

    def clean_apellido(self):
        """Validar apellido"""
        apellido = self.cleaned_data.get('apellido')
        
        # Validar que solo contenga letras y espacios
        if not re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$', apellido):
            raise forms.ValidationError("El apellido solo debe contener letras.")
        
        # Validar longitud mínima
        if len(apellido.strip()) < 2:
            raise forms.ValidationError("El apellido debe tener al menos 2 caracteres.")
        
        return apellido.title()  # Capitalizar primera letra

    def save(self, commit=True):
        """
        Guardar tanto el usuario de Django como el registro en el modelo Usuarios
        """
        # Guardar el usuario de Django
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['nombre']
        user.last_name = self.cleaned_data['apellido']
        
        if commit:
            user.save()
            
            # Crear el registro en el modelo Usuarios
            usuario_perfil = Usuarios.objects.create(
                nombre=self.cleaned_data['nombre'],
                apellido=self.cleaned_data['apellido'],
                email=self.cleaned_data['email'],
                telefono=self.cleaned_data['telefono'],
                cedula=self.cleaned_data['cedula'],
                fecha_nacimiento=self.cleaned_data['fecha_nacimiento'],
                direccion=self.cleaned_data.get('direccion', ''),
                activo=True
            )
            
            return user, usuario_perfil
        
        return user