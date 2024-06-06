# admin.py
from django.contrib import admin #importamos el admin
from .models import Proveedor, Producto, Pedido #Importamos los modelos

# Register your models here.
admin.site.register(Proveedor) #Registramos los modelos
admin.site.register(Producto)
admin.site.register(Pedido)