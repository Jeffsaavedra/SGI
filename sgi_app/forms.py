from django import forms
from .models import Proveedor, Producto, Pedido

# Formularios para Proveedor
class ProveedorForm(forms.ModelForm):
    """Formulario para crear o actualizar un proveedor."""
    class Meta:
        model = Proveedor
        fields = ['nombre', 'direccion', 'telefono']  # Campos a incluir en el formulario
        labels = {
            'nombre': 'Nombre del proveedor',
            'direccion': 'Dirección del proveedor',
            'telefono': 'Teléfono del proveedor'
        }  # Etiquetas personalizadas para los campos
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),  # Widget para el campo nombre
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),  # Widget para el campo dirección
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),  # Widget para el campo teléfono
        }  # Widgets personalizados para los campos

class ProductoForm(forms.ModelForm):
    """Formulario para crear o actualizar un producto."""
    class Meta:
        model = Producto
        fields = '__all__'  # Todos los campos del modelo Producto

    # Opcional: puedes personalizar el formulario aquí agregando widgets o validaciones adicionales

class PedidoForm(forms.ModelForm):
    """Formulario para crear o actualizar un pedido."""
    class Meta:
        model = Pedido
        fields = ['tipo', 'proveedor', 'producto', 'cantidad', 'fecha_entrega']  # Campos a incluir en el formulario
