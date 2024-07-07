from backend.database import ejecutar_query_obtener

def obtener_sala_id_en_funciones_por_pelicula_id_bd(id_pelicula: int):
    query = "SELECT sala_id FROM funciones where pelicula_id = %s"
    return ejecutar_query_obtener(query, "funciones",datos=(id_pelicula,))

def obtener_nombre_sala_por_id_bd(id_sala: int):
    query = "SELECT nombre FROM salas WHERE id = %s"
    return ejecutar_query_obtener(query, "salas", datos =(id_sala,))


def obtener_sala_id_por_nombre_bd(nombre_sala: str):
    query = "SELECT id FROM salas WHERE nombre = %s"
    return ejecutar_query_obtener(query, "salas", datos=(nombre_sala,))

def obtener_salas(id_pelicula: int):
    ids_salas = sorted([i[0] for i in set(obtener_sala_id_en_funciones_por_pelicula_id_bd(id_pelicula))])
    return [obtener_nombre_sala_por_id_bd(id_sala)[0][0] for id_sala in ids_salas]

def obtener_funciones_misma_pelicula(id_pelicula: int,nombre_Sala: int):
    id_sala = obtener_sala_id_por_nombre_bd(nombre_Sala)[0][0]
    query = "SELECT hora,id FROM funciones where pelicula_id = %s and sala_id = %s"
    return ejecutar_query_obtener(query, "funciones", datos=(id_pelicula,id_sala))

def obtener_funciones(id_pelicula: int,nombre_Sala: int):
    fecha  = [str(i[0]) for i in obtener_funciones_misma_pelicula(id_pelicula,nombre_Sala)]
    return sorted(fecha)


def obtener_funcion_id_por_sala_pelicula_id(sala_id: int, pelicula_id: int,hora:str):
    query = "SELECT id FROM funciones WHERE sala_id = %s and pelicula_id = %s and hora = %s"
    return ejecutar_query_obtener(query, "funciones", datos=(sala_id, pelicula_id,hora))[0][0]


def conseguir_tamano_sala_por_nombre_bd(nombre_sala: int):
    query = "SELECT filas,columnas FROM salas WHERE nombre = %s"
    return ejecutar_query_obtener(query, "salas", datos=(nombre_sala,))

def obtener_tamano_sala(nombre_sala: str):
    filas,columnas = conseguir_tamano_sala_por_nombre_bd(nombre_sala)[0]
    return filas,columnas