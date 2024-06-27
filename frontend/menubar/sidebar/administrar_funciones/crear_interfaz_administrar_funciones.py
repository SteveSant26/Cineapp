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
    
    titulo = ctk.CTkLabel(frame_formulario, text="Administrar funciones", font=("Arial", 30, "bold"))
    titulo.grid(row=0, column=0, columnspan=2,pady=10, padx=10, sticky="nsew")
    
    agregar_separador(frame_formulario,1)
    entries_datos_funcion(frame_formulario,base)
    agregar_separador(frame_formulario,6)
    colocar_boton_agregar_funcion(frame_formulario,base)
    colocar_boton_editar_funcion(frame_formulario,base)
    colocar_boton_eliminar_funcion(frame_formulario,base)
    colocar_boton_salir(frame_formulario,base)
    
    frame_formulario.update()



def agregar_separador(frame_formulario,fila):
    separador = ctk.CTkFrame(frame_formulario, height=2,fg_color="black")
    separador.grid(row=fila, column=0, columnspan=2, sticky="nsew",pady=10,padx=20)

def entries_datos_funcion(frame_formulario,base):
    label_id = ctk.CTkLabel(frame_formulario, text="ID Funcion:", font=("Arial",16))
    label_id.grid(row=2, column=0, pady=10, padx=20, sticky="nsew")
    entry_id = ctk.CTkEntry(frame_formulario, font=("Arial",16))
    entry_id.grid(row=2, column=1, pady=10, padx=20, sticky="nsew")
    
    label_id_pelicula = ctk.CTkLabel(frame_formulario, text="ID Pelicula:", font=("Arial",16))   
    label_id_pelicula.grid(row=3, column=0, pady=10, padx=20, sticky="nsew")
    entry_id_pelicula = ctk.CTkEntry(frame_formulario, font=("Arial",16))
    entry_id_pelicula.grid(row=3, column=1, pady=10, padx=20, sticky="nsew")
    
    
    label_id_sala = ctk.CTkLabel(frame_formulario, text="ID sala:", font=("Arial",16))
    label_id_sala.grid(row=4, column=0, pady=10, padx=20, sticky="nsew")
    entry_id_sala = ctk.CTkEntry(frame_formulario, font=("Arial",16))
    entry_id_sala.grid(row=4, column=1, pady=10, padx=20, sticky="nsew")
    
    label_hora = ctk.CTkLabel(frame_formulario, text="Fecha y Hora:", font=("Arial",16))
    label_hora.grid(row=5, column=0, pady=10, padx=20, sticky="nsew")
    entry_hora = ctk.CTkEntry(frame_formulario, font=("Arial",16))
    entry_hora.grid(row=5, column=1, pady=10, padx=20, sticky="nsew")

    
    base.entries_funciones = {
        "id": entry_id,
        "id pelicula": entry_id_pelicula,
        "id sala": entry_id_sala,
        "fecha y hora": entry_hora
    }
def colocar_boton_agregar_funcion(frame_formulario,base):
    boton_agregar_sala = ctk.CTkButton(frame_formulario,text="Agregar funcion",fg_color="#329ADF",hover_color="#31AF9C",font=("Arial", 20, "bold"), command=lambda: FAF.agregar_funcion(base))
    boton_agregar_sala.grid(row=7, columnspan = 2,column=0, pady=10, padx=20, sticky="nsew")
    
def colocar_boton_editar_funcion(frame_formulario,base):
    boton_editar_pelicula = ctk.CTkButton(frame_formulario, text="Editar Funcion",fg_color="#329ADF",hover_color="#31AF9C",font=("Arial", 20, "bold"), command=lambda: FAF.editar_funcion(base))
    boton_editar_pelicula.grid(row=8, columnspan = 2,column=0, pady=10, padx=20, sticky="nsew")

def colocar_boton_eliminar_funcion(frame_formulario,base):
    boton_eliminar_pelicula = ctk.CTkButton(frame_formulario, text="Eliminar Funcion",fg_color="#329ADF",hover_color="#31AF9C",font=("Arial", 20, "bold"), command=lambda: FAF.eliminar_funcion(base))
    boton_eliminar_pelicula.grid(row=9, columnspan = 2,column=0, pady=10, padx=20, sticky="nsew")

def colocar_boton_salir(frame_formulario,base):
    boton_volver = ctk.CTkButton(frame_formulario, text="Volver",fg_color="#329ADF",hover_color="#31AF9C",font=("Arial", 20, "bold"), command=lambda: FAF.volver(base))
    boton_volver.grid(row=10, columnspan = 2,column=0, pady=10, padx=20, sticky="nsew")

def treeview_funciones(frame_administrar_salas,base):
    frame_tree = ctk.CTkFrame(frame_administrar_salas,border_color="black",border_width=2,width=800)
    frame_tree.grid(row=0, column=1, padx=5, pady=10, sticky="nsew")
    frame_tree.grid_propagate(False)

    columnas_nombres = [key.capitalize() for key in base.entries_funciones.keys()]
    
    ancho_columnas = {
        "Id": 100,
        "Id Pelicula": 100,
        "Id Sala": 100,
        "Fecha y Hora": 300
    }
        
    base.tree_funciones = ttk.Treeview(frame_tree, columns=columnas_nombres, show="headings")
    base.tree_funciones.pack(fill="both", expand=True,padx=10,pady=10)
    base.tree_funciones.pack_propagate(False)
    
    base.tree_funciones.bind("<<TreeviewSelect>>", lambda event: seleccionar_fila(event, base, base.tree_funciones))

    
    from ..utils import configurar_insertar_columnas_treeview
    configurar_insertar_columnas_treeview(base.tree_funciones, columnas_nombres, ancho_columnas)
    FAF.insertar_funciones_tree(base.tree_funciones)
    
    
    
    frame_tree.update()

def seleccionar_fila(event, base, tree):
    try:
        item_seleccionado = tree.focus()
        values = tree.item(item_seleccionado)["values"]
        if values:
            print(values)
            for index, (entry) in enumerate(base.entries_funciones.values()):
                entry.delete(0, "end")
                entry.insert(0, values[index])
                
    except Exception as e:
        print(f"Error al seleccionar fila: {e}")