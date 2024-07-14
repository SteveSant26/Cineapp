from .utils_db import ejecutar_query_obtener, ejecutar_query_agregar, ejecutar_query_editar,ejecutar_query_eliminar

def obtener_funciones_bd() -> list:
    """
    Recupera una lista de funciones de la base de datos.

    Retorna:
        list: Una lista de funciones recuperadas de la base de datos.
    """
    query = "SELECT * FROM funciones"
    return ejecutar_query_obtener(query, "funciones")

def agregar_funcion_bd(datos_funcion: tuple) -> bool:
    """
    Agrega una función a la base de datos.

    Parameters:
    datos_funcion (tuple): Una tupla que contiene los datos de la función a agregar. 
                           Los datos deben estar en el siguiente orden: (pelicula_id, sala_id, hora).

    Returna:
    bool: True si la función se agrega correctamente, False en caso contrario

    """
    query = "INSERT INTO funciones (pelicula_id, sala_id, hora) VALUES (%s, %s, %s)"
    return ejecutar_query_agregar(query, datos_funcion, "funciones")


def editar_funcion_bd(datos_funcion: tuple) -> bool:
    """
    Edita una función en la base de datos con los datos proporcionados.

    Parámetros:
        datos_funcion (tuple): Una tupla que contiene los datos actualizados de la función en el siguiente orden:
            - pelicula_id (int): El ID de la película asociada a la función.
            - sala_id (int): El ID de la sala donde se lleva a cabo la función.
            - hora (str): La hora de la función en formato "HH:MM".
            - id (int): El ID de la función a editar.

    Retorna:
        bool: True si la función se edita correctamente, False en caso contrario.
    """
    query = "UPDATE funciones SET pelicula_id = %s, sala_id = %s, hora = %s WHERE id = %s"
    return ejecutar_query_editar(query, datos_funcion, "funciones")

def eliminar_funcion_bd(funcion_id: int) -> bool:
    """
    Elimina una función de la base de datos basándose en el ID de función proporcionado.

    Parámetros:
        id_funcion (int): El ID de la función a eliminar.

    Retorna:
        bool: True si la función se elimina correctamente, False en caso contrario.
    """
    query = "DELETE FROM funciones WHERE id = %s"
    return ejecutar_query_eliminar(query, funcion_id, "funciones")
