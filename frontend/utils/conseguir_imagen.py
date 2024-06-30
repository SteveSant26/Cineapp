from PIL import Image
import customtkinter as ctk

def conseguir_imagen_ctk(path_light: str, ancho: int, largo: int, path_dark: str = None) -> ctk.CTkImage:
    imagen_light = conseguir_imagen_local(path_light)
    if imagen_light is None:
        print(f"Error al cargar la imagen: {path_light}")
        return
    
    if path_dark:
        imagen_dark = conseguir_imagen_local(path_dark)
        if imagen_dark is None:
            print(f"Error al cargar la imagen del modo oscuro: {path_dark}")
        imagen_ctk = ctk.CTkImage(light_image=imagen_light, dark_image=imagen_dark, size=(ancho, largo))
    else:
        imagen_ctk = ctk.CTkImage(light_image=imagen_light, size=(ancho, largo))
    
    return imagen_ctk


def conseguir_imagen_local(path: str):
    """
    Función de ejemplo para conseguir una imagen local.
    Esta función debería estar definida en tu código.
    """
    try:
        return Image.open(path)
    except FileNotFoundError:
        print(f"Archivo no encontrado: {path}")
        return None
    except Exception as e:
        print(f"Error al abrir la imagen: {path} - {e}")
        return None








# Usando os.walk, que básicamente recorre un directorio y sus subdirectorios hasta encontrar el archivo
# def buscar_imagen_en_directorio(directorio: str, nombre_imagen: str) -> bool:

#     for root, _, files in os.walk(directorio):
#         print(files)
#         if nombre_imagen in files:
#             return True
#     return False






