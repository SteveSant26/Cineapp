import customtkinter as ctk
import tkinter as tk

from frontend.cartelera import datos_peliculas as DP
from frontend.utils import Colores_Temas as CT

from .import asientos as A


from . import funcion_botones_opciones as FBO


def crear_combobox(base)->None:
    """ Se crea el combobox para seleccionar la sala de la pelicula seleccionada. """
    # Se crea el titulo del combobox
    titulo_combobox = ctk.CTkLabel(
        base.frame_opciones, text="Seleccione la sala", font=("Arial", 20))
    titulo_combobox.grid(row=2, column=0, pady=10, padx=20)
    #Se pasan las salas de la pelicula seleccionada a la lista salas
    
    base.salas = list(
        DP.PELICULAS[base.titulo_pelicula]["salas"].keys())
    #Se inicializa la sala actual con la primera sala de la lista
    if base.sala_actual is None:
        base.sala_actual = str(base.salas[0])
        
    #Se obtiene la lista de las funciones de la sala actual
    base.funciones = list(
            DP.PELICULAS[base.titulo_pelicula]["salas"][base.sala_actual].keys())

    #Se inicializa la función actual con la primera función de la lista
    base.funcion_actual = str(base.funciones[0])


    # Se crea el combobox con las salas de la pelicula seleccionada
    base.combobox_sala = ctk.CTkComboBox(base.frame_opciones,
                                             font=("Arial", 15, "bold"),
                                             values=base.salas, 
                                             command=lambda event: FBO.actualizar_sala_por_combobox(event, base)) #Se le da un comando que ejecuta cada que se elije algo con el combobox
    base.combobox_sala.grid(row=2, column=1, pady=10, padx=20, sticky="ew")

    base.combobox_sala.set(base.sala_actual) #Se inicializa el combobox con la sala actual

def dibujar_canvas(canvas, color):
    canvas.create_rectangle(1, 1, 39, 39, fill=color, outline="black",width=1)
    
def referencia_colores(base):
    COLORES = {}
    
    if ctk.get_appearance_mode().lower() == "dark":
        COLORES = CT.COLORES_ASIENTO_TEMA_OSCURO
    else:
        COLORES = CT.COLORES_ASIENTO_TEMA_CLARO
    
    frame_colores = ctk.CTkFrame(base.frame_opciones)
    frame_colores.grid(row=1, column=0, columnspan=2, pady=10, padx=10, sticky="nsew")
    
    canvas = {}
    fila_index = 0
    columna_index = 0
    for nombre, color in COLORES.items():
        canvas[nombre] = tk.Canvas(frame_colores, width=30,height=30,background="black", borderwidth=1, highlightthickness=0)
        
        dibujar_canvas(canvas[nombre], color)
        label = ctk.CTkLabel(frame_colores, text=f"{nombre}:", font=("Arial", 15,"bold"))
        label.grid(row=fila_index, column=columna_index * 2, padx=10, pady=5, sticky="w")
        canvas[nombre].grid(row=fila_index, column=columna_index * 2 + 1, padx=10, pady=5, sticky="nsew")
        columna_index += 1
        if columna_index >= 2:
            columna_index = 0
            fila_index += 1


def colocar_boton_mejor_asiento(base)->None:
    """ Se crea el boton de mejor asiento y se coloca en el frame de las opciones."""
    # Se crea el titulo de las opciones
    titulo_opciones = ctk.CTkLabel(base.frame_opciones, text="Opciones",
                                   font=("Arial", 30, "bold"))
    titulo_opciones.grid(row=5, column=0, columnspan=2, pady=10, padx=20)
    # Se crea el boton de mejor asiento
    boton_mejor_asiento = ctk.CTkButton(
        base.frame_opciones, text="Mejor Asiento", fg_color="#329ADF",
hover_color="#31AF9C",command=lambda: A.select_mejor_asiento(base), height=45, font=("Arial", 16, "bold"))
    boton_mejor_asiento.grid(
        row=6, column=0, columnspan=2, pady=10, padx=10, sticky="nsew")


def colocar_boton_reservar(base)->None:
    """ Se crea el boton de reservar asientos y se coloca en el frame de las opciones."""
    # Se crea el boton de reservar asientos
    boton_reservar = ctk.CTkButton(
        base.frame_opciones, text="Reservar Asientos", fg_color="#329ADF",hover_color="#31AF9C",command=lambda: A.preguntar_reservar(base), height=45, font=("Arial", 16, "bold"))
    boton_reservar.grid(
        row=7, column=0, columnspan=2, pady=10, padx=10, sticky="nsew")


def colocar_boton_habilitar_reservar(base)->None:
    """ Se crea el boton de habilitar reservados y se coloca en el frame de las opciones."""
    # Se crea el boton de habilitar reservados
    boton_eliminar_reserva = ctk.CTkButton(
        base.frame_opciones, text="Habilitar reservados", fg_color="#329ADF",hover_color="#31AF9C",command=lambda: A.habilitar_reservados(base), height=45, font=("Arial", 16, "bold"))
    boton_eliminar_reserva.grid(
        row=8, column=0, columnspan=2, pady=10, padx=10, sticky="nsew")

def colocar_boton_regresar(base)->None:
    """
    Crea un botón de regresar en la interfaz gráfica.

    Args:
         (dict): Un diccionario que contiene las variables necesarias para la creación del botón.

    Returns:
        None
    """
    boton_regresar = ctk.CTkButton(
        base.frame_opciones,
        text="Volver a la cartelera",
        fg_color="#329ADF",
        hover_color="#31AF9C",
        font=("Arial", 16, "bold"),
        height=45,
        command=lambda: FBO.regresar(base)
    )
    boton_regresar.grid(row=9, column=0, columnspan=2,
                        pady=15, padx=10, sticky="ew")

def colocar_botones(base)->None:
    """ Se recolectan los botones de las opciones y se encapsulan en una funcion"""
    from .frame_vista_cine import crear_frame_funciones
    referencia_colores(base)
    crear_combobox(base)
    crear_frame_funciones(base)
    colocar_boton_mejor_asiento(base)
    colocar_boton_reservar(base)
    colocar_boton_habilitar_reservar(base)
    colocar_boton_regresar(base)