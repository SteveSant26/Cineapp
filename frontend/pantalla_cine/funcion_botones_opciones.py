import customtkinter as ctk
from frontend import utils
from . import asientos as A
from . import frame_vista_cine as FVC 
from .utils_pc import obtener_funcion_id_por_sala_pelicula_id, obtener_funciones, obtener_sala_id_por_nombre_bd

def actualizar_sala_por_combobox(event: object, base: dict) -> None:
    """
    Actualiza la sala de cine seleccionada en el combobox.

    Args:
        event (object): El evento que disparó la función.
        base (dict): Un diccionario con las variables del programa.

    Returns:
        None
    """
    nueva_sala = base.combobox_sala.get()
    if nueva_sala != base.sala_actual:
        base.mejor_asiento = None
        base.sala_actual = nueva_sala
        base.sala_actual_id = obtener_sala_id_por_nombre_bd(base.sala_actual)[0][0]
        base.funciones = obtener_funciones(base.pelicula_id, nueva_sala)
        base.funcion_actual = base.funciones[0]
        base.funcion_actual_id = obtener_funcion_id_por_sala_pelicula_id(base.sala_actual_id, base.pelicula_id, base.funcion_actual)
        
        actualizar_botones_funciones(base)
        
        base.frame_sala.destroy()
        base.frame_opciones.destroy()
        
        FVC.actualizar_frames(base)

def actualizar_botones_funciones(base: dict) -> None:
    """
    Actualiza los botones de las funciones de la sala de cine.

    Args:
        base (dict): Un diccionario con las variables del programa.

    Returns:
        None
    """
    utils.limpiar_widgets_base(base.frame_funciones)
    base.funciones = obtener_funciones(base.pelicula_id, base.sala_actual)
    base.funcion_actual = base.funciones[0]
    base.funcion_actual_id = obtener_funcion_id_por_sala_pelicula_id(base.sala_actual_id, base.pelicula_id, base.funcion_actual)

    for idx, funcion in enumerate(base.funciones):
        boton = ctk.CTkButton(base.frame_funciones,
                              font=("Arial", 16),
                              text=funcion,
                              hover_color="#31AF9C",
                              fg_color="#79B6DF",
                              command=lambda f=funcion: actualizar_sala_por_funcion(f, base))
        boton.grid(row=0, column=idx, padx=5, pady=5)
        if idx >= 3:
            boton.grid(row=1, column=idx - 3, padx=5, pady=5)

        base.botones_funciones[funcion] = boton
        if funcion == base.funcion_actual:
            boton.configure(state="disabled", fg_color="#248CD3")
        else:
            boton.configure(state="normal", fg_color="#79B6DF")

def actualizar_sala_por_funcion(funcion: str, base: dict) -> None:
    """
    Actualiza la sala de cine seleccionada por la función seleccionada.

    Args:
        funcion (str): La función seleccionada.
        base (dict): Un diccionario con las variables del programa.

    Returns:
        None
    """
    if funcion != base.funcion_actual:
        base.mejor_asiento = None
        base.botones_funciones[base.funcion_actual].configure(state="normal", fg_color="#79B6DF")
        base.botones_funciones[funcion].configure(state="disabled", fg_color="#248CD3")
        base.funcion_actual = funcion
        base.funcion_actual_id = obtener_funcion_id_por_sala_pelicula_id(base.sala_actual_id, base.pelicula_id, base.funcion_actual)
        A.crear_asientos(base)

def regresar(base: ctk.CTkFrame) -> None:
    """
    Regresa al frame principal de la aplicación.

    Args:
        base (ctk.CTkFrame): El frame principal de la aplicación.

    Returns:
        None
    """
    from frontend import cartelera
    utils.limpiar_widgets_base(base)
    cartelera.iniciar_hilo_mostrar_peliculas(base)
