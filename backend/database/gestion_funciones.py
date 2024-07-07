from .utils_db import ejecutar_query_obtener, ejecutar_query_agregar, ejecutar_query_editar,ejecutar_query_eliminar

def obtener_funciones_bd():
    query = "SELECT * FROM funciones"
    return ejecutar_query_obtener(query, "funciones")

def agregar_funcion_bd(datos_funcion: tuple):
    query = "INSERT INTO funciones (pelicula_id, sala_id, hora) VALUES (%s, %s, %s)"
    return ejecutar_query_agregar(query, datos_funcion, "funciones")


def editar_funcion_bd(datos_funcion: tuple):
    query = "UPDATE funciones SET pelicula_id = %s, sala_id = %s, hora = %s WHERE id = %s"
    return ejecutar_query_editar(query, datos_funcion, "funciones")

def eliminar_funcion_bd(id_funcion: int):
    query = "DELETE FROM funciones WHERE id = %s"
    return ejecutar_query_eliminar(query, id_funcion, "funciones")
