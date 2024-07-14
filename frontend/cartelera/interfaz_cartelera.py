import customtkinter as ctk
import threading
from concurrent.futures import ThreadPoolExecutor
from frontend import utils,menubar as MB
from backend.database import ejecutar_query_obtener
from . import utils_cartelera as UC
from .descripcion_peliculas.interfaz_descripcion_peliculas import crear_descripcion_peliculas

def obtener_todas_funciones_pelicula(id_pelicula):
    query = "Select * from funciones where pelicula_id = %s"
    if ejecutar_query_obtener(query, "funciones", (id_pelicula,)):
        return True
    else:
        return False

def crear_cartelera(base, columnas: int):
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




def cargar_y_mostrar_imagen(base, directorio_imagenes,id_pelicula, titulo_pelicula, fila, columna):
    try:

        imagen = UC.conseguir_imagen_portada_ctk(directorio_imagenes, id_pelicula, titulo_pelicula, 250, 300)
        
        crear_boton_pelicula(base, imagen, titulo_pelicula, fila, columna, id_pelicula)
    except Exception as e:
        print(f"Error al obtener la imagen de {titulo_pelicula}: {e}")
        
def crear_boton_pelicula(base, imagen, titulo, fila, columna, id_pelicula):
    maxima_longitud = 30
    titulo_ajustado = titulo
    if len(titulo_ajustado) > maxima_longitud:
        titulo_ajustado = titulo[:maxima_longitud] + "..."
    
        
    boton_pelicula = ctk.CTkButton(
        base.frame_peliculas,
        image=imagen,
        hover_color="#31AF9C",
        compound="top",
        text=titulo_ajustado,
        text_color=("black", "White"),
        font=("Arial", 15, "bold"),
        fg_color="transparent",
        command=lambda titulo_pelicula=titulo: seleccionar_pelicula(base, titulo_pelicula,id_pelicula),
    )
    boton_pelicula.grid(row=fila, column=columna, padx=10, pady=0)

def iniciar_hilo_mostrar_peliculas(base: ctk.CTk):
    utils.limpiar_widgets_base(base)

    hilo = threading.Thread(target=mostrar_peliculas, daemon=True, args=(base,))
    hilo.start()


def mostrar_peliculas(base: ctk.CTk):
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

def seleccionar_pelicula(base: ctk.CTk, pelicula: str,id_pelicula:int):
    from frontend import pantalla_cine as PC

    base.sala_actual = None
    base.salas = None
    base.mejor_asiento = None
    base.botones_funciones = {}
    base.titulo_pelicula = pelicula
    base.pelicula_id = id_pelicula
    
    if base.tipo_usuario == "admin":
        return PC.crear_vista_cine(base)
    if base.tipo_usuario == "cliente":
        return crear_descripcion_peliculas(base, id_pelicula,pelicula)
    
