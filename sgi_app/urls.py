from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import (ProveedorListCreate, ProductoListCreate, 
                    PedidoListCreate, ProductoDetail, 
                    ProductoRetrieveUpdateDestroy, PedidoDetail, 
                    PedidoRetrieveUpdateDestroy, ProveedorDetail, 
                    ProveedorRetrieveUpdateDestroy)

urlpatterns = [
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),  # Para obtener tokens
    # URLS APIS PROVEEDORES
    path('api/proveedores/', ProveedorListCreate.as_view(), name='proveedor-list-create'),
    path('api/proveedores/<int:pk>/', ProveedorDetail.as_view(), name='proveedor-detail'),
    path('api/proveedores/<int:pk>/update/', ProveedorRetrieveUpdateDestroy.as_view(), name='proveedor-update'),
    path('api/proveedores/<int:pk>/delete/', ProveedorRetrieveUpdateDestroy.as_view(), name='proveedor-delete'),
    # URLS APIS PRODUCTOS 
    path('api/productos/', ProductoListCreate.as_view(), name='producto-list-create'),
    path('api/productos/<int:pk>/', ProductoDetail.as_view(), name='producto-detail'),
    path('api/productos/<int:pk>/update/', ProductoRetrieveUpdateDestroy.as_view(), name='producto-update'),
    path('api/productos/<int:pk>/delete/', ProductoRetrieveUpdateDestroy.as_view(), name='producto-delete'),
    # URLS APIS PEDIDOS 
    path('api/pedidos/', PedidoListCreate.as_view(), name='pedido-list-create'),
    path('api/pedidos/<int:pk>/', PedidoDetail.as_view(), name='pedido-detail'),
    path('api/pedidos/<int:pk>/update/', PedidoRetrieveUpdateDestroy.as_view(), name='pedido-update'),
    path('api/pedidos/<int:pk>/delete/', PedidoRetrieveUpdateDestroy.as_view(), name='pedido-delete'),
]


