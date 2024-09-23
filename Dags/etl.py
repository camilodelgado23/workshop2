from airflow import DAG
from airflow.providers.mysql.operators.mysql import MySqlOperator
from airflow.utils.dates import days_ago

default_args = {
    'owner': 'airflow',
    'start_date': days_ago(1),
}

with DAG('leer_mysql',
         default_args=default_args,
         schedule_interval='@daily',
         catchup=False) as dag:

    leer_datos_grammys = MySqlOperator(
        task_id='leer_datos_grammys',
        mysql_conn_id='workshop2',
        sql='SELECT * FROM Grammys;',
        dag=dag
    )
