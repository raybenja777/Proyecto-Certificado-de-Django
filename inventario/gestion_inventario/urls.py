# urls.py en tu aplicación gestion_inventario
from django.urls import path # Importamos path
from . import views # Importamos views

urlpatterns = [ # Definimos las rutas
    path('', views.LoginList.as_view(), name='login'), # Ruta para la página de inicio
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'), # Ruta para el dashboard 
    path('registro/', views.RegistroList.as_view(), name='registro'), # Ruta para el registro
    path('login/', views.LoginList.as_view(), name='login'), # Ruta para el login
    path('logout/', views.LogoutList.as_view(), name='logout'), # Ruta para el logout
    path('proveedores/', views.ProveedorList.as_view(), name='proveedor-list'), # Ruta para la lista de proveedores
    path('proveedores/nuevo/', views.ProveedorCreate.as_view(), name='proveedor-create'), # Ruta para crear un nuevo proveedor
    path('proveedores/<int:pk>/editar/', views.ProveedorUpdate.as_view(), name='proveedor-update'), # Ruta para editar un proveedor 
    path('proveedores/<int:pk>/borrar/', views.ProveedorDelete.as_view(), name='proveedor-delete'), # Ruta para borrar un proveedor
    path('productos/', views.ProductoList.as_view(), name='producto-list'), # Ruta para la lista de productos
    path('productos/nuevo/', views.ProductoCreate.as_view(), name='producto-create'), # Ruta para crear un nuevo producto
    path('productos/<int:pk>/editar/', views.ProductoUpdate.as_view(), name='producto-update'), # Ruta para editar un proyecto
    path('productos/<int:pk>/borrar/', views.ProductoDelete.as_view(), name='producto-delete'), # Ruta para borrar un proyecto
    path('pedidos/', views.PedidoList.as_view(), name='pedido-list'), # Ruta para la lista de pedidos
    path('pedidos/nuevo/', views.PedidoCreate.as_view(), name='pedido-create'), # Ruta para crear un nuevo pedido
    path('pedidos/<int:pk>/editar/', views.PedidoUpdate.as_view(), name='pedido-update'), # Ruta para editar un pedido
    path('pedidos/<int:pk>/borrar/', views.PedidoDelete.as_view(), name='pedido-delete'), # Ruta para borrar un pedido
    path('productos/lista/', views.lista_productos, name='lista-productos'), # Ruta para la lista de productos
    path('informes/stock/', views.informe_stock, name='informe-stock'), # Ruta para el informe de stock
    path('grafico_stock/', views.grafico_stock, name='grafico_stock'), # Ruta para el grafico de stock
    path('descargar_grafico_stock/', views.descargar_grafico_stock, name='descargar_grafico_stock'), # Ruta para descargar el grafico de stock
]





