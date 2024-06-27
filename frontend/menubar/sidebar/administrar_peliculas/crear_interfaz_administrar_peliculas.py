import customtkinter as ctk
from tkinter import ttk
from frontend.utils import mostrar_error
from . import funciones_administrar_peliculas as FAP
from . import agregar_pelicula as AP

def administrar_peliculas(base):
    frame_administrar_peliculas = ctk.CTkFrame(base, fg_color="transparent")
    frame_administrar_peliculas.pack(fill="both", expand=True)

    frame_administrar_peliculas.rowconfigure(0, weight=1)
    frame_administrar_peliculas.columnconfigure(0, weight=1)
    frame_administrar_peliculas.columnconfigure(1, weight=3)

    formulario_pelicula(frame_administrar_peliculas, base)
    treeview_peliculas(frame_administrar_peliculas, base)
    
    frame_administrar_peliculas.update()

def formulario_pelicula(frame_administrar_peliculas, base):
    frame_formulario = ctk.CTkFrame(frame_administrar_peliculas, border_color="black", border_width=2, width=350)
    frame_formulario.grid(row=0, column=0, padx=5, pady=10, sticky="nsew")

    frame_formulario.columnconfigure(0, weight=1)
    frame_formulario.columnconfigure(1, weight=1)
    frame_formulario.grid_propagate(False)

    titulo = ctk.CTkLabel(frame_formulario, text="Administrar Peliculas", font=("Arial", 30, "bold"))
    titulo.grid(row=0, column=0, columnspan=2, pady=10, padx=10, sticky="nsew")

    colocar_boton_agregar_pelicula(frame_formulario, base)
    agregar_separador(frame_formulario, 2)
    entries_datos_pelicula(frame_formulario, base)
    agregar_separador(frame_formulario, 12)
    colocar_boton_editar_pelicula(frame_formulario, base)
    colocar_boton_eliminar_pelicula(frame_formulario, base)
    colocar_boton_salir(frame_formulario, base)

    frame_formulario.update()

def colocar_boton_agregar_pelicula(frame_formulario, base):
    boton_agregar_pelicula = ctk.CTkButton(frame_formulario, text="Agregar Pelicula", fg_color="#329ADF", hover_color="#31AF9C", font=("Arial", 20, "bold"), command=lambda: AP.crear_ventana_agregar_pelicula(base))
    boton_agregar_pelicula.grid(row=1, columnspan=2, column=0, pady=10, padx=20, sticky="nsew")

def agregar_separador(frame_formulario, fila):
    separador = ctk.CTkFrame(frame_formulario, height=2, fg_color="black")
    separador.grid(row=fila, column=0, columnspan=2, sticky="nsew", pady=10, padx=20)

def entries_datos_pelicula(frame_formulario, base):
    label_id = ctk.CTkLabel(frame_formulario, text="ID Pelicula:", font=("Arial", 16))
    label_id.grid(row=3, column=0, pady=10, padx=20, sticky="nsew")
    entry_id = ctk.CTkEntry(frame_formulario, font=("Arial", 16))
    entry_id.grid(row=3, column=1, pady=10, padx=20, sticky="nsew")

    label_titulo = ctk.CTkLabel(frame_formulario, text="Nombre Pelicula:", font=("Arial", 16))   
    label_titulo.grid(row=4, column=0, pady=10, padx=20, sticky="nsew")
    entry_titulo = ctk.CTkEntry(frame_formulario, font=("Arial", 16))
    entry_titulo.grid(row=4, column=1, pady=10, padx=20, sticky="nsew")

    label_sinopsis = ctk.CTkLabel(frame_formulario, text="Sinopsis:", font=("Arial", 16))
    label_sinopsis.grid(row=5, column=0, columnspan=2, pady=10, padx=20, sticky="nsew")
    texbox_sinopsis = ctk.CTkTextbox(frame_formulario, font=("Arial", 14, "bold"), height=50)
    texbox_sinopsis.grid(row=6, column=0, columnspan=2, pady=(0, 10), padx=20, sticky="nsew")
    
    label_genero = ctk.CTkLabel(frame_formulario, text="Genero:", font=("Arial", 16))
    label_genero.grid(row=7, column=0, pady=10, padx=20, sticky="nsew")
    entry_genero = ctk.CTkEntry(frame_formulario, font=("Arial", 16))
    entry_genero.grid(row=7, column=1, pady=10, padx=20, sticky="nsew")

    label_duracion = ctk.CTkLabel(frame_formulario, text="Duracion:", font=("Arial", 16))
    label_duracion.grid(row=8, column=0, pady=10, padx=20, sticky="nsew")
    entry_duracion = ctk.CTkEntry(frame_formulario, font=("Arial", 16))
    entry_duracion.grid(row=8, column=1, pady=10, padx=20, sticky="nsew")

    label_estreno = ctk.CTkLabel(frame_formulario, text="Fecha Estreno:", font=("Arial", 16))
    label_estreno.grid(row=9, column=0, pady=10, padx=20, sticky="nsew")
    entry_estreno = ctk.CTkEntry(frame_formulario, font=("Arial", 16))
    entry_estreno.grid(row=9, column=1, pady=10, padx=20, sticky="nsew")

    label_prom_votos = ctk.CTkLabel(frame_formulario, text="Promedio Votos:", font=("Arial", 16))
    label_prom_votos.grid(row=10, column=0, pady=10, padx=20, sticky="nsew")
    entry_prom_votos = ctk.CTkEntry(frame_formulario, font=("Arial", 16))
    entry_prom_votos.grid(row=10, column=1, pady=10, padx=20, sticky="nsew")
    
    label_ruta_imagen = ctk.CTkLabel(frame_formulario, text="Ruta Imagen:", font=("Arial", 16))
    label_ruta_imagen.grid(row=11, column=0, pady=10, padx=20, sticky="nsew")
    entry_ruta_imagen = ctk.CTkEntry(frame_formulario, font=("Arial", 16))
    entry_ruta_imagen.grid(row=11, column=1, pady=10, padx=20, sticky="nsew")

    base.entries_pelicula = {
        "id": entry_id,
        "titulo": entry_titulo,
        "sinopsis": texbox_sinopsis,
        "genero": entry_genero,
        "duracion": entry_duracion,
        "estreno": entry_estreno,
        "prom_votos" : entry_prom_votos,
        "ruta_imagen": entry_ruta_imagen,
    }

def colocar_boton_editar_pelicula(frame_formulario, base):
    boton_editar_pelicula = ctk.CTkButton(frame_formulario, text="Editar Pelicula", fg_color="#329ADF", hover_color="#31AF9C", font=("Arial", 20, "bold"), command=lambda: FAP.editar_pelicula(base))
    boton_editar_pelicula.grid(row=13, columnspan=2, column=0, pady=10, padx=20, sticky="nsew")

def colocar_boton_eliminar_pelicula(frame_formulario, base):
    boton_eliminar_pelicula = ctk.CTkButton(frame_formulario, text="Eliminar Pelicula", fg_color="#329ADF", hover_color="#31AF9C", font=("Arial", 20, "bold"), command=lambda: FAP.eliminar_pelicula(base))
    boton_eliminar_pelicula.grid(row=14, columnspan=2, column=0, pady=10, padx=20, sticky="nsew")

def colocar_boton_salir(frame_formulario, base):
    boton_volver = ctk.CTkButton(frame_formulario, text="Volver", fg_color="#329ADF", hover_color="#31AF9C", font=("Arial", 20, "bold"), command=lambda: FAP.volver(base))
    boton_volver.grid(row=15, columnspan=2, column=0, pady=10, padx=20, sticky="nsew")

def treeview_peliculas(frame_administrar_peliculas, base):
    frame_tree = ctk.CTkFrame(frame_administrar_peliculas, border_color="black", border_width=2, width=800)
    frame_tree.grid(row=0, column=1, padx=5, pady=10, sticky="nsew")
    frame_tree.grid_propagate(False)

    columnas_nombres = [key.capitalize() for key in base.entries_pelicula.keys() if key != "ruta_imagen"]

    base.tree_peliculas = ttk.Treeview(frame_tree, columns=columnas_nombres, show="headings")

    
    ancho_columnas = {
        "Id": 50,
        "Titulo": 200,
        "Sinopsis": 300,
        "Duracion": 75,
        "Genero": 50,
        "Estreno": 75,
    }

    base.tree_peliculas.pack(fill="both", expand=True, padx=10, pady=10)
    base.tree_peliculas.pack_propagate(False)
    
    base.tree_peliculas.bind("<<TreeviewSelect>>", lambda event: seleccionar_fila(event, base, base.tree_peliculas))
    
    from ..utils import configurar_insertar_columnas_treeview
    
    configurar_insertar_columnas_treeview(base.tree_peliculas, columnas_nombres, ancho_columnas)
    FAP.insertar_peliculas_tree(base.tree_peliculas)
        
    frame_tree.update()
    
def seleccionar_fila(event, base, tree):
    try:
        item_seleccionado = tree.focus()
        values = tree.item(item_seleccionado)["values"]
        if values:
            for index, (key, entry) in enumerate(base.entries_pelicula.items()):
                if key == "sinopsis":
                    entry.delete(1.0, "end")
                    entry.insert(1.0, values[index])
                else:
                    entry.delete(0, "end")
                    entry.insert(0, values[index])
                
    except Exception as e:
        mostrar_error("Error al seleccionar fila", f"Ocurrio un error al seleccionar la fila: {e}")

