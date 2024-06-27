from .crear_conexion import abrir_conexion

def obtener_funciones_bd():
    conexion = abrir_conexion()
    with conexion:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM funciones")
        peliculas = cursor.fetchall()
    return peliculas