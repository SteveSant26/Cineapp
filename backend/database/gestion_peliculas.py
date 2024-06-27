from .crear_conexion import abrir_conexion
from frontend.utils import mostrar_error

def obtener_peliculas_bd():
    conexion = abrir_conexion()
    with conexion:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM peliculas")
        peliculas = cursor.fetchall()
    return peliculas

def agregar_pelicula_bd(datos_pelicula: tuple):
    conexion = abrir_conexion()
    query = "INSERT INTO peliculas (id, ruta_imagen, titulo, sinopsis, genero, duracion, estreno, promedio_votos) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    try:
        with conexion:
            cursor = conexion.cursor()
            cursor.execute(query, datos_pelicula)
            conexion.commit()
        return True
    except Exception as e:
        mostrar_error("Error al agregar pelicula", f"No se pudo agregar la pelicula a la base de datos: {e}")

def editar_pelicula_bd(datos_pelicula: tuple):
    conexion = abrir_conexion()
    query = "UPDATE peliculas SET ruta_imagen = %s, titulo = %s, sinopsis = %s, genero = %s, duracion = %s, estreno = %s, promedio_votos = %s WHERE id = %s"
    try:
        with conexion:
            cursor = conexion.cursor()
            cursor.execute(query, datos_pelicula)
            conexion.commit()
        return True
    except Exception as e:
        mostrar_error("Error al editar pelicula", f"No se pudo editar la pelicula en la base de datos: {e}")
    
def eliminar_pelicula_bd(id_pelicula: int):
    conexion = abrir_conexion()
    query = "DELETE FROM peliculas WHERE id = %s"
    try:
        with conexion:
            cursor = conexion.cursor()
            cursor.execute(query, (id_pelicula,))
            conexion.commit()
        return True
    except Exception as e:
        mostrar_error("Error al eliminar pelicula", f"No se pudo eliminar la pelicula de la base de datos: {e}")