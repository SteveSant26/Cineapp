import customtkinter as ctk
import threading
from concurrent.futures import ThreadPoolExecutor

from backend.database import ejecutar_query_obtener
from frontend import utils,menubar as MB

from . import utils_cartelera as UC
from .descripcion_peliculas import crear_descripcion_peliculas

def cargar_y_mostrar_imagen(base:ctk.CTk, directorio_imagenes:str, pelicula_id:int, pelicula_titulo:str, fila:int, columna:int):
    """
    Carga y muestra la imagen de la película.

    Args:
        base (ctk.CTk): La ventana base.
        directorio_imagenes (str): La ruta del directorio de las imágenes de las películas.
        id_pelicula (int): El ID de la película.
        titulo_pelicula (str): El título de la película.
        fila (int): El índice de fila en la cuadrícula de películas.
        columna (int): El índice de columna en la cuadrícula de películas.
    """
    try:
        imagen = UC.conseguir_imagen_portada_ctk(directorio_imagenes, pelicula_id, pelicula_titulo, 250, 300)
        crear_boton_pelicula(base, imagen, pelicula_titulo, fila, columna, pelicula_id)
    except Exception as e:
        print(f"Error al obtener la imagen de {pelicula_titulo}: {e}")
        
def crear_boton_pelicula(base:ctk.CTk, imagen:ctk.CTkImage, pelicula_titulo:str, fila:int, columna:int, pelicula_id:int):
    """
    Crea un botón para la película.

    Args:
        base (ctk.CTk): La ventana base.
        imagen: La imagen de la película.
        titulo (str): El título de la película.
        fila (int): El índice de fila en la cuadrícula de películas.
        columna (int): El índice de columna en la cuadrícula de películas.
        id_pelicula (int): El ID de la película.
    """
    maxima_longitud = 30
    titulo_ajustado = pelicula_titulo
    if len(titulo_ajustado) > maxima_longitud:
        titulo_ajustado = pelicula_titulo[:maxima_longitud] + "..."
    
        
    boton_pelicula = ctk.CTkButton(
        base.frame_peliculas,
        image=imagen,
        hover_color="#31AF9C",
        compound="top",
        text=titulo_ajustado,
        text_color=("black", "White"),
        font=("Arial", 15, "bold"),
        fg_color="transparent",
        command=lambda titulo_pelicula=pelicula_titulo: seleccionar_pelicula(base, titulo_pelicula, pelicula_id),
    )
    boton_pelicula.grid(row=fila, column=columna, padx=10, pady=0)
    
def obtener_todas_funciones_pelicula(pelicula_id:int) -> bool:
    """
    Obtiene todas las funciones de una película dado su ID.

    Parameters:
    id_pelicula (int): El ID de la película.

    Returns:
    bool: True si se encontraron funciones para la película, False en caso contrario.
    """
    query = "Select * from funciones where pelicula_id = %s"
    if ejecutar_query_obtener(query, "funciones", (pelicula_id,)):
        return True
    else:
        return False

def crear_cartelera(base:ctk.CTk, columnas: int):
    """
    Crea la cartelera de películas en la interfaz gráfica.

    Args:
        base: La base de la interfaz gráfica.
        columnas (int): El número de columnas en las que se mostrarán las películas.

    Returns:
        None
    """
    peliculas = UC.obtener_id_titulo_pelicula_bd()
    filas = (len(peliculas) + columnas - 1) // columnas

    for i in range(filas):
        base.frame_peliculas.grid_rowconfigure(i + 1, weight=1)
    for j in range(columnas):
        base.frame_peliculas.grid_columnconfigure(j, weight=1)

    directorio_imagenes = "frontend\\cartelera\\portadas_peliculas"
    
    with ThreadPoolExecutor(max_workers=8) as executor:
        index = 0
        for (id_pelicula, titulo_pelicula) in peliculas:
            fila = index // columnas + 1
            columna = index % columnas
            if base.tipo_usuario == "cliente":
                if not obtener_todas_funciones_pelicula(id_pelicula):
                    continue
            executor.submit(cargar_y_mostrar_imagen, base, directorio_imagenes, id_pelicula, titulo_pelicula, fila, columna)
            index += 1




def cargar_y_mostrar_imagen(base:ctk.CTk, directorio_imagenes:str, pelicula_id:int, pelicula_titulo:str, fila:int, columna:int):
    """
    Carga y muestra una imagen de portada de una película en la interfaz gráfica.

    Args:
        base (objeto): Objeto base de la interfaz gráfica.
        directorio_imagenes (str): Directorio donde se encuentran las imágenes de las películas.
        id_pelicula (int): ID de la película.
        titulo_pelicula (str): Título de la película.
        fila (int): Fila en la que se mostrará la imagen en la interfaz gráfica.
        columna (int): Columna en la que se mostrará la imagen en la interfaz gráfica.
    """
    try:
        imagen = UC.conseguir_imagen_portada_ctk(directorio_imagenes, pelicula_id, pelicula_titulo, 250, 300)
        crear_boton_pelicula(base, imagen, pelicula_titulo, fila, columna, pelicula_id)
    except Exception as e:
        print(f"Error al obtener la imagen de {pelicula_titulo}: {e}")
        
def crear_boton_pelicula(base:ctk.CTk, imagen:ctk.CTkImage, pelicula_titulo:str, fila:int, columna:int, pelicula_id:int):
    """
    Crea un botón de película en la interfaz de cartelera.

    Args:
        base (objeto): Objeto base de la interfaz.
        imagen (objeto): Imagen de la película.
        titulo (str): Título de la película.
        fila (int): Fila en la que se ubicará el botón.
        columna (int): Columna en la que se ubicará el botón.
        id_pelicula (int): ID de la película.

    Returns:
        None
    """
    maxima_longitud = 30
    titulo_ajustado = pelicula_titulo
    if len(titulo_ajustado) > maxima_longitud:
        titulo_ajustado = pelicula_titulo[:maxima_longitud] + "..."

    boton_pelicula = ctk.CTkButton(
        base.frame_peliculas,
        image=imagen,
        hover_color="#31AF9C",
        compound="top",
        text=titulo_ajustado,
        text_color=("black", "White"),
        font=("Arial", 15, "bold"),
        fg_color="transparent",
        command=lambda titulo_pelicula=pelicula_titulo: seleccionar_pelicula(base, titulo_pelicula, pelicula_id),
    )
    boton_pelicula.grid(row=fila, column=columna, padx=10, pady=0)

def iniciar_hilo_mostrar_peliculas(base: ctk.CTk):
    """
    Inicia un hilo para mostrar las películas en la interfaz de la cartelera.

    Args:
        base (ctk.CTk): La base de la interfaz de la cartelera.

    Returns:
        None
    """
    utils.limpiar_widgets_base(base)

    hilo = threading.Thread(target=mostrar_peliculas, daemon=True, args=(base,))
    hilo.start()

def mostrar_peliculas(base: ctk.CTk):
    """
    Muestra los listados de películas en la interfaz de usuario.

    Args:
        base (ctk.CTk): El widget contenedor base.

    Returns:
        None
    """
    utils.limpiar_widgets_base(base)
    
    base.frame_peliculas = ctk.CTkScrollableFrame(base, fg_color="transparent", border_color="black")
    MB.crear_menu_bar(base) #busqueda=True para mostrar searchbar
    
    base.frame_peliculas.pack(fill="both", expand=True)
    base.frame_peliculas.pack_propagate(False)
    base.frame_peliculas.grid_rowconfigure(0, weight=1)
    base.frame_peliculas.grid_columnconfigure(0, weight=1)

    titulo_cartelera = ctk.CTkLabel(base.frame_peliculas, text="Cartelera", font=("Arial", 40, "bold"))
    titulo_cartelera.grid(row=0, column=0, columnspan=5, pady=10)

    crear_cartelera(base, columnas=5)

def seleccionar_pelicula(base: ctk.CTk, pelicula_titulo: str, pelicula_id: int):
    """
    Selecciona una película y realiza acciones basadas en el tipo de usuario.

    Args:
        base (ctk.CTk): El objeto base que representa la interfaz del cine.
        pelicula (str): El nombre de la película seleccionada.
        id_pelicula (int): El ID de la película seleccionada.

    Returns:
        El resultado de las acciones basadas en el tipo de usuario.
    """

    from frontend import pantalla_cine as PC

    base.sala_actual = None
    base.salas = None
    base.mejor_asiento = None
    base.botones_funciones = {}
    base.titulo_pelicula = pelicula_titulo
    base.pelicula_id = pelicula_id
    
    if base.tipo_usuario == "admin":
        return PC.crear_vista_cine(base)
    if base.tipo_usuario == "cliente":
        return crear_descripcion_peliculas(base, pelicula_id, pelicula_titulo)
    
