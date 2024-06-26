
def agregar_pelicula(base):
    pass
def editar_pelicula(base):
    pass
def eliminar_pelicula(base):
    pass
def volver(base):
    from frontend import cartelera
    from frontend.utils import limpiar_widgets_base
    
    limpiar_widgets_base(base)
    cartelera.mostrar_peliculas(base)
