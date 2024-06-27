from .crear_conexion import abrir_conexion

def obtener_peliculas_bd():
    conexion = abrir_conexion()
    with conexion:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM peliculas")
        peliculas = cursor.fetchall()
    return peliculas

