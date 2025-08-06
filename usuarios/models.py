from django.db import models
from django.contrib.auth.models import User 


# Create your models here.

class Usuarios(models.Model):
    TIPO_DOCUMENTO_CHOICES = [
        ('CC', 'Cédula de Ciudadanía'),
        ('TI', 'Tarjeta de Identidad'),
        ('CE', 'Cédula de Extranjería'),
        ('PP', 'Pasaporte'),
        ('RC', 'Registro Civil'),
    ]
    
    GENERO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otro'),
        ('N', 'Prefiero no decir'),
    ]
    
    TIPO_SANGRE_CHOICES = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
        ('NS', 'No sabe'),
    ]
    
    # Información básica
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    apellido = models.CharField(max_length=100, verbose_name="Apellido")
    email = models.EmailField(unique=True, verbose_name="Correo Electrónico")
    telefono = models.CharField(max_length=15, verbose_name="Teléfono")
    fecha_nacimiento = models.DateField(verbose_name="Fecha de Nacimiento")
    
    # Información de identificación
    tipo_documento = models.CharField(
        max_length=2, 
        choices=TIPO_DOCUMENTO_CHOICES, 
        default='CC',
        verbose_name="Tipo de Documento"
    )
    cedula = models.CharField(
        max_length=20, 
        unique=True, 
        verbose_name="Número de Documento"
    )
    
    # Información adicional
    genero = models.CharField(
        max_length=1, 
        choices=GENERO_CHOICES, 
        blank=True, 
        null=True,
        verbose_name="Género"
    )
    tipo_sangre = models.CharField(
        max_length=3, 
        choices=TIPO_SANGRE_CHOICES, 
        blank=True, 
        null=True,
        verbose_name="Tipo de Sangre"
    )
    direccion = models.TextField(
        blank=True, 
        null=True, 
        verbose_name="Dirección"
    )
    
    # Información de contacto de emergencia
    contacto_emergencia_nombre = models.CharField(
        max_length=100, 
        blank=True, 
        null=True,
        verbose_name="Nombre Contacto de Emergencia"
    )
    contacto_emergencia_telefono = models.CharField(
        max_length=15, 
        blank=True, 
        null=True,
        verbose_name="Teléfono Contacto de Emergencia"
    )
    contacto_emergencia_relacion = models.CharField(
        max_length=50, 
        blank=True, 
        null=True,
        verbose_name="Relación Contacto de Emergencia"
    )
    
    # Información médica básica
    alergias = models.TextField(
        blank=True, 
        null=True,
        verbose_name="Alergias Conocidas",
        help_text="Describa cualquier alergia conocida a medicamentos, alimentos, etc."
    )
    medicamentos_actuales = models.TextField(
        blank=True, 
        null=True,
        verbose_name="Medicamentos Actuales",
        help_text="Liste los medicamentos que toma actualmente"
    )
    condiciones_medicas = models.TextField(
        blank=True, 
        null=True,
        verbose_name="Condiciones Médicas",
        help_text="Describa cualquier condición médica relevante"
    )
    
    # Información del sistema
    fecha_registro = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Registro")
    fecha_actualizacion = models.DateTimeField(auto_now=True, verbose_name="Última Actualización")
    activo = models.BooleanField(default=True, verbose_name="Usuario Activo")
    
    # Relación con el usuario de Django (opcional)
    usuario_django = models.OneToOneField(
        User, 
        on_delete=models.CASCADE, 
        blank=True, 
        null=True,
        verbose_name="Usuario del Sistema"
    )
    
    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
        ordering = ['nombre', 'apellido']
        indexes = [
            models.Index(fields=['cedula']),
            models.Index(fields=['email']),
            models.Index(fields=['fecha_nacimiento']),
        ]
    
    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.cedula}"
    
    def get_full_name(self):
        """Retorna el nombre completo del usuario"""
        return f"{self.nombre} {self.apellido}"
    
    def get_edad(self):
        """Calcula y retorna la edad del usuario"""
        from datetime import date
        today = date.today()
        return today.year - self.fecha_nacimiento.year - (
            (today.month, today.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day)
        )
    
    def get_tipo_documento_display_short(self):
        """Retorna una versión corta del tipo de documento"""
        return self.get_tipo_documento_display()
    
    def tiene_informacion_medica_completa(self):
        """Verifica si el usuario ha completado su información médica básica"""
        return bool(
            self.tipo_sangre and 
            self.contacto_emergencia_nombre and 
            self.contacto_emergencia_telefono
        )
    
    def get_informacion_contacto_emergencia(self):
        """Retorna la información de contacto de emergencia formateada"""
        if self.contacto_emergencia_nombre and self.contacto_emergencia_telefono:
            relacion = f" ({self.contacto_emergencia_relacion})" if self.contacto_emergencia_relacion else ""
            return f"{self.contacto_emergencia_nombre}{relacion} - {self.contacto_emergencia_telefono}"
        return "No registrado"