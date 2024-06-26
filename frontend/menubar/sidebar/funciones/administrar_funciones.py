import customtkinter as ctk
from tkinter import ttk
from . import funciones_administrar_funciones as FAF

def administrar_funciones(base):
    
    frame_administrar_funciones = ctk.CTkFrame(base, fg_color="transparent")
    frame_administrar_funciones.pack(fill="both", expand=True)
    
    frame_administrar_funciones.rowconfigure(0, weight=1)
    frame_administrar_funciones.columnconfigure(0, weight=1)
    frame_administrar_funciones.columnconfigure(1, weight=3)
    
    formulario_funciones(frame_administrar_funciones,base)
    treeview_funciones(frame_administrar_funciones,base)
    
    frame_administrar_funciones.update()

def formulario_funciones(frame_administrar_salas,base):
    frame_formulario = ctk.CTkFrame(frame_administrar_salas,border_color="black",border_width=2,width=350)
    frame_formulario.grid(row=0, column=0, padx=5, pady=10, sticky="nsew")
    
    frame_formulario.columnconfigure(0, weight=1)
    frame_formulario.columnconfigure(1, weight=1)
    frame_formulario.grid_propagate(False)
    
    titulo = ctk.CTkLabel(frame_formulario, text="Administrar Salas", font=("Arial", 30, "bold"))
    titulo.grid(row=0, column=0, columnspan=2,pady=10, padx=10, sticky="nsew")
    
    colocar_boton_agregar_funcion(frame_formulario,base)
    agregar_separador(frame_formulario,2)
    entries_datos_funcion(frame_formulario,base)
    agregar_separador(frame_formulario,7)
    colocar_boton_editar_funcion(frame_formulario,base)
    colocar_boton_eliminar_funcion(frame_formulario,base)
    colocar_boton_salir(frame_formulario,base)
    
    frame_formulario.update()

def colocar_boton_agregar_funcion(frame_formulario,base):
    boton_agregar_sala = ctk.CTkButton(frame_formulario,text="Agregar funcion",fg_color="#329ADF",hover_color="#31AF9C",font=("Arial", 20, "bold"), command=lambda: FAF.agregar_sala(base))
    boton_agregar_sala.grid(row=1, columnspan = 2,column=0, pady=10, padx=20, sticky="nsew")

def agregar_separador(frame_formulario,fila):
    separador = ctk.CTkFrame(frame_formulario, height=2,fg_color="black")
    separador.grid(row=fila, column=0, columnspan=2, sticky="nsew",pady=10,padx=20)

def entries_datos_funcion(frame_formulario,base):
    label_id = ctk.CTkLabel(frame_formulario, text="ID Sala:", font=("Arial",16))
    label_id.grid(row=3, column=0, pady=10, padx=20, sticky="nsew")
    entry_id = ctk.CTkEntry(frame_formulario, font=("Arial",16))
    entry_id.grid(row=3, column=1, pady=10, padx=20, sticky="nsew")
    
    label_id_pelicula = ctk.CTkLabel(frame_formulario, text="ID Pelicula:", font=("Arial",16))   
    label_id_pelicula.grid(row=4, column=0, pady=10, padx=20, sticky="nsew")
    entry_id_pelicula = ctk.CTkEntry(frame_formulario, font=("Arial",16))
    entry_id_pelicula.grid(row=4, column=1, pady=10, padx=20, sticky="nsew")
    
    
    label_id_sala = ctk.CTkLabel(frame_formulario, text="ID sala:", font=("Arial",16))
    label_id_sala.grid(row=5, column=0, pady=10, padx=20, sticky="nsew")
    entry_id_sala = ctk.CTkEntry(frame_formulario, font=("Arial",16))
    entry_id_sala.grid(row=5, column=1, pady=10, padx=20, sticky="nsew")
    
    label_hora = ctk.CTkLabel(frame_formulario, text="Hora:", font=("Arial",16))
    label_hora.grid(row=6, column=0, pady=10, padx=20, sticky="nsew")
    entry_hora = ctk.CTkEntry(frame_formulario, font=("Arial",16))
    entry_hora.grid(row=6, column=1, pady=10, padx=20, sticky="nsew")

    
    base.entries_funciones = {
        "id": entry_id,
        "id pelicula": entry_id_pelicula,
        "id sala": entry_id_sala,
        "hora": entry_hora
    }

def colocar_boton_editar_funcion(frame_formulario,base):
    boton_editar_pelicula = ctk.CTkButton(frame_formulario, text="Editar Funcion",fg_color="#329ADF",hover_color="#31AF9C",font=("Arial", 20, "bold"), command=lambda: FAF.editar_sala(base))
    boton_editar_pelicula.grid(row=8, columnspan = 2,column=0, pady=10, padx=20, sticky="nsew")

def colocar_boton_eliminar_funcion(frame_formulario,base):
    boton_eliminar_pelicula = ctk.CTkButton(frame_formulario, text="Eliminar Funcion",fg_color="#329ADF",hover_color="#31AF9C",font=("Arial", 20, "bold"), command=lambda: FAF.eliminar_sala(base))
    boton_eliminar_pelicula.grid(row=9, columnspan = 2,column=0, pady=10, padx=20, sticky="nsew")

def colocar_boton_salir(frame_formulario,base):
    boton_volver = ctk.CTkButton(frame_formulario, text="Volver",fg_color="#329ADF",hover_color="#31AF9C",font=("Arial", 20, "bold"), command=lambda: FAF.volver(base))
    boton_volver.grid(row=10, columnspan = 2,column=0, pady=10, padx=20, sticky="nsew")

def treeview_funciones(frame_administrar_salas,base):
    frame_tree = ctk.CTkFrame(frame_administrar_salas,border_color="black",border_width=2,width=800)
    frame_tree.grid(row=0, column=1, padx=5, pady=10, sticky="nsew")
    frame_tree.grid_propagate(False)

    columnas_nombres = [key.capitalize() for key in base.entries_funciones.keys()]
    
    tree = ttk.Treeview(frame_tree, columns=columnas_nombres, show="headings")
    
    for columna in columnas_nombres:
        tree.column(columna, anchor="center")
        tree.heading(columna, text=columna)
    
    tree.pack(fill="both", expand=True,padx=10,pady=10)
    tree.pack_propagate(False)
    
    tree.insert("", "end", values=("1", "2", "3", "4"))
    
    frame_tree.update()