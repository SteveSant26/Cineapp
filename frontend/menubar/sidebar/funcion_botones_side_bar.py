import customtkinter as ctk


import frontend.utils as utils

from . import crear_frame_administrar_sala as CFAS


def crear_frame_administrar_peliculas(base: ctk.CTkFrame):
    """Agrega una pelicula a la base de datos."""
    from frontend.menubar import crear_menu_bar
    
    # Limpiar los widgets existentes
    utils.limpiar_widgets_base(base)
    crear_menu_bar(base, busqueda=False)
    CFAS.administrar_peliculas(base)


def crear_frame_administrar_funciones(base:ctk.CTkFrame):
    """ Agrega una función a la base de datos."""
    pass

def crear_frame_administrar_salas(base:ctk.CTkFrame):
    """ Agrega una sala a la base de datos."""
    pass


def cambiar_tema(switch: ctk.CTkSwitch, base: ctk.CTk):
    """Cambia el tema de la aplicación."""
    
    if switch.get() == 1:
        ctk.set_appearance_mode("light")
        text_color = "black"
    else:
        ctk.set_appearance_mode("dark")
        text_color = "white"


    # Actualiza el color del texto de los botones de la cartelera
    if base.frame_peliculas and base.frame_peliculas.winfo_exists():
        for widget in base.frame_peliculas.winfo_children():
            if isinstance(widget, ctk.CTkButton):
                widget.configure(text_color=text_color)

    # Actualiza el color del texto del botón de desplegar menubar
    base.desplegar_menu_boton.configure(text_color=text_color)




def salir(base:ctk.CTkFrame):
    """ Cierra la aplicación."""
    base.destroy()