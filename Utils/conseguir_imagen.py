import customtkinter as ctk
from PIL import Image


def conseguir_imagen_local(path: str) -> Image.Image:
    """Obtiene una imagen local a partir de un path.

    Args:
        path (str): La ruta de la imagen local.

    Returns:
        Image.Image: El objeto de imagen correspondiente.

    Raises:
        IOError: Si ocurre un error al acceder al path.

    """
    try:
        return Image.open(path)
    except IOError as e:
        print(f"Error al acceder al path {path}: {e}")
        return None


def conseguir_imagen_ctk(path_light: str, ancho: int, largo: int,path_dark: str = None) -> ctk.CTkImage:
    """
    Convierte una imagen en un objeto de la clase CTkImage compatible con modos claro y oscuro.
    
    Args:
        path_light (str): La ruta de la imagen para el modo claro.
        ancho (int): El ancho de la imagen.
        largo (int): El largo de la imagen.
        path_dark (str, optional): La ruta de la imagen para el modo oscuro.

    Returns:
        ctk.CTkImage: El objeto CTkImage correspondiente.
    """
    
    imagen_light = conseguir_imagen_local(path_light)
    
    if path_dark:
        imagen_dark = conseguir_imagen_local(path_dark)
        imagen_ctk = ctk.CTkImage(light_image=imagen_light, dark_image=imagen_dark, size=(ancho, largo))
    else:
        imagen_ctk = ctk.CTkImage(light_image=imagen_light, size=(ancho, largo))
    
    return imagen_ctk