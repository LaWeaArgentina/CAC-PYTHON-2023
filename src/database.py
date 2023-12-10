import mysql.connector
from dotenv import load_dotenv
import os
import time

# Carga las variables de entorno de un archivo .env
load_dotenv()

db_config = {
    'host': os.getenv('MYSQL_HOST'),
    'user': os.getenv('MYSQL_USER'),
    'password': os.getenv('MYSQL_PASSWORD'),
    'database': os.getenv('MYSQL_DATABASE')
}

def create_database_connection():
    try:
        connection = mysql.connector.connect(**db_config)
        return connection
    except mysql.connector.Error as err:
        print(f"Error al conectar a la base de datos: {err}")
        return None

# Manejar la señal SIGHUP
def handle_sighup(signum, frame):
    print("Recibida la señal SIGHUP. Recargando la aplicación...")
    sys.exit(0)

# Configurar el manejador de señales
signal.signal(signal.SIGHUP, handle_sighup)

# Crear la conexión a la base de datos
database = create_database_connection()