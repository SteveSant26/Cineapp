import customtkinter as ctk
from tkinter import ttk
from tkcalendar import DateEntry
from CTkSpinbox import *
from .utils_administrar_funciones import obtener_id_nombre_sala_bd, obtener_titulo_pelicula_por_id, obtener_nombre_sala_por_id
from . import funciones_administrar_funciones as FAF
from ..utils_menu_bar import agregar_separador, configurar_insertar_columnas_treeview
from backend.database import ejecutar_query_obtener


def obtener_id_titulo_pelicula_bd() -> list:
    """
    Obtiene una lista con los IDs y títulos de todas las películas.

    Returns:
        list: Una lista de tuplas con los IDs y títulos de las películas.
    """
    query = "SELECT id, titulo FROM peliculas"
    return ejecutar_query_obtener(query, "peliculas")

def administrar_funciones(base: ctk.CTk) -> None:
    """
    Crea la interfaz para administrar funciones.

    Args:
        base (ctk.CTk): La ventana principal de la aplicación.

    Returns:
        None
    """
    frame_administrar_funciones = ctk.CTkFrame(base, fg_color="transparent")
    frame_administrar_funciones.pack(fill="both", expand=True)
    
    frame_administrar_funciones.rowconfigure(0, weight=1)
    frame_administrar_funciones.columnconfigure(0, weight=1)
    frame_administrar_funciones.columnconfigure(1, weight=3)
    
    formulario_funciones(frame_administrar_funciones, base)
    treeview_funciones(frame_administrar_funciones, base)
    
    frame_administrar_funciones.update()

def formulario_funciones(frame_administrar_funciones: ctk.CTkFrame, base: ctk.CTk) -> None:
    """
    Crea el formulario para administrar funciones.

    Args:
        frame_administrar_funciones (ctk.CTkFrame): El frame donde se colocará el formulario.
        base (ctk.CTk): La ventana principal de la aplicación.

    Returns:
        None
    """
    frame_formulario = ctk.CTkFrame(frame_administrar_funciones, border_color="black", border_width=2, width=350)
    frame_formulario.grid(row=0, column=0, padx=5, pady=10, sticky="nsew")
    
    frame_formulario.columnconfigure(0, weight=1)
    frame_formulario.columnconfigure(1, weight=1)
    frame_formulario.grid_propagate(False)
    
    titulo = ctk.CTkLabel(frame_formulario, text="Administrar funciones", font=("Arial", 30, "bold"))
    titulo.grid(row=0, column=0, columnspan=2, pady=10, padx=10, sticky="nsew")
    
    agregar_separador(frame_formulario, 1)
    entries_datos_funcion(frame_formulario, base)
    agregar_separador(frame_formulario, 7)
    colocar_boton_agregar_funcion(frame_formulario, base)
    colocar_boton_editar_funcion(frame_formulario, base)
    colocar_boton_eliminar_funcion(frame_formulario, base)
    colocar_boton_salir(frame_formulario, base)
    
    frame_formulario.update()

def entries_datos_funcion(frame_formulario: ctk.CTkFrame, base: ctk.CTk) -> None:
    """
    Crea los campos de entrada para los datos de las funciones.

    Args:
        frame_formulario (ctk.CTkFrame): El frame donde se colocarán los campos de entrada.
        base (ctk.CTk): La ventana principal de la aplicación.

    Returns:
        None
    """
    label_id = ctk.CTkLabel(frame_formulario, text="ID Función:", font=("Arial", 16))
    label_id.grid(row=2, column=0, pady=10, padx=20)
    entry_id = ctk.CTkEntry(frame_formulario, font=("Arial", 16))
    entry_id.grid(row=2, column=1, pady=10, padx=20, sticky="nsew")
    
    label_id_pelicula = ctk.CTkLabel(frame_formulario, text="ID Película:", font=("Arial", 16))   
    label_id_pelicula.grid(row=3, column=0, pady=10, padx=20)
    
    id_peliculas = [f"{id[0]} - {id[1]}" for id in obtener_id_titulo_pelicula_bd()]
    
    combobox_id_pelicula = ctk.CTkComboBox(frame_formulario, font=("Arial", 16), values=id_peliculas)
    combobox_id_pelicula.grid(row=3, column=1, pady=10, padx=20, sticky="nsew")
    combobox_id_pelicula.set("")
    
    label_id_sala = ctk.CTkLabel(frame_formulario, text="ID Sala:", font=("Arial", 16))
    label_id_sala.grid(row=4, column=0, pady=10, padx=20)
    
    id_salas = [f"{id[0]} - {id[1]}" for id in obtener_id_nombre_sala_bd()]
    
    combobox_id_sala = ctk.CTkComboBox(frame_formulario, font=("Arial", 16), values=id_salas)
    combobox_id_sala.grid(row=4, column=1, pady=10, padx=20, sticky="nsew")
    combobox_id_sala.set("")
    
    label_hora = ctk.CTkLabel(frame_formulario, text="Hora:", font=("Arial", 16))
    label_hora.grid(row=6, column=0, pady=10, padx=20)
    frame_hora = ctk.CTkFrame(frame_formulario)
    frame_hora.grid(row=6, column=1, pady=10)

    spinbox_hora = CTkSpinbox(frame_hora, min_value=0, max_value=23, button_color="#329ADF", button_hover_color="#31AF9C", font=("Arial", 16))
    spinbox_hora.pack(side="left")

    spinbox_minuto = CTkSpinbox(frame_hora, min_value=0, max_value=59, button_color="#329ADF", button_hover_color="#31AF9C", font=("Arial", 16))
    spinbox_minuto.pack(side="left")
    
    base.entries_funciones = {
        "id": entry_id,
        "id pelicula": combobox_id_pelicula,
        "id sala": combobox_id_sala,
        "hora": spinbox_hora,
        "minuto": spinbox_minuto,
    }
    
def colocar_boton_agregar_funcion(frame_formulario: ctk.CTkFrame, base: ctk.CTk) -> None:
    """
    Coloca el botón para agregar una función.

    Args:
        frame_formulario (ctk.CTkFrame): El frame donde se colocará el botón.
        base (ctk.CTk): La ventana principal de la aplicación.

    Returns:
        None
    """
    boton_agregar_funcion = ctk.CTkButton(frame_formulario, text="Agregar función", fg_color="#329ADF", hover_color="#31AF9C", font=("Arial", 20, "bold"), command=lambda: FAF.agregar_funcion(base))
    boton_agregar_funcion.grid(row=8, columnspan=2, column=0, pady=10, padx=20, sticky="nsew")
    
def colocar_boton_editar_funcion(frame_formulario: ctk.CTkFrame, base: ctk.CTk) -> None:
    """
    Coloca el botón para editar una función.

    Args:
        frame_formulario (ctk.CTkFrame): El frame donde se colocará el botón.
        base (ctk.CTk): La ventana principal de la aplicación.

    Returns:
        None
    """
    boton_editar_funcion = ctk.CTkButton(frame_formulario, text="Editar Función", fg_color="#329ADF", hover_color="#31AF9C", font=("Arial", 20, "bold"), command=lambda: FAF.editar_funcion(base))
    boton_editar_funcion.grid(row=9, columnspan=2, column=0, pady=10, padx=20, sticky="nsew")

def colocar_boton_eliminar_funcion(frame_formulario: ctk.CTkFrame, base: ctk.CTk) -> None:
    """
    Coloca el botón para eliminar una función.

    Args:
        frame_formulario (ctk.CTkFrame): El frame donde se colocará el botón.
        base (ctk.CTk): La ventana principal de la aplicación.

    Returns:
        None
    """
    boton_eliminar_funcion = ctk.CTkButton(frame_formulario, text="Eliminar Función", fg_color="#329ADF", hover_color="#31AF9C", font=("Arial", 20, "bold"), command=lambda: FAF.eliminar_funcion(base))
    boton_eliminar_funcion.grid(row=10, columnspan=2, column=0, pady=10, padx=20, sticky="nsew")

def colocar_boton_salir(frame_formulario: ctk.CTkFrame, base: ctk.CTk) -> None:
    """
    Coloca el botón para volver a la vista anterior.

    Args:
        frame_formulario (ctk.CTkFrame): El frame donde se colocará el botón.
        base (ctk.CTk): La ventana principal de la aplicación.

    Returns:
        None
    """
    boton_volver = ctk.CTkButton(frame_formulario, text="Volver", fg_color="#329ADF", hover_color="#31AF9C", font=("Arial", 20, "bold"), command=lambda: FAF.volver(base))
    boton_volver.grid(row=11, columnspan=2, column=0, pady=10, padx=20, sticky="nsew")

def treeview_funciones(frame_administrar_funciones: ctk.CTkFrame, base: ctk.CTk) -> None:
    """
    Crea el Treeview para mostrar las funciones.

    Args:
        frame_administrar_funciones (ctk.CTkFrame): El frame donde se colocará el Treeview.
        base (ctk.CTk): La ventana principal de la aplicación.

    Returns:
        None
    """
    frame_tree = ctk.CTkFrame(frame_administrar_funciones, border_color="black", border_width=2, width=800)
    frame_tree.grid(row=0, column=1, padx=5, pady=10, sticky="nsew")
    frame_tree.grid_propagate(False)

    columnas_nombres = [key.capitalize() for key in base.entries_funciones.keys() if key != "hora" and key != "minuto"] + ["Hora"]
    
    ancho_columnas = {
        "Id": 100,
        "Id Película": 100,
        "Id Sala": 100,
        "Fecha y Hora": 300
    }
        
    base.tree_funciones = ttk.Treeview(frame_tree, columns=columnas_nombres, show="headings")
    base.tree_funciones.pack(fill="both", expand=True, padx=10, pady=10)
    base.tree_funciones.pack_propagate(False)
    
    base.tree_funciones.bind("<<TreeviewSelect>>", lambda event: seleccionar_fila(event, base.entries_funciones, base.tree_funciones))
    
    configurar_insertar_columnas_treeview(base.tree_funciones, columnas_nombres, ancho_columnas)
    FAF.insertar_funciones_tree(base.tree_funciones)
    
    frame_tree.update()

def seleccionar_fila(event: object, entries: dict, tree: ttk.Treeview) -> None:
    """
    Selecciona una fila en el Treeview y muestra los datos en los campos de entrada.

    Args:
        event (object): El evento de selección.
        entries (dict): Los campos de entrada de la función.
        tree (ttk.Treeview): El Treeview con las funciones.

    Returns:
        None
    """
    try:
        if not tree.selection():
            return

        item_seleccionado = tree.focus()
        values = tree.item(item_seleccionado)["values"]
        
        entries["id"].delete(0, "end")
        entries["id"].insert(0, values[0])

        nombre_pelicula_resultado = obtener_titulo_pelicula_por_id(values[1])
        nombre_pelicula = nombre_pelicula_resultado[0][0]
        titulo_id_pelicula = f"{values[1]} - {nombre_pelicula}"
        entries["id pelicula"].set(titulo_id_pelicula)

        nombre_sala_resultado = obtener_nombre_sala_por_id(values[2])
        nombre_sala = nombre_sala_resultado[0][0]
        nombre_id_sala = f"{values[2]} - {nombre_sala}"
        entries["id sala"].set(nombre_id_sala)

        hora = values[3]
        horas = int(hora.split(":")[0])
        minutos = int(hora.split(":")[1])
        
        entries["hora"].set(horas)
        entries["minuto"].set(minutos)
    except Exception as e:
        print(f"Error al seleccionar fila: {e}")
