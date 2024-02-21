from django.test import TestCase
from django.urls import reverse
from .models import Proveedor, Producto, Pedido
from .forms import ProveedorForm, ProductoForm, PedidoForm

class ModelTestCase(TestCase):
    """
    Pruebas para los modelos.
    """

    def setUp(self):
        """
        Configuración inicial para las pruebas de los modelos.
        """
        self.proveedor = Proveedor.objects.create(nombre="Proveedor Test", direccion="Dirección de Prueba", telefono="123456789")
        self.producto = Producto.objects.create(nombre="Producto Test", descripcion="Descripción de Prueba", proveedor=self.proveedor, cantidad_disponible=10, precio_unitario=100.0, fecha_vencimiento="2024-12-31")
        self.pedido = Pedido.objects.create(tipo="COMPRA", proveedor=self.proveedor, producto=self.producto, cantidad=5, fecha_entrega="2024-02-20")

    def test_proveedor_str(self):
        """
        Verifica que la representación de cadena de un proveedor sea correcta.
        """
        self.assertEqual(str(self.proveedor), "Proveedor Test")

    def test_producto_str(self):
        """
        Verifica que la representación de cadena de un producto sea correcta.
        """
        self.assertEqual(str(self.producto), "Producto Test")

    def test_pedido_str(self):
        """
        Verifica que la representación de cadena de un pedido sea correcta.
        """
        self.assertEqual(str(self.pedido), "Pedido de Producto Test (5 unidades)")

class ViewTestCase(TestCase):
    """
    Pruebas para las vistas.
    """

    def test_lista_proveedores_view(self):
        """
        Verifica que la vista de lista de proveedores funcione correctamente.
        """
        response = self.client.get(reverse('lista_proveedores'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lista_proveedores.html')

    def test_detalle_proveedor_view(self):
        """
        Verifica que la vista de detalle de proveedor funcione correctamente.
        """
        proveedor = Proveedor.objects.create(nombre='Proveedor Test', direccion='Dirección de Prueba', telefono='123456789')
        response = self.client.get(reverse('detalle_proveedor', args=[proveedor.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'detalle_proveedor.html')

    def test_crear_proveedor_view(self):
        """
        Verifica que la vista de creación de proveedor funcione correctamente.
        """
        response = self.client.get(reverse('crear_proveedor'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'crear_proveedor.html')

    def test_actualizar_proveedor_view(self):
        """
        Verifica que la vista de actualización de proveedor funcione correctamente.
        """
        proveedor = Proveedor.objects.create(nombre='Proveedor Test', direccion='Dirección de Prueba', telefono='123456789')
        response = self.client.get(reverse('actualizar_proveedor', args=[proveedor.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'actualizar_proveedor.html')

    def test_eliminar_proveedor_view(self):
        """
        Verifica que la vista de eliminación de proveedor funcione correctamente.
        """
        proveedor = Proveedor.objects.create(nombre='Proveedor Test', direccion='Dirección de Prueba', telefono='123456789')
        response = self.client.get(reverse('eliminar_proveedor', args=[proveedor.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'eliminar_proveedor.html')

    def test_lista_pedidos_view(self):
        """
        Verifica que la vista de lista de pedidos funcione correctamente.
        """
        response = self.client.get(reverse('lista_pedidos'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lista_pedidos.html')

    def test_detalle_pedido_view(self):
        """
        Verifica que la vista de detalle de pedido funcione correctamente.
        """
        pedido = Pedido.objects.create(tipo='COMPRA', proveedor=Proveedor.objects.create(nombre='Proveedor Test', direccion='Dirección de Prueba', telefono='123456789'), producto=Producto.objects.create(nombre='Producto Test', descripcion='Descripción de prueba', proveedor=Proveedor.objects.create(nombre='Proveedor Test', direccion='Dirección de Prueba', telefono='123456789'), cantidad_disponible=10, precio_unitario=10.00, fecha_vencimiento='2024-12-31'), cantidad=5, fecha_entrega='2024-02-20')
        response = self.client.get(reverse('detalle_pedido', args=[pedido.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'detalle_pedido.html')

    def test_crear_pedido_view(self):
        """
        Verifica que la vista de creación de pedido funcione correctamente.
        """
        response = self.client.get(reverse('crear_pedido'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'crear_pedido.html')

    def test_actualizar_pedido_view(self):
        """
        Verifica que la vista de actualización de pedido funcione correctamente.
        """
        pedido = Pedido.objects.create(tipo='COMPRA', proveedor=Proveedor.objects.create(nombre='Proveedor Test', direccion='Dirección de Prueba', telefono='123456789'), producto=Producto.objects.create(nombre='Producto Test', descripcion='Descripción de prueba', proveedor=Proveedor.objects.create(nombre='Proveedor Test', direccion='Dirección de Prueba', telefono='123456789'), cantidad_disponible=10, precio_unitario=10.00, fecha_vencimiento='2024-12-31'), cantidad=5, fecha_entrega='2024-02-20')
        response = self.client.get(reverse('actualizar_pedido', args=[pedido.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'actualizar_pedido.html')

    def test_eliminar_pedido_view(self):
        """
        Verifica que la vista de eliminación de pedido funcione correctamente.
        """
        pedido = Pedido.objects.create(tipo='COMPRA', proveedor=Proveedor.objects.create(nombre='Proveedor Test', direccion='Dirección de Prueba', telefono='123456789'), producto=Producto.objects.create(nombre='Producto Test', descripcion='Descripción de prueba', proveedor=Proveedor.objects.create(nombre='Proveedor Test', direccion='Dirección de Prueba', telefono='123456789'), cantidad_disponible=10, precio_unitario=10.00, fecha_vencimiento='2024-12-31'), cantidad=5, fecha_entrega='2024-02-20')
        response = self.client.get(reverse('eliminar_pedido', args=[pedido.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'eliminar_pedido.html')

class FormTestCase(TestCase):
    """
    Pruebas para los formularios.
    """

    def test_proveedor_form_valid(self):
        """
        Verifica que el formulario de proveedor sea válido con datos válidos.
        """
        form_data = {'nombre': 'Proveedor Test', 'direccion': 'Dirección de Prueba', 'telefono': '123456789'}
        form = ProveedorForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_producto_form_valid(self):
        """
        Verifica que el formulario de producto sea válido con datos válidos.
        """
        proveedor = Proveedor.objects.create(nombre='Proveedor Prueba', direccion='Dirección de Prueba', telefono='123456789')
        form_data = {'nombre': 'Producto Test', 'descripcion': 'Descripción de Prueba', 'proveedor': proveedor.id, 'cantidad_disponible': 10, 'precio_unitario': 20.5, 'fecha_vencimiento': '2024-12-31'}
        form = ProductoForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_pedido_form_valid(self):
        """
        Verifica que el formulario de pedido sea válido con datos válidos.
        """
        proveedor = Proveedor.objects.create(nombre='Proveedor Prueba', direccion='Dirección de Prueba', telefono='123456789')
        producto = Producto.objects.create(nombre='Producto Prueba', descripcion='Descripción de Prueba', proveedor=proveedor, cantidad_disponible=10, precio_unitario=20.5, fecha_vencimiento='2024-12-31')
        form_data = {'tipo': 'COMPRA', 'proveedor': proveedor.id, 'producto': producto.id, 'cantidad': 5, 'fecha_entrega': '2024-02-20'}
        form = PedidoForm(data=form_data)
        self.assertTrue(form.is_valid())
