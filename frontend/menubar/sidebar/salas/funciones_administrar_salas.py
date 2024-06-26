def agregar_sala(base):
    pass
def editar_sala(base):
    pass
def eliminar_sala(base):
    pass
def volver(base):
    from frontend import cartelera
    from frontend.utils import limpiar_widgets_base
    
    limpiar_widgets_base(base)
    cartelera.mostrar_peliculas(base)
