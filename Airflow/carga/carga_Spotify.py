import pandas as pd
import numpy as np
import sys
import os

# Agregar la ruta del directorio 'workshop2' al PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from Base_de_Datos_Operaciones.conexionBD import create_connection

# Función para cargar el archivo CSV
def load_spotify_csv(file_path):
    """Cargar y procesar el archivo CSV de Spotify."""
    # Cargar el archivo CSV
    Dataset_Spotify = pd.read_csv(file_path)

    if 'Unnamed: 0' in Dataset_Spotify.columns:
        Dataset_Spotify = Dataset_Spotify.rename(columns={'Unnamed: 0': 'id'})

    if 'id' in Dataset_Spotify.columns:
        Dataset_Spotify['id'] = np.nan

    Dataset_Spotify = Dataset_Spotify.fillna({
        'id': 0,
        'track_id': 0, 
        'artists': 'Unknown',
        'album_name': 'Unknown',
        'track_name': 'Unknown',
        'popularity': 0,
        'duration_ms': 0,
        'explicit': False,
        'danceability': 0.0,
        'energy': 0.0,
        'key': 0,
        'loudness': 0.0,
        'mode': 0,
        'speechiness': 0.0,
        'acousticness': 0.0,
        'instrumentalness': 0.0,
        'liveness': 0.0,
        'valence': 0.0,
        'tempo': 0.0,
        'time_signature': 0,
        'track_genre': 'Unknown'
    })
    
    print("Dataset procesado exitosamente.")
    return Dataset_Spotify

# Función para crear la tabla de Spotify
def create_spotify_table(connection):
    """Crear la tabla Spotify en la base de datos."""
    create_table_query = """
    CREATE TABLE IF NOT EXISTS Spotify  (
        id SERIAL PRIMARY KEY, 
        track_id VARCHAR(700) NOT NULL,
        artists VARCHAR(700) NOT NULL,
        album_name VARCHAR(400) NOT NULL,
        track_name VARCHAR(700) NOT NULL,
        popularity INT NOT NULL,
        duration_ms INT NOT NULL,
        explicit BOOLEAN NOT NULL,
        danceability FLOAT NOT NULL,
        energy FLOAT NOT NULL,
        `key` INT NOT NULL,
        loudness FLOAT NOT NULL,
        mode INT NOT NULL,
        speechiness FLOAT NOT NULL,
        acousticness FLOAT NOT NULL,
        instrumentalness FLOAT NOT NULL,
        liveness FLOAT NOT NULL,
        valence FLOAT NOT NULL,
        tempo FLOAT NOT NULL,
        time_signature INT NOT NULL,
        track_genre VARCHAR(400) NOT NULL
    );
    """
    try:
        cursor = connection.cursor()
        cursor.execute(create_table_query)
        connection.commit()
        print("Tabla Spotify creada exitosamente.")
    except Exception as e:
        print(f"Error al crear la tabla: {e}")
    finally:
        if connection.is_connected():
            cursor.close()

# Función para insertar los datos en la tabla
def insert_spotify_data(connection, Dataset_Spotify):
    """Insertar los datos del dataset en la tabla Spotify."""
    insert_query = """
    INSERT INTO Spotify (id, track_id, artists, album_name, track_name, popularity, duration_ms, explicit, danceability, energy, `key`, loudness, mode, speechiness, acousticness, instrumentalness, liveness, valence, tempo, time_signature, track_genre)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    
    data = Dataset_Spotify.values.tolist()

    try:
        cursor = connection.cursor()
        cursor.executemany(insert_query, data)
        connection.commit()
        print("Datos insertados correctamente en la tabla Spotify.")
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
        Dataset_Spotify = load_spotify_csv(file_path)
        
        create_spotify_table(connection)
        
        insert_spotify_data(connection, Dataset_Spotify)
    else:
        print("Error: No se pudo establecer la conexión con la base de datos.")

if __name__ == "__main__":
    main('workshop2/csv/spotify_dataset.csv')
