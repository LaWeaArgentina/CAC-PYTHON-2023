import mysql.connector
from dotenv import load_dotenv
import os

# Carga las variables de entorno de un archivo .env
load_dotenv()

db_config = {
    'host': os.getenv('MYSQL_HOST'),
    'user': os.getenv('MYSQL_USER'),
    'password': os.getenv('MYSQL_PASSWORD'),
    'database': os.getenv('MYSQL_DATABASE')
}

database = mysql.connector.connect(**db_config)
