import customtkinter as ctk
from frontend.utils import crear_icono_busqueda as CBI

from frontend.utils import enter_hover_boton_busqueda, leave_hover_boton_busqueda

def crear_barra_busqueda(base: ctk.CTk) -> None:
    """
    Crea una barra de búsqueda en la interfaz gráfica.

    Args:
        base (ctk.CTk): La ventana principal de la aplicación.

    Returns:
        None
    """
    
    # Contenedor para centrar la barra de búsqueda
    busqueda_frame = ctk.CTkFrame(base.menu_bar_frame, fg_color="transparent")
    busqueda_frame.pack(side="left", expand=True)
    
    barra_de_busqueda = ctk.CTkEntry(busqueda_frame, font=("Arial", 20, "bold"), width=200, placeholder_text="Buscar película...")
    barra_de_busqueda.pack(side="left")

    boton_barra_de_busqueda = ctk.CTkButton(busqueda_frame, 
                                                 image=CBI.BUSQUEDA_IMAGEN["imagen_busqueda"],
                                                 text=" ", 
                                                 font=("Arial", 20, "bold"), 
                                                 width=10,
                                                 border_width=1,
                                                 border_color=("black", "white"),
                                                 fg_color="transparent",
                                                 hover=False,
                                                 corner_radius=15,
                                                 command=lambda: print("Buscando..."))
    boton_barra_de_busqueda.pack(side="left", padx=0 )
    boton_barra_de_busqueda.bind("<Enter>", lambda e: enter_hover_boton_busqueda(boton_barra_de_busqueda))
    boton_barra_de_busqueda.bind("<Leave>", lambda e: leave_hover_boton_busqueda(boton_barra_de_busqueda))
    generos = ["Todos", "Acción", "Aventura", "Comedia", "Drama", "Fantasía", "Terror", "Romance", "Ciencia Ficción", "Animación", "Documental", "Musical", "Misterio", "Crimen", "Biografía", "Histórico", "Guerra", "Western", "Deportes", "Superhéroes", "Thriller", "Familia", "Infantil", "Anime", "Adultos"]

    combobox_generos = ctk.CTkComboBox(busqueda_frame, font=("Arial", 20, "bold"),values=generos)
    combobox_generos.set("Todos")
    combobox_generos.pack(side="left", padx=(10, 200))
