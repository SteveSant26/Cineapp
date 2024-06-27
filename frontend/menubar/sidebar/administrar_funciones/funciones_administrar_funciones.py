
def agregar_pelicula(base):
    pass
def editar_pelicula(base):
    pass
def eliminar_pelicula(base):
    pass

def insertar_funciones_tree(treeview):
    from backend.database import obtener_funciones_bd
    for funcion in obtener_funciones_bd():
        treeview.insert("", "end", values=funcion)
        print(funcion)

def volver(base):
    from frontend import cartelera
    from frontend.utils import limpiar_widgets_base
    
    limpiar_widgets_base(base)
    cartelera.mostrar_peliculas(base)
