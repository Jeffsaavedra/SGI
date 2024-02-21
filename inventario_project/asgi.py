"""
Configuración ASGI para el proyecto inventario_project.

Exponiendo la aplicación ASGI como una variable de nivel de módulo llamada ``application``.

Para obtener más información sobre este archivo, consulta
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

# Configura la variable de entorno DJANGO_SETTINGS_MODULE con la configuración del proyecto.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'inventario_project.settings')

# Obtiene la aplicación ASGI para la configuración del proyecto.
application = get_asgi_application()
