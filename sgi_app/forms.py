from django import forms
from .models import Proveedor,Producto,Pedido

# fORMS PARA PROVEEDOR
class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['nombre', 'direccion', 'telefono']
        labels = {
            'nombre': 'Nombre del proveedor',
            'direccion': 'Dirección del proveedor',
            'telefono': 'Teléfono del proveedor'
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'  # Todos los campos del modelo

    # Opcional: puedes personalizar el formulario aquí agregando widgets o validaciones adicionales

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['tipo', 'proveedor', 'producto', 'cantidad', 'fecha_entrega']

