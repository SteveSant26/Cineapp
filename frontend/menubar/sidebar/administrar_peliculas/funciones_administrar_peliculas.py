import backend.database as DB
from frontend.utils import mostrar_error, mostrar_mensaje, limpiar_widgets_base


def conseguir_datos_pelicula(base):
    id = base.entries_pelicula["id"].get()
    titulo = base.entries_pelicula["titulo"].get()
    sinopsis = base.entries_pelicula["sinopsis"].get("1.0", "end-1c") 
    genero = base.entries_pelicula["genero"].get()
    duracion = base.entries_pelicula["duracion"].get()
    estreno = base.entries_pelicula["estreno"].get()
    prom_votos = base.entries_pelicula["prom_votos"].get()
    ruta_imagen = base.entries_pelicula["ruta_imagen"].get()

    if not (id and titulo and duracion and estreno and ruta_imagen):
        mostrar_error("Error de Validación", "Todos los campos obligatorios deben estar llenos.")
        return
    datos = (ruta_imagen, titulo, sinopsis, genero, duracion, estreno, prom_votos, int(id))
    return datos

def editar_pelicula(base):
    try:
        datos = conseguir_datos_pelicula(base)
        
        # Editar la película en la base de datos
        if DB.editar_pelicula_bd(datos):
            mostrar_mensaje("Película Editada", "La película ha sido editada correctamente.")
            insertar_peliculas_tree(base.tree_peliculas)
        else:
            mostrar_error("Error al Editar Película", "No se pudo editar la película.")
    except Exception as e:
        mostrar_error("Error", f"Se produjo un error: {e}")
    
def eliminar_pelicula(base):
    id = base.entries_pelicula["id"].get()
    if not id:
        mostrar_error("Error de Validación", "El campo ID es obligatorio")
        return
    if DB.eliminar_pelicula_bd(id):
        mostrar_mensaje("Película Eliminada", "La película ha sido eliminada correctamente.")
        insertar_peliculas_tree(base.tree_peliculas)
    

def insertar_peliculas_tree(treeview):
    from ..utils import limpiar_treeview
    limpiar_treeview(treeview)
    for pelicula in DB.obtener_peliculas_bd():
        pelicula_id = pelicula[0]
        pelicula_titulo = pelicula[2]
        sinopsis_pelicula = pelicula[3]
        genero_pelicula = pelicula[4]
        duracion_pelicula = pelicula[5]
        estreno_pelicula = pelicula[6]
        votacion_pelicula = pelicula[7]
        ruta_imagen = pelicula[1]
        datos_pelicula = [pelicula_id, pelicula_titulo, sinopsis_pelicula, genero_pelicula, duracion_pelicula, estreno_pelicula, votacion_pelicula,ruta_imagen]
        treeview.insert("", "end", values=datos_pelicula)
    
def volver(base):
    from frontend import cartelera
    
    limpiar_widgets_base(base)
    cartelera.mostrar_peliculas(base)
