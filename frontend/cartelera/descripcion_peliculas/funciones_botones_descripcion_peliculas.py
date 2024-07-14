import webbrowser
import pyautogui
import time
import customtkinter as ctk

from backend.API import obtener_trailer
from frontend.utils import mostrar_mensaje, mostrar_error
from .utils_interfaz_descripcion_peliculas import actualizar_comentarios, limpiar_comentario

def ventana_agregar_comentario(base: ctk.CTk, id_pelicula: int, id_usuario: int) -> None:
    """
    Crea y muestra una ventana para agregar un comentario.

    Args:
        base (ctk.CTk): La ventana principal de la aplicación.
        id_pelicula (int): El ID de la película sobre la cual se quiere agregar un comentario.
        id_usuario (int): El ID del usuario que agrega el comentario.
    """
    ventana_agregar_comentario = ctk.CTkToplevel(base)
    ventana_agregar_comentario.title("Agregar comentario")
    ventana_agregar_comentario.geometry("500x300")
    ventana_agregar_comentario.resizable(False, False)
    ventana_agregar_comentario.transient(base)

    comentario_label = ctk.CTkLabel(ventana_agregar_comentario, text="Escribe tu comentario:", font=("Arial", 20))
    comentario_label.pack(pady=10, padx=10)
    comentario_entry = ctk.CTkTextbox(ventana_agregar_comentario, font=("Arial", 20), wrap="word", height=150)
    comentario_entry.pack(pady=10, padx=10, expand=True, fill="x")

    boton_agregar = ctk.CTkButton(ventana_agregar_comentario, 
                                  text="Agregar",
                                  hover_color="#31AF9C",
                                  fg_color="#329ADF",
                                  font=("Arial", 20), 
                                  command=lambda: agregar_comentario(base, ventana_agregar_comentario, id_pelicula, id_usuario, limpiar_comentario(comentario_entry.get(1.0, "end"))))
    boton_agregar.pack(pady=10, padx=10, expand=True)

def agregar_comentario(base: ctk.CTk, ventana_comentario: ctk.CTkToplevel, id_pelicula: int, id_usuario: int, comentario: str) -> None:
    """
    Agrega un nuevo comentario a la base de datos y actualiza la interfaz.

    Args:
        base (ctk.CTk): La ventana principal de la aplicación.
        ventana_comentario (ctk.CTkToplevel): La ventana donde se agrega el comentario.
        id_pelicula (int): El ID de la película sobre la cual se agrega el comentario.
        id_usuario (int): El ID del usuario que agrega el comentario.
        comentario (str): El texto del comentario.
    """
    from backend.database import agregar_comentario_pelicula
    try:
        agregar_comentario_pelicula(id_pelicula, id_usuario, comentario)
        ventana_comentario.destroy()
        actualizar_comentarios(base, id_pelicula)
        mostrar_mensaje("Comentario agregado", "Comentario agregado con éxito")
    except Exception as e:
        print(f"Error al guardar el comentario: {e}")

def reproducir_trailer(id_pelicula: int) -> None:
    """
    Reproduce el trailer de una película en un navegador web.

    Args:
        id_pelicula (int): El ID de la película cuyo trailer se quiere reproducir.
    """
    trailer = obtener_trailer(id_pelicula)
    print(trailer)
    try:
        if trailer:
            ruta_trailer = f"https://www.youtube.com/embed/{trailer}?autoplay=1"
            html_content = f"""
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Reproductor de Trailer</title>
                <style>
                    body, html {{
                        margin: 0;
                        padding: 0;
                        width: 100%;
                        height: 100%;
                        overflow: hidden;
                    }}
                    .video-container {{
                        position: absolute;
                        top: 0;
                        left: 0;
                        width: 100%;
                        height: 100%;
                    }}
                    iframe {{
                        width: 100%;
                        height: 100%;
                    }}
                </style>
            </head>
            <body>
                <div class="video-container">
                    <iframe id="video" src="{ruta_trailer}" frameborder="0" allow="autoplay" allowfullscreen></iframe>
                </div>
            </body>
            </html>
            """

            with open("frontend\\cartelera\\plantilla_trailer.html", "w", encoding="utf-8") as file:
                file.write(html_content)
            webbrowser.open_new("frontend\\cartelera\\plantilla_trailer.html")

            time.sleep(2)
            pyautogui.press('f')
        else:
            mostrar_error("Trailer no disponible", "El trailer de esta película no está disponible")
    except Exception as e:
        print(f"Error al abrir el navegador para reproducir el trailer: {e}")








# def reproducir_trailer(id_pelicula: int):
#     trailer = obtener_trailer(id_pelicula)
#     print(trailer)
#     try:
#         if trailer:
#             webbrowser.open_new_tab(f"https://www.youtube.com/watch?v={trailer}")
#     except Exception as e:
#         print(f"Error al abrir el navegador para reproducir el trailer: {e}")