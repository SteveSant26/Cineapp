from frontend.utils import limpiar_widgets_base,mostrar_error,mostrar_mensaje
import backend.database as DB
from ..utils_menu_bar import limpiar_treeview

def conseguir_datos_funcion(base):
    try:
        id = base.entries_funciones["id"].get()
        id_pelicula = (base.entries_funciones["id pelicula"].get().split(" - ")[0])
        id_sala = (base.entries_funciones["id sala"].get().split(" - ")[0])
        horas = base.entries_funciones["hora"].get()
        minutos = base.entries_funciones["minuto"].get()
        hora = f"{horas:02}:{minutos:02}:00"
        print(id)
        
        if not (id_pelicula and id_sala and hora):
            mostrar_error("Error de Validación", "Todos los campos obligatorios deben estar llenos.")
            return
        datos = (id, int(id_pelicula), int(id_sala), hora)
        return datos
    except Exception as e:
        mostrar_error("Error", f"Se produjo un error: {e}")

def agregar_funcion(base):
    datos_funcion = conseguir_datos_funcion(base)[1:]
    try:
        if not DB.agregar_funcion_bd(datos_funcion):
            return
        mostrar_mensaje("Funcion Agregada", "La funcion ha sido agregada correctamente.")
        insertar_funciones_tree(base.tree_funciones)

    except Exception as e:
        mostrar_error("Error al Agregar Funcion", f"No se pudo agregar la Funcion. {e}")
        
def editar_funcion(base):
    datos = conseguir_datos_funcion(base)
    try:
        datos = (datos[1], datos[2], datos[3], datos[0])
        if not DB.editar_funcion_bd(datos):
            return
        mostrar_mensaje("Funcion Editada", "La Funcion ha sido editada correctamente.")
        insertar_funciones_tree(base.tree_funciones)
    except Exception as e:
        mostrar_error("Error al Editar Funcion", f"No se pudo editar la Funcion. {e}")


def eliminar_funcion(base):
    try:
        id_sala = base.entries_funciones["id"].get()
        if not id_sala:
            mostrar_error("Error de Validación", "El campo ID es obligatorio")
            return
        if not DB.eliminar_funcion_bd(id_sala):
            return
        mostrar_mensaje("Funcion Eliminada", "La Funcion ha sido eliminada correctamente.")
        insertar_funciones_tree(base.tree_funciones)

    except Exception as e:
        mostrar_error("Error al Eliminar Funcion", f"No se pudo eliminar la Funcion. {e}")
    
        

def insertar_funciones_tree(treeview):
    try:
        limpiar_treeview(treeview)
        for funcion in DB.obtener_funciones_bd():
            treeview.insert("", "end", values=funcion)
    except Exception as e:
        mostrar_error("Error al Insertar Funciones", f"No se pudieron insertar las Funciones. {e}")

def volver(base):
    from frontend import cartelera
    
    limpiar_widgets_base(base)
    cartelera.iniciar_hilo_mostrar_peliculas(base)
