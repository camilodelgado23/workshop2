# workshop2: :file_folder:

## Por: Camilo Jose Delgado Bolaños - 2225337 

En este workshop En este taller utilizaremos el conjunto de datos de Spotify para leerlo en Python y Airflow, crear algunas transformaciones y cargarlo en una base de datos. Por otro lado, utilizaremos el conjunto de datos de los Grammy para cargarlo en una base de datos y luego, utilizando Airflow, leeremos los datos desde la base de datos, realizaremos algunas transformaciones, los fusionaremos con los conjuntos de datos de Spotify y la API, y los cargaremos en la base de datos.

Los dataset que se usaron fueron los siguientes:
-  spotify extraido de la siguiente pagina donde puede obtener informacion del contenido del dataset: https://www.kaggle.com/datasets/maharshipandya/-spotify-tracks-dataset

- Grammys extraido de la siguiente pagina donde puede obtener informacion del contenido del dataset: https://www.kaggle.com/datasets/unanimad/grammy-awards

## Herramientas Usadas :wrench:

- Python: 
    - Python Scripting: Para automatizar tareas como la inserción de datos en bases de datos, y la exportación de archivos.
    - Visual Studio Code (VS Code): Como entorno para escribir y ejecutar código Python.
    - Jupyter Notebook: Para desarrollo interactivo de código, exploración de datos, y ejecución de scripts.
    - Virtual Environment (venv): Para gestionar dependencias y aislar el entorno de desarrollo.
- WSL Ubuntu: para ejecutar un entorno de Linux directamente en mi máquina con Windows, facilitando la compatibilidad con herramientas y librerías de Linux.
- MySQL: Para gestión y administración de bases de datos MySQL.
- Airflow: Como herramienta poderosa para la automatización y orquestación de flujos de trabajo
- Git: Para control de versiones y seguimiento de cambios en el proyecto.
- GitHub: Para alojar el repositorio del proyecto, gestionar el control de versiones, y colaborar en el desarrollo del proyecto.
- Power BI: Para la visualizacion de Datos.

## Estructura del Repositorio :memo:

La estructura del repositorio es la siguiente:

**Airflow**: Este directorio contiene todo lo relacionado con Apache Airflow

  **Dags:** Contiene los archivos que definen los DAGs (Directed Acyclic Graphs) de Airflow.
    **data_pipeline_spotify_grammy.py:** Archivo Python que define el pipeline de datos para procesar y analizar los datasets de Spotify y Grammys.

  **Union:** Este directorio maneja la lógica de unión de los datasets.
    **merge_dataset.py:** Archivo Python que contiene funciones para unir los datasets de Spotify y Grammys.

  **carga:** Este directorio contiene scripts para cargar datos en la base de datos y otros servicios.
    **carga_Spotify.py:** Archivo que gestiona la carga del dataset de Spotify en la base de datos.
    **carga_merge.py:** Archivo que se encarga de cargar el dataset combinado en la base de datos.
    **subir_drive.py:** Archivo que contiene la lógica para subir archivos a Google Drive.

**Analisis_de_Datos:** Este directorio contiene notebooks de Jupyter para análisis de datos.
  **E.D.A_Grammys.ipynb:** Notebook que realiza un análisis exploratorio de datos (EDA) sobre el dataset de los Grammys.
  **E.D.A_Spotify.ipynb:** Notebook que realiza un análisis exploratorio de datos (EDA) sobre el dataset de Spotify. 

**Base_de_Datos_Operaciones:** Este directorio contiene scripts y notebooks relacionados con la gestión y operación de la base de datos.
  **__init__.py:** Indica que este directorio debe ser tratado como un paquete Python.
  **carga_dataset_BD.ipynb:** Notebook que  contiene la lógica para cargar el dataset de Grammys a la base de datos.
  **conexionBD.py:** Archivo que contiene la lógica para conectarse a la base de datos.
  **tablasBD.ipynb:** Notebook que podría describir las tablas en la base de datos o cómo trabajar con ellas.

**Dashboard.pdf:** Archivo PDF que contiene el dashboard.
**README.md:** Archivo que proporciona una descripción del proyecto, instrucciones de instalación, uso y otros detalles relevantes.
**requirements.txt:** Archivo que lista las dependencias del proyecto y sus versiones, que pueden ser instaladas mediante pip.

## Instrucciones para la ejecucion :bookmark_tabs:

### Requerimientos 

- Python: https://www.python.org/downloads/
- MySQL: https://dev.mysql.com/downloads/mysql/
- PowerBI: https://www.microsoft.com/es-es/download/details.aspx?id=58494
- MySQL : https://dev.mysql.com/downloads/workbench/
- WSL: https://learn.microsoft.com/es-es/windows/wsl/install

Clonamos el repositorio en nuestro entorno 

```bash
  git clone https://github.com/camilodelgado23/workshop2.git
```
Vamos al repositorio clonado 

```bash
  cd workshop2
```
##### Si desea puede usar un entorno virtual para gestionar dependencias de manera aislada  

Instalamos el entrono virtual 

```bash
  Python -m venv venv 
```
Iniciamos el entorno 

```bash
  source venv/bin/activate
```
Instalamos las librerias necesarias almacenadas en el archivo requirements.txt

```bash
  pip install -r requirements.txt
```
Creamos la Base de Datos en MySQL 

```bash
  CREATE SCHEMA workshop2;
```
Creamos el archivo credentials.py donde almacenaremos las credenciales para conectarnos a la Base de Datos, puede seguir la siguiente estructura para ese archivo:

```bash
  DB_HOST = 'tu_host'
  DB_USER = 'tu_usuario'
  DB_PASSWORD = 'tu_contraseña'
  DB_NAME = 'tu_Base_Datos'
```
Podemos probar si las credenciales son correctas ejecutando nuestro archivo conexionBD.py.

Para la parte de airflow debemos escalarlo: 

```bash
  airflow standalone
```
una vez adentro iniciamos nos dirigimos a p://localhost:8080 e iniciamos secion con el usuario y contraseña que nos aparece en las líneas de código, y en la seccion de Dags buscamos el dag con el pipline del workshop

![Texto alternativo](https://imagenes.notion.site/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2Fb687bcac-6636-49ac-8ce3-1adf66aa571c%2F6eda33ee-063f-4572-97fc-55839169da94%2Fimage.png?table=block&id=11638733-ed67-806a-8729-c568be1e1c07&spaceId=b687bcac-6636-49ac-8ce3-1adf66aa571c&width=1420&userId=&cache=v2)

#### Para una correcta ejecucuion: 

Para una correcta ejecucion de nuestro repositorio ejecutamos primero nuestro notebook tablasBD, donde crearemos la tabla para el dataset de los grammys en la base de datos. Despues ejecutamos el notebook carga_dataset_BD donde cargamos el dataset de los grammys a la bd.

Podemos ejecutar los otros 2 notebooks que son E.D.A_Spotify, y E.D.A_Grammys, en donde realizamos un analisis para comprender mejor el contenido del dataset.

Luego se puede ejecutar el dag y ver su proceso en airflow

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

Finalmente seleccionamos las tablas que vamos a usar 
