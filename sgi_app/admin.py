from django.contrib import admin
from .models import Proveedor, Producto, Pedido

# Registra los modelos en el panel de administración

class ProveedorAdmin(admin.ModelAdmin):
    """Clase para personalizar la visualización y búsqueda de proveedores en el panel de administración."""
    list_display = ['nombre', 'direccion', 'telefono']  # Campos a mostrar en la lista de proveedores
    search_fields = ['nombre', 'direccion', 'telefono']  # Campos por los que se puede buscar un proveedor

admin.site.register(Proveedor, ProveedorAdmin)  # Registra el modelo Proveedor con la personalización definida

class ProductoAdmin(admin.ModelAdmin):
    """Clase para personalizar la visualización, filtrado y búsqueda de productos en el panel de administración."""
    list_display = ['nombre', 'descripcion', 'proveedor', 'cantidad_disponible', 'precio_unitario']  # Campos a mostrar en la lista de productos
    list_filter = ['proveedor', 'fecha_vencimiento']  # Filtros laterales para facilitar la navegación
    search_fields = ['nombre', 'descripcion']  # Campos por los que se puede buscar un producto

    def save_model(self, request, obj, form, change):
        """Método para realizar acciones personalizadas al guardar un producto."""
        obj.usuario_que_lo_agrego = request.user  # Asignar el usuario que agregó el producto
        super().save_model(request, obj, form, change)  # Llama al método save_model de la clase base

admin.site.register(Producto, ProductoAdmin)  # Registra el modelo Producto con la personalización definida

class PedidoAdmin(admin.ModelAdmin):
    """Clase para personalizar la visualización, filtrado y búsqueda de pedidos en el panel de administración."""
    list_display = ['tipo','proveedor','producto', 'cantidad', 'fecha_pedido', 'fecha_entrega']  # Campos a mostrar en la lista de pedidos
    list_filter = ['fecha_pedido', 'fecha_entrega', 'tipo','proveedor']  # Filtros laterales para facilitar la navegación
    search_fields = ['producto__nombre']  # Campos por los que se puede buscar un pedido (en este caso, nombre del producto)

admin.site.register(Pedido, PedidoAdmin)  # Registra el modelo Pedido con la personalización definida
