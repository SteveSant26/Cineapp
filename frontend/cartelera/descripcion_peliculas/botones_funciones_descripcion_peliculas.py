import customtkinter as ctk 
from backend.database import obtener_comentarios_pelicula
from backend.API import obtener_trailer
import webbrowser
import pyautogui
import time
from .. import interfaz_cartelera as IC
from frontend import pantalla_cine as PC
from . utils_interfaz_descripcion_peliculas import obtener_usuario_por_id, agregar_separador


def boton_reservar_asientos(base,frame_botones):
    boton_reservar_asientos = ctk.CTkButton(frame_botones, 
                                            text="Reservar asientos",
                                            hover_color="#31AF9C",
                                            fg_color="#329ADF",
                                            height=40,
                                            font=("Arial", 20), 
                                            command=lambda: PC.crear_vista_cine(base))
    boton_reservar_asientos.grid(row=0, column=0, padx=10)

def boton_ver_trailer(frame_botones, id_pelicula: int):
    boton_ver_trailer = ctk.CTkButton(frame_botones, 
                                            text="Ver trailer",
                                            hover_color="#31AF9C",
                                            fg_color="#329ADF",
                                            height=40,
                                            font=("Arial", 20), 
                                            command=lambda: reproducir_trailer(id_pelicula))
    boton_ver_trailer.grid(row=0, column=1, padx=10)
def boton_agregar_comentario(frame_botones,id_pelicula,usuario_id):
    boton_agregar_comentario = ctk.CTkButton(frame_botones, 
                                            text="Agregar comentario",
                                            hover_color="#31AF9C",
                                            fg_color="#329ADF",
                                            height=40,
                                            font=("Arial", 20), 
                                            command=lambda: agregar_comentario(id_pelicula,usuario_id))
    boton_agregar_comentario.grid(row=0, column=2, padx=10)

def boton_salir(base,frame_botones):
    boton_salir = ctk.CTkButton(frame_botones, 
                                text="Salir",
                                hover_color="#31AF9C",
                                fg_color="#329ADF",
                                height=40,
                                font=("Arial", 20), 
                                command=lambda: IC.iniciar_hilo_mostrar_peliculas(base))
    boton_salir.grid(row=0, column=3, padx=10)

def crear_comentario(frame_comentarios, nombre_usuario, comentario):
    agregar_separador(frame_comentarios)
    frame_comentario = ctk.CTkFrame(frame_comentarios)
    frame_comentario.pack(anchor="w")
    
    comentario = ctk.CTkLabel(frame_comentario, text=comentario, font=("Arial", 20), wraplength=1000, justify="left")
    comentario.grid(row=0, column=0, pady=10, padx=10, sticky="w")
    
    frame_usuario = ctk.CTkFrame(frame_comentario, fg_color="transparent")
    frame_usuario.grid(row=1, column=0, padx=10, sticky="w")
    
    usuario = ctk.CTkLabel(frame_usuario, text=f"Usuario:", font=("Arial", 20,"bold"), wraplength=1000, justify="left")
    usuario.grid(row=0, column=0, padx=10, sticky="w")
    
    nom_usuario = ctk.CTkLabel(frame_usuario, text=nombre_usuario, font=("Arial", 20), wraplength=1000, justify="left")
    nom_usuario.grid(row=0, column=1, padx=10, sticky="w")

def crear_comentarios(frame_descripcion_pelicula, id_pelicula: int):
    comentarios = obtener_comentarios_pelicula(id_pelicula)

    
    for comentario in comentarios:
        usuario_id = comentario[1]
        nombre_usuario = obtener_usuario_por_id(usuario_id)[0][0]
        comentario = comentario[3]

        crear_comentario(frame_descripcion_pelicula, nombre_usuario, comentario)



def agregar_comentario(id_pelicula: int, id_usuario: int):
    pass

def reproducir_trailer(id_pelicula: int):
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

            with open("frontend\\cartelera\\platilla_trailer.html", "w", encoding="utf-8") as file:
                file.write(html_content)
            webbrowser.open_new("frontend\\cartelera\\platilla_trailer.html")

            # Esperar un momento para asegurarse de que el navegador abra la página
            time.sleep(2)
            pyautogui.press('f')
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