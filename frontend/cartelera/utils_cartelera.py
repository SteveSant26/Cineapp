from frontend.utils import conseguir_imagen_local
import os
import re
import requests
from PIL import Image
from io import BytesIO
import customtkinter as ctk

def corregir_nombre_archivo(filename: str) -> str:
    """
    Replace or remove characters that are invalid in filenames.
    """
    return re.sub(r'[<>:"/\\|?*]', '', filename)

def conseguir_imagen_portada_ctk(directorio: str, id_pelicula, titulo_pelicula, ancho: int, largo: str) -> ctk.CTkImage:
    from backend.database import obtener_imagen_pelicula_por_id

    titulo_pelicula_sanitized = corregir_nombre_archivo(titulo_pelicula)
    archivo_png = f"{titulo_pelicula_sanitized}.png"
    ruta_local_imagen = os.path.join(directorio, archivo_png)
    
    portada = conseguir_imagen_local(ruta_local_imagen)
    
    if portada is None:
        print(f"Error al cargar la imagen: {directorio}")
        
        link_imagen = obtener_imagen_pelicula_por_id(id_pelicula)
        nueva_ruta = descargar_imagen(link_imagen, directorio, archivo_png)
        
        portada = conseguir_imagen_local(nueva_ruta)
    
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
        pass
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
