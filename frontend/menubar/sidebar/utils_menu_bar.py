from tkinter import ttk
import customtkinter as ctk

def configurar_treeview_claro() -> None:
    """
    Configura el estilo del Treeview para el modo claro.
    """
    style = ttk.Style()
    
    style.theme_use("clam")
    
    style.configure("Treeview", 
                    font=("Arial", 14),
                    rowheight=50,
                    background="#E5E5E5",
                    fieldbackground="#E5E5E5",
                    foreground="black")
    
    style.configure("Treeview.Heading", 
                    font=("Arial", 16, "bold"),
                    background="#329ADF",
                    foreground="white",
                    relief="flat")
    style.map('Treeview', background=[('selected', '#31AF9C')])
    style.map('Treeview.Heading', background=[('active', '#31AF9C')])

def configurar_treeview_oscuro() -> None:
    """
    Configura el estilo del Treeview para el modo oscuro.
    """
    style = ttk.Style()
    
    style.theme_use("clam")
    
    style.configure("Treeview", 
                    font=("Arial", 16),
                    rowheight=50,
                    background="#1c1c1c",
                    fieldbackground="#1c1c1c",
                    foreground="white")
    
    style.configure("Treeview.Heading", 
                    font=("Arial", 20, "bold"),
                    background="#329ADF",
                    foreground="white",
                    relief="flat")
    
    style.map('Treeview', background=[('selected', '#31AF9C')])
    style.map('Treeview.Heading', background=[('active', '#31AF9C')])

def limpiar_treeview(tree: ttk.Treeview) -> None:
    """
    Limpia el contenido del Treeview.

    Args:
        tree (ttk.Treeview): El Treeview a limpiar.

    Returns:
        None
    """
    for i in tree.get_children():
        tree.delete(i)

def configurar_insertar_columnas_treeview(tree: ttk.Treeview, columnas_nombres: list, ancho_columnas: dict) -> None:
    """
    Configura e inserta columnas en el Treeview.

    Args:
        tree (ttk.Treeview): El Treeview en el cual se insertarán las columnas.
        columnas_nombres (list): Lista de nombres de las columnas.
        ancho_columnas (dict): Diccionario con el ancho de cada columna.

    Returns:
        None
    """
    for columna in columnas_nombres:
        tree.column(columna, width=ancho_columnas.get(columna, 100), anchor="center")
        tree.heading(columna, text=columna)

def agregar_separador(frame: ctk.CTkFrame, fila: int) -> None:
    """
    Agrega un separador en el frame dado.

    Args:
        frame (ctk.CTkFrame): El frame donde se añadirá el separador.
        fila (int): La fila donde se ubicará el separador.

    Returns:
        None
    """
    separador = ctk.CTkFrame(frame, height=2, fg_color="black")
    separador.grid(row=fila, column=0, columnspan=2, sticky="nsew", pady=10, padx=20)
