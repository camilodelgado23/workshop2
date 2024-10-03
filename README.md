# workshop2:file_folder:

## Por: Camilo Jose Delgado Bolaños - 2225337 

En este workshop se recibió un dataset con candidatos a la espera de ser contratados. Dichos datos fueron migrados a una base de datos relacional (MySQL), se les realizó un E.D.A. con el objetivo de entender y comprender el contenido de los mismos, y se realizaron modificaciones en base a ello. Finalmente, se desarrollaron visualizaciones de datos sobre el contenido del dataset

## Herramientas Usadas :wrench:

- Python: 
    - Python Scripting: Para automatizar tareas como la inserción de datos en bases de datos, y la exportación de archivos.
    - Visual Studio Code (VS Code): Como entorno para escribir y ejecutar código Python.
    - Jupyter Notebook: Para desarrollo interactivo de código, exploración de datos, y ejecución de scripts.
    - Virtual Environment (venv): Para gestionar dependencias y aislar el entorno de desarrollo.

- MySQL:
    - MySQL Workbench: Para gestión y administración de bases de datos MySQL.

- Git: Para control de versiones y seguimiento de cambios en el proyecto.
- GitHub: Para alojar el repositorio del proyecto, gestionar el control de versiones, y colaborar en el desarrollo del proyecto.
- Power BI: Para la visualizacion de Datos.

## Estructura del Repositorio :memo:

La estructura del repositorio es la siguiente:

- **Análisis_de_Datos:** Carpeta Donde tendremos los archivos donde se realizaran el análisis del dataset y sacaremos el dataset transformado con el que se realizaran las visualizaciones de datos.
    - **candidates_analisis.ipynb:** En este notebook se lleva acabo el E.D.A del dataset de candidates original para ver que tanto tiene el dataset y poder sacar diversas conclusiones y modificaciones.
    - **candidates_transformado.ipynb:** En este notebook filtraremos el dataset original donde solo dejaremos la información de los empleados contratados, y donde además agregaremos una nueva columna de ID para poder identificar a cada uno de los candidatos con mayor facilidad.
- **Base_de_Datos_Operaciones:** En esta carpeta tendremos las operaciones que realizamos en nuestra Base de Datos en este caso MySQL, como lo es realizar la conexión a la BD, y la creación de las tablas donde insertaremos nuestro dataset.
    - **_init_.py:** Se utiliza para convertir un directorio en un paquete de Python. Esto permite que el contenido del directorio, como otros módulos y subpaquetes, pueda ser importado y utilizado en otros scripts o proyectos.
    - **carga_dataset_BD.ipynb:** En este notebook insertamos los 2 dataset tanto el original como el transformado y los insertamos en las tablas ubicadas en la Base de Datos.
    - **conexionBD.py:** En este archivo tenemos el script que con ayuda de la libreria MySQL connection nos conectamos a la Base de Datos de MySQL.
    - **tablasBD.ipynb:** En este notebook creamos las tablas donde crearemos las tablas de los 2 dataset en la Base de Datos, el original y el transformado.
- **csv:** Carpeta donde almacenaremos nuestros archivos .csv .
    - **candidates_contratados.csv:** Dataset transformado con solo los candidatos contratados y con una columna extra de ID que facilita la identificación de los candidatos.
    - **candidates.csv:** Dataset original de las solicitudes de los candidatos.
- **.gitignore:** Archivo en donde colocamos los archivos que no queremos que se suban a nuestro repositorio de git hub como lo es nuestro entorno virtual o nuestro archivo en donde almacenamos las credenciales.
- **readme.txt:** Archivo donde colocaremos una breve descripción de nuestro proyecto y donde se explica como ejecutar el workshop.
- **requirements.txt:** Archivo en donde colocamos las librerías/bibliotecas que usamos en nuestro entorno para el desarrollo del
workshop.
- **Dashboard.pdf**: Archivo PDF en donde se muestran las visualizaciones de los datos realizadas en PowerBI.

## Instrucciones para la ejecucion :bookmark_tabs:

### Requerimientos 

- Python: https://www.python.org/downloads/
- MySQL: https://dev.mysql.com/downloads/mysql/
- PowerBI: https://www.microsoft.com/es-es/download/details.aspx?id=58494
- MySQL Workbench(Opcional): https://dev.mysql.com/downloads/workbench/

Clonamos el repositorio en nuestro entorno 

```bash
  git clone https://github.com/camilodelgado23/workshop__1.git
```
Vamos al repositorio clonado 

```bash
  cd workshop1
```
##### Si desea puede usar un entorno virtual para gestionar dependencias de manera aislada  

Instalamos el entrono virtual 

```bash
  Python -m venv venv 
```
Iniciamos el entorno 

```bash
  .\venv\Scripts\Activate
```
Instalamos las librerias necesarias almacenadas en el archivo requirements.txt

```bash
  pip install -r requirements.txt
```
Creamos la Base de Datos en MySQL 

```bash
  CREATE SCHEMA workshop1;
```
Creamos el archivo credentials.py donde almacenaremos las credenciales para conectarnos a la Base de Datos, puede seguir la siguiente estructura para ese archivo:

```bash
  DB_HOST = 'tu_host'
  DB_USER = 'tu_usuario'
  DB_PASSWORD = 'tu_contraseña'
  DB_NAME = 'tu_Base_Datos'
```
Podemos probar si las credenciales son correctas ejecutando nuestro archivo conexion.py.

#### Para una correcta ejecucuion: 

Para una correcta ejecucion de nuestro repositorio ejecutamos primero nuestro notebook tablasBD, donde crearemos las tablas en la base de datos. Despues ejecutamos el notebook carga_dataset_BD donde cargamos los 2 datasets a las tablas ya creadas en la BD. 

Podemos ejecutar los otros 2 notebooks que son candidates_analisis, y candidates_transformado, en donde realizamos el E.D.A del dataset original y el proceso de filtracion para exportar el dataset candidates_contratados.csv 

#### Conexion a PowerBI 

Para realizar las visualizaciones de datos tenemos que conectar la Base de Datos MySQL al PowerBI para esto seguimos los siguientes pasos: 

Nos vamos a PowerBI y lo iniciamos, nos vamos a la pantalla de inicio y le damos a obtener datos donde buscaremos la opción de Base de datos MySQL 

![Texto alternativo](https://imagenes.notion.site/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2Fb687bcac-6636-49ac-8ce3-1adf66aa571c%2F4539b281-2eba-4cec-a5c7-fec87fab4788%2F1.png?table=block&id=bbd0ce8c-679a-4172-9554-83256498112d&spaceId=b687bcac-6636-49ac-8ce3-1adf66aa571c&width=1420&userId=&cache=v2)

Nos toca descargar un conector nos dirigimos al siguiente enlace y lo descargamos

Descargar conector: https://dev.mysql.com/downloads/connector/net/

![Texto alternativo](https://imagenes.notion.site/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2Fb687bcac-6636-49ac-8ce3-1adf66aa571c%2F9a782ec1-3061-493a-af7b-f33dcb7050d2%2F2.1.png?table=block&id=f11e0989-9b38-43fd-82d3-f2fb2779dc75&spaceId=b687bcac-6636-49ac-8ce3-1adf66aa571c&width=1420&userId=&cache=v2)

Ingresamos el nombre del servidor y el de nuestra Base de datos 

![Texto alternativo](https://imagenes.notion.site/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2Fb687bcac-6636-49ac-8ce3-1adf66aa571c%2F610cfd99-14fe-42d2-af6f-56b7938d56cf%2F2.png?table=block&id=3c8dfff3-b062-4e3d-a717-21a7c3ae2da1&spaceId=b687bcac-6636-49ac-8ce3-1adf66aa571c&width=1420&userId=&cache=v2)

Seleccionamos Base de datos y Colocamos nuestro usuario y contraseña 

![Texto alternativo](https://imagenes.notion.site/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2Fb687bcac-6636-49ac-8ce3-1adf66aa571c%2Fe2ab8ccb-f840-4ec1-adc6-46b4174fe76c%2F3.png?table=block&id=3a0475da-07f1-40d6-a8aa-91010f552e16&spaceId=b687bcac-6636-49ac-8ce3-1adf66aa571c&width=1420&userId=&cache=v2)

Finalmente seleccionamos las tablas que vamos a usar en este caso usaremos la de candidates_contratados 

![Texto alternativo](https://imagenes.notion.site/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2Fb687bcac-6636-49ac-8ce3-1adf66aa571c%2Fd8646e93-1d66-434c-b2eb-66216c016e56%2Fimage.png?table=block&id=feffc280-9bfc-4f48-83e2-14b289894e8b&spaceId=b687bcac-6636-49ac-8ce3-1adf66aa571c&width=1420&userId=&cache=v2)
