import customtkinter as ctk
import tkinter as tk

from . import colores_asientos as CA
from . import asientos as A
from .utils_pc import obtener_salas, obtener_funciones, obtener_funcion_id_por_sala_pelicula_id, obtener_sala_id_por_nombre_bd
from . import funcion_botones_opciones as FBO

def crear_combobox(base: dict) -> None:
    """
    Crea el combobox para seleccionar la sala de la película seleccionada.

    Args:
        base (dict): Un diccionario con las variables del programa.

    Returns:
        None
    """
    titulo_combobox = ctk.CTkLabel(base.frame_opciones, text="Seleccione la sala", font=("Arial", 20))
    titulo_combobox.grid(row=2, column=0, pady=10, padx=20)
    
    if base.salas is None:
        base.salas = obtener_salas(base.pelicula_id)

    if base.sala_actual is None:
        base.sala_actual = base.salas[0]
        base.sala_actual_id = obtener_sala_id_por_nombre_bd(base.sala_actual)[0][0]
        
    base.funciones = obtener_funciones(base.pelicula_id, base.sala_actual)
    base.funcion_actual = base.funciones[0]
    base.funcion_actual_id = obtener_funcion_id_por_sala_pelicula_id(base.sala_actual_id, base.pelicula_id, base.funcion_actual)
    
    base.combobox_sala = ctk.CTkComboBox(base.frame_opciones, font=("Arial", 15, "bold"), values=base.salas, command=lambda event: FBO.actualizar_sala_por_combobox(event, base))
    base.combobox_sala.grid(row=2, column=1, pady=10, padx=20, sticky="ew")
    base.combobox_sala.set(base.sala_actual)

def dibujar_canvas(canvas: tk.Canvas, color: str) -> None:
    """
    Dibuja un rectángulo en un canvas con un color específico.

    Args:
        canvas (tk.Canvas): El canvas donde se dibujará el rectángulo.
        color (str): El color del rectángulo.

    Returns:
        None
    """
    canvas.create_rectangle(1, 1, 39, 39, fill=color, outline="black", width=1)

def referencia_colores(base: dict) -> None:
    """
    Actualiza los colores de referencia para los asientos en función del tema actual y del tipo de usuario.

    Args:
        base (dict): Un diccionario con las variables del programa.

    Returns:
        None
    """
    def actualizar_colores() -> None:
        COLORES = {}
        
        if ctk.get_appearance_mode().lower() == "dark":
            if base.tipo_usuario == "admin":
                COLORES = CA.COLORES_ASIENTO_TEMA_OSCURO_ADMIN
            else:
                COLORES = CA.COLORES_ASIENTO_TEMA_OSCURO_CLIENTE
        else:
            if base.tipo_usuario == "admin":
                COLORES = CA.COLORES_ASIENTO_TEMA_CLARO_ADMIN
            else:
                COLORES = CA.COLORES_ASIENTO_TEMA_CLARO_CLIENTE
                
        for widget in frame_colores.winfo_children():
            widget.destroy()
        
        canvas = {}
        fila_index = 0
        columna_index = 0
        for nombre, color in COLORES.items():
            canvas[nombre] = tk.Canvas(frame_colores, width=30, height=30, background="black", borderwidth=1, highlightthickness=0)
            dibujar_canvas(canvas[nombre], color)
            label = ctk.CTkLabel(frame_colores, text=f"{nombre}:", font=("Arial", 15, "bold"))
            label.grid(row=fila_index, column=columna_index * 2, padx=10, pady=5, sticky="w")
            canvas[nombre].grid(row=fila_index, column=columna_index * 2 + 1, padx=10, pady=5, sticky="nsew")
            columna_index += 1
            if columna_index >= 2:
                columna_index = 0
                fila_index += 1

    def verificar_cambio_tema() -> None:
        nonlocal ultimo_tema
        tema_actual = ctk.get_appearance_mode().lower()
        if tema_actual != ultimo_tema:
            ultimo_tema = tema_actual
            actualizar_colores()
        frame_colores.after(500, verificar_cambio_tema)

    frame_colores = ctk.CTkFrame(base.frame_opciones)
    frame_colores.grid(row=1, column=0, columnspan=2, pady=10, padx=10, sticky="nsew")

    ultimo_tema = ctk.get_appearance_mode().lower()
    actualizar_colores()
    verificar_cambio_tema()

def colocar_boton_mejor_asiento(base: dict) -> None:
    """
    Crea y coloca el botón de mejor asiento en el frame de las opciones.

    Args:
        base (dict): Un diccionario con las variables del programa.

    Returns:
        None
    """
    titulo_opciones = ctk.CTkLabel(base.frame_opciones, text="Opciones", font=("Arial", 30, "bold"))
    titulo_opciones.grid(row=5, column=0, columnspan=2, pady=10, padx=20)
    
    boton_mejor_asiento = ctk.CTkButton(base.frame_opciones, text="Mejor Asiento", fg_color="#329ADF", hover_color="#31AF9C", command=lambda: A.select_mejor_asiento(base), height=45, font=("Arial", 16, "bold"))
    boton_mejor_asiento.grid(row=6, column=0, columnspan=2, pady=10, padx=10, sticky="nsew")

def colocar_boton_reservar(base: dict) -> None:
    """
    Crea y coloca el botón de reservar asientos en el frame de las opciones.

    Args:
        base (dict): Un diccionario con las variables del programa.

    Returns:
        None
    """
    boton_reservar = ctk.CTkButton(base.frame_opciones, text="Reservar Asientos", fg_color="#329ADF", hover_color="#31AF9C", command=lambda: A.preguntar_reservar(base), height=45, font=("Arial", 16, "bold"))
    boton_reservar.grid(row=7, column=0, columnspan=2, pady=10, padx=10, sticky="nsew")

def colocar_boton_habilitar_reservar(base: dict) -> None:
    """
    Crea y coloca el botón de habilitar reservados en el frame de las opciones.

    Args:
        base (dict): Un diccionario con las variables del programa.

    Returns:
        None
    """
    boton_eliminar_reserva = ctk.CTkButton(base.frame_opciones, text="Habilitar reservados", fg_color="#329ADF", hover_color="#31AF9C", command=lambda: A.habilitar_reservados(base), height=45, font=("Arial", 16, "bold"))
    boton_eliminar_reserva.grid(row=8, column=0, columnspan=2, pady=10, padx=10, sticky="nsew")

def colocar_boton_regresar(base: dict) -> None:
    """
    Crea y coloca el botón de regresar a la cartelera en el frame de las opciones.

    Args:
        base (dict): Un diccionario con las variables del programa.

    Returns:
        None
    """
    boton_regresar = ctk.CTkButton(base.frame_opciones, text="Volver a la cartelera", fg_color="#329ADF", hover_color="#31AF9C", font=("Arial", 16, "bold"), height=45, command=lambda: FBO.regresar(base))
    if base.tipo_usuario == "admin":
        boton_regresar.grid(row=9, column=0, columnspan=2, pady=15, padx=10, sticky="ew")
    else:
        boton_regresar.grid(row=8, column=0, columnspan=2, pady=15, padx=10, sticky="ew")

def colocar_botones(base: dict) -> None:
    """
    Coloca los botones de las opciones encapsulados en una función.

    Args:
        base (dict): Un diccionario con las variables del programa.

    Returns:
        None
    """
    from .frame_vista_cine import crear_frame_funciones
    referencia_colores(base)
    crear_combobox(base)
    crear_frame_funciones(base)
    colocar_boton_mejor_asiento(base)
    colocar_boton_reservar(base)
    if base.tipo_usuario == "admin":
        colocar_boton_habilitar_reservar(base)
    colocar_boton_regresar(base)
