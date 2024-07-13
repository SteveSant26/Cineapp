import customtkinter as ctk
from concurrent.futures import ThreadPoolExecutor
from . import crear_asientos_img as CAI
from . import utils_asientos as UA
from frontend.utils import mostrar_error
from ..utils_pc import obtener_tamano_sala, obtener_funcion_id_por_sala_pelicula_id



def crear_asientos(base) -> None:
    """Crea los asientos de la sala seleccionada y los muestra en el frame de la sala."""
    # Se obtienen las filas y columnas de la sala seleccionada
    try:
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
                                        border_color=("black","white"),
                                        border_width=1,
                                        image=CAI.ASIENTOS_IMAGEN["asiento_libre"],
                                        fg_color="transparent",
                                        command=lambda fila=i + 2, columna=j + 1: UA.seleccionar_asiento(fila, columna, base))
                asiento.grid(row=i + 2, column=j + 1, padx=5, pady=5, sticky="nsew")
                

                asientos[(i+2, j+1)] = asiento

        actualizar_asientos(base)


        
        # Actualizar asientos basados en su estado (seleccionado, reservado o libre)
        for (i, j), asiento in asientos.items():
            if (i, j) in base.asientos_seleccionados:
                asiento.configure(image=CAI.ASIENTOS_IMAGEN["asiento_hover"], state="normal",border_color="#31AF5D")
                UA.bind_asiento(asiento, CAI.ASIENTOS_IMAGEN["asiento_libre"], CAI.ASIENTOS_IMAGEN["asiento_hover"])
            elif (i, j) in base.asientos_reservados:
                asiento.configure(image=CAI.ASIENTOS_IMAGEN["asiento_reservado"], state="disabled", border_color=("white","black"))
                
                if base.tipo_usuario == "cliente":
                    if base.asientos_cliente:
                        if (i, j) in base.asientos_cliente:
                            asiento.configure(image=CAI.ASIENTOS_IMAGEN["asiento_ocupado"], state="disabled", border_color="#C15F44")
            else:
                UA.bind_asiento(asiento, CAI.ASIENTOS_IMAGEN["asiento_hover"], CAI.ASIENTOS_IMAGEN["asiento_libre"])
                
    except Exception as e:
        mostrar_error("Error al crear asientos", f"No se pudieron crear los asientos de la sala seleccionada {e}")




def actualizar_asientos(base):
    base.asientos = UA.obtener_todos_asientos_reservados(base.funcion_actual_id,base.usuario,base.tipo_usuario)
    base.asientos_reservados_id = UA.obtener_id_asiento(base.funcion_actual_id)


    if base.asientos:
        if base.tipo_usuario == "cliente":
            asientos_cliente = base.asientos.get(base.usuario, [])
            if asientos_cliente:
                base.asientos_cliente = asientos_cliente
            else:
                base.asientos_cliente = {}
            print(base.asientos_cliente)
        base.asientos_reservados = base.asientos.get("todos_asientos", [])
        print(base.asientos_reservados)
    else:
        base.asientos_reservados = {}
        
    base.asientos_habilitados = False
    base.asientos_seleccionados = set()