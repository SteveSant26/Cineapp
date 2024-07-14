from .utils_db import ejecutar_query_obtener, ejecutar_query_agregar, ejecutar_query_editar, ejecutar_query_eliminar

def obtener_peliculas_bd() -> list:
    """
    Obtiene todas las películas de la base de datos.

    Returns:
        list: Lista de películas.
    """
    query = "SELECT * FROM peliculas"
    return ejecutar_query_obtener(query, "peliculas")

def agregar_pelicula_bd(datos_pelicula: tuple) ->bool:
    """
    Agrega una nueva película a la base de datos.

    Args:
        datos_pelicula (tuple): Datos de la película a agregar.

    Returns:
        bool: True si se agregó la película, False en caso contrario.
    """
    query = "INSERT INTO peliculas (id, ruta_imagen, titulo, sinopsis, genero, duracion, estreno, promedio_votos) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    return ejecutar_query_agregar(query, datos_pelicula, "peliculas")

def editar_pelicula_bd(datos_pelicula: tuple) -> bool:
    """
    Edita los datos de una película en la base de datos.

    Args:
        datos_pelicula (tuple): Nuevos datos de la película.

    Returns:
        bool: True si se editó la película, False en caso contrario.
    """
    query = "UPDATE peliculas SET ruta_imagen = %s, titulo = %s, sinopsis = %s, genero = %s, duracion = %s, estreno = %s, promedio_votos = %s WHERE id = %s"
    return ejecutar_query_editar(query, datos_pelicula, "peliculas")

def eliminar_pelicula_bd(pelicula_id: int) -> bool:
    """
    Elimina una película de la base de datos.

    Args:
        id_pelicula (int): ID de la película a eliminar.

    Returns:
        bool: True si se eliminó la película, False en caso contrario.
    """
    query = "DELETE FROM peliculas WHERE id = %s"
    return ejecutar_query_eliminar(query, pelicula_id, "peliculas")