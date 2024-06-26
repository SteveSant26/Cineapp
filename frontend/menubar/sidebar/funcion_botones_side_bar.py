import customtkinter as ctk
from frontend import utils



def crear_frame_administrar_peliculas(base: ctk.CTkFrame):
    """Agrega una pelicula a la base de datos."""
    from frontend import menubar as MB
    from .peliculas import administrar_peliculas as AP
    
    utils.limpiar_widgets_base(base)
    MB.crear_menu_bar(base)
    AP.administrar_peliculas(base)

def crear_frame_administrar_salas(base:ctk.CTkFrame):
    """ Agrega una sala a la base de datos."""
    from frontend import menubar as MB
    from .salas import administrar_salas as AS
    utils.limpiar_widgets_base(base)
    MB.crear_menu_bar(base)
    AS.administrar_salas(base)

def crear_frame_administrar_funciones(base:ctk.CTkFrame):
    """ Agrega una función a la base de datos."""
    from frontend import menubar as MB
    from .funciones import administrar_funciones as AF
    
    utils.limpiar_widgets_base(base)
    MB.crear_menu_bar(base)
    AF.administrar_funciones(base)
    



def cambiar_tema(switch: ctk.CTkSwitch, base: ctk.CTk):
    """Cambia el tema de la aplicación."""
    try:
        if switch.get() == 1:
            ctk.set_appearance_mode("light")
            utils.configurar_treeview_claro()
        else:
            ctk.set_appearance_mode("dark")
            utils.configurar_treeview_oscuro()
    except Exception as e:
        print(f"Error changing theme: {e}")




def salir(base:ctk.CTkFrame):
    """ Cierra la aplicación."""
    base.destroy()