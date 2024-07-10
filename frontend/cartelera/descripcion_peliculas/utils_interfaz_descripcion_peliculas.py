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