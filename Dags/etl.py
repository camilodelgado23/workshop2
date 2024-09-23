from airflow import DAG
from airflow.providers.mysql.operators.mysql import MySqlOperator
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago

default_args = {
    'owner': 'airflow',
    'start_date': days_ago(1),
}

with DAG('proceso_etl',
         default_args=default_args,
         schedule_interval='@daily',
         catchup=False) as dag:

    # Task de lectura de datos
    leer_datos_grammys = MySqlOperator(
        task_id='leer_datos_grammys',
        mysql_conn_id='workshop2',
        sql='SELECT * FROM Grammys;',
        dag=dag
    )

    # Placeholder para la tarea de transformación
    transformar_datos = PythonOperator(
        task_id='transformar_datos',
        python_callable=tu_funcion_transformacion,  # Define tu función de transformación
        dag=dag
    )

    # Placeholder para la tarea de carga
    cargar_datos = PythonOperator(
        task_id='cargar_datos',
        python_callable=tu_funcion_carga,  # Define tu función de carga
        dag=dag
    )

    # Definir las dependencias
    leer_datos_grammys >> transformar_datos >> cargar_datos
