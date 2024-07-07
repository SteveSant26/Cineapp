from backend.database import ejecutar_query_obtener

def obtener_id_nombre_sala_bd():
    query = "SELECT id, nombre FROM salas"
    return ejecutar_query_obtener(query,"salas")

def obtener_nombre_sala_por_id(id_sala: int):
    query = "SELECT nombre FROM salas WHERE id = %s"
    return ejecutar_query_obtener(query, "salas", datos =(id_sala,))


def obtener_titulo_pelicula_por_id(id_pelicula: int):
    query = "SELECT titulo FROM peliculas WHERE id = %s"
    return ejecutar_query_obtener(query, "peliculas", datos=(id_pelicula,))


