import mysql.connector

import os

def abrir_conexion() -> mysql.connector.connection.MySQLConnection:
    """
    Abre una conexión a la base de datos del cine.

    Returns:
        mysql.connector.connection.MySQLConnection: El objeto de conexión si tiene éxito, None en caso contrario.
    """
    try:
        conexion = mysql.connector.connect(
            host=os.getenv('MYSQL_HOST', '127.0.0.1'),
            user=os.getenv('MYSQL_USER', 'root'),
            password=os.getenv('MYSQL_PASSWORD', '032605Bryan*'),
            database=os.getenv('MYSQL_DB', 'cinema'),
            port=os.getenv('MYSQL_PORT', '3306')
        )
        return conexion
    except mysql.connector.Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None
