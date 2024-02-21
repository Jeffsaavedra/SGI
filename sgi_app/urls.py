from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import ProveedorListCreate, ProductoListCreate, PedidoListCreate

urlpatterns = [
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),  # Para obtener tokens
    path('api/proveedores/', ProveedorListCreate.as_view(), name='proveedor-list-create'),
    path('api/productos/', ProductoListCreate.as_view(), name='producto-list-create'),
    path('api/pedidos/', PedidoListCreate.as_view(), name='pedido-list-create'),
]
