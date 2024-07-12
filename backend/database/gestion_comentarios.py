from .utils_db import ejecutar_query_obtener, ejecutar_query_agregar,ejecutar_query_editar,ejecutar_query_eliminar

def obtener_comentarios_pelicula(pelicula_id:int):
    query = "SELECT * FROM comentarios WHERE pelicula_id = %s"
    return ejecutar_query_obtener(query, "comentarios",datos=(pelicula_id,))

def agregar_comentario_pelicula(pelicula_id:int,usuario_id:int,comentario:str):
    datos = (usuario_id,pelicula_id,comentario)
    query = "INSERT INTO comentarios (usuario_id,pelicula_id,comentario) VALUES (%s,%s,%s)"
    return ejecutar_query_agregar(query,datos,"comentarios")

def editar_comentario_pelicula(comentario_id:int,comentario:str):
    datos = (comentario,comentario_id)
    query = "UPDATE comentarios SET comentario = %s WHERE id = %s"
    return ejecutar_query_editar(query,datos,"comentarios")

def eliminar_comentario_pelicula(comentario_id:int):
    query = "DELETE FROM comentarios WHERE id = %s"
    return ejecutar_query_eliminar(query,comentario_id,"comentarios")