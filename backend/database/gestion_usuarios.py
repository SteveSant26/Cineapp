from .utils_db import ejecutar_query_obtener, ejecutar_query_agregar, ejecutar_query_editar, ejecutar_query_eliminar

def obtener_usuarios_bd() -> list:
    """
    Obtiene la lista de usuarios desde la base de datos.

    Returns:
        list: Lista de usuarios.
    """
    query = "SELECT * FROM usuarios"
    return ejecutar_query_obtener(query, "usuarios")

def agregar_usuario_bd(datos_usuario: tuple) -> bool:
    """
    Agrega un nuevo usuario a la base de datos.

    Args:
        datos_usuario (tuple): Datos del usuario a agregar.

    Returns:
        bool: True si se agrega correctamente, False en caso contrario.
    """
    query = "INSERT INTO usuarios (nombre, apellido,usuario, contrasena, tipo_usuario) VALUES (%s, %s, %s, %s, %s)"
    return ejecutar_query_agregar(query, datos_usuario, "usuarios")

def editar_usuario_bd(datos_usuario: tuple) -> bool:
    """
    Edita los datos de un usuario en la base de datos.

    Args:
        datos_usuario (tuple): Nuevos datos del usuario.

    Returns:
        bool: True si se edita correctamente, False en caso contrario.
    """
    query = "UPDATE usuarios SET nombre = %s, apellido = %s, usuario = %s, contrasena = %s WHERE id = %s"
    return ejecutar_query_editar(query, datos_usuario, "usuarios")

def eliminar_usuario_bd(id_usuario: int) -> bool:
    """
    Elimina un usuario de la base de datos.

    Args:
        id_usuario (int): ID del usuario a eliminar.

    Returns:
        bool: True si se elimina correctamente, False en caso contrario.
    """
    query = "DELETE FROM usuarios WHERE id = %s"
    return ejecutar_query_eliminar(query, id_usuario, "usuarios")