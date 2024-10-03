import pandas as pd
import numpy as np
import sys
import os

# Agregar la ruta del directorio 'Base_de_Datos_Operaciones' al PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from Base_de_Datos_Operaciones.conexionBD import create_connection

# Función para cargar el archivo CSV
def load_merge_csv(file_path):
    """Cargar y procesar el archivo CSV de Spotify."""
    # Cargar el archivo CSV
    Dataset_merge = pd.read_csv(file_path)

    # Rellenar valores nulos con valores predeterminados
    Dataset_merge= Dataset_merge.fillna({
        'id': 0,
        'track_id': 'Unknown', 
        'artists': 'Unknown',
        'album_name': 'Unknown',
        'track_name': 'Unknown',
        'popularity': 0,
        'duration_ms': 0,
        'explicit': False,
        'danceability': 0.0,
        'energy': 0.0,
        'loudness': 0.0,
        'mode': 0,
        'speechiness': 0.0,
        'acousticness': 0.0,
        'instrumentalness': 0.0,
        'liveness': 0.0,
        'valence': 0.0,
        'tempo': 0.0,
        'track_genre': 'Unknown',
        'year': 0,
        'category': 'Unknown',
        'nominee': 'Unknown',
        'winner': False
    })
    
    # Asegurarse de que 'explicit' sea booleano
    Dataset_merge['explicit'] = Dataset_merge['explicit'].astype(bool)

    print("Dataset procesado exitosamente.")
    print(Dataset_merge.head())  # Verificar los datos procesados
    return Dataset_merge

# Función para crear la tabla de Spotify
def create_merge_table(connection):
    """Crear la tabla merge en la base de datos."""
    create_table_query = """
    CREATE TABLE IF NOT EXISTS merge (
        id INT AUTO_INCREMENT PRIMARY KEY,
        track_id VARCHAR(700) NOT NULL,
        artists VARCHAR(700) NOT NULL,
        album_name VARCHAR(400) NOT NULL,
        track_name VARCHAR(700) NOT NULL,
        popularity INT NOT NULL,
        duration_ms INT NOT NULL,
        explicit BOOLEAN NOT NULL,
        danceability FLOAT NOT NULL,
        energy FLOAT NOT NULL,
        loudness FLOAT NOT NULL,
        mode INT NOT NULL,
        speechiness FLOAT NOT NULL,
        acousticness FLOAT NOT NULL,
        instrumentalness FLOAT NOT NULL,
        liveness FLOAT NOT NULL,
        valence FLOAT NOT NULL,
        tempo FLOAT NOT NULL,
        track_genre VARCHAR(400) NOT NULL,
        year INT NOT NULL,
        category VARCHAR(400),
        nominee VARCHAR(400),
        winner VARCHAR(400)
    );
    """
    try:
        cursor = connection.cursor()
        cursor.execute(create_table_query)
        connection.commit()
        print("Tabla merge creada exitosamente.")
    except Exception as e:
        print(f"Error al crear la tabla: {e}")
    finally:
        if connection.is_connected():
            cursor.close()

def insert_merge_data(connection, Dataset_merge):
    """Insertar los datos del dataset en la tabla merge."""
    insert_query = """
    INSERT INTO merge (
        track_id, artists, album_name, track_name, popularity, duration_ms,
        explicit, danceability, energy, loudness, mode, speechiness,
        acousticness, instrumentalness, liveness, valence, tempo,
        track_genre, year, category, nominee, winner
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    
    # Especificar las columnas a insertar (sin 'id')
    selected_columns = [
        'track_id', 'artists', 'album_name', 'track_name', 
        'popularity', 'duration_ms', 'explicit', 
        'danceability', 'energy', 'loudness', 
        'mode', 'speechiness', 'acousticness', 
        'instrumentalness', 'liveness', 'valence', 
        'tempo', 'track_genre', 'year', 
        'category', 'nominee', 'winner'
    ]
    
    # Filtra el DataFrame para que solo contenga las columnas necesarias
    data = Dataset_merge[selected_columns].values.tolist()
    
    print(f"Número de filas a insertar: {len(data)}")
    print(f"Primeros registros a insertar: {data[:5]}")

    try:
        cursor = connection.cursor()
        for record in data:
            if len(record) != 21:  # Verifica que la longitud sea 21
                print(f"Error: El registro tiene {len(record)} elementos, se esperaban 21. Registro: {record}")
                continue
            
            cursor.execute(insert_query, record)
        connection.commit()
        print("Datos insertados correctamente.")
    except Exception as e:
        print(f"Error al insertar datos: {e}")
    finally:
        if connection.is_connected():
            cursor.close()

# Función principal para ejecutar todo el proceso
def main(file_path):
    """Proceso principal: Cargar CSV, crear tabla, e insertar datos."""
    connection = create_connection()
    
    if connection:
        Dataset_merge = load_merge_csv(file_path)
        
        create_merge_table(connection)
        
        insert_merge_data(connection, Dataset_merge)
    else:
        print("Error: No se pudo establecer la conexión con la base de datos.")

if __name__ == "__main__":
    main('workshop2/csv/mergedg_dataset.csv')  # Cambia a la ruta de tu archivo CSV
