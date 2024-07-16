from backend.database import ejecutar_query_obtener
def obtener_todos_generos_bd() -> list:
    """
    Obtiene todos los géneros de la base de datos.

    Returns:
        list: Una lista con los géneros de la base de datos.
    """
    query = "SELECT DISTINCT genero FROM peliculas"
    return ejecutar_query_obtener(query, "peliculas")

def obtener_todos_generos() -> list:
    listas_generos = obtener_todos_generos_bd()
    todos_generos = set()
    for generos in listas_generos:
        for genero in generos[0].split(","):
            todos_generos.add(genero.strip())
            

        
    return list(generos)

# print(obtener_todos_generos())