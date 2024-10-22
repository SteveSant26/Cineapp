import customtkinter as ctk
import tkinter.ttk as ttk
from frontend.utils import mostrar_error, mostrar_mensaje, limpiar_widgets_base
import backend.database as DB
from ..utils_menu_bar import limpiar_treeview

def conseguir_datos_pelicula(base: ctk.CTk) -> tuple:
    """
    Obtiene los datos de la película desde los campos de entrada.

    Args:
        base (ctk.CTk): La ventana principal de la aplicación.

    Returns:
        tuple: Los datos de la película.
    """
    try:
        id = base.entries_pelicula["id"].get()
        titulo = base.entries_pelicula["titulo"].get()
        sinopsis = base.entries_pelicula["sinopsis"].get("1.0", "end-1c")
        genero = base.entries_pelicula["genero"].get()
        duracion = base.entries_pelicula["duracion"].get()
        estreno = base.entries_pelicula["estreno"].get()
        prom_votos = base.entries_pelicula["promedio votos"].get()
        ruta_imagen = base.entries_pelicula["ruta_imagen"].get()

        if not (id and titulo and duracion and estreno and ruta_imagen):
            mostrar_error("Error de Validación", "Todos los campos obligatorios deben estar llenos.")
            return
        datos = (ruta_imagen, titulo, sinopsis, genero, duracion, estreno, prom_votos, int(id))
        return datos
    except Exception as e:
        mostrar_error("Error", f"Se produjo un error: {e}")

def editar_pelicula(base: ctk.CTk) -> None:
    """
    Edita una película existente en la base de datos y actualiza el Treeview.

    Args:
        base (ctk.CTk): La ventana principal de la aplicación.

    Returns:
        None
    """
    datos = conseguir_datos_pelicula(base)
    try:
        if not DB.editar_pelicula_bd(datos):
            return
        mostrar_mensaje("Película Editada", "La película ha sido editada correctamente.")
        insertar_peliculas_tree(base.tree_peliculas)
    except Exception as e:
        mostrar_error("Error", f"Se produjo un error: {e}")
        
def eliminar_pelicula(base: ctk.CTk) -> None:
    """
    Elimina una película de la base de datos y actualiza el Treeview.

    Args:
        base (ctk.CTk): La ventana principal de la aplicación.

    Returns:
        None
    """
    try:
        id = base.entries_pelicula["id"].get()
        if not id:
            mostrar_error("Error de Validación", "El campo ID es obligatorio")
            return
        
        if not DB.eliminar_pelicula_bd(id):
            return
        mostrar_mensaje("Película Eliminada", "La película ha sido eliminada correctamente.")
        insertar_peliculas_tree(base.tree_peliculas)
    except Exception as e:
        mostrar_error("Error", f"Se produjo un error: {e}")

def insertar_peliculas_tree(treeview: ttk.Treeview) -> None:
    """
    Inserta las películas en el Treeview.

    Args:
        treeview (ttk.Treeview): El Treeview donde se mostrarán las películas.

    Returns:
        None
    """
    try:
        limpiar_treeview(treeview)
        for pelicula in DB.obtener_peliculas_bd():
            insertar_pelicula_tree(treeview, pelicula)
    except Exception as e:
        mostrar_error("Error al Insertar Películas", f"No se pudieron insertar las películas. {e}")

def insertar_pelicula_tree(treeview: ttk.Treeview, pelicula: tuple) -> None:
    """
    Inserta una película en el Treeview.

    Args:
        treeview (ttk.Treeview): El Treeview donde se mostrarán las películas.
        pelicula (tuple): Los datos de la película.

    Returns:
        None
    """
    pelicula_id = pelicula[0]
    pelicula_titulo = pelicula[2]
    sinopsis_pelicula = pelicula[3]
    genero_pelicula = pelicula[4]
    duracion_pelicula = pelicula[5]
    estreno_pelicula = pelicula[6]
    votacion_pelicula = pelicula[7]
    ruta_imagen = pelicula[1]
    datos_pelicula = [pelicula_id, pelicula_titulo, sinopsis_pelicula, genero_pelicula, duracion_pelicula, estreno_pelicula, votacion_pelicula, ruta_imagen]
    treeview.insert("", "end", values=datos_pelicula)

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
