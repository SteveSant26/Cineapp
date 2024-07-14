from .utils_db import ejecutar_query_obtener, ejecutar_query_agregar,ejecutar_query_editar,ejecutar_query_eliminar

def obtener_comentarios_pelicula(pelicula_id:int) -> list:
    """
    Obtiene los comentarios de una película dado su ID.

    Parameters:
    pelicula_id (int): El ID de la película.

    Returns:
    list: Una lista de comentarios de la película.
    """
    query = "SELECT * FROM comentarios WHERE pelicula_id = %s"
    return ejecutar_query_obtener(query, "comentarios",datos=(pelicula_id,))

def agregar_comentario_pelicula(pelicula_id:int,usuario_id:int,comentario:str) -> bool:
    """
    Agrega un comentario de un usuario a una película en la base de datos.

    Parameters:
    pelicula_id (int): El ID de la película a la que se desea agregar el comentario.
    usuario_id (int): El ID del usuario que realiza el comentario.
    comentario (str): El contenido del comentario.

    Returns:
    bool: True si el comentario se agregó correctamente, False en caso contrario.
    """
    datos = (usuario_id,pelicula_id,comentario)
    query = "INSERT INTO comentarios (usuario_id,pelicula_id,comentario) VALUES (%s,%s,%s)"
    return ejecutar_query_agregar(query,datos,"comentarios")

def editar_comentario_pelicula(comentario_id:int,comentario:str) -> bool:
    """
        Edita un comentario de una película en la base de datos.

        Parámetros:
        comentario_id (int): El ID del comentario que se desea editar.
        comentario (str): El nuevo texto del comentario.

        Retorna:
        bool: True si el comentario se editó correctamente, False en caso contrario.
    """
    
    datos = (comentario,comentario_id)
    query = "UPDATE comentarios SET comentario = %s WHERE id = %s"
    return ejecutar_query_editar(query,datos,"comentarios")

def eliminar_comentario_pelicula(comentario_id:int) -> bool:
    """
    Elimina un comentario de la base de datos basado en el ID del comentario.

    Parámetros:
    comentario_id (int): El ID del comentario que se desea eliminar.

    Retorna:
    bool: True si el comentario se eliminó correctamente, False en caso contrario.
    """
    query = "DELETE FROM comentarios WHERE id = %s"
    return ejecutar_query_eliminar(query,comentario_id,"comentarios")