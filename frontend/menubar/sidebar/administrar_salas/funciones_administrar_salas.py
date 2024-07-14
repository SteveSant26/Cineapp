import customtkinter as ctk
from tkinter import ttk

from frontend.utils import limpiar_widgets_base, mostrar_error, mostrar_mensaje
from backend.database import obtener_salas_bd,agregar_sala_bd,editar_sala_bd,eliminar_sala_bd
from ..utils_menu_bar import limpiar_treeview

def conseguir_datos_sala(base) -> tuple:
    """
    Obtiene los datos de la sala desde los campos de entrada.

    Args:
        base (ctk.CTk): La ventana principal de la aplicación.

    Returns:
        tuple: Los datos de la sala.
    """
    try:
        id = base.entries_salas["id"].get()
        nombre = base.entries_salas["nombre"].get()
        filas = base.entries_salas["filas"].get()
        columnas = base.entries_salas["columnas"].get()
        
        if not (nombre and filas and columnas):
            mostrar_error("Error de Validación", "Todos los campos obligatorios deben estar llenos.")
            return
        datos = (int(id), nombre, filas, columnas)
        return datos
    except Exception as e:
        mostrar_error("Error", f"Se produjo un error: {e}")

def agregar_sala(base: ctk.CTk) -> None:
    """
    Agrega una nueva sala a la base de datos y actualiza el Treeview.

    Args:
        base (ctk.CTk): La ventana principal de la aplicación.

    Returns:
        None
    """
    datos = conseguir_datos_sala(base)[1:]
    try:
        if not agregar_sala_bd(datos):
            return
        mostrar_mensaje("Sala Agregada", "La sala ha sido agregada correctamente.")
        insertar_salas_tree(base.tree_salas)
    except Exception as e:
        mostrar_error("Error al Agregar Sala", f"No se pudo agregar la sala. {e}")

def editar_sala(base: ctk.CTk) -> None:
    """
    Edita una sala existente en la base de datos y actualiza el Treeview.

    Args:
        base (ctk.CTk): La ventana principal de la aplicación.

    Returns:
        None
    """
    datos = conseguir_datos_sala(base)
    try:
        datos = (datos[1], datos[2], datos[3], datos[0])
        
        if not editar_sala_bd(datos):
            return
        mostrar_mensaje("Sala Editada", "La sala ha sido editada correctamente.")
        insertar_salas_tree(base.tree_salas)
    except Exception as e:
        mostrar_error("Error al Editar Sala", f"No se pudo editar la sala. {e}")

def eliminar_sala(base: ctk.CTk) -> None:
    """
    Elimina una sala de la base de datos y actualiza el Treeview.

    Args:
        base (ctk.CTk): La ventana principal de la aplicación.

    Returns:
        None
    """
    try:
        id_sala = base.entries_salas["id"].get()
        if not eliminar_sala_bd(id_sala):
            return
        mostrar_mensaje("Sala Eliminada", "La sala ha sido eliminada correctamente.")
        insertar_salas_tree(base.tree_salas)
    except Exception as e:
        mostrar_error("Error al Eliminar Sala", f"No se pudo eliminar la sala. {e}")

def insertar_salas_tree(treeview: ttk.Treeview) -> None:
    """
    Inserta las salas en el Treeview.

    Args:
        treeview (ttk.Treeview): El Treeview donde se mostrarán las salas.

    Returns:
        None
    """
    try:
        limpiar_treeview(treeview)
        for sala in obtener_salas_bd():
            treeview.insert("", "end", values=sala)
    except Exception as e:
        mostrar_error("Error al Insertar Salas", f"No se pudieron insertar las salas. {e}")

def volver(base: ctk.CTk) -> None:
    """
    Vuelve a la vista anterior de la cartelera.

    Args:
        base (ctk.CTk): La ventana principal de la aplicación.

    Returns:
        None
    """
    from frontend import cartelera
    
    limpiar_widgets_base(base)
    cartelera.iniciar_hilo_mostrar_peliculas(base)
