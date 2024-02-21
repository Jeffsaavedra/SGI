"""
Configuración de URLs para el proyecto inventario_project.

La lista `urlpatterns` enruta URLs a vistas. Para obtener más información, consulta:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/

Ejemplos:
Vistas basadas en funciones
    1. Agrega una importación: from my_app import views
    2. Agrega una URL a urlpatterns: path('', views.home, name='home')
Vistas basadas en clases
    1. Agrega una importación: from other_app.views import Home
    2. Agrega una URL a urlpatterns: path('', Home.as_view(), name='home')
Incluir otro URLconf
    1. Importa la función include(): from django.urls import include, path
    2. Agrega una URL a urlpatterns: path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # URL para la interfaz de administración de Django
    path('', include('sgi_app.urls')),  # Incluye las rutas de la aplicación sgi_app
]
