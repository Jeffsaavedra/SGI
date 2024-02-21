from rest_framework import serializers
from .models import Proveedor, Producto, Pedido

# Serializador para el modelo Proveedor
class ProveedorSerializer(serializers.ModelSerializer):
    """
    Serializador para convertir objetos Proveedor en representaciones JSON y viceversa.
    """
    class Meta:
        model = Proveedor
        fields = '__all__'  # Incluir todos los campos del modelo

# Serializador para el modelo Producto
class ProductoSerializer(serializers.ModelSerializer):
    """
    Serializador para convertir objetos Producto en representaciones JSON y viceversa.
    """
    class Meta:
        model = Producto
        fields = '__all__'  # Incluir todos los campos del modelo

# Serializador para el modelo Pedido
class PedidoSerializer(serializers.ModelSerializer):
    """
    Serializador para convertir objetos Pedido en representaciones JSON y viceversa.
    """
    class Meta:
        model = Pedido
        fields = '__all__'  # Incluir todos los campos del modelo
