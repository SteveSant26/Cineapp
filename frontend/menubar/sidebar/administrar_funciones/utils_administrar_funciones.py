from backend.database import ejecutar_query_obtener


def obtener_id_nombre_sala_bd() -> list:
    """
    Obtiene una lista con los IDs y nombres de todas las salas.

    Returns:
        list: Una lista de tuplas con los IDs y nombres de las salas.
    """
    query = "SELECT id, nombre FROM salas"
    return ejecutar_query_obtener(query, "salas")

def obtener_nombre_sala_por_id(id_sala: int) -> str:
    """
    Obtiene el nombre de una sala dado su ID.

    Args:
        id_sala (int): El ID de la sala.

    Returns:
        str: El nombre de la sala.
    """
    query = "SELECT nombre FROM salas WHERE id = %s"
    resultado = ejecutar_query_obtener(query, "salas", datos=(id_sala,))
    return resultado if resultado else None

def obtener_titulo_pelicula_por_id(id_pelicula: int) -> str:
    """
    Obtiene el título de una película dado su ID.

    Args:
        id_pelicula (int): El ID de la película.

    Returns:
        str: El título de la película.
    """
    query = "SELECT titulo FROM peliculas WHERE id = %s"
    resultado = ejecutar_query_obtener(query, "peliculas", datos=(id_pelicula,))
    return resultado if resultado else None
