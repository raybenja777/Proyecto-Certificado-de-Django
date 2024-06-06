# models.py
from django.db import models # Importa el modelo de base de datos
from django.contrib.auth.models import User # Importa el modelo de usuario
# Create your models here.
class Proveedor(models.Model): # Define la clase Proveedor
    nombre = models.CharField(max_length=255) # Define el campo nombre como una cadena de caracteres
    contacto = models.CharField(max_length=255) # Define el campo contacto como una cadena de caracteres
    telefono = models.CharField(max_length=15) # Define el campo telefono como una cadena de caracteres
    direccion = models.TextField() # Define el campo direccion como un campo de texto
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='proveedores') # Define el campo user como una clave foránea
 
    def __str__(self): # Sobrescribe el método __str__ para mostrar el nombre del proveedor
        return self.nombre

class Producto(models.Model): # Define la clase Producto
    usuario = models.ForeignKey(User, on_delete=models.CASCADE) # Define el campo usuario como una clave foránea
    nombre = models.CharField(max_length=255) # Define el campo nombre como una cadena de caracteres
    descripcion = models.TextField() # Define el campo descripcion como un campo de texto
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE) # Define el campo proveedor como una clave foránea
    precio = models.DecimalField(max_digits=10, decimal_places=2) # Define el campo precio como un decimal
    stock = models.IntegerField() # Define el campo stock como un entero

    def __str__(self): # Sobrescribe el método __str__ para mostrar el nombre del producto
        return self.nombre
    
    def actualizar_stock(self, cantidad, operacion): # Define el método actualizar_stock
        if operacion == 'Compra': 
            self.stock += cantidad
        elif operacion == 'Venta':
            self.stock -= cantidad
        self.save()

class Pedido(models.Model): # Define la clase Pedido
    TIPO_PEDIDO = (
        ('Compra', 'Compra'),
        ('Venta', 'Venta'),
    )
    tipo = models.CharField(max_length=6, choices=TIPO_PEDIDO) # Define el campo tipo como una cadena de caracteres
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE) # Define el campo proyecto como una clave foránea
    cantidad = models.IntegerField() # Define el campo cantidad como un entero
    fecha = models.DateTimeField(auto_now_add=True) # Define el campo fecha como una fecha

    def __str__(self): # Sobrescribe el método __str__ para mostrar el tipo de pedido
        return f"{self.tipo} - {self.producto.nombre} - {self.cantidad}"
    
    def save(self, *args, **kwargs): # Sobrescribe el método save
        """
        Sobrescribe el método save para actualizar el stock del producto.
        """
        super().save(*args, **kwargs)
        self.producto.actualizar_stock(self.cantidad, self.tipo) # Actualiza el stock del producto