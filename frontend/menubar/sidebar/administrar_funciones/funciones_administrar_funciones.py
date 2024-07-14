import customtkinter as ctk
import tkinter.ttk as ttk
from frontend.utils import limpiar_widgets_base, mostrar_error, mostrar_mensaje
import backend.database as DB
from ..utils_menu_bar import limpiar_treeview

def conseguir_datos_funcion(base: ctk.CTk) -> tuple:
    """
    Obtiene los datos de la función desde los campos de entrada.

    Args:
        base (ctk.CTk): La ventana principal de la aplicación.

    Returns:
        tuple: Los datos de la función.
    """
    try:
        id = base.entries_funciones["id"].get()
        id_pelicula = int(base.entries_funciones["id pelicula"].get().split(" - ")[0])
        id_sala = int(base.entries_funciones["id sala"].get().split(" - ")[0])
        horas = base.entries_funciones["hora"].get()
        minutos = base.entries_funciones["minuto"].get()
        hora = f"{horas:02}:{minutos:02}:00"
        
        if not (id_pelicula and id_sala and hora):
            mostrar_error("Error de Validación", "Todos los campos obligatorios deben estar llenos.")
            return
        datos = (id, id_pelicula, id_sala, hora)
        return datos
    except Exception as e:
        mostrar_error("Error", f"Se produjo un error: {e}")

def agregar_funcion(base: ctk.CTk) -> None:
    """
    Agrega una nueva función a la base de datos y actualiza el Treeview.

    Args:
        base (ctk.CTk): La ventana principal de la aplicación.

    Returns:
        None
    """
    datos_funcion = conseguir_datos_funcion(base)[1:]
    try:
        if not DB.agregar_funcion_bd(datos_funcion):
            return
        mostrar_mensaje("Función Agregada", "La función ha sido agregada correctamente.")
        insertar_funciones_tree(base.tree_funciones)
    except Exception as e:
        mostrar_error("Error al Agregar Función", f"No se pudo agregar la función. {e}")

def editar_funcion(base: ctk.CTk) -> None:
    """
    Edita una función existente en la base de datos y actualiza el Treeview.

    Args:
        base (ctk.CTk): La ventana principal de la aplicación.

    Returns:
        None
    """
    datos = conseguir_datos_funcion(base)
    try:
        datos = (datos[1], datos[2], datos[3], datos[0])
        if not DB.editar_funcion_bd(datos):
            return
        mostrar_mensaje("Función Editada", "La función ha sido editada correctamente.")
        insertar_funciones_tree(base.tree_funciones)
    except Exception as e:
        mostrar_error("Error al Editar Función", f"No se pudo editar la función. {e}")

def eliminar_funcion(base: ctk.CTk) -> None:
    """
    Elimina una función de la base de datos y actualiza el Treeview.

    Args:
        base (ctk.CTk): La ventana principal de la aplicación.

    Returns:
        None
    """
    try:
        id_funcion = base.entries_funciones["id"].get()
        if not id_funcion:
            mostrar_error("Error de Validación", "El campo ID es obligatorio")
            return
        if not DB.eliminar_funcion_bd(id_funcion):
            return
        mostrar_mensaje("Función Eliminada", "La función ha sido eliminada correctamente.")
        insertar_funciones_tree(base.tree_funciones)
    except Exception as e:
        mostrar_error("Error al Eliminar Función", f"No se pudo eliminar la función. {e}")

def insertar_funciones_tree(treeview: ttk.Treeview) -> None:
    """
    Inserta las funciones en el Treeview.

    Args:
        treeview (ttk.Treeview): El Treeview donde se mostrarán las funciones.

    Returns:
        None
    """
    try:
        limpiar_treeview(treeview)
        for funcion in DB.obtener_funciones_bd():
            treeview.insert("", "end", values=funcion)
    except Exception as e:
        mostrar_error("Error al Insertar Funciones", f"No se pudieron insertar las funciones. {e}")

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
