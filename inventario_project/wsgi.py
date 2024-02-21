"""
Configuración WSGI para el proyecto inventario_project.

Expone el callable WSGI como una variable de nivel de módulo llamada `application`.

Para obtener más información sobre este archivo, consulta:
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# Establece la configuración de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'inventario_project.settings')

# Obtiene la aplicación WSGI
application = get_wsgi_application()
