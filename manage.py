#!/usr/bin/env python
"""
Utilidad de línea de comandos de Django para tareas administrativas.

Este script te permite interactuar con varios comandos de Django
para administrar tu proyecto desde la línea de comandos.
"""
import os
import sys


def main():
    """
    Ejecuta tareas administrativas.

    Esta función configura el entorno de Django y ejecuta
    el comando apropiado según los argumentos proporcionados.
    """
     # Establece la variable de entorno DJANGO_SETTINGS_MODULE para que apunte al archivo de configuración de tu proyecto
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'inventario_project.settings')
    try:
        # Importa la función execute_from_command_line del módulo de gestión de Django
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # Maneja ImportError si Django no está instalado o no está disponible
        raise ImportError(
            "No se pudo importar Django. ¿Estás seguro de que está instalado y "
            "disponible en tu variable de entorno PYTHONPATH? ¿Olvidaste activar "
            "un entorno virtual?"
        ) from exc
    # Ejecuta el comando apropiado según los argumentos pasados al script
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    # Llama a la función main cuando el script se ejecuta directamente
    main()