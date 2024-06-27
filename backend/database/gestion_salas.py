from .crear_conexion import abrir_conexion

def obtener_salas_bd():
    conexion = abrir_conexion()
    with conexion:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM salas")
        peliculas = cursor.fetchall()
    return peliculas

