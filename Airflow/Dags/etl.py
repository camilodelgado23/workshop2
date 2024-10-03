from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.hooks.base_hook import BaseHook
from datetime import datetime
import pandas as pd
import sqlalchemy

def create_spotify_table(engine):
    # Definir la consulta para crear la tabla
    create_table_query = """
    CREATE TABLE IF NOT EXISTS spotify_table (
        id INT AUTO_INCREMENT PRIMARY KEY,
        track_name VARCHAR(255),
        artist_name VARCHAR(255),
        album_name VARCHAR(255),
        release_date DATE,
        duration_ms INT,
        popularity INT
        -- Agrega aquí otras columnas según sea necesario
    )
    """
    with engine.connect() as connection:
        connection.execute(create_table_query)

def read_spotify_data():
    # Leer el archivo CSV
    df = pd.read_csv('csv/spotify_data.csv')
    
    # Obtener la conexión a MySQL desde Airflow
    connection = BaseHook.get_connection('my_mysql_connection')  # Cambia 'my_mysql_connection' por el nombre de tu conexión
    
    # Crear el motor de SQLAlchemy utilizando la conexión
    engine = sqlalchemy.create_engine(
        f"mysql+pymysql://{connection.login}:{connection.password}@{connection.host}:{connection.port}/{connection.schema}"
    )
    
    # Crear la tabla si no existe
    create_spotify_table(engine)

    # Guardar en la base de datos MySQL
    df.to_sql('spotify_table', con=engine, if_exists='replace', index=False)

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 9, 30),
}

with DAG('spotify_etl', default_args=default_args, schedule_interval='@daily') as dag:
    task_read_spotify = PythonOperator(
        task_id='read_spotify',
        python_callable=read_spotify_data
    )
