from django.db import models

# Modelo para Proveedor
class Proveedor(models.Model):
    """
    Modelo para representar un proveedor.
    """
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return self.nombre

# Modelo para Producto
class Producto(models.Model):
    """
    Modelo para representar un producto.
    """
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    cantidad_disponible = models.PositiveIntegerField(default=0)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_vencimiento = models.DateField()

    def __str__(self):
        return self.nombre

# Modelo para Pedido
class Pedido(models.Model):
    """
    Modelo para representar pedidos de compra y venta.
    """
    TIPO_CHOICES = (
        ('COMPRA', 'Compra'),
        ('VENTA', 'Venta'),
    )

    tipo = models.CharField(max_length=6, choices=TIPO_CHOICES, null=True)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, null=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    fecha_pedido = models.DateField(auto_now_add=True)
    fecha_entrega = models.DateField()

    def __str__(self):
        return f"Pedido de {self.producto.nombre} ({self.cantidad} unidades)"
