# serializers.py
from rest_framework import serializers # Importamos el serializador
from .models import Producto, Proveedor, Pedido # Importamos los modelos

class ProductoSerializer(serializers.ModelSerializer): # Serializador para Productos
    class Meta:
        model = Producto
        fields = ['id', 'usuario', 'nombre', 'descripcion', 'proveedor', 'precio', 'stock']

class ProveedorSerializer(serializers.ModelSerializer): # Serializador para Proveedores
    class Meta:
        model = Proveedor
        fields = ['id', 'nombre', 'contacto', 'telefono', 'direccion']

class PedidoSerializer(serializers.ModelSerializer): # Serializador para Pedidos
    class Meta:
        model = Pedido
        fields = ['id', 'tipo', 'producto', 'cantidad', 'fecha']
