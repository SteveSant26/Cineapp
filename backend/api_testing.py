import requests 

def conseguir_datos_peliculas(response_json):
    datos = {
    "id" : response_json["id"],
    "ruta_imagen" : response_json["poster_path"],
    "titulo": response_json["title"],
    "sinopsis":response_json["overview"],
    "genero": ", ".join([genero["name"] for genero in response_json["genres"]]),
    "duracion":response_json["runtime"],
    "estreno":response_json["release_date"],
    "promedio_votos":response_json["vote_average"]}
    return datos


movie_id = 150540

url = f"https://api.themoviedb.org/3/movie/{movie_id}"

parametros = {
    "language": "es-ES"
}

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI0MDE4NDJkMTJhYzgxZDFmN2Y3ZGE2YzQzNzEwYzgwZSIsInN1YiI6IjY2NmNkNDFiYzkyNjg4ZDhmYmNlMjNkNiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.svnAGa6VzB2wayS8IQ__rneq5TelmDvMJwg7vhCj0uA"
}

response = requests.get(url, headers=headers,params=parametros)
response_json = response.json()

for value in conseguir_datos_peliculas(response_json).values():
    print(value)
    print("\n")



