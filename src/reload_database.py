# reload_database.py

from database import create_database_connection

def reload_database():
    # Intentar reconectar a la base de datos
    connection = create_database_connection()

    if connection is None:
        print("Error al reconectar a la base de datos. La recarga se canceló.")
        return

    cursor = connection.cursor()

    # Ejecutar FLUSH TABLES para reiniciar la conexión
    try:
        cursor.execute("FLUSH TABLES")
        connection.commit()
        print("Base de datos reiniciada exitosamente.")
    except Exception as e:
        print(f"Error al reiniciar la base de datos: {e}")
    finally:
        cursor.close()
        connection.close()

if __name__ == "__main__":
    reload_database()