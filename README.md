
# **Sistema de Gestión de Inventario (SGI)**

Este proyecto es un Sistema de Gestión de Inventario (SGI) desarrollado utilizando Django y Django Rest Framework para la creación de una API RESTful.

A continuación se detalla el paso a paso para ejecutar el proyecto


## **1.  Creacion de un entorno virtual**

 - [Guia Windows](https://micro.recursospython.com/recursos/como-crear-un-entorno-virtual-venv.html)

1. Abre una terminal y ubícate en el directorio en donde deseas crear el entorno virtual
2. Ejecuta ```python -m venv mi_entorno```
3. Ejecuta ```mi_entorno\Scripts\activate```
4. Puedes activar el entorno virtual también haciendo ```mi_entorno\Scripts\activate.bat```, es exactamente lo mismo.

Nota:
    Se recomienda nombrar tu entorno como env o venv.


## **2. Instalacion**

## 2.1 Instalación (opción 1)

Instala el framework django

```python
pip install django
```
    
Instala django-rest-framework
```
  pip install djangorestframework

```
## 2.2 clonar e instalar (opción 2)

En caso que desees clonar y ejecutar este proyecto has esto:

1. Clona el repositorio
```python
git clone <url_del_repositorio>
```
2. ingresa al directorio del proyecto `inventario_project`
```python
cd inventario_project
```
3. Instala los requerimientos

```python
pip install requirements.txt
```
4. Salta a la parte 9 para probar el proyecto, la parte 10 Para ingresar a las urls de los templates y la parte 11 para poder acceder a la autenticación de token


## **3. Empezamos con el proyecto**

Creamos el proyecto de nombre `inventario_project`
```
django-admin startproject inventario_project
```

Accedemos dentro de la carpeta del proyecto `inventario_app`

```
cd inventario_project
```

Creamos una aplicacion sgi_app (sistema de gatión de Inventario) dentro del proyecto
```
python manage.py startapp sgi_app
```

Ahora dentro en la carpeta `inventario_project/settings.py`

debemos agregar lo siguiente en `INSTALLED_APPS` el nombre de nuestra aplicacion
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Agrega las nuevas aplicaciones aquí, por ejemplo:
    'sgi_app',
    'rest_framework',
]
```
También debemos hacer ciertas configuraciones adicionales en settings.py 

- **Configuración de las `settings.py`:**
  - `ALLOWED_HOSTS`: Agregar 'localhost' y '127.0.0.1'.
  - `INSTALLED_APPS`: Agregar 'sgi_app'.
  - `LANGUAGE_CODE`: Cambiar a 'es-co' (español para Colombia).
  - `TIME_ZONE`: Cambiar a 'America/Bogota' (zona horaria de Colombia).


## **4. Definimos el modelo**

En el archivo `sgi_app/models.py`

- se define el modelo Proveedor para representar un proveedor de productos.
    - Atributos:
        - nombre (str): Nombre del proveedor.
        - direccion (str): Dirección del proveedor.
        - telefono (str): Número de teléfono del proveedor.
- Se define el modelo Producto para representar un producto en el inventario.
    - Atributos:
        - nombre (str): Nombre del producto.
        - descripcion (str): Descripción del producto.
        - proveedor (Proveedor): Proveedor del producto.
        - cantidad_disponible (int): Cantidad disponible del producto en el inventario.
        - precio_unitario (Decimal): Precio unitario del producto.
- Se define un modelo Pedido para representar un pedido de productos.
    - Atributos:
        - producto (Producto): Producto pedido.
        - cantidad (int): Cantidad del producto en el pedido.
        - fecha_pedido (date): Fecha en que se realizó el pedido.
        - fecha_entrega (date): Fecha de entrega del pedido.

Se vería así:

```python
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


```

Ahora realizamos migraciones de la siguiente manera:

1. Con el siguiente comango creas migraciones para tus modelos definiendo la estructura la base de datos

``` 
python manage.py makemigrations

```
2. Después, con el siguiente comando aplica las migraciones para crear la tabla en la base de datos

```
python manage.py migrate
```
Si puedes observar la base de datos `db.sqlite3` ya se encuentran creadas las tablas

Nota:
    Si quieres visualizar las tablas es recomendable descargar alguna de la siguientes opciones: 

- [DB Browser for SQLite](https://sqlitebrowser.org/dl/)
- Extensión de VSC SQLite Viewer (si estás trabajando con Visual Studio Code)


## **5. Registrar los modelos en Admin**
Ahora debes realizar la personalización del panel de administración de Django para gestionar los modelos creados en el archivo admin.py, si no lo tienes crealo dentro de `sgi_app`.

El archivo debe verse así:
```python
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

```


## **6. Serializando**

Debes serializers para transformar los modelos Django en JSON y viceversa, utilizando tanto serializers simples como ModelSerializer.

Asi que creamos el archivo `sgi_app/serializers.py`:
```python
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

```


## **7. Vista para la API**

Realizar la implementación de las vistas basadas en clases para la api.

En el archivo `sgi_app/views.py`

```python
# Create your views here.
from django.shortcuts import render
from rest_framework import generics
from .models import Proveedor, Producto, Pedido
from .serializers import ProveedorSerializer, ProductoSerializer, PedidoSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import status
from django.http import Http404

# ------------------------------->>>>>>>>>>>>VISTAS PROVEEDOR<<<<<<<<<-----------------------------------
# Vista para listar y crear proveedores
class ProveedorListCreate(generics.ListCreateAPIView):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer
    
# Vista para ver, actualizar y eliminar un proveedor
class ProveedorRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer

# Vista para obtener detalles de un proveedor
class ProveedorDetail(APIView):
    def get_object(self, pk):
        try:
            return Proveedor.objects.get(pk=pk)
        except Proveedor.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        proveedor = self.get_object(pk)
        serializer = ProveedorSerializer(proveedor)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        proveedor = self.get_object(pk)
        serializer = ProveedorSerializer(proveedor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        proveedor = self.get_object(pk)
        proveedor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# ------------------------------->>>>>>>>>>>>VISTAS PRODUCTO<<<<<<<<<-----------------------------------
# Vista para listar y crear productos
class ProductoListCreate(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

# Vista para ver, actualizar y eliminar un producto
class ProductoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

# Vista para obtener detalles de un producto
class ProductoDetail(APIView):
    def get_object(self, pk):
        try:
            return Producto.objects.get(pk=pk)
        except Producto.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        producto = self.get_object(pk)
        serializer = ProductoSerializer(producto)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        producto = self.get_object(pk)
        serializer = ProductoSerializer(producto, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        producto = self.get_object(pk)
        producto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# ------------------------------->>>>>>>>>>>>VISTAS PEDIDO<<<<<<<<<-----------------------------------
# Vista para listar y crear pedidos
class PedidoListCreate(generics.ListCreateAPIView):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

# Vista para ver, actualizar y eliminar un pedido
class PedidoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

# Vista para obtener detalles de un pedido
class PedidoDetail(APIView):
    def get_object(self, pk):
        try:
            return Pedido.objects.get(pk=pk)
        except Pedido.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        pedido = self.get_object(pk)
        serializer = PedidoSerializer(pedido)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        pedido = self.get_object(pk)
        serializer = PedidoSerializer(pedido, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        pedido = self.get_object(pk)
        pedido.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
```

El término "generic" en GenericAPIView se refiere a que esta clase proporciona una serie de comportamientos genéricos que son comunes en muchas API web, como la creación, recuperación, actualización y eliminación (CRUD) de objetos. Esta clase sirve como base para vistas que interactúan con modelos de base de datos de una manera genérica y reutilizable.

GenericAPIView no implementa directamente la lógica para operaciones CRUD, pero proporciona mixins (mezclas) que pueden ser utilizados junto con ella para añadir funcionalidades específicas. Algunos de los mixins más comunes son:

- ListAPIView: Para la recuperación de una lista de objetos.
- CreateAPIView: Para la creación de nuevos objetos.
- RetrieveAPIView: Para la recuperación de un objeto específico.
- UpdateAPIView: Para la actualización de un objeto existente.
- DestroyAPIView: Para la eliminación de un objeto.

## **8. Configuración de las URL**
Crea el archivo `urls.py` dentro de `sgi_app`, y cuando estés en `sgi_app/url.py` configura las URL para tu vista de la API:
```python
from django.urls import path
from .views import (ProveedorListCreate, ProductoListCreate,
                    PedidoListCreate, ProductoDetail, 
                    ProductoRetrieveUpdateDestroy, PedidoDetail, 
                    PedidoRetrieveUpdateDestroy, ProveedorDetail, 
                    ProveedorRetrieveUpdateDestroy,
    )

urlpatterns = [
    # Rutas para API de Proveedores
    path('api/proveedores/', ProveedorListCreate.as_view(), name='proveedor-list-create'),
    path('api/proveedores/<int:pk>/', ProveedorDetail.as_view(), name='proveedor-detail'),
    path('api/proveedores/<int:pk>/update/', ProveedorRetrieveUpdateDestroy.as_view(), name='proveedor-update'),
    path('api/proveedores/<int:pk>/delete/', ProveedorRetrieveUpdateDestroy.as_view(), name='proveedor-delete'),

    # Rutas para API de Productos
    path('api/productos/', ProductoListCreate.as_view(), name='producto-list-create'),
    path('api/productos/<int:pk>/', ProductoDetail.as_view(), name='producto-detail'),
    path('api/productos/<int:pk>/update/', ProductoRetrieveUpdateDestroy.as_view(), name='producto-update'),
    path('api/productos/<int:pk>/delete/', ProductoRetrieveUpdateDestroy.as_view(), name='producto-delete'),

    # Rutas para API de Pedidos
    path('api/pedidos/', PedidoListCreate.as_view(), name='pedido-list-create'),
    path('api/pedidos/<int:pk>/', PedidoDetail.as_view(), name='pedido-detail'),
    path('api/pedidos/<int:pk>/update/', PedidoRetrieveUpdateDestroy.as_view(), name='pedido-update'),
    path('api/pedidos/<int:pk>/delete/', PedidoRetrieveUpdateDestroy.as_view(), name='pedido-delete'),
]
```

después de esto en el archivo `urls.py` del proyecto es decir `inventario_project/urls.py`:
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # URL para la interfaz de administración de Django
    path('', include('sgi_app.urls')),  # Incluye las rutas de la aplicación sgi_app
]
```


## **9. Probamos el proyecto**

**Primero debes crear un super usuario desde la consola así:**

- Introduce y ejecuta el siguiente comando en tu terminal:

```
python manage.py createsuperuser
```
- Te va a solicitar la siguiente información, la cuál debes proporcionar:

       - username (ingresa tu nuevo nombre de ususario)
       - email (ingresa tu correo electrónico)
       - password (ingresa tu nueva contraseña)

    Nota: 
        Por seguridad la terminal no permite visualizar la contraseña mientras la escribes

- Debes ingresar al admin de la API y crear los objetos para pedidos, proveedores y productos para poderlos visualizar desde los endpoints
    
    - Ve a http://127.0.0.1:8000/admin/
    - Logueate con tu username y tu password previamente creadas
    - Crea por lo menos 1 o 2 pedidos, proveedores y productos

**Ahora vamos a ejecutar el proyecto para probar la puncionalidad de la API.**

```
python manage.py runserver
```

**Tenemos los siguientes endpoints**

Vistas DRF para Proveedores
- http://127.0.0.1:8000/api/proveedores/
- http://127.0.0.1:8000/api/proveedores/<int:pk>/
- http://127.0.0.1:8000/api/proveedores/<int:pk>/update/
- http://127.0.0.1:8000/api/proveedores/<int:pk>/delete/

Vistas DRF para Productos
- http://127.0.0.1:8000/api/productos/
- http://127.0.0.1:8000/api/productos/<int:pk>/
- http://127.0.0.1:8000/api/productos/<int:pk>/update/
- http://127.0.0.1:8000/api/productos/<int:pk>/delete/

Vistas DRF para Pedidos
- http://127.0.0.1:8000/api/pedidos/
- http://127.0.0.1:8000/api/pedidos/<int:pk>/
- http://127.0.0.1:8000/api/pedidos/<int:pk>/update/
- http://127.0.0.1:8000/api/pedidos/<int:pk>/delete/

**Debes crear algunos registros de Post para luego visualizarlos.**

Nota:
    No olvides reemplazar `<int:pk>` por el id del proveedor, producto o pedido específico.

    Por ejemplo: 
        - http://127.0.0.1:8000/api/pedidos/1/
        - http://127.0.0.1:8000/api/pedidos/1/
        - http://127.0.0.1:8000/api/pedidos/1/update/
        - http://127.0.0.1:8000/api/pedidos/1/delete/

Nota importante:
    si vienes de clonar este repositorio te aparecerá que no proporcionaste las credenciales para visualizar los objetos.

**Tambien ve probando con POSTMAN `https://www.postman.com/` o la extension de VSCode**


## **10. Django Templates**

**En este paso debemos hacer lo siguiente:**

- Desarrollar templates Django para la renderización de HTML en el frontend, utilizando la sintaxis de templates de Django para mostrar datos dinámicos.

- Uso de css y configuración de los templates para una vejor vista de acuerdo a las preferencias.

Así:

1. Crea la carpeta templates dentro de `sgi_app`.

2. Ahora dentro de `sgi_app/templates` debes crear tus templates con html.

Nota:
    Ve a `sgi_app/templates` en este repositorio si deseas ver o usar los templates para tu proyecto. En total son 16 templates usado en este proyecto.

3. Para los estilos e imagenes como iconos creamos la carpeta `static` dentro de `sgi_app`.

4. Dentro de la carpeta static crea la carpeta `sgi_app` para almacenar el archivo `css` para los estilos de los templates.

5. Crea el archivo `styles.css` dentro de `static/sgi_app` con los estilos que desees para tus templates.

`sgi_app/static/sgi_app/style.css`
```css
/* Estilos generales */

/* Configuración del cuerpo de la página */
body {
    font-family: Arial, sans-serif; /* Fuente y familia de fuentes para el texto */
    margin: 20px; /* Margen externo */
    padding: 20px; /* Relleno interno */
    background-color: #f4f4f4; /* Color de fondo */
}

/* Estilo para contenedores principales */
.container {
    max-width: 800px; /* Ancho máximo del contenedor */
    margin: 0 auto; /* Centrar horizontalmente */
    background-color: #8fd1fbe2; /* Color de fondo */
    padding: 20px; /* Relleno interno */
    border-radius: 2px; /* Bordes redondeados */
    box-shadow: 0 0 15px rgba(0, 0, 0, 0.656); /* Sombra */
    text-align: center; /* Alineación del texto al centro */
}

/* Estilo para otro tipo de contenedor */
.container2 {
    max-width: 800px; /* Ancho máximo del contenedor */
    margin: 0 auto; /* Centrar horizontalmente */
    background-color: #8fd1fbe2; /* Color de fondo */
    padding: 20px; /* Relleno interno */
    border-radius: 22px; /* Bordes redondeados */
    box-shadow: 0 0 15px rgba(0, 0, 0, 0.656); /* Sombra */
    text-align: start; /* Alineación del texto a la izquierda */
}

/* Estilo para otro tipo de contenedor */
.container3 {
    max-width: 800px; /* Ancho máximo del contenedor */
    margin: 0 auto; /* Centrar horizontalmente */
    background-color: #0b459de2; /* Color de fondo */
    padding: 20px; /* Relleno interno */
    border-radius: 2px; /* Bordes redondeados */
    box-shadow: 0 0 15px rgba(0, 0, 0, 0.656); /* Sombra */
    text-align: center; /* Alineación del texto al centro */
}

/* Estilos para títulos */
h1, h2 {
    text-align: center; /* Alineación del texto al centro */
}

h1 {
    color: #333; /* Color del texto */
}

h2 {
    color: #555; /* Color del texto */
}

/* Estilos para párrafos de fecha */
p.date {
    color: #999; /* Color del texto */
    font-style: italic; /* Estilo de fuente cursiva */
}

/* Estilos para botones */
button {
    padding: 10px 20px; /* Relleno interno */
    background-color: #1483f9; /* Color de fondo del botón */
    color: #fff; /* Color del texto del botón */
    border: none; /* Sin borde */
    border-radius: 5px; /* Bordes redondeados */
    cursor: pointer; /* Cambio de cursor al pasar sobre el botón */
    box-shadow: 0 2px 4px rgba(42, 40, 40, 0.1); /* Sombra */
}

/* Estilos al pasar el mouse sobre el botón */
button:hover {
    background-color: #0457b0; /* Cambiar el color de fondo al pasar el mouse sobre el botón */
    border-radius: 15px; /* Bordes redondeados */
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2); /* Cambiar la sombra al pasar el mouse sobre el botón */
}

```

6. Después de esto verifica que tú arbol de archivos quede así:

```
inventario_project/
│
├── sgi_app/
│   ├── migrations/
│   ├── static/
│   │   └── sgi_app/
│   │       └── style.css
│   ├── templates/
│   │   ├── base.html
│   │   └── post_list.html
|   │   └── post_detail.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
│
├── inventario_project/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
└── manage.py
```

7. Ahora hay que crear y agregar los endpoints para estos templates. Asi que actualizamos el archivo `sgi_app/views.py` quedando ahora así:

```python
# Create your views here.
from django.shortcuts import render
from rest_framework import generics
from .models import Proveedor, Producto, Pedido
from .serializers import ProveedorSerializer, ProductoSerializer, PedidoSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import status
from django.http import Http404

# ------------------------------->>>>>>>>>>>>VISTAS PROVEEDOR<<<<<<<<<-----------------------------------
# Vista para listar y crear proveedores
class ProveedorListCreate(generics.ListCreateAPIView):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer
    
# Vista para ver, actualizar y eliminar un proveedor
class ProveedorRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer

# Vista para obtener detalles de un proveedor
class ProveedorDetail(APIView):
    def get_object(self, pk):
        try:
            return Proveedor.objects.get(pk=pk)
        except Proveedor.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        proveedor = self.get_object(pk)
        serializer = ProveedorSerializer(proveedor)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        proveedor = self.get_object(pk)
        serializer = ProveedorSerializer(proveedor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        proveedor = self.get_object(pk)
        proveedor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
# Vistas renderizadas para templates de proveedor-------------------------------------------------------------------------
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Proveedor
from .forms import ProveedorForm

# Vista para mostrar la lista de proveedores
def lista_proveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'lista_proveedores.html', {'proveedores': proveedores})

# Vista para ver los detalles de un proveedor
def detalle_proveedor(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    return render(request, 'detalle_proveedor.html', {'proveedor': proveedor})

# Vista para crear un nuevo proveedor
class CrearProveedor(CreateView):
    model = Proveedor
    form_class = ProveedorForm
    template_name = 'crear_proveedor.html'
    success_url = '/proveedores/'

# Vista para actualizar un proveedor existente
class ActualizarProveedor(UpdateView):
    model = Proveedor
    form_class = ProveedorForm
    template_name = 'actualizar_proveedor.html'
    success_url = '/proveedores/'

# Vista para eliminar un proveedor existente
class EliminarProveedor(DeleteView):
    model = Proveedor
    template_name = 'eliminar_proveedor.html'
    success_url = '/proveedores/'

# ------------------------------->>>>>>>>>>>>VISTAS PRODUCTO<<<<<<<<<-----------------------------------
# Vista para listar y crear productos
class ProductoListCreate(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

# Vista para ver, actualizar y eliminar un producto
class ProductoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

# Vista para obtener detalles de un producto
class ProductoDetail(APIView):
    def get_object(self, pk):
        try:
            return Producto.objects.get(pk=pk)
        except Producto.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        producto = self.get_object(pk)
        serializer = ProductoSerializer(producto)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        producto = self.get_object(pk)
        serializer = ProductoSerializer(producto, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        producto = self.get_object(pk)
        producto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
# Vistas renderizadas para templates de producto-------------------------------------------------------------------------

from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .forms import ProductoForm

# Vista para mostrar la lista de productos
def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'lista_productos.html', {'productos': productos})

# Vista para ver los detalles de un producto
def detalle_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    return render(request, 'detalle_producto.html', {'producto': producto})

# Vista para crear un nuevo producto
def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm()
    return render(request, 'crear_producto.html', {'form': form})

# Vista para actualizar un producto existente
def actualizar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('detalle_producto', pk=pk)
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'actualizar_producto.html', {'form': form})

# Vista para eliminar un producto existente
def eliminar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto.delete()
        return redirect('lista_productos')
    return render(request, 'eliminar_producto.html', {'producto': producto})

# ------------------------------->>>>>>>>>>>>VISTAS PEDIDO<<<<<<<<<-----------------------------------
# Vista para listar y crear pedidos
class PedidoListCreate(generics.ListCreateAPIView):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

# Vista para ver, actualizar y eliminar un pedido
class PedidoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

# Vista para obtener detalles de un pedido
class PedidoDetail(APIView):
    def get_object(self, pk):
        try:
            return Pedido.objects.get(pk=pk)
        except Pedido.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        pedido = self.get_object(pk)
        serializer = PedidoSerializer(pedido)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        pedido = self.get_object(pk)
        serializer = PedidoSerializer(pedido, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        pedido = self.get_object(pk)
        pedido.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
# Vistas renderizadas para templates de pedidos-------------------------------------------------------------------------
from django.shortcuts import render, redirect, get_object_or_404
from .models import Pedido
from .forms import PedidoForm

# Vista para mostrar la lista de pedidos
def lista_pedidos(request):
    pedidos = Pedido.objects.all()
    return render(request, 'lista_pedidos.html', {'pedidos': pedidos})

# Vista para ver los detalles de un pedido
def detalle_pedido(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk)
    return render(request, 'detalle_pedido.html', {'pedido': pedido})

# Vista para crear un nuevo pedido
def crear_pedido(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_pedidos')
    else:
        form = PedidoForm()
    return render(request, 'crear_pedido.html', {'form': form})

# Vista para actualizar un pedido existente
def actualizar_pedido(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk)
    if request.method == 'POST':
        form = PedidoForm(request.POST, instance=pedido)
        if form.is_valid():
            form.save()
            return redirect('detalle_pedido', pk=pk)
    else:
        form = PedidoForm(instance=pedido)
    return render(request, 'actualizar_pedido.html', {'form': form})

# Vista para eliminar un pedido existente
def eliminar_pedido(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk)
    if request.method == 'POST':
        pedido.delete()
        return redirect('lista_pedidos')
    return render(request, 'eliminar_pedido.html', {'pedido': pedido})

# ------------------------------->>>>>>>>>>>>VISTA INICIAL<<<<<<<<<-------------------------------------
# Vista para renderizar el template de index
def index(request):
    return render(request, 'index.html')
```

8. Por último debemos crear y actualizar las urls (endpoints) para estos renders en el archivo `sgi_app/urls.py`

```python
from django.urls import path
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
    # Rutas para API de Proveedores
    path('api/proveedores/', ProveedorListCreate.as_view(), name='proveedor-list-create'),
    path('api/proveedores/<int:pk>/', ProveedorDetail.as_view(), name='proveedor-detail'),
    path('api/proveedores/<int:pk>/update/', ProveedorRetrieveUpdateDestroy.as_view(), name='proveedor-update'),
    path('api/proveedores/<int:pk>/delete/', ProveedorRetrieveUpdateDestroy.as_view(), name='proveedor-delete'),

    # Rutas para API de Productos
    path('api/productos/', ProductoListCreate.as_view(), name='producto-list-create'),
    path('api/productos/<int:pk>/', ProductoDetail.as_view(), name='producto-detail'),
    path('api/productos/<int:pk>/update/', ProductoRetrieveUpdateDestroy.as_view(), name='producto-update'),
    path('api/productos/<int:pk>/delete/', ProductoRetrieveUpdateDestroy.as_view(), name='producto-delete'),

    # Rutas para API de Pedidos
    path('api/pedidos/', PedidoListCreate.as_view(), name='pedido-list-create'),
    path('api/pedidos/<int:pk>/', PedidoDetail.as_view(), name='pedido-detail'),
    path('api/pedidos/<int:pk>/update/', PedidoRetrieveUpdateDestroy.as_view(), name='pedido-update'),
    path('api/pedidos/<int:pk>/delete/', PedidoRetrieveUpdateDestroy.as_view(), name='pedido-delete'),

    # Ruta inicial
    path('', index, name='index'),

    # Rutas para las vistas de Proveedores
    path('proveedores/', lista_proveedores, name='lista_proveedores'),
    path('proveedores/<int:pk>/', detalle_proveedor, name='detalle_proveedor'),
    path('proveedores/crear/', CrearProveedor.as_view(), name='crear_proveedor'),
    path('proveedores/<int:pk>/actualizar/', ActualizarProveedor.as_view(), name='actualizar_proveedor'),
    path('proveedores/<int:pk>/eliminar/', EliminarProveedor.as_view(), name='eliminar_proveedor'),

    # Rutas para las vistas de Productos
    path('productos/', lista_productos, name='lista_productos'),
    path('productos/<int:pk>/', detalle_producto, name='detalle_producto'),
    path('productos/crear/', crear_producto, name='crear_producto'),
    path('productos/<int:pk>/actualizar/', actualizar_producto, name='actualizar_producto'),
    path('productos/<int:pk>/eliminar/', eliminar_producto, name='eliminar_producto'),

    # Rutas para las vistas de Pedidos
    path('pedidos/', lista_pedidos, name='lista_pedidos'),
    path('pedidos/<int:pk>/', detalle_pedido, name='detalle_pedido'),
    path('pedidos/crear/', crear_pedido, name='crear_pedido'),
    path('pedidos/<int:pk>/actualizar/', actualizar_pedido, name='actualizar_pedido'),
    path('pedidos/<int:pk>/eliminar/', eliminar_pedido, name='eliminar_pedido'),    
]

```
## **11. Administración DRF (autenticacion basada en token)**
 
**Proceso de verificar la identidad mediante la comprobación de un token** 

Un `token` es un elemento simbólico que expide una fuente de confianza. Pensemos en cómo los policías llevan consigo una insignia expedida por las autoridades que legitima su autoridad. Las fichas pueden ser físicas (como una llave USB) o digitales (un mensaje generado por ordenador o una firma digital)

1. Debes añadir `rest_framework.authtoken` a la lista de apps instaladas (`INSTALLED_APPS`) dentro de `inventario_project/settings.py` así:

```python
INSTALLED_APPS = [
    # previo codigo...,
    'rest_framework',
    'sgi_app',
    'rest_framework.authtoken' #agregamos esta linea
]
```
2. Debes añadir final del archivo `settings.py`lo siguiente:

```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
}

```
3. Actualizamos las vistas de DRF creadas con generics, en `sgi_app/views.py` de modo que el archivo quede así:
```python
# Create your views here.
from django.shortcuts import render
from rest_framework import generics
from .models import Proveedor, Producto, Pedido
from .serializers import ProveedorSerializer, ProductoSerializer, PedidoSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import status
from django.http import Http404

# ------------------------------->>>>>>>>>>>>VISTAS PROVEEDOR<<<<<<<<<-----------------------------------
# Vista para listar y crear proveedores
class ProveedorListCreate(generics.ListCreateAPIView):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer
    permission_classes = [IsAuthenticated]
    
# Vista para ver, actualizar y eliminar un proveedor
class ProveedorRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer
    permission_classes = [IsAuthenticated]

# Vista para obtener detalles de un proveedor
class ProveedorDetail(APIView):
    permission_classes = [IsAuthenticated]
    def get_object(self, pk):
        try:
            return Proveedor.objects.get(pk=pk)
        except Proveedor.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        proveedor = self.get_object(pk)
        serializer = ProveedorSerializer(proveedor)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        proveedor = self.get_object(pk)
        serializer = ProveedorSerializer(proveedor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        proveedor = self.get_object(pk)
        proveedor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
# Vistas renderizadas para templates de proveedor-------------------------------------------------------------------------
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Proveedor
from .forms import ProveedorForm

# Vista para mostrar la lista de proveedores
def lista_proveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'lista_proveedores.html', {'proveedores': proveedores})

# Vista para ver los detalles de un proveedor
def detalle_proveedor(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    return render(request, 'detalle_proveedor.html', {'proveedor': proveedor})

# Vista para crear un nuevo proveedor
class CrearProveedor(CreateView):
    model = Proveedor
    form_class = ProveedorForm
    template_name = 'crear_proveedor.html'
    success_url = '/proveedores/'

# Vista para actualizar un proveedor existente
class ActualizarProveedor(UpdateView):
    model = Proveedor
    form_class = ProveedorForm
    template_name = 'actualizar_proveedor.html'
    success_url = '/proveedores/'

# Vista para eliminar un proveedor existente
class EliminarProveedor(DeleteView):
    model = Proveedor
    template_name = 'eliminar_proveedor.html'
    success_url = '/proveedores/'

# ------------------------------->>>>>>>>>>>>VISTAS PRODUCTO<<<<<<<<<-----------------------------------
# Vista para listar y crear productos
class ProductoListCreate(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = [IsAuthenticated]

# Vista para ver, actualizar y eliminar un producto
class ProductoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = [IsAuthenticated]

# Vista para obtener detalles de un producto
class ProductoDetail(APIView):
    permission_classes = [IsAuthenticated]
    def get_object(self, pk):
        try:
            return Producto.objects.get(pk=pk)
        except Producto.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        producto = self.get_object(pk)
        serializer = ProductoSerializer(producto)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        producto = self.get_object(pk)
        serializer = ProductoSerializer(producto, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        producto = self.get_object(pk)
        producto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
# Vistas renderizadas para templates de producto-------------------------------------------------------------------------

from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .forms import ProductoForm

# Vista para mostrar la lista de productos
def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'lista_productos.html', {'productos': productos})

# Vista para ver los detalles de un producto
def detalle_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    return render(request, 'detalle_producto.html', {'producto': producto})

# Vista para crear un nuevo producto
def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm()
    return render(request, 'crear_producto.html', {'form': form})

# Vista para actualizar un producto existente
def actualizar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('detalle_producto', pk=pk)
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'actualizar_producto.html', {'form': form})

# Vista para eliminar un producto existente
def eliminar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto.delete()
        return redirect('lista_productos')
    return render(request, 'eliminar_producto.html', {'producto': producto})

# ------------------------------->>>>>>>>>>>>VISTAS PEDIDO<<<<<<<<<-----------------------------------
# Vista para listar y crear pedidos
class PedidoListCreate(generics.ListCreateAPIView):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
    permission_classes = [IsAuthenticated]

# Vista para ver, actualizar y eliminar un pedido
class PedidoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
    permission_classes = [IsAuthenticated]

# Vista para obtener detalles de un pedido
class PedidoDetail(APIView):
    permission_classes = [IsAuthenticated]
    def get_object(self, pk):
        try:
            return Pedido.objects.get(pk=pk)
        except Pedido.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        pedido = self.get_object(pk)
        serializer = PedidoSerializer(pedido)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        pedido = self.get_object(pk)
        serializer = PedidoSerializer(pedido, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        pedido = self.get_object(pk)
        pedido.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
# Vistas renderizadas para templates de pedidos-------------------------------------------------------------------------
from django.shortcuts import render, redirect, get_object_or_404
from .models import Pedido
from .forms import PedidoForm

# Vista para mostrar la lista de pedidos
def lista_pedidos(request):
    pedidos = Pedido.objects.all()
    return render(request, 'lista_pedidos.html', {'pedidos': pedidos})

# Vista para ver los detalles de un pedido
def detalle_pedido(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk)
    return render(request, 'detalle_pedido.html', {'pedido': pedido})

# Vista para crear un nuevo pedido
def crear_pedido(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_pedidos')
    else:
        form = PedidoForm()
    return render(request, 'crear_pedido.html', {'form': form})

# Vista para actualizar un pedido existente
def actualizar_pedido(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk)
    if request.method == 'POST':
        form = PedidoForm(request.POST, instance=pedido)
        if form.is_valid():
            form.save()
            return redirect('detalle_pedido', pk=pk)
    else:
        form = PedidoForm(instance=pedido)
    return render(request, 'actualizar_pedido.html', {'form': form})

# Vista para eliminar un pedido existente
def eliminar_pedido(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk)
    if request.method == 'POST':
        pedido.delete()
        return redirect('lista_pedidos')
    return render(request, 'eliminar_pedido.html', {'pedido': pedido})

# ------------------------------->>>>>>>>>>>>VISTA INICIAL<<<<<<<<<-------------------------------------
# Vista para renderizar el template de index
def index(request):
    return render(request, 'index.html')

```

Nota importante:
    Al añadir `permission_classes = [IsAuthenticated]` en las vista relacionadas a la Api limitamos consumo unicamente a personas que estén registradas y provean un token

4. Tambien es importante actualizar las URLs (endpoints)

```python
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
    # Ruta para obtener tokens de autenticación
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),

    # Rutas para API de Proveedores
    path('api/proveedores/', ProveedorListCreate.as_view(), name='proveedor-list-create'),
    path('api/proveedores/<int:pk>/', ProveedorDetail.as_view(), name='proveedor-detail'),
    path('api/proveedores/<int:pk>/update/', ProveedorRetrieveUpdateDestroy.as_view(), name='proveedor-update'),
    path('api/proveedores/<int:pk>/delete/', ProveedorRetrieveUpdateDestroy.as_view(), name='proveedor-delete'),

    # Rutas para API de Productos
    path('api/productos/', ProductoListCreate.as_view(), name='producto-list-create'),
    path('api/productos/<int:pk>/', ProductoDetail.as_view(), name='producto-detail'),
    path('api/productos/<int:pk>/update/', ProductoRetrieveUpdateDestroy.as_view(), name='producto-update'),
    path('api/productos/<int:pk>/delete/', ProductoRetrieveUpdateDestroy.as_view(), name='producto-delete'),

    # Rutas para API de Pedidos
    path('api/pedidos/', PedidoListCreate.as_view(), name='pedido-list-create'),
    path('api/pedidos/<int:pk>/', PedidoDetail.as_view(), name='pedido-detail'),
    path('api/pedidos/<int:pk>/update/', PedidoRetrieveUpdateDestroy.as_view(), name='pedido-update'),
    path('api/pedidos/<int:pk>/delete/', PedidoRetrieveUpdateDestroy.as_view(), name='pedido-delete'),

    # Ruta inicial
    path('', index, name='index'),

    # Rutas para las vistas de Proveedores
    path('proveedores/', lista_proveedores, name='lista_proveedores'),
    path('proveedores/<int:pk>/', detalle_proveedor, name='detalle_proveedor'),
    path('proveedores/crear/', CrearProveedor.as_view(), name='crear_proveedor'),
    path('proveedores/<int:pk>/actualizar/', ActualizarProveedor.as_view(), name='actualizar_proveedor'),
    path('proveedores/<int:pk>/eliminar/', EliminarProveedor.as_view(), name='eliminar_proveedor'),

    # Rutas para las vistas de Productos
    path('productos/', lista_productos, name='lista_productos'),
    path('productos/<int:pk>/', detalle_producto, name='detalle_producto'),
    path('productos/crear/', crear_producto, name='crear_producto'),
    path('productos/<int:pk>/actualizar/', actualizar_producto, name='actualizar_producto'),
    path('productos/<int:pk>/eliminar/', eliminar_producto, name='eliminar_producto'),

    # Rutas para las vistas de Pedidos
    path('pedidos/', lista_pedidos, name='lista_pedidos'),
    path('pedidos/<int:pk>/', detalle_pedido, name='detalle_pedido'),
    path('pedidos/crear/', crear_pedido, name='crear_pedido'),
    path('pedidos/<int:pk>/actualizar/', actualizar_pedido, name='actualizar_pedido'),
    path('pedidos/<int:pk>/eliminar/', eliminar_pedido, name='eliminar_pedido'),    
]

```
Nota importante:
    Creamos un endpoint `api-token-auth` para que un usuario pueda obtener su respectivo `token` mediante un metodo POST. Y asi poder acceder a las vistas de la API.

5. Para poder acceder a alguna es necesaria obtener el token del usuario en http://127.0.0.1:8000/api-token-auth mediante postman con el metodo POST y agregando en el body el `username` y `password`

6. finalmente con el token generado del usuario podemos hacer el GET al endpoint que nos interesa pasando el token en el campo de `Authorization: tu Token`

## **11. Documentación**

- Este README proporciona instrucciones detalladas para la instalación, configuración y uso del proyecto.
- Se han incluido comentarios en el código para explicar las partes complejas o importantes.