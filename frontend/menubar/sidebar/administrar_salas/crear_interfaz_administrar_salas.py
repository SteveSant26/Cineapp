import customtkinter as ctk
from CTkSpinbox import *
from tkinter import ttk
from . import funciones_administrar_salas as FAS

def administrar_salas(base):
    
    frame_administrar_salas = ctk.CTkFrame(base, fg_color="transparent")
    frame_administrar_salas.pack(fill="both", expand=True)
    
    frame_administrar_salas.rowconfigure(0, weight=1)
    frame_administrar_salas.columnconfigure(0, weight=1)
    frame_administrar_salas.columnconfigure(1, weight=3)
    
    formulario_salas(frame_administrar_salas,base)
    treeview_salas(frame_administrar_salas,base)
    
    frame_administrar_salas.update()

def formulario_salas(frame_administrar_salas,base):
    frame_formulario = ctk.CTkFrame(frame_administrar_salas,border_color="black",border_width=2,width=350)
    frame_formulario.grid(row=0, column=0, padx=5, pady=10, sticky="nsew")
    
    frame_formulario.columnconfigure(0, weight=1)
    frame_formulario.columnconfigure(1, weight=1)
    frame_formulario.grid_propagate(False)
    
    titulo = ctk.CTkLabel(frame_formulario, text="Administrar Salas", font=("Arial", 30, "bold"))
    titulo.grid(row=0, column=0, columnspan=2,pady=10, padx=10, sticky="nsew")
    
    agregar_separador(frame_formulario,1)
    entries_datos_sala(frame_formulario,base)
    agregar_separador(frame_formulario,6)
    colocar_boton_agregar_sala(frame_formulario,base)
    colocar_boton_editar_sala(frame_formulario,base)
    colocar_boton_eliminar_sala(frame_formulario,base)
    colocar_boton_salir(frame_formulario,base)
    
    frame_formulario.update()


def agregar_separador(frame_formulario,fila):
    separador = ctk.CTkFrame(frame_formulario, height=2,fg_color="black")
    separador.grid(row=fila, column=0, columnspan=2, sticky="nsew",pady=10,padx=20)

def entries_datos_sala(frame_formulario,base):
    label_id = ctk.CTkLabel(frame_formulario, text="ID Sala:", font=("Arial",16))
    label_id.grid(row=2, column=0, pady=10, padx=20, sticky="nsew")
    entry_id = ctk.CTkEntry(frame_formulario, font=("Arial",16))
    entry_id.grid(row=2, column=1, pady=10, padx=20, sticky="nsew")
    
    label_nombre = ctk.CTkLabel(frame_formulario, text="Nombre Sala:", font=("Arial",16))   
    label_nombre.grid(row=3, column=0, pady=10, padx=20, sticky="nsew")
    entry_nombre = ctk.CTkEntry(frame_formulario, font=("Arial",16))
    entry_nombre.grid(row=3, column=1, pady=10, padx=20, sticky="nsew")
    
    label_filas = ctk.CTkLabel(frame_formulario, text="Filas sala:", font=("Arial",16))
    label_filas.grid(row=4, column=0, pady=10, padx=20, sticky="nsew")
    
    filas_var = ctk.IntVar()
    spinbox_filas = CTkSpinbox(frame_formulario, min_value=1, max_value=20, start_value=4,button_color="#329ADF",button_hover_color="#31AF9C",variable=filas_var,font=("Arial",16))
    spinbox_filas.grid(row=4, column=1, pady=10, padx=20, sticky="nsew")
    
    # entry_filas = ctk.CTkEntry(frame_formulario, font=("Arial",16))
    # entry_filas.grid(row=5, column=1, pady=10, padx=20, sticky="nsew")
    
    label_columnas = ctk.CTkLabel(frame_formulario, text="Columnas sala:", font=("Arial",16))
    label_columnas.grid(row=5, column=0, pady=10, padx=20, sticky="nsew")
    
    spinbox_columnas = CTkSpinbox(frame_formulario, min_value=1, max_value=20, start_value=4,button_color="#329ADF",button_hover_color="#31AF9C",font=("Arial",16))
    spinbox_columnas.grid(row=5, column=1, pady=10, padx=20, sticky="nsew")
    
    # entry_columnas = ctk.CTkEntry(frame_formulario, font=("Arial",16))
    # entry_columnas.grid(row=6, column=1, pady=10, padx=20, sticky="nsew")

    
    base.entries_salas = {
        "id": entry_id,
        "nombre": entry_nombre,
        "filas": spinbox_filas,
        "columnas": spinbox_columnas
    }
def colocar_boton_agregar_sala(frame_formulario,base):
    boton_agregar_sala = ctk.CTkButton(frame_formulario,text="Agregar Sala",fg_color="#329ADF",hover_color="#31AF9C",font=("Arial", 20, "bold"), command=lambda: FAS.agregar_sala(base))
    boton_agregar_sala.grid(row=7, columnspan = 2,column=0, pady=10, padx=20, sticky="nsew")
    
def colocar_boton_editar_sala(frame_formulario,base):
    boton_editar_pelicula = ctk.CTkButton(frame_formulario, text="Editar Sala",fg_color="#329ADF",hover_color="#31AF9C",font=("Arial", 20, "bold"), command=lambda: FAS.editar_sala(base))
    boton_editar_pelicula.grid(row=8, columnspan = 2,column=0, pady=10, padx=20, sticky="nsew")

def colocar_boton_eliminar_sala(frame_formulario,base):
    boton_eliminar_pelicula = ctk.CTkButton(frame_formulario, text="Eliminar Sala",fg_color="#329ADF",hover_color="#31AF9C",font=("Arial", 20, "bold"), command=lambda: FAS.eliminar_sala(base))
    boton_eliminar_pelicula.grid(row=9, columnspan = 2,column=0, pady=10, padx=20, sticky="nsew")

def colocar_boton_salir(frame_formulario,base):
    boton_volver = ctk.CTkButton(frame_formulario, text="Volver",fg_color="#329ADF",hover_color="#31AF9C",font=("Arial", 20, "bold"), command=lambda: FAS.volver(base))
    boton_volver.grid(row=10, columnspan = 2,column=0, pady=10, padx=20, sticky="nsew")

def treeview_salas(frame_administrar_salas,base):
    frame_tree = ctk.CTkFrame(frame_administrar_salas,border_color="black",border_width=2,width=800)
    frame_tree.grid(row=0, column=1, padx=5, pady=10, sticky="nsew")
    frame_tree.grid_propagate(False)

    columnas_nombres = [key.capitalize() for key in base.entries_salas.keys()]
    
    tree = ttk.Treeview(frame_tree, columns=columnas_nombres, show="headings")
    
    ancho_columnas = {
        "Id": 50,
        "Nombre": 300,
        "Filas": 300,
        "Columnas": 300
    }
    
    from ..utils import configurar_insertar_columnas_treeview
    configurar_insertar_columnas_treeview(tree, columnas_nombres, ancho_columnas)
    
    tree.pack(fill="both", expand=True,padx=10,pady=10)
    tree.pack_propagate(False)
    
    tree.bind("<<TreeviewSelect>>", lambda event: seleccionar_fila(event, base, tree))
    
    FAS.insertar_salas_tree(tree)    
    frame_tree.update()

def seleccionar_fila(event, base, tree):
    try:
        item_seleccionado = tree.focus()
        if item_seleccionado:
            values = tree.item(item_seleccionado)["values"]
            
            
            base.entries_salas["id"].delete(0, "end")
            base.entries_salas["nombre"].delete(0, "end")

            
            base.entries_salas["id"].insert(0, values[0])
            base.entries_salas["nombre"].insert(0, values[1])
            
            base.entries_salas["filas"].set(values[2])
            base.entries_salas["columnas"].set(values[3])
            
    except Exception as e:
        print(f"Error al seleccionar la fila: {e}")