from django.apps import AppConfig

class SgiAppConfig(AppConfig):
    """Configuración de la aplicación SGI (Sistema de Gestión de Inventario)."""
    default_auto_field = 'django.db.models.BigAutoField'  # Define el tipo de campo automático para la clave primaria
    name = 'sgi_app'  # Nombre de la aplicación
