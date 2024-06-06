"""
URL configuration for inventario project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# urls.py del proyecto
from django.contrib import admin # Importa el administrador
from django.urls import path, include  # Importa las URLs
from django.views.generic import RedirectView # Importa la vista RedirectView
from gestion_inventario import views # Importa la vista

urlpatterns = [
    path('', RedirectView.as_view(url='login/', permanent=False), name='index'), # Redirecciona a la página de inicio desde un principio
    path('admin/', admin.site.urls), # URL del administrador
    path('login/', views.LoginList.as_view(), name='login'),  # Página de inicio de sesión
    path('logout/', views.LogoutList.as_view(), name='logout'), # Página de inicio de sesión como la página principal
    path('registro/', views.RegistroList.as_view(), name='registro'), # Página de registro
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'), # Página de inicio
    path('gestion_inventario/', include('gestion_inventario.urls')), # URL de la app gestion_inventario
    path('accounts/profile/', RedirectView.as_view(url='dashboard/', permanent=False)), # Redirecciona a la página de inicio al iniciar la sesión (dashboard)include('django.contrib.auth.urls')),
]


