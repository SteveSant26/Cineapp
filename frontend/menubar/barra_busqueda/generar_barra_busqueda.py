import customtkinter as ctk
from .utils_barra_busqueda import enter_hover_boton_busqueda, leave_hover_boton_busqueda
from . import crear_busqueda_img as CBI

def crear_barra_busqueda(base: ctk.CTk) -> None:
    """
    Crea una barra de búsqueda en la interfaz gráfica.

    Args:
        base (ctk.CTk): La ventana principal de la aplicación.

    Returns:
        None
    """
    
    # Contenedor para centrar la barra de búsqueda
    base.busqueda_frame = ctk.CTkFrame(base.menu_bar_frame, fg_color="transparent")
    base.busqueda_frame.pack(side="left", expand=True)
    
    barra_de_busqueda = ctk.CTkEntry(base.busqueda_frame, font=("Arial", 20, "bold"), width=200, placeholder_text="Buscar película...")
    barra_de_busqueda.pack(side="left")

    base.boton_barra_de_busqueda = ctk.CTkButton(base.busqueda_frame, 
                                                 image=CBI.BUSQUEDA_IMAGEN["imagen_busqueda"],
                                                 text=" ", 
                                                 font=("Arial", 20, "bold"), 
                                                 width=10,
                                                 border_width=2,
                                                 border_color="black",
                                                 fg_color="transparent",
                                                 hover=False,
                                                 corner_radius=15,
                                                 command=lambda: print("Buscando..."))
    base.boton_barra_de_busqueda.pack(side="left", padx=(0, 200))
    
    base.boton_barra_de_busqueda.bind("<Enter>", lambda e: enter_hover_boton_busqueda(base.boton_barra_de_busqueda))
    base.boton_barra_de_busqueda.bind("<Leave>", lambda e: leave_hover_boton_busqueda(base.boton_barra_de_busqueda))
