import customtkinter as ctk
from frontend.utils import mostrar_error
from . import asientos as A
from . import funcion_botones_opciones as FBO
from . import botones_opciones as BO

def crear_vista_cine(base: ctk.CTk) -> None:
    """
    Inicializa el frame donde se guardan las opciones de la sala y los asientos de la película seleccionada.

    Args:
        base (ctk.CTk): La ventana principal de la aplicación.

    Returns:
        None
    """
    from frontend import utils, menubar as MB
    try:
        utils.limpiar_widgets_base(base)
        MB.crear_menu_bar(base)
        
        crear_frame_vista_cine(base)
        actualizar_frames(base)
    except Exception as e:
        mostrar_error("Error al crear la vista del cine", f"Ocurrió un error al intentar crear la vista del cine: {e}")

def crear_frame_vista_cine(base: ctk.CTk) -> None:
    """
    Crea el frame que almacena las opciones y la sala.

    Args:
        base (ctk.CTk): La ventana principal de la aplicación.

    Returns:
        None
    """
    base.frame_opciones_sala = ctk.CTkFrame(base, fg_color="transparent")
    base.frame_opciones_sala.pack(fill="both", expand=True)
    base.frame_opciones_sala.rowconfigure(0, weight=1)
    base.frame_opciones_sala.columnconfigure(0, weight=1)
    base.frame_opciones_sala.columnconfigure(1, weight=3)

def crear_frame_opciones(base: ctk.CTk) -> None:
    """
    Crea el frame que almacena las opciones para seleccionar la sala y la función de la película seleccionada.

    Args:
        base (ctk.CTk): La ventana principal de la aplicación.

    Returns:
        None
    """
    try:
        base.frame_opciones = ctk.CTkFrame(base.frame_opciones_sala, border_color="black", border_width=2, width=500)
        base.frame_opciones.grid(row=0, column=0, sticky="nsew", padx=5, pady=10)
        base.frame_opciones.columnconfigure(0, weight=1)
        base.frame_opciones.columnconfigure(1, weight=1)
        base.frame_opciones.grid_propagate(False)

        titulo_menu = ctk.CTkLabel(base.frame_opciones, text=f"{base.titulo_pelicula}", font=("Arial", 30, "bold"), wraplength=400)
        titulo_menu.grid(row=0, column=0, pady=20, padx=20, columnspan=2, sticky="nsew")

        BO.colocar_botones(base)
    except Exception as e:
        mostrar_error("Error al crear frame de opciones", "No hay funciones ni salas asignadas a esta película")
        FBO.regresar(base)

def crear_frame_sala(base: ctk.CTk) -> None:
    """
    Crea el frame que almacena los asientos de la sala de la película seleccionada.

    Args:
        base (ctk.CTk): La ventana principal de la aplicación.

    Returns:
        None
    """
    base.frame_sala = ctk.CTkFrame(base.frame_opciones_sala, border_color="black", border_width=2, width=1100)
    base.frame_sala.grid(row=0, column=1, sticky="nsew", padx=5, pady=10)
    base.frame_sala.grid_propagate(False)

def actualizar_frames(base: ctk.CTk) -> None:
    """
    Actualiza los frames de la sala y las opciones.

    Args:
        base (ctk.CTk): La ventana principal de la aplicación.

    Returns:
        None
    """
    crear_frame_sala(base)
    crear_frame_opciones(base)
    A.crear_asientos(base)

def crear_frame_funciones(base: ctk.CTk) -> None:
    """
    Crea el frame que almacena las funciones de la sala seleccionada.

    Args:
        base (ctk.CTk): La ventana principal de la aplicación.

    Returns:
        None
    """
    titulo_funciones = ctk.CTkLabel(base.frame_opciones, text="Seleccione su función", font=("Arial", 30, "bold"))
    titulo_funciones.grid(row=3, column=0, columnspan=2, pady=10, padx=20)

    base.frame_funciones = ctk.CTkFrame(base.frame_opciones)
    base.frame_funciones.grid(row=4, column=0, pady=10, padx=10, columnspan=2, sticky="nsew")
    
    FBO.actualizar_botones_funciones(base)
