"""
Configuraciones de Django para el proyecto inventario_project.

Generado por 'django-admin startproject' utilizando Django 5.0.2.

Para obtener más información sobre este archivo, consulta
https://docs.djangoproject.com/en/5.0/topics/settings/

Para ver la lista completa de configuraciones y sus valores, consulta
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path

# Directorio base del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent


# Configuraciones de desarrollo rápido - no adecuadas para producción
# Consulta https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# Clave secreta - DEBE mantenerse en secreto en producción
SECRET_KEY = 'django-insecure-dwod66$id4)07ipkt+^^(ek&jrtka!&*k*-)v(0)wqb2*e)aoq'

# Depuración - DEBE establecerse en False en producción
DEBUG = True

# Hosts permitidos en producción
ALLOWED_HOSTS = []


# Definición de aplicaciones instaladas
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Agrega las nuevas aplicaciones aquí, por ejemplo:
    'sgi_app',
    'rest_framework',
    'rest_framework.authtoken'
]

# Middleware utilizado por Django
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Configuración de las URLs raíz del proyecto
ROOT_URLCONF = 'inventario_project.urls'

# Configuración de los templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Configuración de la aplicación WSGI para servir el proyecto
WSGI_APPLICATION = 'inventario_project.wsgi.application'


# Configuración de la base de datos
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Validación de contraseñas
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Configuraciones de internacionalización
LANGUAGE_CODE = 'es-co'  # Idioma español para Colombia
TIME_ZONE = 'America/Bogota'  # Zona horaria de Colombia
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Configuraciones de archivos estáticos (CSS, JavaScript, Imágenes)
STATIC_URL = '/static/'

# Tipo de campo de clave primaria predeterminado
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Configuración de autenticación para la API REST
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
}
