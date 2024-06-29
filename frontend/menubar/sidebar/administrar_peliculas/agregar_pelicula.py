import threading
import customtkinter as ctk
from tkinter import ttk
from concurrent.futures import ThreadPoolExecutor

from frontend.utils import mostrar_error, mostrar_mensaje
from backend.database import agregar_pelicula_bd
from .funciones_administrar_peliculas import insertar_peliculas_tree
from ..utils_menu_bar import limpiar_treeview, configurar_insertar_columnas_treeview
from ...barra_busqueda import enter_hover_boton_busqueda, leave_hover_boton_busqueda, crear_busqueda_img as CBI
from backend import API

executor = ThreadPoolExecutor(max_workers=3)


def crear_ventana_agregar_pelicula(base):
    ventana_agregar_pelicula = ctk.CTkToplevel(base)
    ventana_agregar_pelicula.title("Agregar Pelicula")
    ventana_agregar_pelicula.geometry("1400x500")
    ventana_agregar_pelicula.resizable(False, False)
    ventana_agregar_pelicula.transient(base)
    
    frame_opciones_agregar_pelicula(ventana_agregar_pelicula, base)
    tree_agregar_pelicula(ventana_agregar_pelicula, base)

def frame_opciones_agregar_pelicula(ventana_agregar_pelicula, base):
    frame_opciones = ctk.CTkFrame(ventana_agregar_pelicula, border_color="black", fg_color="transparent")
    frame_opciones.pack(side="top", expand=True)

    label_nombre = ctk.CTkLabel(frame_opciones, text="Ingrese el nombre de la pelicula:", font=("Arial", 16))
    label_nombre.grid(row=0, column=0, pady=10, padx=10, sticky="w")
    entry_nombre = ctk.CTkEntry(frame_opciones, font=("Arial", 16), width=300)
    entry_nombre.grid(row=0, column=1, pady=10, padx=10, sticky="w")
    
    boton_buscar = ctk.CTkButton(frame_opciones, 
                                image=CBI.BUSQUEDA_IMAGEN["imagen_busqueda"],
                                text=" ", 
                                font=("Arial", 20, "bold"), 
                                width=10,
                                border_width=2,
                                border_color="black",
                                fg_color="transparent",
                                hover=False,
                                corner_radius=15,
                                command=lambda : iniciar_hilo_buscar_peliculas(entry_nombre.get(), ventana_agregar_pelicula))
    boton_buscar.grid(row=0, column=2, pady=10, padx=10, sticky="w")
    
    boton_buscar.bind("<Enter>", lambda e: enter_hover_boton_busqueda(boton_buscar))
    boton_buscar.bind("<Leave>", lambda e: leave_hover_boton_busqueda(boton_buscar))
    
    boton_agregar = ctk.CTkButton(frame_opciones, text="Agregar", fg_color="#329ADF", hover_color="#31AF9C", font=("Arial", 16), command=lambda: agregar_pelicula(ventana_agregar_pelicula, base))
    boton_agregar.grid(row=0, column=3, pady=10, padx=10, sticky="w")
    
    boton_recientes = ctk.CTkButton(frame_opciones, text="Mostrar peliculas mas recientes", fg_color="#329ADF", hover_color="#31AF9C", font=("Arial", 16), command=lambda: iniciar_hilo_peliculas_mas_recientes(ventana_agregar_pelicula))
    boton_recientes.grid(row=0, column=4, pady=10, padx=10, sticky="w")

    boton_cancelar = ctk.CTkButton(frame_opciones, text="Cancelar", fg_color="#329ADF", hover_color="#31AF9C", font=("Arial", 16), command=lambda: salir_ventana_agregar_pelicula(ventana_agregar_pelicula))
    boton_cancelar.grid(row=0, column=5, pady=10, padx=10, sticky="w")

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

    configurar_insertar_columnas_treeview(tree, columnas_nombres, ancho_columnas)

    tree.pack(fill="both", expand=True, padx=10, pady=10)
    tree.pack_propagate(False)
    
    ventana_agregar_pelicula.tree = tree


def iniciar_hilo_buscar_peliculas(entry_result, ventana_agregar_pelicula):
    hilo_buscar_peliculas = threading.Thread(target=buscar_peliculas, args=(entry_result, ventana_agregar_pelicula))
    hilo_buscar_peliculas.start()
    print(f"Hilos activos: {threading.active_count()}")


def buscar_peliculas(entry_result, ventana_agregar_pelicula):
    limpiar_treeview(ventana_agregar_pelicula.tree)
    if not entry_result:
        mostrar_error("Error", "No se ha ingresado un nombre de pelicula")
        return
    respuesta = API.obtener_peliculas(entry_result)
    try:
        resultados = respuesta.get("results")
        if not respuesta or not resultados:
            mostrar_error("Error", "No se encontraron peliculas")
            return
        
        future_peliculas = [executor.submit(API.obtener_datos_pelicula, valor["id"]) for valor in resultados]
        insertar_peliculas_tree_agregar(future_peliculas, ventana_agregar_pelicula.tree)
        
    except Exception as e:
        mostrar_error("Error", f"No se pudo buscar las peliculas: {e}")

def iniciar_hilo_peliculas_mas_recientes(ventana_agregar_pelicula):
    hilo_mas_recientes = threading.Thread(target=peliculas_mas_recientes, args=(ventana_agregar_pelicula,))
    hilo_mas_recientes.start()
    print(f"Hilos activos: {threading.active_count()}")

def peliculas_mas_recientes(ventana_agregar_pelicula):
    limpiar_treeview(ventana_agregar_pelicula.tree)
    respuesta = API.obtener_peliculas_mas_recientes()
    try:
        resultados = respuesta.get("results")
        if not respuesta or not resultados:
            mostrar_error("Error", "No se encontraron peliculas")
            return
        future_peliculas = [executor.submit(API.obtener_datos_pelicula, valor["id"]) for valor in resultados]
        insertar_peliculas_tree_agregar(future_peliculas, ventana_agregar_pelicula.tree)
                
    except Exception as e:
        mostrar_error("Error", f"No se pudo obtener las peliculas mas recientes: {e}")


def agregar_pelicula(ventana_agregar_pelicula, base):
    seleccion = ventana_agregar_pelicula.tree.selection()
    if seleccion:
        pelicula = ventana_agregar_pelicula.tree.item(seleccion[0])["values"]
        if pelicula:
            pelicula_id, pelicula_titulo, sinopsis_pelicula, genero_pelicula, duracion_pelicula, estreno_pelicula, votacion_pelicula,ruta_imagen = pelicula
            datos_pelicula = (pelicula_id, ruta_imagen, pelicula_titulo, sinopsis_pelicula, genero_pelicula, duracion_pelicula, estreno_pelicula, votacion_pelicula)

            if agregar_pelicula_bd(datos_pelicula):
                mostrar_mensaje("Agregar Pelicula", f"Se agregó la pelicula '{pelicula_titulo}' a la base de datos")
                insertar_peliculas_tree(base.tree_peliculas)
            else:
                mostrar_error("Agregar Pelicula", "No se pudo agregar la película a la base de datos")
        else:
            mostrar_error("Agregar Pelicula", "No se ha seleccionado ninguna pelicula")
    else:
        mostrar_error("Agregar Pelicula", "No se ha seleccionado ninguna pelicula")


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

def insertar_peliculas_tree_agregar(future_peliculas, treeview):
    for future in future_peliculas:
        try:
            resultado = future.result()
            if resultado:
                insertar_pelicula_tree_agregar(resultado, treeview)
        except Exception as e:
                mostrar_error("Error", f"Error al obtener datos de la película: {e}")

def salir_ventana_agregar_pelicula(ventana_agregar_pelicula):
    ventana_agregar_pelicula.destroy()
    executor.shutdown(wait=False)
    print(f"Hilos activos: {threading.active_count()}")