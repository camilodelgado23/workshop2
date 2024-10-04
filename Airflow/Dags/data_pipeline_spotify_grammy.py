from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
from datetime import timedelta
import sys
import os

import pandas as pd

# Agregar la ruta del directorio 'workshop2' al PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

# Importar tus módulos
from Airflow.carga.carga_Spotify import main as carga_spotify
from Airflow.Union.merge_dataset import seleccionar_spotify, seleccionar_grammys, unir_datasets
from Airflow.carga.carga_merge import main as carga_merge
from Base_de_Datos_Operaciones.conexionBD import create_connection

# Definir argumentos por defecto del DAG
default_args = {
    'owner': 'cami',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Definir el DAG
dag = DAG(
    'spotify_grammy_data_pipeline',
    default_args=default_args,
    description='Pipeline de datos para Spotify y Grammys',
    schedule_interval=None,  # Aquí defines el intervalo de ejecución. None es para ejecución manual
    start_date=days_ago(1),  # La fecha de inicio se ajusta a ayer
    catchup=False,
)

# 1. Tarea: Cargar el dataset de Spotify en la base de datos y seleccionar los datos
def cargar_y_seleccionar_spotify():
    # Cargar el CSV en la base de datos
    carga_spotify('workshop2/csv/spotify_dataset.csv')  # Asegúrate de que la función carga_spotify esté implementada para esto
    
    # Crear conexión y seleccionar datos de la tabla
    connection = create_connection()
    spotify_df = seleccionar_spotify(connection, 'Spotify')
    connection.close()
    
    return spotify_df  # Retornar el DataFrame

cargar_spotify_task = PythonOperator(
    task_id='cargar_y_seleccionar_csv_spotify',
    python_callable=cargar_y_seleccionar_spotify,
    dag=dag,
)

# 2. Tarea: Transformar el dataset de Spotify (eliminación de columnas)
def transformacion_spotify_dataset(ti):
    spotify_df = ti.xcom_pull(task_ids='cargar_y_seleccionar_csv_spotify')  # Obtener el DataFrame de la tarea anterior
    
    if spotify_df is not None:
        # Eliminación de columnas innecesarias
        spotify_df = spotify_df.drop(columns=['time_signature', 'key'], errors='ignore')
        return spotify_df  # Retornar el DataFrame transformado

transformacion_spotify_task = PythonOperator(
    task_id='transformacion_dataset_spotify',
    python_callable=transformacion_spotify_dataset,
    dag=dag,
)

# 3. Extraer datos de la BD de Grammys
def extraccion_grammys():
    connection = create_connection()
    grammys_df = seleccionar_grammys(connection, 'Grammys')
    connection.close()
    return grammys_df  

extraccion_grammys_task = PythonOperator(
    task_id='extraccion_bd_grammys',
    python_callable=extraccion_grammys,
    dag=dag,
)

# 4. Tarea: Transformar el dataset de Grammys (eliminación de columnas innecesarias)
def transformacion_grammys_dataset():
    connection = create_connection()
    grammys_df = seleccionar_grammys(connection, 'Grammys')
    
    grammys_df = grammys_df.drop(columns=['published_at', 'updated_at', 'workers', 'img'], errors='ignore')
    
    connection.close()
    return grammys_df

transformacion_grammys_task = PythonOperator(
    task_id='transformacion_dataset_grammys',
    python_callable=transformacion_grammys_dataset,
    dag=dag,
)

# Tarea: Unir los datasets de Spotify y Grammys
def unir_datasets_spotify_grammys():
    connection = create_connection()

    # Seleccionar los datasets de Spotify y Grammys directamente de la base de datos
    spotify_df = seleccionar_spotify(connection, 'Spotify')
    grammys_df = seleccionar_grammys(connection, 'Grammys')

    if spotify_df is not None and grammys_df is not None:
        merged_df = unir_datasets(spotify_df, grammys_df)
        merged_df.to_csv('workshop2/csv/mergedg_dataset.csv', index=False)  # Guardar dataset unido
    else:
        print("No se pudieron obtener los DataFrames para la unión.")

    connection.close()

unir_datasets_task = PythonOperator(
    task_id='dataset_union',
    python_callable=unir_datasets_spotify_grammys,
    dag=dag,
)

# Tarea: Cargar el dataset unido en la base de datos
def cargar_merge_data():
    file_path = 'workshop2/csv/mergedg_dataset.csv'  # Ruta del archivo CSV generado
    carga_merge.main(file_path)  # Llama a la función main de carga_merge

cargar_merge_task = PythonOperator(
    task_id='cargar_merge_datos',
    python_callable=cargar_merge_data,
    dag=dag,
)

# Definir dependencias entre las tareas
cargar_spotify_task >> transformacion_spotify_task >> unir_datasets_task >> cargar_merge_task
extraccion_grammys_task >> transformacion_grammys_task >> unir_datasets_task

