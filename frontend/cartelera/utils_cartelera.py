from frontend.utils import conseguir_imagen_local
import os
import re
import requests
from PIL import Image
from io import BytesIO
import customtkinter as ctk
from backend.database import ejecutar_query_obtener

def obtener_id_titulo_pelicula_bd():
    query = "SELECT id, titulo FROM peliculas"
    return ejecutar_query_obtener(query,"peliculas")

def obtener_imagen_pelicula_por_id(id_pelicula: int):
    query = "SELECT ruta_imagen FROM peliculas WHERE id = %s"
    return ejecutar_query_obtener(query, "peliculas", datos=(id_pelicula,))[0][0]

def corregir_nombre_archivo(filename: str) -> str:
    """
    Replace or remove characters that are invalid in filenames.
    """
    return re.sub(r'[<>:"/\\|?*]', '', filename)

def conseguir_imagen_portada_ctk(directorio: str, id_pelicula, titulo_pelicula, ancho: int, largo: int) -> ctk.CTkImage:
    titulo_pelicula_sanitized = corregir_nombre_archivo(titulo_pelicula)
    archivo_png = f"{titulo_pelicula_sanitized}.png"
    ruta_local_imagen = os.path.join(directorio, archivo_png)
    
    portada = conseguir_imagen_local(ruta_local_imagen)
    
    if portada is None:
        print(f"Error al cargar la imagen: {ruta_local_imagen}")
        
        link_imagen = obtener_imagen_pelicula_por_id(id_pelicula)

        nueva_ruta = descargar_imagen(link_imagen, directorio, archivo_png)
        
        portada = conseguir_imagen_local(nueva_ruta)
    
    if portada is None:
        portada = conseguir_imagen_local("frontend\\cartelera\\portadas_peliculas\\not_found_img.jpg")
    
    portada_ctk = ctk.CTkImage(light_image=portada, size=(ancho, largo))
    return portada_ctk

def buscar_imagen_recursivamente(directorio: str, archivo_png: str) -> bool:
    try:
        archivos_directorios = os.listdir(directorio)
        for archivo_dir in archivos_directorios:
            path = os.path.join(directorio, archivo_dir)
            if os.path.isdir(path):
                if buscar_imagen_recursivamente(path, archivo_png):
                    return True
            elif os.path.isfile(path) and archivo_dir == archivo_png:
                return True
    except PermissionError:
        print(f"Error de permisos al buscar la imagen: {archivo_png}")
        return False

def descargar_imagen(url: str, directorio_destino: str, archivo_png: str) -> str:
    if not os.path.exists(directorio_destino):
        os.makedirs(directorio_destino)

    if buscar_imagen_recursivamente(directorio_destino, archivo_png):
        return os.path.join(directorio_destino, archivo_png)
    
    ruta_archivo_png = os.path.join(directorio_destino, archivo_png)
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()

        imagen = Image.open(BytesIO(response.content))
        imagen.save(ruta_archivo_png, format='PNG')

        return ruta_archivo_png
    except requests.RequestException as e:
        print(f"Error al descargar la imagen desde URL: {url} - {e}")
        return None

