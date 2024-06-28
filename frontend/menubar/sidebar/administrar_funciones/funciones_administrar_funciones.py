from frontend.utils import limpiar_widgets_base,mostrar_error,mostrar_mensaje
from backend.database import obtener_funciones_bd,agregar_funcion_bd,editar_funcion_bd,eliminar_funcion_bd
from ..utils_menu_bar import limpiar_treeview

def conseguir_datos_funcion(base):
    id = base.entries_funciones["id"].get()
    id_pelicula = base.entries_funciones["id pelicula"].get()
    id_sala = base.entries_funciones["id sala"].get()
    fecha_hora = base.entries_funciones["fecha y hora"].get()
    

    
    if not (id and id_pelicula and id_sala and fecha_hora):
        mostrar_error("Error de Validación", "Todos los campos obligatorios deben estar llenos.")
        return
    datos = (int(id), int(id_pelicula), int(id_sala), fecha_hora)
    return datos

def agregar_funcion(base):
    datos_funcion = conseguir_datos_funcion(base)
    try:
        if agregar_funcion_bd(datos_funcion):
            mostrar_mensaje("Funcion Agregada", "La funcion ha sido agregada correctamente.")
            insertar_funciones_tree(base.tree_funciones)
        else:
            mostrar_error("Error al Agregar Funcion", "No se pudo agregar la Funcion.")
    except Exception as e:
        mostrar_error("Error al Agregar Funcion", f"No se pudo agregar la Funcion. {e}")
        
def editar_funcion(base):
    datos = conseguir_datos_funcion(base)
    datos = (datos[1], datos[2], datos[3], datos[0])
    try:
        if editar_funcion_bd(datos):
            mostrar_mensaje("Funcion Editada", "La Funcion ha sido editada correctamente.")
            insertar_funciones_tree(base.tree_funciones)
        else:
            mostrar_error("Error al Editar Funcion", "No se pudo editar la Funcion.")
    except Exception as e:
        mostrar_error("Error al Editar Funcion", f"No se pudo editar la Funcion. {e}")
        
def eliminar_funcion(base):
    id_sala = base.entries_funciones["id"].get()
    try:
        if eliminar_funcion_bd(id_sala):
            mostrar_mensaje("Funcion Eliminada", "La Funcion ha sido eliminada correctamente.")
            insertar_funciones_tree(base.tree_funciones)
        else:
            mostrar_error("Error al Eliminar Funcion", "No se pudo eliminar la Funcion.")
    except Exception as e:
        mostrar_error("Error al Eliminar Funcion", f"No se pudo eliminar la Funcion. {e}")

def insertar_funciones_tree(treeview):
    limpiar_treeview(treeview)
    for funcion in obtener_funciones_bd():
        treeview.insert("", "end", values=funcion)

def volver(base):
    from frontend import cartelera
    
    limpiar_widgets_base(base)
    cartelera.mostrar_peliculas(base)
