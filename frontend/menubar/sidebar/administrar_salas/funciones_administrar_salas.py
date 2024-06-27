def agregar_sala(base):
    pass
def editar_sala(base):
    pass
def eliminar_sala(base):
    pass

def insertar_salas_tree(treeview):
    from backend.database import obtener_salas_bd
    for sala in obtener_salas_bd():
        print(sala)
        treeview.insert("", "end", values=sala)
        
def volver(base):
    from frontend import cartelera
    from frontend.utils import limpiar_widgets_base
    
    limpiar_widgets_base(base)
    cartelera.mostrar_peliculas(base)
