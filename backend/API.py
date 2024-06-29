import requests
from typing import Dict, Any, List
from concurrent.futures import ThreadPoolExecutor, as_completed

BASE_URL = "https://api.themoviedb.org/3"
IMAGE_BASE_URL = "https://image.tmdb.org/t/p/original/"
DEFAULT_IMAGE_URL = "https://www.publicdomainpictures.net/pictures/280000/velka/not-found-image-15383864787lu.jpg"
HEADERS = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI0MDE4NDJkMTJhYzgxZDFmN2Y3ZGE2YzQzNzEwYzgwZSIsInN1YiI6IjY2NmNkNDFiYzkyNjg4ZDhmYmNlMjNkNiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.svnAGa6VzB2wayS8IQ__rneq5TelmDvMJwg7vhCj0uA"
}

def hacer_consulta_api(endpoint: str, parametros: Dict) -> Dict:
    url = f"{BASE_URL}/{endpoint}"
    try:
        response = requests.get(url, headers=HEADERS, params=parametros)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None

def obtener_peliculas(nombre: str) -> Dict:
    parametros = {"query": nombre, "language": "es-ES"}
    return hacer_consulta_api("search/movie", parametros)

def obtener_peliculas_mas_recientes() -> Dict:
    parametros = {"language": "es-ES"}
    return hacer_consulta_api("movie/now_playing", parametros)

def obtener_datos_pelicula(pelicula_id: int) -> Dict:
    response_json = hacer_consulta_api(f"movie/{pelicula_id}", {"language": "es-ES"})
    if response_json:
        poster_path = response_json.get("poster_path")
        link_default_imagen = IMAGE_BASE_URL + poster_path if poster_path else DEFAULT_IMAGE_URL

        total_minutos = response_json.get("runtime", 0)
        horas, minutos = divmod(total_minutos, 60)
        duracion = f"{horas}h {minutos}m" if horas > 0 else f"{minutos}m"

        datos = {
            "id": response_json.get("id"),
            "ruta_imagen": link_default_imagen,
            "titulo": response_json.get("title"),
            "sinopsis": response_json.get("overview"),
            "genero": ", ".join(genero["name"] for genero in response_json.get("genres", [])),
            "duracion": duracion,
            "estreno": response_json.get("release_date"),
            "promedio_votos": response_json.get("vote_average")
        }
        return datos
    else:
        print("Error al obtener detalles de la película")
        return None
