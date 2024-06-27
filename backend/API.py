import requests

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI0MDE4NDJkMTJhYzgxZDFmN2Y3ZGE2YzQzNzEwYzgwZSIsInN1YiI6IjY2NmNkNDFiYzkyNjg4ZDhmYmNlMjNkNiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.svnAGa6VzB2wayS8IQ__rneq5TelmDvMJwg7vhCj0uA"
}

def obtener_peliculas(nombre):
    parametros = {"query": nombre, "language": "es-ES"}
    url = "https://api.themoviedb.org/3/search/movie"
    try:
        response = requests.get(url, headers=headers, params=parametros)
        
        if response.status_code == 200:
            # pprint.(response.json())
            return response.json()
        else:
            print(f"Error: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"No se pudo obtener la película: {e}")
        return None
    
def obtener_peliculas_mas_recientes():
    url = "https://api.themoviedb.org/3/movie/now_playing"
    parametros = {"language": "es-ES"}
    try:
        response = requests.get(url, headers=headers, params=parametros)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error al obtener las películas más recientes: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"No se pudieron obtener las películas más recientes: {e}")
        return None
    
def obtener_datos_pelicula(pelicula_id):
    url = f"https://api.themoviedb.org/3/movie/{pelicula_id}"
    parametros = {"language": "es-ES"}

    try:
        response = requests.get(url, headers=headers, params=parametros)
        if response.status_code == 200:
            response_json = response.json()
            link_default_imagen = "https://image.tmdb.org/t/p/original/"
            if not response_json.get("poster_path"):
                link_default_imagen = "https://www.publicdomainpictures.net/pictures/280000/velka/not-found-image-15383864787lu.jpg"
            else:
                link_default_imagen += response_json.get("poster_path")
                
            duracion_total_minutos = response_json.get("runtime", 0)
            duracion_horas = duracion_total_minutos // 60
            duracion_minutos = duracion_total_minutos % 60
            duracion = f"{duracion_horas}h {duracion_minutos}m" if duracion_horas > 0 else f"{duracion_minutos}m"
            datos = {
                "id": response_json.get("id"),
                "ruta_imagen": link_default_imagen,
                "titulo": response_json.get("title"),
                "sinopsis": response_json.get("overview"),
                "genero": ", ".join([genero["name"] for genero in response_json.get("genres", [])]),
                "duracion": duracion,
                "estreno": response_json.get("release_date"),
                "promedio_votos": response_json.get("vote_average")
            }
            return datos
        else:
            print(f"Error al obtener detalles de la película: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"No se pudieron obtener los detalles de la película: {e}")
        return None


# respuesta = obtener_peliculas("Dragon Ball")
# # if respuesta:
# #     for value in respuesta.get("results", []):
# #         datos_pelicula = obtener_datos_pelicula(value["id"])
# #         if datos_pelicula:
# #             pprint.pprint(datos_pelicula)
            
# datos_pelicula = obtener_datos_pelicula(respuesta["results"][0]["id"])

# pprint.pprint(datos_pelicula)