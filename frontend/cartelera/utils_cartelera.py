import os
import re
import requests
from PIL import Image
from io import BytesIO
import customtkinter as ctk


from backend.database import ejecutar_query_obtener
from frontend.utils import conseguir_imagen_local

def obtener_id_titulo_pelicula_bd() -> list:
    """
    Obtiene el id y el título de las películas desde la base de datos.

    Retorna:
        Una lista de tuplas que contiene el id y el título de las películas.
    """
    query = "SELECT id, titulo FROM peliculas"
    return ejecutar_query_obtener(query,"peliculas")

def obtener_imagen_pelicula_por_id(id_pelicula: int) -> str:
    """
    Obtiene la ruta de la imagen de una película dado su ID.

    Args:
        id_pelicula (int): El ID de la película.

    Returns:
        str: La ruta de la imagen de la película.
    """
    query = "SELECT ruta_imagen FROM peliculas WHERE id = %s"
    return ejecutar_query_obtener(query, "peliculas", datos=(id_pelicula,))[0][0]


def corregir_nombre_archivo(filename: str) -> str:
    """
    Elimina los caracteres inválidos del nombre de archivo proporcionado.

    Args:
        filename (str): El nombre de archivo a corregir.

    Returns:
        str: El nombre de archivo corregido con los caracteres inválidos eliminados.
    """
    return re.sub(r'[<>:"/\\|?*]', '', filename)

def conseguir_imagen_portada_ctk(directorio: str, id_pelicula:int, titulo_pelicula:str, ancho: int, largo: int) -> ctk.CTkImage:
    """
    Obtiene la imagen de portada de una película en formato CTkImage.

    Args:
        directorio (str): El directorio donde se encuentra la imagen.
        id_pelicula (int): El ID de la película.
        titulo_pelicula (str): El título de la película.
        ancho (int): El ancho de la imagen CTkImage.
        largo (int): El alto de la imagen CTkImage.

    Returns:
        ctk.CTkImage: La imagen de portada de la película en formato CTkImage.
    """
    
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
    """
    Busca de forma recursiva un archivo de imagen en un directorio y sus subdirectorios.

    Args:
        directorio (str): El directorio desde donde comenzar la búsqueda.
        archivo_png (str): El nombre del archivo de imagen a buscar.

    Returns:
        bool: True si se encuentra el archivo de imagen, False en caso contrario.
    """
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
    """
    Descarga una imagen desde una URL y la guarda en un directorio de destino.

    Args:
        url (str): La URL de la imagen a descargar.
        directorio_destino (str): El directorio donde se guardará la imagen descargada.
        archivo_png (str): El nombre del archivo de imagen a guardar.

    Returns:
        str: La ruta completa del archivo de imagen descargado.
    """
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