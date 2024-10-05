from aifc import Error
import sys
import os
import pandas as pd
import sqlalchemy

# Agregar la ruta del directorio 'workshop2' al PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from Base_de_Datos_Operaciones.conexionBD import create_connection

# Función para seleccionar datos de Spotify
def seleccionar_spotify(connection, nombre_tabla):
    """Seleccionar todos los datos de la tabla de Spotify."""
    try:
        query = f"SELECT * FROM {nombre_tabla}"
        spotify_df = pd.read_sql(query, connection)

        if not spotify_df.empty:
            print(f"Tabla '{nombre_tabla}' seleccionada correctamente.")
            return spotify_df
        else:
            print(f"La tabla '{nombre_tabla}' está vacía.")
            return None

    except Error as e:
        print(f"Error al seleccionar datos de la tabla '{nombre_tabla}': {e}")
        return None

# Función para seleccionar datos de Grammys
def seleccionar_grammys(connection, nombre_tabla):
    """Seleccionar todos los datos de la tabla de Grammys."""
    try:
        query = f"SELECT * FROM {nombre_tabla}"
        grammys_df = pd.read_sql(query, connection)

        if not grammys_df.empty:
            print(f"Tabla '{nombre_tabla}' seleccionada correctamente.")
            return grammys_df
        else:
            print(f"La tabla '{nombre_tabla}' está vacía.")
            return None

    except Error as e:
        print(f"Error al seleccionar datos de la tabla '{nombre_tabla}': {e}")
        return None

# Función para unir los datasets
def unir_datasets(spotify_df, grammys_df):
    """Unir los datasets de Spotify y Grammys."""
    # Eliminar columnas innecesarias de Spotify
    spotify_df = spotify_df.drop(columns=['time_signature', 'key'], errors='ignore')
    
    # Eliminar columnas innecesarias de Grammys
    grammys_df = grammys_df.drop(columns=['published_at', 'updated_at', 'workers', 'img'], errors='ignore')

    grammys_df.rename(columns={'title': 'track_name', 'artist': 'artists'}, inplace=True)

    merged_df = pd.merge(spotify_df, grammys_df, on=['track_name', 'artists'], how='left')

    return merged_df

# Función para exportar a CSV
def exportar_a_csv(dataframe, nombre_archivo):
    """Exportar el DataFrame a un archivo CSV."""
    dataframe.to_csv(nombre_archivo, index=False)
    print(f"Datos exportados a '{nombre_archivo}'.")

# Función principal
def main():
    connection = create_connection()  
    spotify_df = seleccionar_spotify(connection, 'Spotify')
    grammys_df = seleccionar_grammys(connection, 'Grammys')

    if spotify_df is not None and grammys_df is not None:
        merged_df = unir_datasets(spotify_df, grammys_df)
        exportar_a_csv(merged_df, 'mergedg_dataset.csv')
    connection.close()

if __name__ == '__main__':
    main()
