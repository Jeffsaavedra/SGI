from django.urls import path
from .views import ProveedorListCreate, ProductoListCreate, PedidoListCreate

urlpatterns = [
    path('proveedores/', ProveedorListCreate.as_view(), name='proveedor-list-create'),
    path('productos/', ProductoListCreate.as_view(), name='producto-list-create'),
    path('pedidos/', PedidoListCreate.as_view(), name='pedido-list-create'),
]
