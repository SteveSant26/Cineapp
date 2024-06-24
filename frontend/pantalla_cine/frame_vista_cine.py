import customtkinter as ctk

from frontend import utils

import frontend.pantalla_cine.asientos as AS

from . import funcion_botones_opciones as FBO
from . import botones_opciones as BO






def crear_vista_cine(base:ctk.CTk)->None:
    """Inicializa el frame donde se guardan las opciones de la sala de la pelicula seleccionada los asientos.

    Args:
        base (ctk.CTkFrame): El frame principal donde se mostrarán las opciones de la sala.
        pelicula (str): El título de la película seleccionada.
    """
    utils.limpiar_widgets_base(base)
    # Se inicializa el diccionario de variables
    crear_frame_vista_cine(base)
    # Se actualizan todos los frames
    actualizar_frames(base)
    
def crear_frame_vista_cine(base)->None:
    """Se crea el frame que almacena las opciones y la sala.

    Args:
         (dict): El diccionario de variables.
    """
    # Se crea el frame de las opciones y la sala
    base.frame_opciones_sala = ctk.CTkFrame(base,
                                               fg_color="transparent")
    base.frame_opciones_sala.pack(fill="both", expand=True)

    # Se configura el frame para que no se expanda con el resto de la ventana
    base.frame_opciones_sala.pack_propagate(False)

    # Se configuran las filas y columnas para que los widgets dentro se expandan uniformemente
    base.frame_opciones_sala.rowconfigure(0, weight=1)
    base.frame_opciones_sala.columnconfigure(0, weight=1)
    base.frame_opciones_sala.columnconfigure(1, weight=3)

def crear_frame_opciones(base)->None:
    """ Se crea el frame que almacena las opciones para seleccionar la sala y la función de la pelicula seleccionada."""

    # Se crea el frame de las opciones
    base.frame_opciones = ctk.CTkFrame(base.frame_opciones_sala,
                                          border_color="black",
                                          border_width=2,
                                          width=550)

    base.frame_opciones.grid(
        row=0, column=0, sticky="nsew", padx=5, pady=10)

    # Se configura el frame para que no se expanda con el resto de la ventana

    base.frame_opciones.grid_propagate(False)

    # Se crea el titulo del menu de las opciones
    titulo_menu = ctk.CTkLabel(base.frame_opciones, text=f"MENU - {base.titulo_pelicula}",
                               font=("Arial", 30, "bold"))

    titulo_menu.grid(row=0, column=0, pady=20, padx=20,
                     columnspan=2, sticky="nsew")

    #Se colocan los botones de las opciones
    BO.colocar_botones(base)
    
def actualizar_frames(base)->None:

    
    # Se crea la sala de la pelicula seleccionada
    crear_frame_sala(base)
    # Se crea el frame de las opciones
    crear_frame_opciones(base)
    # Se generan los asientos de la sala seleccionada
    AS.crear_asientos(base)


def crear_frame_sala(base)->None:
    """ Se crea el frame que almacena los asientos de la sala de la pelicula seleccionada."""
    #Se crea el frame de la sala
    base.frame_sala = ctk.CTkFrame(
        base.frame_opciones_sala,
        border_color="black",
        border_width=2,
        width=1200,
        height=700)
    base.frame_sala.grid(row=0, column=1, sticky="nsew", padx=5, pady=10)
    
    # Se configura el frame para que no se expanda con el resto de la ventana
    base.frame_sala.grid_propagate(False)


def crear_frame_funciones(base)->None:
    """ Se crea el frame que almacena las funciones de la sala seleccionada."""
    # Se crea el titulo de las funciones
    titulo_funciones = ctk.CTkLabel(
        base.frame_opciones, text="Seleccione su funcion", font=("Arial", 30, "bold"))
    titulo_funciones.grid(row=3, column=0, columnspan=2, pady=10, padx=20)

    # Se crea el frame que almacena los botones de las funciones
    base.frame_funciones = ctk.CTkFrame(base.frame_opciones)
    base.frame_funciones.grid(
        row=4, column=0, pady=10, padx=10, columnspan=2, sticky="nsew")
    
    
    #Se llama a la funcion que ubica los botones de las funciones
    FBO.actualizar_botones_funciones(base)

