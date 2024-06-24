import customtkinter as ctk

from frontend.cartelera import datos_peliculas as DP
import frontend.utils as utils

import frontend.pantalla_cine.asientos as AS

from . import frame_vista_cine as FVC 


def actualizar_sala_por_combobox(event, base)->None:
    """
    Actualiza la sala de cine seleccionada en el combobox.

    Args:
        event: El evento que disparó la función.
        base (dict): Un diccionario con las variables del programa.

    Returns:
        None
    """


    nueva_sala = base.combobox_sala.get()
    if nueva_sala != base.sala_actual:
        
        # Se actualiza la sala actual, se cambia el mejor asiento a none otra vez
        base.mejor_asiento = None

        base.sala_actual = nueva_sala
        #Se obtiene la primera funcion de la sala actual
        base.funciones = list(
            DP.PELICULAS[base.titulo_pelicula]["salas"][base.sala_actual].keys())
        
        base.funcion_actual = base.funciones[0]
        
        # Se actualizan los botones de las funciones
        actualizar_botones_funciones(base)
        base.frame_sala.destroy()
        
        base.frame_opciones.destroy()
        # Actualiza los frames de la sala y opciones
        FVC.actualizar_frames(base)


def actualizar_botones_funciones(base)->None:
    """ Actualiza los botones de las funciones de la sala de cine."""
    # Se eliminan los botones de las funciones actuales
    utils.limpiar_widgets_base(base.frame_funciones)

    #Se obtienen las funciones de la sala actual
    base.funciones = list(
        DP.PELICULAS[base.titulo_pelicula]['salas'][base.sala_actual].keys())
    #Se obtiene la primera funcion de la sala actual
    base.funcion_actual = base.funciones[0]

    # Se crean los botones de las funciones
    for idx, funcion in enumerate(base.funciones):
        boton = ctk.CTkButton(base.frame_funciones,
                              font=("Arial", 16),
                              text=funcion,
                              hover_color="#31AF9C",
                              fg_color="#79B6DF",
                              command=lambda f=funcion: actualizar_sala_por_funcion(f, base))
        boton.grid(row=0, column=idx, padx=5, pady=5)
        #En caso de que haya mas de 3 funciones en una fila, se muestran en la siguiente fila
        if idx >= 3:
            boton.grid(row=1, column=idx-3, padx=5, pady=5)

        # Se agrega el boton al diccionario de botones de funciones
        base.botones_funciones[funcion] = boton
        if funcion == base.funcion_actual:
        # Se configura el boton de la funcion actual como desabilitado ya que es el seleccionado
            boton.configure(state="disabled", fg_color="#248CD3")
        else:
        # Se configura el boton de la funcion actual como normal
            boton.configure(
                state="normal",fg_color="#79B6DF")


def actualizar_sala_por_funcion(funcion:str, base)->None:
    """ Actualiza la sala de cine seleccionada por la función seleccionada."""

    # Se verifica que la funcion seleccionada sea diferente a la funcion actual
    if funcion != base.funcion_actual:
        
        # Se actualiza la sala actual, se cambia el mejor asiento a none otra vez
        base.mejor_asiento = None
        #Se habilita el boton de la funcion actual ya que se selecciono otra funcion
        base.botones_funciones[base.funcion_actual].configure(state="normal",fg_color="#79B6DF",
)
        #se deshabilita el boton de la funcion seleccionada ya que es la funcion actual
        base.botones_funciones[funcion].configure(state="disabled", fg_color="#248CD3")
        #Se actualiza la funcion actual
        base.funcion_actual = funcion
        #Se generan los asientos de la sala actual
        AS.generar_asientos(base)


def regresar(base:ctk.CTkFrame)->None:
    import frontend.cartelera as cartelera
    """ Regresa al frame principal de la aplicación."""
    # Se eliminan los widgets del frame principal
    utils.limpiar_widgets_base(base)
    #Se importa la funcion de Cartelera.py para mostrar las peliculas
    cartelera.mostrar_peliculas(base)



