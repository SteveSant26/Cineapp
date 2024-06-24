import customtkinter as ctk

import utils
import menubar as MB


def crear_cartelera(base, peliculas:dict[dict], columnas:int):
    """
    Crea los botones de las películas y los ubica en el frame_peliculas.

    Args:
        base (ctk.CTk): La base de la GUI.
        peliculas (dict): Un diccionario con el nombre de las películas y sus respectivas imágenes.
        columnas (int): El número de columnas en las que se mostrarán los botones.
    """
    # Se calcula el número de filas necesarias para mostrar todas las películas
    # para que las filas se generen aun si no se completa la última fila
    filas = (len(peliculas) + columnas - 1) // columnas
    
    #Se configura el frame de las peliculas
    for i in range(filas):
        # En las filas se empieza desde el 1 porque la fila 0 es para el título
        base.frame_peliculas.grid_rowconfigure(i + 1, weight=1)
    for j in range(columnas):
        base.frame_peliculas.grid_columnconfigure(j, weight=1)

    # Se crea un diccionario con el nombre de las películas a mostrar y sus respectivas imágenes
    peliculas_a_mostrar = {}
    for pelicula, info in peliculas.items():
        try:
            peliculas_a_mostrar[pelicula] = utils.conseguir_imagen_ctk(info["path"],250,300)
        except Exception as e:
            print(f"Error al cargar la imagen de la película {pelicula}: {e}")

    
    # Se crean los botones de las películas y se ubican en el base.frame_peliculas
    for i, (pelicula, imagen) in enumerate(peliculas_a_mostrar.items()):
        fila = i // columnas + 1
        columna = i % columnas
        boton_pelicula = ctk.CTkButton(
            base.frame_peliculas,
            text=pelicula,
            image=imagen,
            hover_color="#31AF9C",
            compound="top",
            font=("Arial", 15, "bold"),
            fg_color="transparent",
            # Se le da la referencia al comando de seleccionar pelicula a cada boton
            # para que ejecute esta opción cuando se haga click en el
            command=lambda p=pelicula: seleccionar_pelicula(
                base, p),
        )
        utils.cambiar_color_texto(boton_pelicula)
            

        boton_pelicula.grid(row=fila, column=columna, padx=10, pady=0)
                


def mostrar_peliculas(base: ctk.CTk):
    
    """
    Crea el frame de las películas, lo configura y muestra las películas en la cartelera.

    Args:
        base (ctk.CTk): El frame principal donde se mostrará el frame de las películas.
    """
    from . import datos_peliculas as DP

    utils.limpiar_widgets_base(base)

    # Se crea el frame de las películas
    base.frame_peliculas = ctk.CTkScrollableFrame(
        base, fg_color="transparent", border_color="black")

    #Ubico el menu aqui para que se cree despues del frame de las peliculas
    MB.crear_menu_bar(base)
    
    base.frame_peliculas.pack(fill="both", expand=True)
    base.frame_peliculas.pack_propagate(False)

    base.frame_peliculas.grid_rowconfigure(0, weight=1)
    base.frame_peliculas.grid_columnconfigure(0, weight=1)


    # Se crea el título del frame de las películas
    titulo_cartelera = ctk.CTkLabel(
        base.frame_peliculas, text="Cartelera", font=("Arial", 40, "bold"))
    titulo_cartelera.grid(row=0, column=0, columnspan=5, pady=10)

    crear_cartelera(base, DP.PELICULAS, columnas=5)


def seleccionar_pelicula(base:ctk.CTk, pelicula: str):
    """
    Destruye el frame de las películas y muestra las opciones de la sala de la película seleccionada.

    Args:
        base (ctk.CTk): La base de la GUI.
        pelicula (str): El nombre de la película seleccionada.
    """
    import pantalla_cine as PC

    base.sala_actual = None
    base.mejor_asiento = None
    base.botones_funciones  = {}
    base.titulo_pelicula = pelicula
    
    PC.crear_vista_cine(base)

