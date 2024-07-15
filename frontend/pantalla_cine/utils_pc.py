from backend.database import ejecutar_query_obtener

def obtener_sala_id_en_funciones_por_pelicula_id_bd(id_pelicula: int) -> list:
    """
    Obtiene los IDs de las salas donde se proyecta una película específica.

    Args:
        id_pelicula (int): El ID de la película.

    Returns:
        list: Una lista de tuplas con los IDs de las salas.
    """
    query = "SELECT sala_id FROM funciones where pelicula_id = %s"
    return ejecutar_query_obtener(query, "funciones", datos=(id_pelicula,))

def obtener_nombre_sala_por_id_bd(id_sala: int) -> list:
    """
    Obtiene el nombre de una sala dado su ID.

    Args:
        id_sala (int): El ID de la sala.

    Returns:
        list: Una lista con el nombre de la sala.
    """
    query = "SELECT nombre FROM salas WHERE id = %s"
    return ejecutar_query_obtener(query, "salas", datos=(id_sala,))

def obtener_sala_id_por_nombre_bd(nombre_sala: str) -> list:
    """
    Obtiene el ID de una sala dado su nombre.

    Args:
        nombre_sala (str): El nombre de la sala.

    Returns:
        list: Una lista con el ID de la sala.
    """
    query = "SELECT id FROM salas WHERE nombre = %s"
    return ejecutar_query_obtener(query, "salas", datos=(nombre_sala,))

def obtener_salas(id_pelicula: int) -> list:
    """
    Obtiene los nombres de las salas donde se proyecta una película específica.

    Args:
        id_pelicula (int): El ID de la película.

    Returns:
        list: Una lista con los nombres de las salas.
    """
    ids_salas = sorted([i[0] for i in set(obtener_sala_id_en_funciones_por_pelicula_id_bd(id_pelicula))])
    return [obtener_nombre_sala_por_id_bd(id_sala)[0][0] for id_sala in ids_salas]

def obtener_funciones_misma_pelicula(id_pelicula: int, nombre_Sala: str) -> list:
    """
    Obtiene las funciones de una película específica en una sala específica.

    Args:
        id_pelicula (int): El ID de la película.
        nombre_Sala (str): El nombre de la sala.

    Returns:
        list: Una lista de tuplas con la hora y el ID de las funciones.
    """
    id_sala = obtener_sala_id_por_nombre_bd(nombre_Sala)[0][0]
    query = "SELECT hora, id FROM funciones where pelicula_id = %s and sala_id = %s"
    return ejecutar_query_obtener(query, "funciones", datos=(id_pelicula, id_sala))

def obtener_funciones(id_pelicula: int, nombre_Sala: str) -> list:
    """
    Obtiene las horas de las funciones de una película específica en una sala específica.

    Args:
        id_pelicula (int): El ID de la película.
        nombre_Sala (str): El nombre de la sala.

    Returns:
        list: Una lista con las horas de las funciones.
    """
    fechas = [str(i[0]) for i in obtener_funciones_misma_pelicula(id_pelicula, nombre_Sala)]
    return sorted(fechas)

def obtener_funcion_id_por_sala_pelicula_id(sala_id: int, pelicula_id: int, hora: str) -> int:
    """
    Obtiene el ID de una función dado el ID de la sala, el ID de la película y la hora de la función.

    Args:
        sala_id (int): El ID de la sala.
        pelicula_id (int): El ID de la película.
        hora (str): La hora de la función.

    Returns:
        int: El ID de la función.
    """
    query = "SELECT id FROM funciones WHERE sala_id = %s and pelicula_id = %s and hora = %s"
    return ejecutar_query_obtener(query, "funciones", datos=(sala_id, pelicula_id, hora))[0][0]

def conseguir_tamano_sala_por_nombre_bd(nombre_sala: str) -> list:
    """
    Obtiene el tamaño de una sala (filas y columnas) dado su nombre.

    Args:
        nombre_sala (str): El nombre de la sala.

    Returns:
        list: Una lista con el número de filas y columnas de la sala.
    """
    query = "SELECT filas, columnas FROM salas WHERE nombre = %s"
    return ejecutar_query_obtener(query, "salas", datos=(nombre_sala,))

def obtener_tamano_sala(nombre_sala: str) -> tuple:
    """
    Obtiene el tamaño de una sala (filas y columnas) dado su nombre.

    Args:
        nombre_sala (str): El nombre de la sala.

    Returns:
        tuple: Una tupla con el número de filas y columnas de la sala.
    """
    filas, columnas = conseguir_tamano_sala_por_nombre_bd(nombre_sala)[0]
    return filas, columnas
