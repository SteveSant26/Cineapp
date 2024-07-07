import customtkinter as ctk
from concurrent.futures import ThreadPoolExecutor
from . import crear_asientos_img as CAI
from . import utils_asientos as U
from ..utils_pc import obtener_tamano_sala, obtener_funcion_id_por_sala_pelicula_id

def obtener_asiento(frame_sala, fila, columna):
    """Obtiene el asiento de la grilla en la posición dada."""
    return frame_sala.grid_slaves(row=fila, column=columna)[0]

def crear_asientos(base) -> None:
    """Crea los asientos de la sala seleccionada y los muestra en el frame de la sala."""
    # Se obtienen las filas y columnas de la sala seleccionada
    base.filas_sala, base.columnas_sala = obtener_tamano_sala(base.sala_actual)

    # Configurar las filas y columnas para que se expandan uniformemente
    for i in range(base.filas_sala):
        base.frame_sala.grid_rowconfigure(i + 2, weight=1)
    for j in range(base.columnas_sala):
        base.frame_sala.grid_columnconfigure(j + 1, weight=1)

    # Verificar si la función actual está en la lista de funciones de la película
    if base.funcion_actual not in base.funciones:
        base.funcion_actual = base.funciones[0]
        base.funcion_actual_id = obtener_funcion_id_por_sala_pelicula_id(base.sala_actual_id, base.pelicula_id, base.funcion_actual)

    # Crear el título de la sala
    titulo_sala = ctk.CTkLabel(base.frame_sala, text=f"| Pantalla {base.sala_actual.lower()}  |", font=("Arial", 40, "bold"))
    titulo_sala.grid(row=0, column=0, pady=20, padx=20, columnspan=base.columnas_sala + 1, sticky="nsew")

    # Este abecedario se usará para nombrar las filas de los asientos
    abecedario = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # Crear nuevos botones de asientos y actualizar el diccionario de asientos
    asientos = {}

    for i in range(base.filas_sala):
        letra = ctk.CTkLabel(base.frame_sala, text=abecedario[i], font=("Arial", 20, "bold"))
        letra.grid(row=i + 2, column=0, padx=10, pady=5, sticky="nsew")
        
        for j in range(base.columnas_sala):
            numero = ctk.CTkLabel(base.frame_sala, text=str(j + 1), font=("Arial", 20, "bold"))
            numero.grid(row=1, column=j + 1, sticky="nsew", padx=10, pady=5)
            
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
            
            U.bind_asiento(asiento, CAI.ASIENTOS_IMAGEN["asiento_hover"], CAI.ASIENTOS_IMAGEN["asiento_libre"])

            asientos[(i+2, j+1)] = asiento

    # Obtener los asientos reservados y sus IDs en paralelo
    with ThreadPoolExecutor(max_workers=5) as executor:
        future_asientos_reservados = executor.submit(U.obtener_todos_asientos_reservados, base.funcion_actual_id)
        future_asientos_reservados_id = executor.submit(U.obtener_id_asiento, base.funcion_actual_id)
        
        base.asientos_reservados = future_asientos_reservados.result()
        base.asientos_reservados_id = future_asientos_reservados_id.result()

    base.asientos_habilitados = False
    base.asientos_seleccionados = set()

    # Actualizar asientos basados en su estado (seleccionado, reservado o libre)
    for (i, j), asiento in asientos.items():
        U.unbind_asiento(asiento)
        if (i, j) in base.asientos_seleccionados:
            asiento.configure(image=CAI.ASIENTOS_IMAGEN["asiento_hover"], state="normal")
            U.bind_asiento(asiento, CAI.ASIENTOS_IMAGEN["asiento_libre"], CAI.ASIENTOS_IMAGEN["asiento_hover"])
        elif (i, j) in base.asientos_reservados:
            asiento.configure(image=CAI.ASIENTOS_IMAGEN["asiento_reservado"], state="disabled")
        else:
            asiento.configure(image=CAI.ASIENTOS_IMAGEN["asiento_libre"], state="normal")
            U.bind_asiento(asiento, CAI.ASIENTOS_IMAGEN["asiento_hover"], CAI.ASIENTOS_IMAGEN["asiento_libre"])
