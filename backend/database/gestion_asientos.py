from .utils_db import ejecutar_query_obtener, ejecutar_query_agregar, ejecutar_query_editar
import json

def obtener_asientos_reservados(funcion_id:int) -> list:
    """
    Obtiene los asientos reservados para una función específica.

    Parameters:
    funcion_id (int): El ID de la función para la cual se desean obtener los asientos reservados.

    Returns:
    list: Una lista de los asientos reservados para la función especificada.
    """
    
    query = "SELECT * FROM asientos_reservados WHERE funcion_id = %s"
    return ejecutar_query_obtener(query, "asientos_reservados",datos=(funcion_id,))

def crear_asientos_reservados(funcion_id:int) -> bool:
    """
    Crea registros de asientos reservados en la base de datos para una función específica.

    Parameters:
    funcion_id (int): El ID de la función para la cual se crearán los registros de asientos reservados.

    Returns:
    bool: True si los registros se crean correctamente, False en caso contrario.

    """
    datos = (funcion_id,)
    query = "INSERT INTO asientos_reservados (funcion_id) VALUES (%s)"
    return ejecutar_query_agregar(query,datos,"asientos_reservados")

def editar_asiento_reservado(asientos_id, asientos_json) -> bool:
    """
    Edita los asientos reservados para un ID de asiento dado.

    Args:
        id_asientos (int): El ID del asiento.
        asientos_json (str): La representación JSON de los asientos reservados.

    Returns:
        bool: True si los asientos se editan correctamente, False en caso contrario.

    Raises:
        ValueError: Si id_asientos es None.

    """
    if asientos_id is None:
        raise ValueError("id_asientos cannot be None in editar_asiento_reservado")

    datos = (asientos_json, asientos_id)
    query = "UPDATE asientos_reservados SET asientos = %s WHERE id = %s"
    return ejecutar_query_editar(query, datos, "asientos_reservados")
