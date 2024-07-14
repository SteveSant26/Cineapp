from .utils_db import ejecutar_query_obtener, ejecutar_query_agregar, ejecutar_query_editar, ejecutar_query_eliminar

def obtener_salas_bd() -> list:
    """
    Obtiene todas las salas de la base de datos.

    Returns:
        list: Una lista de diccionarios que representan las salas.
    """
    query = "SELECT * FROM salas"
    return ejecutar_query_obtener(query, "salas")

def agregar_sala_bd(datos_sala: tuple) -> bool:
    """
    Agrega una nueva sala a la base de datos.

    Args:
        datos_sala (tuple): Una tupla con los datos de la sala (nombre, filas, columnas).

    Returns:
        bool: True si la sala se agregó correctamente, False en caso contrario.
    """
    query = "INSERT INTO salas (nombre, filas, columnas) VALUES (%s, %s, %s)"
    return ejecutar_query_agregar(query, datos_sala, "salas")

def editar_sala_bd(datos_sala: tuple) -> bool:
    """
    Edita los datos de una sala en la base de datos.

    Args:
        datos_sala (tuple): Una tupla con los nuevos datos de la sala (nombre, filas, columnas, id).

    Returns:
        bool: True si la sala se editó correctamente, False en caso contrario.
    """
    query = "UPDATE salas SET nombre = %s, filas = %s, columnas = %s WHERE id = %s"
    return ejecutar_query_editar(query, datos_sala, "salas")

def eliminar_sala_bd(sala_id: int) -> bool:
    """
    Elimina una sala de la base de datos.

    Args:
        id_sala (int): El ID de la sala a eliminar.

    Returns:
        bool: True si la sala se eliminó correctamente, False en caso contrario.
    """
    query = "DELETE FROM salas WHERE id = %s"
    return ejecutar_query_eliminar(query, sala_id, "salas")