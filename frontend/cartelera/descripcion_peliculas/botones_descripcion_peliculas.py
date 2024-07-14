import customtkinter as ctk 
from tkinter import messagebox

from backend.database import obtener_comentarios_pelicula,editar_comentario_pelicula,eliminar_comentario_pelicula
from frontend import pantalla_cine as PC
from frontend.utils import mostrar_mensaje,mostrar_error

from .. import interfaz_cartelera as IC
from .funciones_botones_descripcion_peliculas import ventana_agregar_comentario, reproducir_trailer
from .utils_interfaz_descripcion_peliculas import obtener_usuario_por_id, agregar_separador, actualizar_comentarios,limpiar_comentario



def boton_reservar_asientos(base: ctk.CTk, frame_botones: ctk.CTkFrame) -> None:
    """
    Crea y añade un botón para reservar asientos en el frame de botones.

    Args:
        base (ctk.CTk): La ventana principal de la aplicación.
        frame_botones (ctk.CTkFrame): El frame donde se añadirá el botón.
    """
    boton_reservar_asientos = ctk.CTkButton(frame_botones, 
                                            text="Reservar asientos",
                                            hover_color="#31AF9C",
                                            fg_color="#329ADF",
                                            height=40,
                                            font=("Arial", 20), 
                                            command=lambda: PC.crear_vista_cine(base))
    boton_reservar_asientos.grid(row=0, column=0, padx=10)

def boton_ver_trailer(frame_botones: ctk.CTkFrame, id_pelicula: int) -> None:
    """
    Crea y añade un botón para ver el trailer de una película en el frame de botones.

    Args:
        frame_botones (ctk.CTkFrame): El frame donde se añadirá el botón.
        id_pelicula (int): El ID de la película cuyo trailer se quiere ver.
    """
    boton_ver_trailer = ctk.CTkButton(frame_botones, 
                                      text="Ver trailer",
                                      hover_color="#31AF9C",
                                      fg_color="#329ADF",
                                      height=40,
                                      font=("Arial", 20), 
                                      command=lambda: reproducir_trailer(id_pelicula))
    boton_ver_trailer.grid(row=0, column=1, padx=10)

def boton_agregar_comentario(base: ctk.CTk, frame_botones: ctk.CTkFrame, id_pelicula: int) -> None:
    """
    Crea y añade un botón para agregar un comentario sobre una película en el frame de botones.

    Args:
        base (ctk.CTk): La ventana principal de la aplicación.
        frame_botones (ctk.CTkFrame): El frame donde se añadirá el botón.
        id_pelicula (int): El ID de la película sobre la cual se quiere agregar un comentario.
    """
    boton_agregar_comentario = ctk.CTkButton(frame_botones, 
                                             text="Agregar comentario",
                                             hover_color="#31AF9C",
                                             fg_color="#329ADF",
                                             height=40,
                                             font=("Arial", 20), 
                                             command=lambda: ventana_agregar_comentario(base, id_pelicula, base.usuario_id))
    boton_agregar_comentario.grid(row=0, column=2, padx=10)

def boton_salir(base: ctk.CTk, frame_botones: ctk.CTkFrame) -> None:
    """
    Crea y añade un botón para volver a la cartelera en el frame de botones.

    Args:
        base (ctk.CTk): La ventana principal de la aplicación.
        frame_botones (ctk.CTkFrame): El frame donde se añadirá el botón.
    """
    boton_salir = ctk.CTkButton(frame_botones, 
                                text="Volver a la cartelera",
                                hover_color="#31AF9C",
                                fg_color="#329ADF",
                                height=40,
                                font=("Arial", 20), 
                                command=lambda: IC.iniciar_hilo_mostrar_peliculas(base))
    boton_salir.grid(row=0, column=3, padx=10)

def crear_comentario(base: ctk.CTk, frame_comentarios: ctk.CTkFrame, nombre_usuario: str, comentario: str, comentario_id: int, id_pelicula: int) -> None:
    """
    Crea y añade un comentario en el frame de comentarios.

    Args:
        base (ctk.CTk): La ventana principal de la aplicación.
        frame_comentarios (ctk.CTkFrame): El frame donde se añadirán los comentarios.
        nombre_usuario (str): El nombre del usuario que realizó el comentario.
        comentario (str): El texto del comentario.
        comentario_id (int): El ID del comentario.
        id_pelicula (int): El ID de la película sobre la cual se realizó el comentario.
    """
    agregar_separador(frame_comentarios)
    frame_comentario = ctk.CTkFrame(frame_comentarios, fg_color="transparent")
    frame_comentario.pack(anchor="w")
    
    comentario_label = ctk.CTkLabel(frame_comentario, text=comentario, font=("Arial", 20), wraplength=1000, justify="left")
    comentario_label.grid(row=0, column=0, pady=10, padx=10, sticky="w")
    
    frame_usuario = ctk.CTkFrame(frame_comentario, fg_color="transparent")
    frame_usuario.grid(row=1, column=0, padx=10, sticky="w")
    
    usuario = ctk.CTkLabel(frame_usuario, text=f"Usuario:", font=("Arial", 20, "bold"), wraplength=1000, justify="left")
    usuario.grid(row=0, column=0, padx=10, sticky="w")
    
    if nombre_usuario == base.usuario:
        nombre_usuario = f"{nombre_usuario} (Tú)"
        
        boton_editar_comentario = ctk.CTkButton(frame_usuario, text="Editar", font=("Arial", 20),
                                                fg_color="#329ADF",
                                                hover_color="#31AF9C",
                                                command=lambda: ventana_editar_comentario(base, comentario, comentario_id, id_pelicula))
        boton_editar_comentario.grid(row=0, column=2, padx=10, sticky="w")
        
        boton_eliminar_comentario = ctk.CTkButton(frame_usuario, text="Eliminar", font=("Arial", 20),
                                                  fg_color="#329ADF",
                                                  hover_color="#31AF9C",
                                                  command=lambda: eliminar_comentario(base, comentario_id, id_pelicula))
        
        boton_eliminar_comentario.grid(row=0, column=3, padx=10, sticky="w")
    
    nom_usuario = ctk.CTkLabel(frame_usuario, text=nombre_usuario, font=("Arial", 20), wraplength=1000, justify="left")
    nom_usuario.grid(row=0, column=1, padx=10, sticky="w")

def crear_comentarios(base: ctk.CTk, frame_descripcion_pelicula: ctk.CTkFrame, id_pelicula: int) -> None:
    """
    Crea y añade todos los comentarios sobre una película en el frame de descripción de la película.

    Args:
        base (ctk.CTk): La ventana principal de la aplicación.
        frame_descripcion_pelicula (ctk.CTkFrame): El frame donde se añadirán los comentarios.
        id_pelicula (int): El ID de la película cuyos comentarios se desean ver.
    """
    comentarios = obtener_comentarios_pelicula(id_pelicula)
    frame_comentarios = ctk.CTkFrame(frame_descripcion_pelicula)
    frame_comentarios.pack(pady=10, expand=True, fill="both")
    
    agregar_separador(frame_comentarios)
    
    label_comentarios = ctk.CTkLabel(frame_comentarios, text="Comentarios", font=("Arial", 30, "bold"))
    label_comentarios.pack(pady=10)
    
    for comentario in comentarios:
        comentario_id = comentario[0]
        usuario_id = comentario[1]
        nombre_usuario = obtener_usuario_por_id(usuario_id)[0][0]
        comentario_texto = comentario[3]

        crear_comentario(base, frame_comentarios, nombre_usuario, comentario_texto, comentario_id, id_pelicula)
    base.frame_comentarios = frame_comentarios

def ventana_editar_comentario(base: ctk.CTk, comentario: str, comentario_id: int, id_pelicula: int) -> None:
    """
    Crea y muestra una ventana para editar un comentario.

    Args:
        base (ctk.CTk): La ventana principal de la aplicación.
        comentario (str): El texto del comentario a editar.
        comentario_id (int): El ID del comentario a editar.
        id_pelicula (int): El ID de la película a la que pertenece el comentario.
    """
    ventana_editar_comentario = ctk.CTkToplevel(base)
    ventana_editar_comentario.title("Editar comentario")
    ventana_editar_comentario.geometry("500x300")
    ventana_editar_comentario.resizable(False, False)
    ventana_editar_comentario.transient(base)

    comentario_label = ctk.CTkLabel(ventana_editar_comentario, text="Edita tu comentario:", font=("Arial", 20))
    comentario_label.pack(pady=10, padx=10)
    comentario_entry = ctk.CTkTextbox(ventana_editar_comentario, font=("Arial", 20), wrap="word", height=150)
    comentario_entry.pack(pady=10, padx=10, expand=True, fill="x")
    comentario_entry.insert(1.0, comentario)

    boton_editar = ctk.CTkButton(ventana_editar_comentario, 
                                 text="Editar", 
                                 hover_color="#31AF9C",
                                 fg_color="#329ADF", 
                                 font=("Arial", 20), 
                                 command=lambda: editar_comentario(base, ventana_editar_comentario, limpiar_comentario(comentario_entry.get(1.0, "end")), comentario_id, id_pelicula))
    boton_editar.pack(pady=10, padx=10, expand=True)

def editar_comentario(base: ctk.CTk, ventana_comentario: ctk.CTkToplevel, comentario: str, comentario_id: int, id_pelicula: int) -> None:
    """
    Edita un comentario existente.

    Args:
        base (ctk.CTk): La ventana principal de la aplicación.
        ventana_comentario (ctk.CTkToplevel): La ventana donde se edita el comentario.
        comentario (str): El nuevo texto del comentario.
        comentario_id (int): El ID del comentario a editar.
        id_pelicula (int): El ID de la película a la que pertenece el comentario.
    """
    try:
        if not messagebox.askyesno("Editar comentario", "¿Estás seguro de que deseas editar el comentario?"):
            return
        editar_comentario_pelicula(comentario_id, comentario)
        ventana_comentario.destroy()
        actualizar_comentarios(base, id_pelicula)
        mostrar_mensaje("Comentario editado", "Comentario editado con éxito")
    except Exception as e:
        mostrar_error("Error al guardar el comentario", f"Error al guardar el comentario: {e}")
        print(f"Error al guardar el comentario: {e}")

def eliminar_comentario(base: ctk.CTk, comentario_id: int, id_pelicula: int) -> None:
    """
    Elimina un comentario existente.

    Args:
        base (ctk.CTk): La ventana principal de la aplicación.
        comentario_id (int): El ID del comentario a eliminar.
        id_pelicula (int): El ID de la película a la que pertenece el comentario.
    """
    try:
        if not messagebox.askyesno("Eliminar comentario", "¿Estás seguro de que deseas eliminar el comentario?"):
            return
        eliminar_comentario_pelicula(comentario_id)
        actualizar_comentarios(base, id_pelicula)
        mostrar_mensaje("Comentario eliminado", "Comentario eliminado con éxito")
    except Exception as e:
        mostrar_error("Error al eliminar el comentario", f"Error al eliminar el comentario  {e}")
        print(f"Error al eliminar el comentario: {e}")