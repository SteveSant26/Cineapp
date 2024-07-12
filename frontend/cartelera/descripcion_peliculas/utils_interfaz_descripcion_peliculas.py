import customtkinter as ctk
from backend.database import ejecutar_query_obtener


def obtener_pelicula_por_id(id_pelicula: int):
    query = "SELECT * FROM peliculas WHERE id = %s"
    return ejecutar_query_obtener(query, "peliculas",datos=(id_pelicula,))

def obtener_usuario_por_id(id_usuario: int):
    query = "SELECT usuario FROM usuarios WHERE id = %s"
    return ejecutar_query_obtener(query, "usuarios",datos=(id_usuario,))

def agregar_separador(frame):
    separador = ctk.CTkFrame(frame, height=2,fg_color="black")
    separador.pack(fill="x", pady=10)
    
def actualizar_comentarios(base, id_pelicula):
    from .botones_descripcion_peliculas import crear_comentarios
    base.frame_comentarios.destroy()
    crear_comentarios(base,base.frame_descripcion_pelicula, id_pelicula)
    
def limpiar_comentario(comentario):
    lineas = comentario.splitlines()
    lineas_limpias = [linea for linea in lineas if linea.strip() != ""]
    return "\n".join(lineas_limpias)