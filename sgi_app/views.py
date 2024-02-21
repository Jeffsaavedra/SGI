# Create your views here.
from django.shortcuts import render
from rest_framework import generics
from .models import Proveedor, Producto, Pedido
from .serializers import ProveedorSerializer, ProductoSerializer, PedidoSerializer
#from .permissions import IsAdminOrReadOnly
from rest_framework.permissions import IsAuthenticated

class ProveedorListCreate(generics.ListCreateAPIView):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer
    permission_classes = [IsAuthenticated]
    
class ProductoListCreate(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = [IsAuthenticated]

class PedidoListCreate(generics.ListCreateAPIView):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
    permission_classes = [IsAuthenticated]