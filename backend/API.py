import requests
import json

BASE_URL = "https://api.themoviedb.org/3"
IMAGEN_BASE_URL = "https://image.tmdb.org/t/p/original/"
IMAGEN_DEFAULT_URL = "https://www.publicdomainpictures.net/pictures/280000/velka/not-found-image-15383864787lu.jpg"


HEADERS = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI0MDE4NDJkMTJhYzgxZDFmN2Y3ZGE2YzQzNzEwYzgwZSIsInN1YiI6IjY2NmNkNDFiYzkyNjg4ZDhmYmNlMjNkNiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.svnAGa6VzB2wayS8IQ__rneq5TelmDvMJwg7vhCj0uA"
}

def hacer_consulta_api(endpoint: str, parametros: dict) -> json:
    """
    Realiza una solicitud al punto de conexión de la API con los parámetros dados y devuelve la respuesta como un objeto JSON.

    Args:
        endpoint (str): El punto de conexión de la API a consultar.
        parametros (Dict): Los parámetros a incluir en la solicitud.

    Returns:
        Dict: La respuesta JSON de la API.

    Raises:
        requests.exceptions.RequestException: Si la solicitud a la API falla.
    """
    url = f"{BASE_URL}/{endpoint}"
    try:
        respuesta = requests.get(url, headers=HEADERS, params=parametros)
        respuesta.raise_for_status()
        return respuesta.json()
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None

def obtener_peliculas(nombre: str) -> json:
    """
    Obtiene las películas que coinciden con el nombre dado o similitudes.

    Args:
        nombre (str): El nombre de la película a buscar.

    Returns:
        Dict: Un diccionario con la respuesta de la consulta a la API.
    """
    parametros = {"query": nombre, "language": "es-ES"}
    return hacer_consulta_api("search/movie", parametros)

def obtener_peliculas_mas_recientes() -> json:
    """
    Obtiene las películas más recientes desde una API externa.

    Returns:
        Un diccionario con la información de las películas más recientes.
    """
    parametros = {"language": "es-ES"}
    return hacer_consulta_api("movie/now_playing", parametros)

def obtener_datos_pelicula(pelicula_id: int) -> dict:
    """
    Obtiene los datos de una película a partir de su ID.

    Args:
        pelicula_id (int): El ID de la película.

    Returns:
        dict: Un diccionario con los datos de la película, incluyendo el ID, la ruta de la imagen,
              el título, la sinopsis, el género, la duración, la fecha de estreno y el promedio de votos.
              Si no se puede obtener los datos de la película, se retorna None.
    """
    
    respuesta_json = hacer_consulta_api(f"movie/{pelicula_id}", {"language": "es-ES"})
    if respuesta_json:
        poster_ruta = respuesta_json.get("poster_path")
        link_default_imagen = IMAGEN_BASE_URL + poster_ruta if poster_ruta else IMAGEN_DEFAULT_URL

        total_minutos = respuesta_json.get("runtime", 0)
        horas, minutos = divmod(total_minutos, 60)
        duracion = f"{horas}h {minutos}m" if horas > 0 else f"{minutos}m"

        datos = {
            "id": respuesta_json.get("id"),
            "ruta_imagen": link_default_imagen,
            "titulo": respuesta_json.get("title"),
            "sinopsis": respuesta_json.get("overview"),
            "genero": ", ".join(genero["name"] for genero in respuesta_json.get("genres", [])),
            "duracion": duracion,
            "estreno": respuesta_json.get("release_date"),
            "promedio_votos": respuesta_json.get("vote_average")
        }
        return datos
    else:
        print("Error al obtener detalles de la película")
        return None

def obtener_trailer(pelicula_id: int) -> str:
    """
    Obtiene el enlace del trailer de una película dado su ID.

    Args:
        pelicula_id (int): El ID de la película.

    Returns:
        str: El enlace del trailer de la película, o None si no se encuentra.

    """
    def hacer_consulta(pelicula_id: int, idioma: str):
        return hacer_consulta_api(f"movie/{pelicula_id}/videos", {"language": idioma})
    
    response_json = hacer_consulta(pelicula_id, "es-ES")
    if response_json:
        for video in response_json.get("results", []):
            if video.get("type") == "Trailer" and video.get("site") == "YouTube":
                return video.get("key")
    
    response_json = hacer_consulta(pelicula_id, "en-US")
    if response_json:
        for video in response_json.get("results", []):
            if video.get("type") == "Trailer" and video.get("site") == "YouTube":
                return video.get("key")
    return None
