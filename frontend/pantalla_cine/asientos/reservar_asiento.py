import customtkinter as ctk
from tkinter import messagebox

from frontend.cartelera import datos_peliculas as DP
from frontend import utils

from . import crear_asientos_img as CAI
from . import utils_asientos as U

        
        
def reservar_asientos(base:ctk.CTk)->None:
    """
    Reserva los asientos seleccionados en la sala de cine.

    Args:
        vars (dict): Un diccionario con las variables del programa.

    Returns:
        None
    """
    # Se comprueba si hay un mejor asiento seleccionado
    if base.mejor_asiento:
        # Si hay un mejor asiento, se agrega al set de asientos seleccionados
        DP.PELICULAS[base.titulo_pelicula]["salas"][base.sala_actual][base.funcion_actual]["seleccionados"].add(base.mejor_asiento)
        fila, columna = base.mejor_asiento
        # Se obtiene el asiento y se cambia su imagen a asiento_hover
        U.unbind_asiento(base.frame_sala.grid_slaves(row=fila, column=columna)[0])
        
        # Se vuelve a dar el valor de none al mejor asiento
        base.mejor_asiento = None

    # Se recorren los asientos seleccionados
    for asiento in DP.PELICULAS[base.titulo_pelicula]["salas"][base.sala_actual][base.funcion_actual]["seleccionados"]:
        # Se obtiene la fila y columna del asiento para habilitarlo y cambiar su color a gris
        fila, columna = asiento
        U.unbind_asiento(base.frame_sala.grid_slaves(row=fila, column=columna)[0])
            
        base.frame_sala.grid_slaves(
            row=fila, column=columna)[0].configure(image=CAI.ASIENTOS_IMAGEN["asiento_reservado"], state="disabled")
        
        # Se agrega el asiento al set de asientos reservados
        DP.PELICULAS[base.titulo_pelicula]["salas"][base.sala_actual][base.funcion_actual]["reservados"].add(asiento)

    # Se obtiene el número de asientos seleccionados
    numero_asientos_seleccionados = len(
        DP.PELICULAS[base.titulo_pelicula]["salas"][base.sala_actual][base.funcion_actual]["seleccionados"])

    # Se muestra un mensaje de cuantos asientos han sido reservados
    messagebox.showinfo("Asientos reservados", f"Usted ha reservado {numero_asientos_seleccionados} asient{'os' if numero_asientos_seleccionados > 1 else 'o'}")
    # Se limpian los asientos seleccionados
    DP.PELICULAS[base.titulo_pelicula]["salas"][base.sala_actual][base.funcion_actual]["seleccionados"].clear()

    print(f"Asientos reservados: {DP.PELICULAS[base.titulo_pelicula]["salas"][base.sala_actual][base.funcion_actual]["reservados"]}")

def preguntar_reservar(base)->None:
    """
    Pregunta al usuario si desea reservar los asientos seleccionados.

    Args:
        base: la instancia de la ventana principal a la que se le dan ciertos atributos para mejor acceso de sus elementos 

    Returns:
        None
    """
    if not DP.PELICULAS[base.titulo_pelicula]["salas"][base.sala_actual][base.funcion_actual]["seleccionados"] and not base.mejor_asiento:
        utils.mostrar_error(
            "Sin selecciones", "No ha seleccionado ningún asiento para reservar")
        return

    # Confirmar si se desea reservar estos asientos
    if messagebox.askyesno("Confirmar Reserva", "¿Desea reservar los asientos seleccionados?"):
        reservar_asientos(base)
        # Actualizar set de de funcion actual con el set de los asientos reservados de la sala actual
        DP.PELICULAS[base.titulo_pelicula]["salas"][base.sala_actual][base.funcion_actual]["reservados"].update(
            DP.PELICULAS[base.titulo_pelicula]["salas"][base.sala_actual][base.funcion_actual]["seleccionados"])
        
        print(f"Asientos reservados: {DP.PELICULAS[base.titulo_pelicula]["salas"][base.sala_actual][base.funcion_actual]["reservados"]}")

def habilitar_reservados(base:ctk.CTk)->None:
    """
    Deselecciona los asientos reservados.

    Args:
        vars (dict): Un diccionario con las variables del programa.

    Returns:
        None
    """
    # Si no hay asientos reservados, se muestra un mensaje de error
    if not DP.PELICULAS[base.titulo_pelicula]["salas"][base.sala_actual][base.funcion_actual]["reservados"]:
        utils.mostrar_error("Sin asientos reservados", "No hay asientos reservados")
        return

    # Se recorren los asientos reservados
    for (fila,columna) in DP.PELICULAS[base.titulo_pelicula]["salas"][base.sala_actual][base.funcion_actual]["reservados"]:
        # Se agrega el asiento al set de asientos seleccionados para poderlos volver a seleccionar
        DP.PELICULAS[base.titulo_pelicula]["salas"][base.sala_actual][base.funcion_actual]["seleccionados"].add((fila, columna))

        # Se habilita el asiento y se cambia su color al original
        
        asiento_reservado = base.frame_sala.grid_slaves(row=fila , column=columna)[0]
        asiento_reservado.configure(image=CAI.ASIENTOS_IMAGEN["asiento_habilitado"], state="normal")
        # Se le asigna un evento al asiento

        asiento_reservado.bind("<Button-1>", lambda event, row=fila, col=columna: click_en_asiento(row, col, base)) #se aplica este comando unicamente en estos asientos

        U.bind_asiento(asiento_reservado,CAI.ASIENTOS_IMAGEN["asiento_libre"],CAI.ASIENTOS_IMAGEN["asiento_habilitado"])


def click_en_asiento(fila:int, columna:int, base:ctk.CTk)->None:
    """
    Función llamada cuando se hace clic en un asiento habilitado.

    Args:
        row (int): La fila del asiento.
        col (int): La columna del asiento.
        vars (dict): Un diccionario con las variables del programa.

    Returns:
        None
    """
    # Se recorren los asientos reservados para ver si el asiento clickeado está reservado    
    if (fila, columna) in DP.PELICULAS[base.titulo_pelicula]["salas"][base.sala_actual][base.funcion_actual]["reservados"]:
        # Se recorren los asientos reservados para ver si el asiento clickeado está seleccionado
        if (fila, columna) in DP.PELICULAS[base.titulo_pelicula]["salas"][base.sala_actual][base.funcion_actual]["seleccionados"]:
            # Se obtiene el asiento
            asiento = base.frame_sala.grid_slaves(row=fila, column=columna)[0]
            #Se remueve el comando de seleccionar asiento
            asiento.unbind("<Button-1>")
            U.unbind_asiento(asiento)

            # Se restaura el color original y se habilita el asiento
            asiento.configure(image=CAI.ASIENTOS_IMAGEN["asiento_libre"], state="normal")
            
            U.bind_asiento(asiento,CAI.ASIENTOS_IMAGEN["asiento_hover"],CAI.ASIENTOS_IMAGEN["asiento_libre"])
            
            print(f"Asiento en la fila {fila}, columna {columna} deseleccionado")
            # Se remueve de la lista de asientos reservados
            DP.PELICULAS[base.titulo_pelicula]["salas"][base.sala_actual][base.funcion_actual]["reservados"].remove((fila, columna))
            # Se remueve de la lista de asientos seleccionados, ya que se ha deseleccionado
            DP.PELICULAS[base.titulo_pelicula]["salas"][base.sala_actual][base.funcion_actual]["seleccionados"].remove((fila, columna))

