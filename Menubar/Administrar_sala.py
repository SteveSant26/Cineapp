import customtkinter as ctk
import os
import sys

sys.path.append(os.path.dirname(__file__))

def administrar_peliculas(base):
    
    # Crear el frame para administrar películas
    base.frame_administrar_peliculas = ctk.CTkFrame(base, fg_color="transparent")
    base.frame_administrar_peliculas.pack(fill="both", expand=True)
    base.frame_administrar_peliculas.pack_propagate(False)

    base.frame_administrar_peliculas.rowconfigure(0, weight=1)
    base.frame_administrar_peliculas.columnconfigure(0, weight=1)
    base.frame_administrar_peliculas.columnconfigure(1, weight=2)




    frame_formulario = ctk.CTkFrame(base.frame_administrar_peliculas,border_color="black",border_width=2,width=600)
    frame_formulario.grid(row=0, column=0, padx=5, pady=10, sticky="nsew")
    frame_formulario.grid_propagate(False)

    titulo = ctk.CTkLabel(frame_formulario, text="Administrar Peliculas", font=("Arial", 30, "bold"))
    titulo.grid(row=0, column=0, columnspan=2,pady=20, padx=20, sticky="nsew")

    boton_agregar_pelicula = ctk.CTkButton(frame_formulario, text="Agregar Pelicula", font=("Arial", 20, "bold"), command=lambda: agregar_pelicula(base))
    boton_agregar_pelicula.grid(row=1, columnspan = 2,column=0, pady=20, padx=20, sticky="nsew")



    frame_tree = ctk.CTkFrame(base.frame_administrar_peliculas,border_color="black",border_width=2,width=1300)
    frame_tree.grid(row=0, column=1, padx=5, pady=10, sticky="nsew")
    frame_tree.grid_propagate(False)
    
def agregar_pelicula(base):
    pass