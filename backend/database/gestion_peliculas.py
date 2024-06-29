from.utils_db import ejecutar_query_obtener,ejecutar_query_agregar,ejecutar_query_editar,ejecutar_query_eliminar

def obtener_peliculas_bd():
    query = "SELECT * FROM peliculas"
    return ejecutar_query_obtener(query,"peliculas")

def obtener_id_titulo_pelicula_bd():
    query = "SELECT id, titulo FROM peliculas"
    return ejecutar_query_obtener(query,"peliculas")

def obtener_titulo_pelicula_por_id(id_pelicula: int):
    query = "SELECT titulo FROM peliculas WHERE id = %s"
    return ejecutar_query_obtener(query, "peliculas", datos=(id_pelicula,))

def agregar_pelicula_bd(datos_pelicula: tuple):
    query = "INSERT INTO peliculas (id, ruta_imagen, titulo, sinopsis, genero, duracion, estreno, promedio_votos) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    return ejecutar_query_agregar(query, datos_pelicula, "peliculas")

def editar_pelicula_bd(datos_pelicula: tuple):
    query = "UPDATE peliculas SET ruta_imagen = %s, titulo = %s, sinopsis = %s, genero = %s, duracion = %s, estreno = %s, promedio_votos = %s WHERE id = %s"
    return ejecutar_query_editar(query, datos_pelicula, "peliculas")

def eliminar_pelicula_bd(id_pelicula: int):
    query = "DELETE FROM peliculas WHERE id = %s"
    return ejecutar_query_eliminar(query, id_pelicula, "peliculas")