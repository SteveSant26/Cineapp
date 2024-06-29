from frontend.utils import limpiar_widgets_base,mostrar_error, mostrar_mensaje
import backend.database as DB
from ..utils_menu_bar import limpiar_treeview

def conseguir_datos_sala(base):
    try:
        id = base.entries_salas["id"].get()
        nombre = base.entries_salas["nombre"].get()
        filas = base.entries_salas["filas"].get()
        columnas = base.entries_salas["columnas"].get()
        
        if not (id and nombre and filas and columnas):
            mostrar_error("Error de Validación", "Todos los campos obligatorios deben estar llenos.")
            return
        datos = (int(id), nombre, filas, columnas)
        return datos
    except Exception as e:
        mostrar_error("Error", f"Se produjo un error: {e}")

def agregar_sala(base):
    datos = conseguir_datos_sala(base)
    try:
        if not DB.agregar_sala_bd(datos):
            return
        mostrar_mensaje("Sala Agregada", "La sala ha sido agregada correctamente.")
        insertar_salas_tree(base.tree_salas)

    except Exception as e:
        mostrar_error("Error al Agregar Sala", f"No se pudo agregar la sala. {e}")

def editar_sala(base):
    datos = conseguir_datos_sala(base)
    try:
        datos = (datos[1], datos[2], datos[3], datos[0])
        
        if not DB.editar_sala_bd(datos):
            return
        mostrar_mensaje("Sala Editada", "La sala ha sido editada correctamente.")
        insertar_salas_tree(base.tree_salas)

    except Exception as e:
        mostrar_error("Error al Editar Sala", f"No se pudo editar la sala. {e}")
        
def eliminar_sala(base):
    try:
        id_sala = base.entries_salas["id"].get()
        if not DB.eliminar_sala_bd(id_sala):
            return
        mostrar_mensaje("Sala Eliminada", "La sala ha sido eliminada correctamente.")
        insertar_salas_tree(base.tree_salas)
    except Exception as e:
        mostrar_error("Error al Eliminar Sala", f"No se pudo eliminar la sala. {e}")

def insertar_salas_tree(treeview):
    try:
        limpiar_treeview(treeview)
        for sala in DB.obtener_salas_bd():
            treeview.insert("", "end", values=sala)
    except Exception as e:
        mostrar_error("Error al Insertar Salas", f"No se pudieron insertar las salas. {e}")
        
def volver(base):
    from frontend import cartelera
    
    limpiar_widgets_base(base)
    cartelera.mostrar_peliculas(base)
