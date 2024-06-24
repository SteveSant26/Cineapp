import customtkinter as ctk

from cartelera import datos_peliculas as DP
from . import crear_asientos_img as CAI

def seleccionar_asiento(fila: int, columna: int, base) -> None:
    """
    Selecciona o deselecciona un asiento en la sala de cine.

    Args:
        fila (int): La fila del asiento.
        columna (int): La columna del asiento.
        vars (dict): Un diccionario con las variables del programa.

    Returns:
        None
    """
    # Si el asiento está reservado, no se puede seleccionar
    if (fila, columna) in DP.PELICULAS[base.titulo_pelicula]["salas"][base.sala_actual][base.funcion_actual]["reservados"]:
        return
    
    # Obtener el botón del asiento
    asiento = base.frame_sala.grid_slaves(row=fila, column=columna)[0]
    unbind_asiento(asiento)
    
    
    # Si el asiento ya está seleccionado, se de-selecciona y se quita del set de asientos seleccionados
    if (fila, columna) in DP.PELICULAS[base.titulo_pelicula]["salas"][base.sala_actual][base.funcion_actual]["seleccionados"]:
        asiento.configure(image=CAI.ASIENTOS_IMAGEN["asiento_libre"])
        bind_asiento(asiento,CAI.ASIENTOS_IMAGEN["asiento_hover"],CAI.ASIENTOS_IMAGEN["asiento_libre"])

        DP.PELICULAS[base.titulo_pelicula]["salas"][base.sala_actual][base.funcion_actual]["seleccionados"].remove((fila, columna))
    
    elif base.mejor_asiento == (fila, columna):
        asiento.configure(image=CAI.ASIENTOS_IMAGEN["asiento_libre"])
        base.mejor_asiento = None
        
        bind_asiento(asiento,CAI.ASIENTOS_IMAGEN["asiento_hover"],CAI.ASIENTOS_IMAGEN["asiento_libre"])
    
    # Si el asiento no está seleccionado, se selecciona y se agrega al set de asientos seleccionados
    else:
        asiento.configure(image=CAI.ASIENTOS_IMAGEN["asiento_hover"])
        DP.PELICULAS[base.titulo_pelicula]["salas"][base.sala_actual][base.funcion_actual]["seleccionados"].add((fila, columna))
        bind_asiento(asiento,CAI.ASIENTOS_IMAGEN["asiento_libre"],CAI.ASIENTOS_IMAGEN["asiento_hover"])

    print(f"Asientos seleccionados: {DP.PELICULAS[base.titulo_pelicula]["salas"][base.sala_actual][base.funcion_actual]["seleccionados"]}")
    
def bind_asiento(asiento:ctk.CTkButton, asiento_entrada,asiento_salida)->None:
    """
    Asigna un evento a un asiento.

    Args:
        asiento (ctk.CTkButton): El asiento al que se le asignará el evento.
        vars (dict): Un diccionario con las variables del programa.
        fila (int): La fila del asiento.
        columna (int): La columna del asiento.

    Returns:
        None
    """
    asiento.bind("<Enter>", lambda event, asiento=asiento: asiento.configure(image=asiento_entrada))
    asiento.bind("<Leave>", lambda event, asiento=asiento: asiento.configure(image=asiento_salida))
    
def unbind_asiento(asiento:ctk.CTkButton)->None:
    """
    Remueve el evento de un asiento.

    Args:
        asiento (ctk.CTkButton): El asiento al que se le removerá el evento.

    Returns:
        None
    """
    asiento.unbind("<Enter>")
    asiento.unbind("<Leave>")