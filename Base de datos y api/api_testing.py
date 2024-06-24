import requests 
import json
import tkinter as tk
from PIL import Image, ImageTk 
from io import BytesIO 
movie_id = 150540
url = f"https://api.themoviedb.org/3/movie/{movie_id}"



headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI0MDE4NDJkMTJhYzgxZDFmN2Y3ZGE2YzQzNzEwYzgwZSIsInN1YiI6IjY2NmNkNDFiYzkyNjg4ZDhmYmNlMjNkNiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.svnAGa6VzB2wayS8IQ__rneq5TelmDvMJwg7vhCj0uA"
}

response = requests.get(url, headers=headers)
response = json.loads(response.text)
print(json.dumps(response, indent=4))
print()
print(response['overview'])

imagen_path = response['poster_path']
print(imagen_path)

def conseguir_imagen(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return Image.open(BytesIO(response.content))
    except requests.RequestException as e:
        print(f"Error al acceder al url {url}: {e}")
        return None
imagen = conseguir_imagen(f"https://image.tmdb.org/t/p/w500{imagen_path}")

window = tk.Tk()
window.title("Movie")

image = ImageTk.PhotoImage(imagen)
label = tk.Label(window, image=image)

label.pack()
window.mainloop()