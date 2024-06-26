import customtkinter as ctk
from tkinter import ttk
from . import funciones_administrar_peliculas as FAP

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
    agregar_separador(frame_formulario, 10)
    colocar_boton_editar_pelicula(frame_formulario, base)
    colocar_boton_eliminar_pelicula(frame_formulario, base)
    colocar_boton_salir(frame_formulario, base)

    frame_formulario.update()


def colocar_boton_agregar_pelicula(frame_formulario, base):
    boton_agregar_pelicula = ctk.CTkButton(frame_formulario, text="Agregar Pelicula", fg_color="#329ADF", hover_color="#31AF9C", font=("Arial", 20, "bold"), command=lambda: FAP.agregar_pelicula(base))
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

    label_genero = ctk.CTkLabel(frame_formulario, text="Genero:", font=("Arial", 16))
    label_genero.grid(row=5, column=0, pady=10, padx=20, sticky="nsew")
    entry_genero = ctk.CTkEntry(frame_formulario, font=("Arial", 16))
    entry_genero.grid(row=5, column=1, pady=10, padx=20, sticky="nsew")

    label_duracion = ctk.CTkLabel(frame_formulario, text="Duracion", font=("Arial", 16))
    label_duracion.grid(row=6, column=0, pady=10, padx=20, sticky="nsew")
    entry_duracion = ctk.CTkEntry(frame_formulario, font=("Arial", 16))
    entry_duracion.grid(row=6, column=1, pady=10, padx=20, sticky="nsew")

    label_estreno = ctk.CTkLabel(frame_formulario, text="Fecha Estreno:", font=("Arial", 16))
    label_estreno.grid(row=7, column=0, pady=10, padx=20, sticky="nsew")
    entry_estreno = ctk.CTkEntry(frame_formulario, font=("Arial", 16))
    entry_estreno.grid(row=7, column=1, pady=10, padx=20, sticky="nsew")

    label_sinopsis = ctk.CTkLabel(frame_formulario, text="Sinopsis:", font=("Arial", 16))
    label_sinopsis.grid(row=8, column=0, columnspan=2, pady=10, padx=20, sticky="nsew")
    texbox_sinopsis = ctk.CTkTextbox(frame_formulario, font=("Arial", 14, "bold"), height=50)
    texbox_sinopsis.grid(row=9, column=0, columnspan=2, pady=(0, 10), padx=20, sticky="nsew")

    base.entries_pelicula = {
        "id": entry_id,
        "titulo": entry_titulo,
        "genero": entry_genero,
        "duracion": entry_duracion,
        "estreno": entry_estreno,
        "sinopsis": texbox_sinopsis
    }

def colocar_boton_editar_pelicula(frame_formulario, base):
    boton_editar_pelicula = ctk.CTkButton(frame_formulario, text="Editar Pelicula", fg_color="#329ADF", hover_color="#31AF9C", font=("Arial", 20, "bold"), command=lambda: FAP.editar_pelicula(base))
    boton_editar_pelicula.grid(row=11, columnspan=2, column=0, pady=10, padx=20, sticky="nsew")

def colocar_boton_eliminar_pelicula(frame_formulario, base):
    boton_eliminar_pelicula = ctk.CTkButton(frame_formulario, text="Eliminar Pelicula", fg_color="#329ADF", hover_color="#31AF9C", font=("Arial", 20, "bold"), command=lambda: FAP.eliminar_pelicula(base))
    boton_eliminar_pelicula.grid(row=12, columnspan=2, column=0, pady=10, padx=20, sticky="nsew")

def colocar_boton_salir(frame_formulario, base):
    boton_volver = ctk.CTkButton(frame_formulario, text="Volver", fg_color="#329ADF", hover_color="#31AF9C", font=("Arial", 20, "bold"), command=lambda: FAP.volver(base))
    boton_volver.grid(row=13, columnspan=2, column=0, pady=10, padx=20, sticky="nsew")

def treeview_peliculas(frame_administrar_peliculas, base):
    frame_tree = ctk.CTkFrame(frame_administrar_peliculas, border_color="black", border_width=2,width=800)
    frame_tree.grid(row=0, column=1, padx=5, pady=10, sticky="nsew")
    frame_tree.grid_propagate(False)

    columnas_nombres = [key.capitalize() for key in base.entries_pelicula.keys()]

    tree = ttk.Treeview(frame_tree, columns=columnas_nombres, show="headings")

    for columna in columnas_nombres:
        tree.column(columna, anchor="center")
        tree.heading(columna, text=columna)

    tree.pack(fill="both", expand=True, padx=10, pady=10)
    tree.pack_propagate(False)

    tree.insert("", "end", values=("1", "Pelicula1", "Genero1", "Duracion1", "Estreno1", "Sinopsis1"))
    
    frame_tree.update()