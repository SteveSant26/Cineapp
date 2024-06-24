import customtkinter as ctk
from .. import salas

import cartelera.datos_peliculas as DP

from . import crear_asientos_img as CAI
from . import utils as U


def generar_asientos(base) -> None:
    """Crea los asientos de la sala seleccionada y los muestra en el frame de la sala."""
    # Se obtienen las filas y columnas de la sala seleccionada
    base.filas_sala = salas.SALAS[base.sala_actual]["tamano"][0]
    base.columnas_sala = salas.SALAS[base.sala_actual]["tamano"][1]

    # Configurar las filas y columnas para que se expandan uniformemente
    for i in range(base.filas_sala):
        base.frame_sala.grid_rowconfigure(i + 2, weight=1)
    for j in range(base.columnas_sala):
        base.frame_sala.grid_columnconfigure(j + 1, weight=1)

    # Verificar si la función actual está en la lista de funciones de la película
    if base.funcion_actual not in base.funciones:
        base.funcion_actual = base.funciones[0]

    # Crear el título de la sala
    titulo_sala = ctk.CTkLabel(base.frame_sala, text=f"| Pantalla {base.sala_actual.lower()}  |",
                               font=("Arial", 40, "bold"))
    titulo_sala.grid(row=0, column=0, pady=20, padx=20, columnspan=base.columnas_sala + 1, sticky="nsew")


    # Este abecedario se usará para nombrar las filas de los asientos
    abecedario = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # Crear nuevos botones de asientos y actualizar el diccionario de asientos
    asientos = {}

    for i in range(base.filas_sala):
        base.titulo_pelicula
        letra = ctk.CTkLabel(base.frame_sala, text=abecedario[i], font=("Arial", 20, "bold"))
        letra.grid(row=i + 2, column=0, padx= 10, pady=5,sticky="nsew")
        
        for j in range(base.columnas_sala):
            
            numero = ctk.CTkLabel(base.frame_sala, text=str(j + 1), font=("Arial", 20, "bold"))
            numero.grid(row=1, column=j + 1, sticky="nsew",padx=10, pady=5)
            
            asiento = ctk.CTkButton(base.frame_sala,
                                    text=" ",
                                    corner_radius=50,
                                    hover=False,
                                    border_color="black",
                                    border_width=2,
                                    image=CAI.ASIENTOS_IMAGEN["asiento_libre"],
                                    fg_color="transparent",
                                    command=lambda fila=i + 2, columna=j + 1: U.seleccionar_asiento(fila, columna, base))
            asiento.grid(row=i + 2, column=j + 1, padx=5, pady=5, sticky="nsew")
            
            U.bind_asiento(asiento,CAI.ASIENTOS_IMAGEN["asiento_hover"],CAI.ASIENTOS_IMAGEN["asiento_libre"])



            asientos[(i+2, j+1)] = asiento

    for (i, j), asiento in asientos.items():
        U.unbind_asiento(asiento)
        try:
            # Si el asiento está seleccionado, se cambia su imagen a asiento_hover
            if (i, j) in DP.PELICULAS[base.titulo_pelicula]["salas"][base.sala_actual][base.funcion_actual]["seleccionados"]:
                asiento.configure(image=CAI.ASIENTOS_IMAGEN["asiento_hover"], state="normal")
                U.bind_asiento(asiento,CAI.ASIENTOS_IMAGEN["asiento_libre"],CAI.ASIENTOS_IMAGEN["asiento_hover"])

            # Si el asiento está reservado, se cambia su imagen a asiento_reservado y se deshabilita
            elif (i, j) in DP.PELICULAS[base.titulo_pelicula]["salas"][base.sala_actual][base.funcion_actual]["reservados"]:
                asiento.configure(image=CAI.ASIENTOS_IMAGEN["asiento_reservado"], state="disabled")

            else:
            # Si el asiento está libre, se cambia su imagen a asiento_libre
                asiento.configure(image=CAI.ASIENTOS_IMAGEN["asiento_libre"], state="normal")
                U.bind_asiento(asiento,CAI.ASIENTOS_IMAGEN["asiento_hover"],CAI.ASIENTOS_IMAGEN["asiento_libre"])
                
        except KeyError as e:
            print(f"KeyError: {e} not found in the data structure.")