import customtkinter as ctk
from tkinter import ttk
from frontend.utils import mostrar_error, mostrar_mensaje
from backend import API
import threading

# Variable global para almacenar el temporizador
consulta_temporizador = None

def crear_ventana_agregar_pelicula(base):
    global ventana_agregar_pelicula_abierta

    ventana_agregar_pelicula_abierta = True

    ventana_agregar_pelicula = ctk.CTkToplevel(base)
    ventana_agregar_pelicula.title("Agregar Pelicula")
    
    ventana_agregar_pelicula.geometry("1400x500")
    ventana_agregar_pelicula.resizable(False, False)
    ventana_agregar_pelicula.transient(base)
    
    frame_opciones_agregar_pelicula(ventana_agregar_pelicula,base)
    tree_agregar_pelicula(ventana_agregar_pelicula, base)

def frame_opciones_agregar_pelicula(ventana_agregar_pelicula,base):
    frame_opciones = ctk.CTkFrame(ventana_agregar_pelicula, border_color="black", fg_color="transparent")
    frame_opciones.pack(side="top", expand=True)

    label_nombre = ctk.CTkLabel(frame_opciones, text="Ingrese el nombre de la pelicula:", font=("Arial", 16))
    label_nombre.grid(row=0, column=0, pady=10, padx=10, sticky="w")
    
    entry_nombre = ctk.CTkEntry(frame_opciones, font=("Arial", 16), width=300)
    entry_nombre.grid(row=0, column=1, pady=10, padx=10, sticky="w")
    
    entry_nombre.bind("<KeyRelease>", lambda event: iniciar_temporizador(entry_nombre.get(), ventana_agregar_pelicula))
    
    boton_agregar = ctk.CTkButton(frame_opciones, text="Agregar", fg_color="#329ADF", hover_color="#31AF9C", font=("Arial", 16), command=lambda: agregar_pelicula(ventana_agregar_pelicula,base))
    boton_agregar.grid(row=0, column=2, pady=10, padx=10, sticky="w")
    
    boton_agregar = ctk.CTkButton(frame_opciones, text="Mostrar peliculas mas recientes", fg_color="#329ADF", hover_color="#31AF9C", font=("Arial", 16), command=lambda: peliculas_mas_recientes(ventana_agregar_pelicula,base))
    boton_agregar.grid(row=0, column=3, pady=10, padx=10, sticky="w")

    boton_cancelar = ctk.CTkButton(frame_opciones, text="Cancelar", fg_color="#329ADF", hover_color="#31AF9C", font=("Arial", 16), command=lambda: ventana_agregar_pelicula.destroy())
    boton_cancelar.grid(row=0, column=4, pady=10, padx=10, sticky="w")

def tree_agregar_pelicula(ventana_agregar_pelicula, base):
    frame_tree = ctk.CTkFrame(ventana_agregar_pelicula, border_color="black", border_width=2, width=800)
    frame_tree.pack(fill="both", expand=True, side="bottom")

    columnas_nombres = [key.capitalize() for key in base.entries_pelicula.keys() if key != "ruta_imagen"]

    tree = ttk.Treeview(frame_tree, columns=columnas_nombres, show="headings")

    ancho_columnas = {
        "Id": 50,
        "Titulo": 200,
        "Sinopsis": 300,
        "Duracion": 75,
        "Genero": 50,
        "Estreno": 75,
    }

    for columna in columnas_nombres:
        tree.heading(columna, text=columna)
        tree.column(columna, width=ancho_columnas.get(columna, 100), anchor="center")

    tree.pack(fill="both", expand=True, padx=10, pady=10)
    tree.pack_propagate(False)
    
    
    ventana_agregar_pelicula.tree = tree


def iniciar_temporizador(entry_result, ventana_agregar_pelicula):
    global consulta_temporizador

    if consulta_temporizador:
        consulta_temporizador.cancel()

    consulta_temporizador = threading.Timer(0.2, lambda: actualizar_treeview(ventana_agregar_pelicula, entry_result))
    consulta_temporizador.start()

def actualizar_treeview(ventana_agregar_pelicula, entry_result):
    if entry_result.strip():
        respuesta = API.obtener_peliculas(entry_result)
        if respuesta:
            peliculas = []
            for value in respuesta.get("results", []):
                datos_pelicula = API.obtener_datos_pelicula(value["id"])
                if datos_pelicula:
                    peliculas.append(datos_pelicula)
            # Actualizar Treeview en el hilo principal
            ventana_agregar_pelicula.after(0, insertar_peliculas_tree_agregar, ventana_agregar_pelicula.tree, peliculas)

def peliculas_mas_recientes(ventana_agregar_pelicula,base):
    respuesta = API.obtener_peliculas_mas_recientes()
    if respuesta:
        peliculas = []
        for value in respuesta.get("results", []):
            datos_pelicula = API.obtener_datos_pelicula(value["id"])
            if datos_pelicula:
                peliculas.append(datos_pelicula)
        ventana_agregar_pelicula.after(0, insertar_peliculas_tree_agregar, ventana_agregar_pelicula.tree, peliculas)
    else:
        mostrar_error("Error", "No se pudieron obtener las películas más recientes")

def agregar_pelicula(ventana_agregar_pelicula,base):
    seleccion = ventana_agregar_pelicula.tree.selection()
    if seleccion:
        pelicula = ventana_agregar_pelicula.tree.item(seleccion[0])["values"]
        if pelicula:
            pelicula_id = pelicula[0]
            pelicula_titulo = pelicula[1]
            sinopsis_pelicula = pelicula[2]
            genero_pelicula = pelicula[3]
            duracion_pelicula = pelicula[4]
            estreno_pelicula = pelicula[5]
            votacion_pelicula = pelicula[6]
            ruta_imagen = pelicula[7]
            datos_pelicula = (pelicula_id, ruta_imagen, pelicula_titulo, sinopsis_pelicula, genero_pelicula, duracion_pelicula, estreno_pelicula, votacion_pelicula)

            from backend.database import agregar_pelicula_bd
            if agregar_pelicula_bd(datos_pelicula):
                
            
                mostrar_mensaje("Agregar Pelicula", f"Se agregó la pelicula '{pelicula_titulo}' a la base de datos")
                from .funciones_administrar_peliculas import insertar_peliculas_tree
                insertar_peliculas_tree(base.tree_peliculas)
            else:
                return
        else:
            mostrar_error("Agregar Pelicula", "No se ha seleccionado ninguna pelicula")
            return
    else:
        mostrar_error("Agregar Pelicula", "No se ha seleccionado ninguna pelicula")
        return




def insertar_peliculas_tree_agregar(tree, peliculas):
    from ..utils import limpiar_treeview
    limpiar_treeview(tree)
    
    # Insertar nuevas películas
    for datos_pelicula in peliculas:
        insertar_pelicula_tree_agregar(datos_pelicula,tree)

def insertar_pelicula_tree_agregar(datos, treeview):
    pelicula_id = datos["id"]
    pelicula_titulo = datos["titulo"]
    sinopsis_pelicula = datos["sinopsis"]
    genero_pelicula = datos["genero"]
    duracion_pelicula = datos["duracion"]
    estreno_pelicula = datos["estreno"]
    votacion_pelicula = datos["promedio_votos"]
    ruta_imagen = datos["ruta_imagen"]
    datos_pelicula = [pelicula_id, pelicula_titulo, sinopsis_pelicula, genero_pelicula, duracion_pelicula, estreno_pelicula, votacion_pelicula, ruta_imagen]
    treeview.insert("", "end", values=datos_pelicula)