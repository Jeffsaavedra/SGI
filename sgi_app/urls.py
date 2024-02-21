from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import (ProveedorListCreate, ProductoListCreate,
                    PedidoListCreate, ProductoDetail, 
                    ProductoRetrieveUpdateDestroy, PedidoDetail, 
                    PedidoRetrieveUpdateDestroy, ProveedorDetail, 
                    ProveedorRetrieveUpdateDestroy,
                    lista_proveedores, detalle_proveedor, 
                    CrearProveedor, ActualizarProveedor, 
                    EliminarProveedor,
                    lista_productos,
                    detalle_producto,
                    crear_producto,
                    actualizar_producto,
                    eliminar_producto,
                    lista_pedidos, detalle_pedido, 
                    crear_pedido, actualizar_pedido, 
                    eliminar_pedido, index,
    )

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
    #URL INICIAL
    path('', index, name='index'),
    #URLS PROVEEDORES 
    path('proveedores/', lista_proveedores, name='lista_proveedores'),
    path('proveedores/<int:pk>/', detalle_proveedor, name='detalle_proveedor'),
    path('proveedores/crear/', CrearProveedor.as_view(), name='crear_proveedor'),
    path('proveedores/<int:pk>/actualizar/', ActualizarProveedor.as_view(), name='actualizar_proveedor'),
    path('proveedores/<int:pk>/eliminar/', EliminarProveedor.as_view(), name='eliminar_proveedor'),
    #URLS PRODUCTOS
    path('productos/', lista_productos, name='lista_productos'),
    path('productos/<int:pk>/', detalle_producto, name='detalle_producto'),
    path('productos/crear/', crear_producto, name='crear_producto'),
    path('productos/<int:pk>/actualizar/', actualizar_producto, name='actualizar_producto'),
    path('productos/<int:pk>/eliminar/', eliminar_producto, name='eliminar_producto'),
    #URLS PEDIDOS
    path('pedidos/', lista_pedidos, name='lista_pedidos'),
    path('pedidos/<int:pk>/', detalle_pedido, name='detalle_pedido'),
    path('pedidos/crear/', crear_pedido, name='crear_pedido'),
    path('pedidos/<int:pk>/actualizar/', actualizar_pedido, name='actualizar_pedido'),
    path('pedidos/<int:pk>/eliminar/', eliminar_pedido, name='eliminar_pedido'),    
        
        ]


