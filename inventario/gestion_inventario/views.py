# views.py en tu aplicación gestion_inventario
import matplotlib # Importa la librería matplotlib
matplotlib.use('Agg') # Establece el backend de matplotlib para 'Agg'
from .models import Proveedor, Producto, Pedido # Importa los modelos
from django.views.generic import FormView, CreateView, View, ListView, UpdateView, DeleteView, TemplateView # Importa las clases genericas
from django.urls import reverse_lazy # Importa la clase reverse_lazy
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm # Importa los formularios
from django.contrib.auth import login, logout # Importa las funciones login y logout
from django.shortcuts import redirect, render # Importa las funciones redirect y render
from django.contrib.auth.mixins import LoginRequiredMixin # Importa la clase LoginRequiredMixin
from .models import Proveedor, Pedido, Producto # Importa los modelos
from django.utils.dateparse import parse_datetime # Importa la clase parse_datetime
import matplotlib.pyplot as plt # Importa la librería matplotlib
import io # Importa la clase io
import urllib, base64 # Importa las clases urllib y base64
from django.http import HttpResponse # Importa la clase HttpResponse


class LoginRedirectView(View): # Clase que redirige al usuario dependiendo de si está autenticado o no
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard')  # Si el usuario está autenticado, redirige al dashboard
        else:
            return redirect('login')  # Si no está autenticado, redirige al inicio de sesión

class LoginList(FormView): # Clase que permite el inicio de sesión
    template_name = 'registration/login.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('dashboard')
    
    def form_valid(self, form):
        user = form.get_user()
        if user is not None:
            login(self.request, user)  # Autentica al usuario
            return super().form_valid(form)
        else:
            return self.form_invalid(form)
    
class RegistroList(CreateView): # Clase que permite el registro
    template_name = 'registro.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.save()
        login(self.request, user)  # Autenticar al usuario después del registro
        return response
    
class LogoutList(View): # Clase que permite el cierre de sesión
    def post(self, request, *args, **kwargs): 
        logout(request) # Cierra la sesión
        return redirect(reverse_lazy('login')) 
    
class DashboardView(LoginRequiredMixin, TemplateView): # Clase que muestra el dashboard
    template_name = 'dashboard.html'
    
    def get_context_data(self, **kwargs): # Obtiene los datos para el dashboard
        context = super().get_context_data(**kwargs)
        context['username'] = self.request.user.username # Obtiene el nombre de usuario
        return context

class ProveedorList(ListView, LoginRequiredMixin): # Clase que muestra la lista de proveedores
    model = Proveedor
    template_name = 'lista_proveedores.html'
    context_object_name = 'proveedores'
    
    def get_queryset(self): # Obtiene los datos de la lista de tareas
        return Proveedor.objects.filter(user=self.request.user)
    
    def get_context_data(self, **kwargs): # Obtiene los datos para el dashboard
        context = super().get_context_data(**kwargs)
        context['username'] = self.request.user.username
        return context
    
class ProveedorCreate(CreateView, LoginRequiredMixin): # Clase que permite crear un nuevo proveedor
    model = Proveedor
    fields = ['nombre', 'telefono', 'direccion']
    template_name = 'nuevo_proveedor.html'
    success_url = reverse_lazy('dashboard')
    
    
    def form_valid(self, form): # Verifica que el formulario sea valido
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class ProveedorUpdate(UpdateView, LoginRequiredMixin): # Clase que permite editar un proveedor
    model = Proveedor 
    fields = ['nombre', 'telefono', 'direccion']
    template_name = 'nuevo_proveedor.html'
    success_url = reverse_lazy('proveedor-list')
    
class ProveedorDelete(DeleteView, LoginRequiredMixin): # Clase que permite eliminar un proveedor
    model = Proveedor
    success_url = reverse_lazy('proveedor-list')
    template_name = 'borrar_proveedor.html'

class ProductoList(ListView, LoginRequiredMixin): # Clase que muestra la lista de productos
    model = Producto
    template_name = 'lista_productos.html'
    context_object_name = 'productos'
    
    def get_queryset(self): # Obtiene los datos de la lista de tareas
        return Producto.objects.filter(usuario=self.request.user)
    
    def get_context_data(self, **kwargs): # Obtiene los datos para el dashboard
        context = super().get_context_data(**kwargs)
        context['username'] = self.request.user.username
        return context
    
    
class ProductoCreate(CreateView, LoginRequiredMixin): # Clase que permite crear un nuevo producto
    model = Producto
    fields = ['nombre', 'descripcion', 'proveedor', 'stock', 'precio']
    template_name = 'nuevo_producto.html'
    success_url = reverse_lazy('producto-list')
    
    def form_valid(self, form): # Verifica que el formulario sea valido
        form.instance.usuario = self.request.user
        return super().form_valid(form)
    
class ProductoUpdate(UpdateView, LoginRequiredMixin): # Clase que permite editar un producto
    model = Producto
    fields = ['nombre', 'descripcion', 'proveedor', 'stock', 'precio']
    template_name = 'nuevo_producto.html'
    success_url = reverse_lazy('producto-list')
    
    
class ProductoDelete(DeleteView, LoginRequiredMixin): # Clase que permite eliminar un producto
    model = Producto
    success_url = reverse_lazy('producto-list')
    template_name = 'borrar_producto.html'


class PedidoList(ListView, LoginRequiredMixin): # Clase que muestra la lista de pedidos
    model = Pedido
    template_name = 'lista_pedidos.html'
    context_object_name = 'pedidos'
    
    def get_queryset(self): # Obtiene los datos de la lista de tareas
        return Pedido.objects.filter(producto__usuario=self.request.user)
    
    def get_context_data(self, **kwargs): # Obtiene los datos para el dashboard
        context = super().get_context_data(**kwargs)
        context['username'] = self.request.user.username
        return context
    
class PedidoCreate(CreateView, LoginRequiredMixin): # Clase que permite crear un nuevo pedido
    model = Pedido
    fields = ['tipo', 'producto', 'cantidad']
    template_name = 'nuevo_pedido.html'
    success_url = reverse_lazy('pedido-list')
    
    def form_valid(self, form): # Verifica que el formulario sea valido
        response = super().form_valid(form)
        fecha_str = self.request.POST.get('fecha')
        if fecha_str:
            fecha = parse_datetime(fecha_str)
            if fecha:
                self.object.fecha = fecha
                self.object.save()
        return response
    
class PedidoUpdate(UpdateView, LoginRequiredMixin): # Clase que permite editar un pedido
    model = Pedido
    fields = ['tipo', 'producto', 'cantidad', ]
    template_name = 'nuevo_pedido.html'
    success_url = reverse_lazy('pedido-list')
    
    def form_valid(self, form): # Verifica que el formulario sea valido
        response = super().form_valid(form)
        fecha_str = self.request.POST.get('fecha')
        if fecha_str:
            fecha = parse_datetime(fecha_str)
            if fecha:
                self.object.fecha = fecha
                self.object.save()
        return response
    
class PedidoDelete(DeleteView, LoginRequiredMixin): # Clase que permite eliminar un pedido
    model = Pedido
    success_url = reverse_lazy('pedido-list')
    template_name = 'borrar_pedido.html'


def lista_productos(request): # Muestra la lista de productos
    productos = Producto.objects.filter(usuario=request.user)
    return render(request, 'lista_productos.html', {'productos': productos})

def informe_stock(request): # Muestra el informe de stock
    # Filtrar los productos basados en el usuario actual
    productos_usuario = Producto.objects.filter(usuario=request.user)
    
    context = {
        'productos': productos_usuario,
        'username': request.user.username
    }
    return render(request, 'informes_stock.html', context)


def grafico_stock(request): # Muestra el gráfico de stock
    productos_usuario = Producto.objects.filter(usuario=request.user)

    # Datos para el gráfico
    nombres_productos = [producto.nombre for producto in productos_usuario]
    cantidades_stock = [producto.stock for producto in productos_usuario]
    plt.fill_between( nombres_productos, cantidades_stock, alpha=0.1, color='blue')

   # Crear el gráfico
    plt.figure(figsize=(7, 5))
    plt.plot(nombres_productos, cantidades_stock, marker='o', linewidth=2)
    plt.title('Gráfico de Stock')
    plt.xlabel('Productos')
    plt.ylabel('Stock')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.grid(True)
    

# Guardar el gráfico en un objeto BytesIO
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    plt.close()
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()

# Convertir a base64 para incrustar en HTML
    graphic = base64.b64encode(image_png)
    graphic = graphic.decode('utf-8')

    context = {
   'graphic': graphic
   }
    return render(request, 'grafico_stock.html', context)

def descargar_grafico_stock(request): # Descarga el gráfico de stock
    productos_usuario = Producto.objects.filter(usuario=request.user)

    # Datos para el gráfico
    nombres_productos = [producto.nombre for producto in productos_usuario]
    cantidades_stock = [producto.stock for producto in productos_usuario]
    plt.fill_between( nombres_productos, cantidades_stock, alpha=0.1, color='blue')

    # Crear el gráfico
    plt.figure(figsize=(8, 5))
    plt.plot(nombres_productos, cantidades_stock, marker='o', linewidth=2)
    plt.title('Gráfico de Stock')
    plt.xlabel('Productos')
    plt.ylabel('Stock')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.grid(True)

    # Guardar el gráfico en un objeto BytesIO
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    plt.close()
    buffer.seek(0)

    # Devolver el gráfico como una respuesta HTTP
    response = HttpResponse(buffer, content_type='image/png')
    response['Content-Disposition'] = 'attachment; filename="grafico_stock.png"'
    return response