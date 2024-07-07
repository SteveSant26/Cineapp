from .utils_db import ejecutar_query_obtener,ejecutar_query_agregar,ejecutar_query_editar,ejecutar_query_eliminar

def obtener_salas_bd():
    query = "SELECT * FROM salas"
    return ejecutar_query_obtener(query, "salas")

def agregar_sala_bd(datos_sala: tuple):
    query = "INSERT INTO salas (nombre, filas, columnas) VALUES (%s, %s, %s)"
    return ejecutar_query_agregar(query, datos_sala, "salas")

def editar_sala_bd(datos_sala: tuple):
    query = "UPDATE salas SET nombre = %s, filas = %s, columnas = %s WHERE id = %s"
    return ejecutar_query_editar(query, datos_sala, "salas")

def eliminar_sala_bd(id_sala: int):
    query = "DELETE FROM salas WHERE id = %s"
    return ejecutar_query_eliminar(query, id_sala, "salas")