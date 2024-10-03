from aifc import Error
import sys
import os

# Agregar la ruta del directorio 'workshop2' al PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from Base_de_Datos_Operaciones.conexionBD import create_connection

# Función para seleccionar datos de Spotify
def seleccionar_Spotify(connection, nombre_tabla):
    """Seleccionar todos los datos de una tabla específica."""
    try:
        cursor = connection.cursor()
        query = f"SELECT * FROM {nombre_tabla}"
        cursor.execute(query)

        resultados = cursor.fetchall()

        if resultados:
            print(f"Tabla '{nombre_tabla}' seleccionada correctamente.")
        else:
            print(f"La tabla '{nombre_tabla}' está vacía.")

    except Error as e:
        print(f"Error al seleccionar datos de la tabla '{nombre_tabla}': {e}")
    finally:
        cursor.close()

# Función para seleccionar datos de Grammys
def seleccionar_Grammys(connection, nombre_tabla):
    """Seleccionar todos los datos de una tabla específica."""
    try:
        cursor = connection.cursor()
        query = f"SELECT * FROM {nombre_tabla}"
        cursor.execute(query)

        resultados = cursor.fetchall()

        if resultados:
            print(f"Tabla '{nombre_tabla}' seleccionada correctamente.")
        else:
            print(f"La tabla '{nombre_tabla}' está vacía.")

    except Error as e:
        print(f"Error al seleccionar datos de la tabla '{nombre_tabla}': {e}")
    finally:
        cursor.close()


if __name__ == "__main__":
    connection = create_connection()

    if connection:
        seleccionar_Spotify(connection, "Spotify")
        
        seleccionar_Grammys(connection, "Grammys")
    
    if connection.is_connected():
        connection.close()
