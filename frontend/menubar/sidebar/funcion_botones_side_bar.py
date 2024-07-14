import customtkinter as ctk
from frontend import utils
from frontend import menubar as MB
from frontend import login
from . import administrar_peliculas as AP
from . import administrar_funciones as AF
from . import administrar_salas as AS

def crear_frame_editar_perfil(base: ctk.CTkFrame) -> None:
    """
    Crea el frame para editar el perfil del usuario.

    Args:
        base (ctk.CTkFrame): El frame base donde se creará la interfaz de edición de perfil.

    Returns:
        None
    """
    from frontend import menubar as MB
    from . import editar_perfil as EP
    utils.limpiar_widgets_base(base)
    MB.crear_menu_bar(base)
    EP.editar_perfil(base)

def crear_frame_administrar_peliculas(base: ctk.CTkFrame) -> None:
    """
    Crea el frame para administrar películas en la base de datos.

    Args:
        base (ctk.CTkFrame): El frame base donde se creará la interfaz de administración de películas.

    Returns:
        None
    """

    
    utils.limpiar_widgets_base(base)
    MB.crear_menu_bar(base)
    AP.administrar_peliculas(base)

def crear_frame_administrar_salas(base: ctk.CTkFrame) -> None:
    """
    Crea el frame para administrar salas en la base de datos.

    Args:
        base (ctk.CTkFrame): El frame base donde se creará la interfaz de administración de salas.

    Returns:
        None
    """

    utils.limpiar_widgets_base(base)
    MB.crear_menu_bar(base)
    AS.administrar_salas(base)

def crear_frame_administrar_funciones(base: ctk.CTkFrame) -> None:
    """
    Crea el frame para administrar funciones en la base de datos.

    Args:
        base (ctk.CTkFrame): El frame base donde se creará la interfaz de administración de funciones.

    Returns:
        None
    """

    
    utils.limpiar_widgets_base(base)
    MB.crear_menu_bar(base)
    AF.administrar_funciones(base)

def cambiar_tema(switch: ctk.CTkSwitch) -> None:
    """
    Cambia el tema de la aplicación entre claro y oscuro.

    Args:
        switch (ctk.CTkSwitch): El switch que determina el tema seleccionado.

    Returns:
        None
    """
    from .utils_menu_bar import configurar_treeview_claro, configurar_treeview_oscuro
    try:
        if switch.get() == 1:
            ctk.set_appearance_mode("light")
            configurar_treeview_claro()
        else:
            ctk.set_appearance_mode("dark")
            configurar_treeview_oscuro()
    except Exception as e:
        print(f"Error changing theme: {e}")

def cerrar_sesion(base: ctk.CTkFrame) -> None:
    """
    Cierra la sesión actual y muestra la pantalla de login.

    Args:
        base (ctk.CTkFrame): El frame base donde se creará la interfaz de login.

    Returns:
        None
    """
    utils.limpiar_widgets_base(base)
    utils.configurar_ventana_login(base)
    login.crear_login(base)
