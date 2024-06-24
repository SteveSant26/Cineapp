import requests
import pprint

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI0MDE4NDJkMTJhYzgxZDFmN2Y3ZGE2YzQzNzEwYzgwZSIsInN1YiI6IjY2NmNkNDFiYzkyNjg4ZDhmYmNlMjNkNiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.svnAGa6VzB2wayS8IQ__rneq5TelmDvMJwg7vhCj0uA"
}

def obtener_peliculas(nombre):
    parametros = {"query": nombre,
                  "language": "es-ES"}
    url = "https://api.themoviedb.org/3/search/movie"
    try:
        response = requests.get(url, headers=headers, params=parametros)
        if response.status_code == 200:
            pprint.pprint(response.json())
            return response.json()
        else:
            return None
    except requests.exceptions.RequestException as e:
        print(f"No se pudo obtener la pelicula: {e}")

def obtener_datos_pelicula(json):
    link_default_imagen = "https://image.tmdb.org/t/p/original/"
    datos = {
    "id" : json["results"][0]["id"],
    "ruta_imagen" : f"{link_default_imagen}{json["results"][0]["poster_path"]}",
    "titulo" : json["results"][0]["title"],
    "sinopsis" : json["results"][0]["overview"],
    "genero" : ", ".join([genero["name"] for genero in json["results"][0]["genres"]]),
    "duracion" : json["results"][0]["runtime"],
    "fecha_estreno" : json["results"][0]["release_date"],
    "promedio_votos" : json["results"][0]["vote_average"],
    }
    return datos

