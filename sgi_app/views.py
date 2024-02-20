# Create your views here.
from django.shortcuts import render
from rest_framework import generics
from .models import Proveedor, Producto, Pedido
from .serializers import ProveedorSerializer, ProductoSerializer, PedidoSerializer
from .permissions import IsAdminOrReadOnly
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

class ProveedorListCreate(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminOrReadOnly, IsAuthenticated]
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer
    
class ProductoListCreate(generics.ListCreateAPIView):
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAdminOrReadOnly, IsAuthenticated]
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer


class PedidoListCreate(generics.ListCreateAPIView):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
