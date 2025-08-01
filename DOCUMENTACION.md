# Documentación del Proyecto APP_Citas_Medicas

## Descripción General

APP_Citas_Medicas es una aplicación web desarrollada con Django para la gestión de citas médicas. Permite a los usuarios registrarse, iniciar sesión, gestionar su perfil y administrar sus citas médicas de manera eficiente y segura.

## Estructura del Proyecto

```
APP_Citas_Medicas/
├── citas_medicas/           # Configuración principal del proyecto Django
│   ├── settings.py          # Configuraciones del proyecto
│   ├── urls.py              # Definición de rutas URL principales
│   ├── wsgi.py              # Configuración para despliegue WSGI
│   └── asgi.py              # Configuración para despliegue ASGI
├── usuarios/                # Aplicación para gestión de usuarios
│   ├── templates/           # Plantillas HTML
│   │   ├── base.html        # Plantilla base con estructura común
│   │   ├── home.html        # Página de inicio
│   │   ├── registro.html    # Formulario de registro
│   │   ├── login.html       # Formulario de inicio de sesión
│   │   └── ...              # Otras plantillas
│   ├── static/              # Archivos estáticos
│   │   ├── css/             # Hojas de estilo
│   │   ├── js/              # Scripts JavaScript
│   │   └── img/             # Imágenes
│   ├── views.py             # Vistas de la aplicación
│   ├── models.py            # Modelos de datos
│   └── urls.py              # Definición de rutas URL de la aplicación
├── staticfiles/             # Archivos estáticos recopilados para producción
└── manage.py                # Script de gestión de Django
```

## Tecnologías Utilizadas

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Base de Datos**: SQLite (desarrollo)
- **Iconos**: Font Awesome
- **Fuentes**: Google Fonts

## Componentes Principales

### 1. Estructura Base (base.html)

La plantilla base proporciona la estructura común para todas las páginas, incluyendo:

- Encabezado con logo y navegación
- Menú de navegación adaptable (responsive)
- Sistema de mensajes para notificaciones
- Pie de página con información de contacto y enlaces rápidos

### 2. Estilos (styles.css)

El archivo de estilos define la apariencia visual de la aplicación:

- Variables CSS para colores y fuentes consistentes
- Diseño responsive para adaptarse a diferentes dispositivos
- Estilos para componentes como botones, formularios, tarjetas y alertas
- Clases de utilidad para márgenes, padding y alineación

### 3. JavaScript (main.js)

Proporciona interactividad a la aplicación:

- Funcionalidad del menú hamburguesa para dispositivos móviles
- Manejo de la navegación activa
- Sistema de alertas con cierre automático
- Animaciones para tarjetas y elementos interactivos

### 4. Vistas (views.py)

Contiene las funciones que manejan las solicitudes HTTP y renderizan las plantillas:

- `home`: Página de inicio
- `registro`: Registro de usuarios
- `login`: Inicio de sesión
- `perfil`: Visualización del perfil de usuario
- `editar_perfil`: Edición de información del perfil
- `cambiar_contraseña`: Cambio de contraseña
- `eliminar_cuenta`: Eliminación de cuenta de usuario
- `notificaciones`: Visualización de notificaciones

### 5. URLs (urls.py)

Define las rutas URL de la aplicación:

- Rutas para páginas principales (inicio, registro, login)
- Rutas para gestión de perfil (ver, editar, cambiar contraseña, eliminar)
- Rutas para funcionalidades adicionales (notificaciones)

## Funcionalidades Implementadas

### Gestión de Usuarios

- Registro de nuevos usuarios
- Inicio de sesión
- Visualización y edición de perfil
- Cambio de contraseña
- Eliminación de cuenta

### Sistema de Notificaciones

- Visualización de notificaciones del usuario
- Ejemplos de notificaciones incluyen confirmaciones de citas, recordatorios y actualizaciones de perfil

### Interfaz Responsive

- Diseño adaptable para dispositivos móviles y de escritorio
- Menú hamburguesa para navegación en dispositivos pequeños
- Estilos optimizados para diferentes tamaños de pantalla

## Guía de Desarrollo

### Configuración del Entorno

1. Clonar el repositorio
2. Crear y activar un entorno virtual
3. Instalar dependencias: `pip install -r requirements.txt`
4. Aplicar migraciones: `python manage.py migrate`
5. Iniciar servidor de desarrollo: `python manage.py runserver`

### Estructura de Archivos Estáticos

- Los archivos CSS se encuentran en `staticfiles/css/`
- Los archivos JavaScript se encuentran en `staticfiles/js/`
- Las imágenes se encuentran en `staticfiles/img/`

### Plantillas HTML

Todas las plantillas extienden de `base.html` y utilizan el sistema de plantillas de Django:

```html
{% extends "base.html" %}

{% block content %}
<!-- Contenido específico de la página -->
{% endblock %}
```

## Próximas Mejoras

- Implementación de formularios funcionales para registro y login
- Desarrollo de modelos de datos para citas médicas
- Integración de un sistema de reserva de citas
- Implementación de un panel de administración para médicos
- Añadir sistema de notificaciones en tiempo real

## Contacto

Para más información sobre el proyecto, contactar a:
- Email: soporte@medicitas.com
- Teléfono: +1 (555) 123-4567

---

© 2023 MediCitas. Todos los derechos reservados.