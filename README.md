# SGV Ingeniería Civil

Se desarrolló una página web para una empresa ficitcia de Ingeniería Civil, dedicada al cálculo de estructuras. La página web cuenta con lo siguiente:
* Página de Inicio con imagen inicial, "¿Qué hacemos?" y "Mail de contacto"
* Página de "¿Quienes somos? con los profesionales de la empresa
* Página de Proyectos
* Página de Socios
* Página de Clientes
* Página de Sumate al equipo

Para ingresar a la página de la empresa es necesario registrarse y posteriormente iniciar sesión. Una vez que se inicia sesión se podrá modificar la información del usuario y se podrán ver las diferentes partes de la web.

Cada parte de la página cuenta con formularios de búsqueda para los diferentes profesionales, proyectos, socios y clientes. Además, se podrá ver el detalle de cada uno de ellos. Particularmente los "superusuarios" tendrán la posibilidad de actualizar, eliminar y agregar nuevos datos.
En "Sumate al equipo" se tiene un formulario para enviar información a la Base de Datos para todos aquellos que se quieran sumar a la empresa.

Para salir de la página se puede usar el botón "Salir" para hacer un deslogeo.

## Requisitos Previos

* Python
* Git
* Django
* Pillow

## Instalación

Una vez instalado lo indicado en "Requisitos Previos":
* En terminal: "git clone https://github.com/sebigonzalezv/Entrega-Final-Gonzalez-Vescovo.git"
* En terminal: "python manage.py runserver"
* Ingresar a la URL

## Testeo de la aplicación

Se podrá ingresar a la aplicación en la URL: "http://127.0.0.1:8000/app/":
* Registrar: Se crea un usuario y contraseña
* Ingresar: Se debe iniciar sesión con el usuario y contraseña antes creados

Para el testeo de la aplicación se recomienda iniciar sesión primero con un superusuario y luego con un usuario cualquier, para ver las diferencias entre ambos:
1)  Superusuario:       sebigonzalezv
    Contraseña:         123456
2)  Usuario:            Ejemplo
    Contraseña:         Ej123456

Una vez iniciada la sesión se podrán recorrer las diferentes partes con el "navbar":
* Página de inicio: Se podrá enviar un mail en "Mail de contacto"
* Página de "Quienes somos", Proyectos, Socios y Clientes: Se podrá ver información en detalle, actualizar/eliminar/agregar datos (solo para superusuarios) y buscar información en la Base de Datos
* Página de Sumate al equipo: Se podrá enviar información a la Base de Datos completando el formulario
* Usuario: Se podrá modificar la información del usuario al hacer click en el nombre
* Salir: Se cierra la sesión del usuario

## Testeo del panel de administración

Se podrá ingresar al panel de administración en la URL: "http://127.0.0.1:8000//admin".
Se podrá observar y modificar la base de datos ingresando con el superusuario.