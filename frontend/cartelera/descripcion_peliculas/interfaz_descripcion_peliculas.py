import customtkinter as ctk

from .. import utils_cartelera as UC
from .utils_interfaz_descripcion_peliculas import obtener_pelicula_por_id, agregar_separador
from frontend import utils, menubar as MB
from . import botones_descripcion_peliculas as BFDP

def crear_descripcion_peliculas(base, id_pelicula: int, pelicula: str):
    """
    Crea la interfaz de descripción de películas.

    Args:
        base: El widget base donde se creará la interfaz.
        id_pelicula (int): El ID de la película.
        pelicula (str): El título de la película.
    """
    utils.limpiar_widgets_base(base)
    frame_foto_descripcion = ctk.CTkFrame(base, fg_color="transparent", border_color="black")
    MB.crear_menu_bar(base)
    
    frame_foto_descripcion.pack(expand=True, fill="both")
    
    frame_foto_descripcion.rowconfigure(0, weight=1)
    frame_foto_descripcion.columnconfigure(1, weight=1)

    crear_frame_foto_pelicula(frame_foto_descripcion, id_pelicula, pelicula)
    crear_frame_descripcion_pelicula(base,frame_foto_descripcion, id_pelicula, pelicula)

def crear_frame_foto_pelicula(frame_foto_descripcion, id_pelicula: int, pelicula: str):
    """
    Crea el frame de la foto de la película.

    Args:
        frame_foto_descripcion: El frame donde se colocará la foto de la película.
        id_pelicula (int): El ID de la película.
        pelicula (str): El título de la película.
    """
    directorio_imagenes = "frontend\\cartelera\\portadas_peliculas"
    imagen = UC.conseguir_imagen_portada_ctk(directorio_imagenes, id_pelicula, pelicula, 500, 800)
    
    foto_pelicula = ctk.CTkLabel(frame_foto_descripcion, image=imagen, text="")
    foto_pelicula.grid(row=0, column=0, sticky="nsew")

def crear_frame_descripcion_pelicula(base,frame_foto_descripcion, id_pelicula: int, titulo_pelicula: str):
    """
    Crea el frame de la descripción de la película.

    Args:
        base: El widget base donde se creará el frame de la descripción.
        frame_foto_descripcion: El frame donde se colocará el frame de la descripción.
        id_pelicula (int): El ID de la película.
        titulo_pelicula (str): El título de la película.
    """
    frame_descripcion_pelicula = ctk.CTkScrollableFrame(frame_foto_descripcion, border_width=2, border_color="black")
    frame_descripcion_pelicula.grid(row=0, column=1, sticky="nsew",padx=(10,0))
    
    titulo_pelicula = ctk.CTkLabel(frame_descripcion_pelicula, text=titulo_pelicula, font=("Arial", 40, "bold"), wraplength=1000)
    titulo_pelicula.pack(pady=10)
    
    agregar_separador(frame_descripcion_pelicula)
    
    datos = obtener_pelicula_por_id(id_pelicula)[0]
    
    sinopsis = datos[3]
    generos = datos[4]
    duracion = datos[5]
    fecha_estreno = datos[6]
    prom_votos = datos[7]
    
    sinopsis_label = ctk.CTkLabel(frame_descripcion_pelicula, text=sinopsis, font=("Arial", 25), wraplength=1000, justify="left")
    sinopsis_label.pack(pady=10)
    
    agregar_separador(frame_descripcion_pelicula)

    frame_genero = ctk.CTkFrame(frame_descripcion_pelicula)
    frame_genero.pack(anchor="w")
    genero_texto = ctk.CTkLabel(frame_genero, text="Géneros:", font=("Arial", 20, "bold"))
    genero_texto.grid(row=0, column=0, pady=10,padx=10, sticky="w")
    generos_label = ctk.CTkLabel(frame_genero, text=generos, font=("Arial", 20))
    generos_label.grid(row=0, column=1, pady=10, sticky="w")

    frame_duracion = ctk.CTkFrame(frame_descripcion_pelicula)
    frame_duracion.pack(anchor="w")
    duracion_texto = ctk.CTkLabel(frame_duracion, text="Duracion:", font=("Arial", 20, "bold"))
    duracion_texto.grid(row=0, column=0, pady=10,padx=10, sticky="w")
    duracion_label = ctk.CTkLabel(frame_duracion, text=duracion, font=("Arial", 20))
    duracion_label.grid(row=0, column=1, pady=10, sticky="w")

    fecha_estreno_frame = ctk.CTkFrame(frame_descripcion_pelicula)
    fecha_estreno_frame.pack(anchor="w")
    fecha_estreno_texto = ctk.CTkLabel(fecha_estreno_frame, text="Fecha de estreno:", font=("Arial", 20, "bold"))
    fecha_estreno_texto.grid(row=0, column=0, pady=10,padx=10, sticky="w")
    fecha_estreno_label = ctk.CTkLabel(fecha_estreno_frame, text=fecha_estreno, font=("Arial", 20))
    fecha_estreno_label.grid(row=0, column=1, pady=10, sticky="w")

    prom_votos_frame = ctk.CTkFrame(frame_descripcion_pelicula)
    prom_votos_frame.pack(anchor="w")
    prom_votos_texto = ctk.CTkLabel(prom_votos_frame, text="Promedio de votos:", font=("Arial", 20, "bold"))
    prom_votos_texto.grid(row=0, column=0, pady=10,padx=10, sticky="w")
    prom_votos_label = ctk.CTkLabel(prom_votos_frame, text=prom_votos, font=("Arial", 20))
    prom_votos_label.grid(row=0, column=1, pady=10, sticky="w")
        
    agregar_separador(frame_descripcion_pelicula)
    
    frame_botones = ctk.CTkFrame(frame_descripcion_pelicula)
    frame_botones.pack(pady=10)

    BFDP.boton_reservar_asientos(base,frame_botones)
    BFDP.boton_ver_trailer(frame_botones, id_pelicula)
    BFDP.boton_agregar_comentario(base,frame_botones, id_pelicula)
    BFDP.boton_salir(base,frame_botones)
    BFDP.crear_comentarios(base,frame_descripcion_pelicula, id_pelicula)

    base.frame_descripcion_pelicula = frame_descripcion_pelicula


