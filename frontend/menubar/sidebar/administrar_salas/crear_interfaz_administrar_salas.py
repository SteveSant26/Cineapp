import customtkinter as ctk
from CTkSpinbox import CTkSpinbox
from tkinter import ttk
from ..utils_menu_bar import agregar_separador, configurar_insertar_columnas_treeview
from . import funciones_administrar_salas as FAS

def administrar_salas(base: ctk.CTk) -> None:
    """
    Crea la interfaz de administración de salas.

    Args:
        base (ctk.CTk): La ventana principal de la aplicación.

    Returns:
        None
    """
    frame_administrar_salas = ctk.CTkFrame(base, fg_color="transparent")
    frame_administrar_salas.pack(fill="both", expand=True)
    
    frame_administrar_salas.rowconfigure(0, weight=1)
    frame_administrar_salas.columnconfigure(0, weight=1)
    frame_administrar_salas.columnconfigure(1, weight=3)
    
    formulario_salas(frame_administrar_salas, base)
    treeview_salas(frame_administrar_salas, base)
    
    frame_administrar_salas.update()

def formulario_salas(frame_administrar_salas: ctk.CTkFrame, base: ctk.CTk) -> None:
    """
    Crea el formulario para administrar salas.

    Args:
        frame_administrar_salas (ctk.CTkFrame): El frame donde se colocará el formulario.
        base (ctk.CTk): La ventana principal de la aplicación.

    Returns:
        None
    """
    frame_formulario = ctk.CTkFrame(frame_administrar_salas, border_color="black", border_width=2, width=350)
    frame_formulario.grid(row=0, column=0, padx=5, pady=10, sticky="nsew")
    
    frame_formulario.columnconfigure(0, weight=1)
    frame_formulario.columnconfigure(1, weight=1)
    frame_formulario.grid_propagate(False)
    
    titulo = ctk.CTkLabel(frame_formulario, text="Administrar Salas", font=("Arial", 30, "bold"))
    titulo.grid(row=0, column=0, columnspan=2, pady=10, padx=10, sticky="nsew")
    
    agregar_separador(frame_formulario, 1)
    entries_datos_sala(frame_formulario, base)
    agregar_separador(frame_formulario, 6)
    colocar_boton_agregar_sala(frame_formulario, base)
    colocar_boton_editar_sala(frame_formulario, base)
    colocar_boton_eliminar_sala(frame_formulario, base)
    colocar_boton_salir(frame_formulario, base)
    
    frame_formulario.update()

def entries_datos_sala(frame_formulario: ctk.CTkFrame, base: ctk.CTk) -> None:
    """
    Crea los campos de entrada para los datos de las salas.

    Args:
        frame_formulario (ctk.CTkFrame): El frame donde se colocarán los campos de entrada.
        base (ctk.CTk): La ventana principal de la aplicación.

    Returns:
        None
    """
    label_id = ctk.CTkLabel(frame_formulario, text="ID Sala:", font=("Arial", 16))
    label_id.grid(row=2, column=0, pady=10, padx=20)
    entry_id = ctk.CTkEntry(frame_formulario, font=("Arial", 16))
    entry_id.grid(row=2, column=1, pady=10, padx=20, sticky="nsew")
    
    label_nombre = ctk.CTkLabel(frame_formulario, text="Nombre Sala:", font=("Arial", 16))
    label_nombre.grid(row=3, column=0, pady=10, padx=20)
    entry_nombre = ctk.CTkEntry(frame_formulario, font=("Arial", 16))
    entry_nombre.grid(row=3, column=1, pady=10, padx=20, sticky="nsew")
    
    label_filas = ctk.CTkLabel(frame_formulario, text="Filas sala:", font=("Arial", 16))
    label_filas.grid(row=4, column=0, pady=10, padx=20)
    spinbox_filas = CTkSpinbox(frame_formulario, min_value=1, max_value=10, start_value=4, button_color="#329ADF", button_hover_color="#31AF9C", font=("Arial", 16))
    spinbox_filas.grid(row=4, column=1, pady=10, padx=20, sticky="nsew")
    
    label_columnas = ctk.CTkLabel(frame_formulario, text="Columnas sala:", font=("Arial", 16))
    label_columnas.grid(row=5, column=0, pady=10, padx=20)
    spinbox_columnas = CTkSpinbox(frame_formulario, min_value=1, max_value=10, start_value=4, button_color="#329ADF", button_hover_color="#31AF9C", font=("Arial", 16))
    spinbox_columnas.grid(row=5, column=1, pady=10, padx=20, sticky="nsew")
    
    base.entries_salas = {
        "id": entry_id,
        "nombre": entry_nombre,
        "filas": spinbox_filas,
        "columnas": spinbox_columnas
    }

def colocar_boton_agregar_sala(frame_formulario: ctk.CTkFrame, base: ctk.CTk) -> None:
    """
    Coloca el botón para agregar una sala.

    Args:
        frame_formulario (ctk.CTkFrame): El frame donde se colocará el botón.
        base (ctk.CTk): La ventana principal de la aplicación.

    Returns:
        None
    """
    boton_agregar_sala = ctk.CTkButton(frame_formulario, text="Agregar Sala", fg_color="#329ADF", hover_color="#31AF9C", font=("Arial", 20, "bold"), command=lambda: FAS.agregar_sala(base))
    boton_agregar_sala.grid(row=7, columnspan=2, column=0, pady=10, padx=20, sticky="nsew")

def colocar_boton_editar_sala(frame_formulario: ctk.CTkFrame, base: ctk.CTk) -> None:
    """
    Coloca el botón para editar una sala.

    Args:
        frame_formulario (ctk.CTkFrame): El frame donde se colocará el botón.
        base (ctk.CTk): La ventana principal de la aplicación.

    Returns:
        None
    """
    boton_editar_sala = ctk.CTkButton(frame_formulario, text="Editar Sala", fg_color="#329ADF", hover_color="#31AF9C", font=("Arial", 20, "bold"), command=lambda: FAS.editar_sala(base))
    boton_editar_sala.grid(row=8, columnspan=2, column=0, pady=10, padx=20, sticky="nsew")

def colocar_boton_eliminar_sala(frame_formulario: ctk.CTkFrame, base: ctk.CTk) -> None:
    """
    Coloca el botón para eliminar una sala.

    Args:
        frame_formulario (ctk.CTkFrame): El frame donde se colocará el botón.
        base (ctk.CTk): La ventana principal de la aplicación.

    Returns:
        None
    """
    boton_eliminar_sala = ctk.CTkButton(frame_formulario, text="Eliminar Sala", fg_color="#329ADF", hover_color="#31AF9C", font=("Arial", 20, "bold"), command=lambda: FAS.eliminar_sala(base))
    boton_eliminar_sala.grid(row=9, columnspan=2, column=0, pady=10, padx=20, sticky="nsew")

def colocar_boton_salir(frame_formulario: ctk.CTkFrame, base: ctk.CTk) -> None:
    """
    Coloca el botón para volver a la vista anterior.

    Args:
        frame_formulario (ctk.CTkFrame): El frame donde se colocará el botón.
        base (ctk.CTk): La ventana principal de la aplicación.

    Returns:
        None
    """
    boton_volver = ctk.CTkButton(frame_formulario, text="Volver", fg_color="#329ADF", hover_color="#31AF9C", font=("Arial", 20, "bold"), command=lambda: FAS.volver(base))
    boton_volver.grid(row=10, columnspan=2, column=0, pady=10, padx=20, sticky="nsew")

def treeview_salas(frame_administrar_salas: ctk.CTkFrame, base: ctk.CTk) -> None:
    """
    Crea el Treeview para mostrar las salas.

    Args:
        frame_administrar_salas (ctk.CTkFrame): El frame donde se colocará el Treeview.
        base (ctk.CTk): La ventana principal de la aplicación.

    Returns:
        None
    """
    frame_tree = ctk.CTkFrame(frame_administrar_salas, border_color="black", border_width=2, width=800)
    frame_tree.grid(row=0, column=1, padx=5, pady=10, sticky="nsew")
    frame_tree.grid_propagate(False)

    columnas_nombres = [key.capitalize() for key in base.entries_salas.keys()]
    
    base.tree_salas = ttk.Treeview(frame_tree, columns=columnas_nombres, show="headings")
    
    ancho_columnas = {
        "Id": 50,
        "Nombre": 300,
        "Filas": 300,
        "Columnas": 300
    }
    
    configurar_insertar_columnas_treeview(base.tree_salas, columnas_nombres, ancho_columnas)
    
    base.tree_salas.pack(fill="both", expand=True, padx=10, pady=10)
    base.tree_salas.pack_propagate(False)
    
    base.tree_salas.bind("<<TreeviewSelect>>", lambda event: seleccionar_fila(event, base, base.tree_salas))
    
    FAS.insertar_salas_tree(base.tree_salas)    
    frame_tree.update()

def seleccionar_fila(event: object, base: ctk.CTk, tree: ttk.Treeview) -> None:
    """
    Selecciona una fila en el Treeview y muestra los datos en los campos de entrada.

    Args:
        event (object): El evento de selección.
        base (ctk.CTk): La ventana principal de la aplicación.
        tree (ttk.Treeview): El Treeview con las salas.

    Returns:
        None
    """
    try:
        item_seleccionado = tree.focus()
        values = tree.item(item_seleccionado)["values"]
        if values:
            base.entries_salas["id"].delete(0, "end")
            base.entries_salas["nombre"].delete(0, "end")

            base.entries_salas["id"].insert(0, values[0])
            base.entries_salas["nombre"].insert(0, values[1])
            
            base.entries_salas["filas"].set(values[2])
            base.entries_salas["columnas"].set(values[3])
            
    except Exception as e:
        print(f"Error al seleccionar la fila: {e}")
