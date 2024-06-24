import sqlite3

    
    
def crear_conexion():
    try:
        conexion =  sqlite3.connect("Base de datos y api\\cinema.db")
        return conexion
    except sqlite3.Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None

def obtener_peliculas():
    conexion = crear_conexion()
    with conexion:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM peliculas")
        peliculas = cursor.fetchall()
    print(peliculas)
    return peliculas