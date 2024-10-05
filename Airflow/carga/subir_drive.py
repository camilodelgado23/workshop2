from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

def upload_to_drive(file_path):
    # Autenticación y creación del servicio de Google Drive
    SCOPES = ['https://www.googleapis.com/auth/drive.file']
    SERVICE_ACCOUNT_FILE = 'workshop2/credentials.json'  # Ruta a tu archivo de credenciales

    # Cargar las credenciales
    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

    # Crear el servicio de Google Drive
    service = build('drive', 'v3', credentials=credentials)

    # Crear un archivo en Google Drive
    file_metadata = {
        'name': 'mergedg_dataset.csv',  # Nombre del archivo en Drive
        'mimeType': 'text/csv'  # Tipo de archivo
    }

    media = MediaFileUpload(file_path, mimetype='text/csv')

    # Crear el archivo en Drive
    file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
    print(f'Archivo subido, ID: {file.get("id")}')
