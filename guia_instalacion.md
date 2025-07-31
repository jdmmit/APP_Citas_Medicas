# 🚀 Guía de Instalación del Entorno de Desarrollo para Aplicación de Citas Médicas (Python + Django)

¡Sigue estos pasos para tener tu entorno listo y comenzar a desarrollar tu app de citas médicas! 🩺

---

## 1. 🐍 Instalar Python

- Descarga Python desde la página oficial: [python.org/downloads](https://www.python.org/downloads/)
- Elige la versión recomendada (3.10 o superior).
- Durante la instalación, **marca la casilla "Add Python to PATH"**.
- Verifica la instalación abriendo una terminal o consola y ejecutando:
  ```
  python --version
  ```
  Debería mostrar la versión instalada ✅

---

## 2. 🌀 Instalar Git (opcional pero recomendado)

- Descarga Git desde: [git-scm.com/downloads](https://git-scm.com/downloads)
- Instala siguiendo las instrucciones para tu sistema operativo.
- Verifica la instalación:
  ```
  git --version
  ```

---

## 3. 🧪 Crear y activar un entorno virtual

- Abre una terminal en la carpeta donde guardarás tu proyecto.
- Crea el entorno virtual:
  ```
  python -m venv venv
  ```
- Activa el entorno virtual:
  - **Windows:**
    ```
    venv\Scripts\activate
    ```
  - **Linux/MacOS:**
    ```
    source venv/bin/activate
    ```
- Sabrás que está activo porque verás `(venv)` al inicio de la línea en la terminal 🟢

---

## 4. ⬆️ Actualizar pip (opcional pero recomendado)

```
pip install --upgrade pip
```

---

## 5. 🦄 Instalar Django

```
pip install django
```

- Verifica la instalación:
  ```
  python -m django --version
  ```
  Si ves la versión, ¡todo está listo! 🎉

---

## 6. 🏗️ Crear el proyecto Django

```
django-admin startproject citas_medicas
cd citas_medicas
```

---

## 7. 🧩 Crear las aplicaciones principales

Por ejemplo, para la app de usuarios:
```
python manage.py startapp usuarios
```
Repite para otras apps como `citas`, `notificaciones`, etc.

---

## 8. 📦 Instalar dependencias adicionales (opcional)

Si vas a usar Django REST Framework:
```
pip install djangorestframework
```
Agrega `'rest_framework'` a `INSTALLED_APPS` en `settings.py`.

---

## 9. 🌱 Inicializar repositorio Git (opcional pero recomendado)

```
git init
echo venv/ > .gitignore
git add .
git commit -m "Proyecto inicial de Django"
```

---

## 10. ▶️ Ejecutar el servidor de desarrollo

```
python manage.py runserver
```
Abre tu navegador y entra a [http://127.0.0.1:8000/](http://127.0.0.1:8000/) para ver tu proyecto en marcha 🚦

---

> 💡 **Consejo:** Documenta cada paso en tu `README.md` y actualiza la guía si agregas nuevas dependencias o pasos importantes. ¡La buena documentación es clave para el éxito de tu proyecto!
