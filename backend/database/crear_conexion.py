import mysql.connector

def abrir_conexion():
    try:
        conexion =  mysql.connector.connect(
                                            host = '127.0.0.1',
                                            user = 'root',
                                            password = '032605Bryan*',
                                            database = 'cinema',
                                            port = '3306'
                                            )
        return conexion
    except mysql.connector.Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None