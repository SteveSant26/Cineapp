import customtkinter as ctk
from backend.database import ejecutar_query_obtener


def obtener_pelicula_por_id(id_pelicula: int) -> dict:
    """
    Obtiene los datos de una película por su ID.

    Args:
        id_pelicula (int): El ID de la película.

    Returns:
        dict: Un diccionario con los datos de la película.
    """
    query = "SELECT * FROM peliculas WHERE id = %s"
    return ejecutar_query_obtener(query, "peliculas",datos=(id_pelicula,))

def obtener_usuario_por_id(id_usuario: int) -> dict:
    """
    Obtiene los datos de un usuario por su ID.

    Args:
        id_usuario (int): El ID del usuario.

    Returns:
        dict: Un diccionario con los datos del usuario.
    """
    query = "SELECT usuario FROM usuarios WHERE id = %s"
    return ejecutar_query_obtener(query, "usuarios",datos=(id_usuario,))

def agregar_separador(frame) -> None:
    """
    Agrega un separador horizontal a un frame.

    Args:
        frame: El frame al que se agregará el separador.
    """
    separador = ctk.CTkFrame(frame, height=2,fg_color="black")
    separador.pack(fill="x", pady=10)
    
def actualizar_comentarios(base, id_pelicula) -> None:
    """
    Actualiza los comentarios de una película en la interfaz.

    Args:
        base: La base de la interfaz.
        id_pelicula (int): El ID de la película.
    """
    from .botones_descripcion_peliculas import crear_comentarios
    base.frame_comentarios.destroy()
    crear_comentarios(base,base.frame_descripcion_pelicula, id_pelicula)
    
def limpiar_comentario(comentario) -> str:
    """
    Limpia un comentario eliminando las líneas vacías.

    Args:
        comentario (str): El comentario a limpiar.

    Returns:
        str: El comentario limpio.
    """
    lineas = comentario.splitlines()
    lineas_limpias = [linea for linea in lineas if linea.strip() != ""]
    return "\n".join(lineas_limpias)