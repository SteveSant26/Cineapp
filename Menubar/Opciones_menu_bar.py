import customtkinter as ctk


import Utils.Colores_Temas as CT
from Menubar.Administrar_sala import administrar_peliculas
import Pantalla_cine.Funcion_botones_opciones as FB


def crear_frame_administrar_peliculas(base: ctk.CTkFrame):
    """Agrega una pelicula a la base de datos."""
    # Limpiar los widgets existentes
    from Menubar.Menu_bar import crear_menu_bar
    FB.limpiar_widgets_base(base)
    crear_menu_bar(base, busqueda=False)
    administrar_peliculas(base)


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

def enter_hover_text(base):
    base.desplegar_menu_boton.configure(text_color="#31AF9C")

def leave_hover_text(base):
    if ctk.get_appearance_mode() == "Dark":
        base.desplegar_menu_boton.configure(text_color="white")
    else:
        base.desplegar_menu_boton.configure(text_color="black")



def salir(base:ctk.CTkFrame):
    """ Cierra la aplicación."""
    base.destroy()