
def agregar_pelicula(base):
    pass
def editar_pelicula(base):
    pass
def eliminar_pelicula(base):
    pass

def insertar_peliculas_tree(treeview):
    from backend.database import obtener_peliculas_bd
    for pelicula in obtener_peliculas_bd():
        pelicula_id = pelicula[0]
        pelicula_titulo = pelicula[2]
        sinopsis_pelicula = pelicula[3]
        genero_pelicula = pelicula[4]
        horas = pelicula[5] // 60
        minutos = pelicula[5] % 60
        duracion_pelicula = f"{horas}h {minutos}m"
        estreno_pelicula = pelicula[6]
        votacion_pelicula = pelicula[7]
        ruta_imagen = pelicula[1]
        datos_pelicula = [pelicula_id, pelicula_titulo, sinopsis_pelicula, genero_pelicula, duracion_pelicula, estreno_pelicula, votacion_pelicula,ruta_imagen]
        print(pelicula)
        treeview.insert("", "end", values=datos_pelicula)
    
def volver(base):
    from frontend import cartelera
    from frontend.utils import limpiar_widgets_base
    
    limpiar_widgets_base(base)
    cartelera.mostrar_peliculas(base)
