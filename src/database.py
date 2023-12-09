import mysql.connector

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '1',
    'database': 'presupuestar'
}

database = mysql.connector.connect(**db_config)
