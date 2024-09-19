import mysql.connector
from mysql.connector import Error
import sys
import os

# Puede instalar las librerias ejecutando el siguiente comando en la terminal: pip install -r requirements.txt

# Añadir el directorio raíz al sys.path para permitir importaciones
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importar las credenciales
import credentials as credentials

def create_connection():
    """Crear Conexion con Base de Datos."""
    try:
        print("Conectando con la Base de Datos...")
        connection = mysql.connector.connect(
            host=credentials.DB_HOST,
            user=credentials.DB_USER,
            password=credentials.DB_PASSWORD,
            database=credentials.DB_NAME
        )
        if connection.is_connected():
            print('Conexion con la Base de Datos MySQL Lograda.')
            return connection
        else:
            print('Conexion Fallida.')
            return None
    except Error as e:
        print(f'Error: {e}')
        return None

if __name__ == "__main__":
    create_connection()
    