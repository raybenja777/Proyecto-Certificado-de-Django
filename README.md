# Proyecto-Certificado-de-Django
Este proyecto es un sistema de gestión de inventarios desarrollado con Django, que permite a los usuarios gestionar proveedores, productos y pedidos. Incluye funcionalidades de registro e inicio de sesión, panel de control personalizado, informes de stock y visualización gráfica de los inventarios.

## Características

- Autenticación de Usuarios: Registro de nuevos usuarios, inicio y cierre de sesión.
- Gestión de Proveedores: Añadir, actualizar, listar y eliminar proveedores.
- Gestión de Productos: Añadir, actualizar, listar y eliminar productos, con información detallada y stock disponible.
- Gestión de Pedidos: Crear, actualizar, listar y eliminar pedidos asociados a productos.
- Panel de Control: Panel de control personalizado que da la bienvenida al usuario y proporciona acceso rápido a todas las funcionalidades.
- Informes de Stock: Visualización de informes de stock filtrados por usuario.
- Gráficos de Stock: Generación de gráficos de stock usando Matplotlib, con opción de descarga.
- Interfaz de Usuario: Interfaz amigable con videos de fondo y botones personalizados.

## Requisitos

- Python
- Django
- Django Rest Framework
- Matplotlib

## Instalación

1. Clona este repositorio a tu máquina local.
2. Crea un entorno virtual para el proyecto. Puedes hacerlo con el siguiente comando: *python3 -m venv myenv*. *myenv* es el nombre del proyecto, puedes poner el que desees.
3. Activa el entorno virtual. Dependiendo de tu sistema operativo, el comando puede variar: para Windows *myenv\Scripts\activate*, para MacOS y Linux *source myenv/bin/activate*.
4. Instala Django, Django Rest Framework, y Matplotlib con *pip install django django restframework matplotlib*, o simplemente instalarlos con *pip install -r requirements.txt*.
5. Realiza las migraciones de la base de datos con *python manage.py migrate*.
6. Genera las migraciones necesarias para los modelos de ser necesario con *python manage.py makemigrations*.
7. Aplica las migraciones con *python manage.py migrate*.
8. Ejecuta el servidor de desarrollo con *python manage.py runserver*.

## Uso 

- Una vez hayas ejecutado el servidor de desarrollo, accede a la dirección que se te proporciona en la terminal.
- Si ya tienes una cuenta, inicia sesión con tu nombre de usuario y contraseña. Si no, haz clic en el botón "Registrarse" para crear una nueva cuenta.
- Después de iniciar sesión, serás redirigido automáticamente al dashboard. Aquí podrás acceder a las distintas funcionalidades de la aplicación.
- Puedes gestionar proveedores, productos y pedidos desde las opciones del menú en el dashboard, a partir de los datos proporcionados se va a generar el informe de stock.
- Para generar un informe de stock, selecciona la opción correspondiente en el menú.
- Dentro de informe de stock, vas a tener la opcion de de ver el grafico de stock, selecciona si deseas verlo.
- Dentro de la vista que muestra el grafico de stock, vas a tener la opcion de descargar el grafico.
- Cuando hayas terminado de trabajar con la aplicación, puedes cerrar sesión haciendo clic en el enlace "Cerrar sesión" en el dashboard.

## Créditos

Este proyecto fue creado por Randy Benjamín Cuevas Sánchez.

