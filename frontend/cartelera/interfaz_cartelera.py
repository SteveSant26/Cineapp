import customtkinter as ctk
import threading
from concurrent.futures import ThreadPoolExecutor
from frontend import utils,menubar as MB
from . import utils_cartelera as UC
from backend.database import obtener_id_titulo_pelicula_bd

def crear_cartelera(base, columnas: int):
    peliculas = obtener_id_titulo_pelicula_bd()
    filas = (len(peliculas) + columnas - 1) // columnas

    for i in range(filas):
        base.frame_peliculas.grid_rowconfigure(i + 1, weight=1)
    for j in range(columnas):
        base.frame_peliculas.grid_columnconfigure(j, weight=1)

    directorio_imagenes = "frontend\\cartelera\\portadas_peliculas"
    
    
    with ThreadPoolExecutor(max_workers=8) as executor:
        for index, (id_pelicula, titulo_pelicula) in enumerate(peliculas):
            fila = index // columnas + 1
            columna = index % columnas
            executor.submit(cargar_y_mostrar_imagen, base, directorio_imagenes, id_pelicula, titulo_pelicula, fila, columna)




def cargar_y_mostrar_imagen(base, directorio_imagenes,id_pelicula, titulo_pelicula, fila, columna):
    try:
        imagen = UC.conseguir_imagen_portada_ctk(directorio_imagenes, id_pelicula, titulo_pelicula, 250, 300)
        
        crear_boton_pelicula(base, imagen, titulo_pelicula, fila, columna, id_pelicula)
    except Exception as e:
        print(f"Error al obtener la imagen de {titulo_pelicula}: {e}")
        
def crear_boton_pelicula(base, imagen, titulo, fila, columna, id_pelicula):
    boton_pelicula = ctk.CTkButton(
        base.frame_peliculas,
        image=imagen,
        hover_color="#31AF9C",
        compound="top",
        text=titulo,
        text_color=("black", "White"),
        font=("Arial", 15, "bold"),
        fg_color="transparent",
        command=lambda p=titulo: seleccionar_pelicula(base, p),
    )
    boton_pelicula.grid(row=fila, column=columna, padx=10, pady=0)

def iniciar_hilo_mostrar_peliculas(base: ctk.CTk):
    utils.limpiar_widgets_base(base)

    hilo = threading.Thread(target=mostrar_peliculas, daemon=True, args=(base,))
    hilo.start()


def mostrar_peliculas(base: ctk.CTk):
    utils.limpiar_widgets_base(base)
    
    base.frame_peliculas = ctk.CTkScrollableFrame(base, fg_color="transparent", border_color="black")
    MB.crear_menu_bar(base, busqueda=True)
    
    base.frame_peliculas.pack(fill="both", expand=True)
    base.frame_peliculas.pack_propagate(False)
    base.frame_peliculas.grid_rowconfigure(0, weight=1)
    base.frame_peliculas.grid_columnconfigure(0, weight=1)

    titulo_cartelera = ctk.CTkLabel(base.frame_peliculas, text="Cartelera", font=("Arial", 40, "bold"))
    titulo_cartelera.grid(row=0, column=0, columnspan=5, pady=10)

    crear_cartelera(base, columnas=5)

def seleccionar_pelicula(base: ctk.CTk, pelicula: str):
    from frontend import pantalla_cine as PC

    base.sala_actual = None
    base.mejor_asiento = None
    base.botones_funciones = {}
    base.titulo_pelicula = pelicula
    
    PC.crear_vista_cine(base)
