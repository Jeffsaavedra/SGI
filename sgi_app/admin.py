from django.contrib import admin
from .models import Proveedor, Producto, Pedido

# Register your models here.

class ProveedorAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'direccion', 'telefono']
    search_fields = ['nombre', 'direccion', 'telefono']

admin.site.register(Proveedor, ProveedorAdmin)

class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'descripcion', 'proveedor', 'cantidad_disponible', 'precio_unitario']
    list_filter = ['proveedor', 'fecha_vencimiento']
    search_fields = ['nombre', 'descripcion']

    def save_model(self, request, obj, form, change):
        # Realizar una acción personalizada al guardar el producto
        obj.usuario_que_lo_agrego = request.user  # Por ejemplo, asignar el usuario que lo agregó
        super().save_model(request, obj, form, change)

admin.site.register(Producto, ProductoAdmin)

class PedidoAdmin(admin.ModelAdmin):
    list_display = ['producto', 'cantidad', 'fecha_pedido', 'fecha_entrega']
    list_filter = ['fecha_pedido', 'fecha_entrega']
    search_fields = ['producto__nombre']  # Buscar por nombre del producto

admin.site.register(Pedido, PedidoAdmin)
