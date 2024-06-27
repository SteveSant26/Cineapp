from tkinter import ttk
def configurar_treeview_claro()->None:
    """ Se configura el treeview de la aplicación."""
    style = ttk.Style()
    
    style.theme_use("clam")
    
    style.configure("Treeview", 
                    font=("Arial", 14),
                    rowheight=30,
                    background="#E5E5E5",
                    fieldbackground="#E5E5E5",
                    foreground="black")
    
    style.configure("Treeview.Heading", 
                    font=("Arial", 16, "bold"),
                    background="#329ADF",
                    foreground="white",
                    relief="flat")
    style.map('Treeview',background=[('selected', '#31AF9C')])
    style.map('Treeview.Heading',background=[('active', '#31AF9C')])

def configurar_treeview_oscuro()->None:
    """ Se configura el treeview de la aplicación."""
    style = ttk.Style()
    
    style.theme_use("clam")
    
    style.configure("Treeview", 
                    font=("Arial", 14),
                    rowheight=30,
                    background="#1c1c1c",
                    fieldbackground="#1c1c1c",
                    foreground="white")
    
    style.configure("Treeview.Heading", 
                    font=("Arial", 16, "bold"),
                    background="#329ADF",
                    foreground="white",
                    relief="flat")
    
    
    style.map('Treeview',background=[('selected', '#31AF9C')])
    style.map('Treeview.Heading',background=[('active', '#31AF9C')])
    
    
def limpiar_treeview(tree):
    """ Limpia el contenido del treeview."""
    for i in tree.get_children():
        tree.delete(i)
    
def configurar_insertar_columnas_treeview(tree, columnas_nombres,ancho_columnas):
    for columna in columnas_nombres:
        tree.column(columna, width=ancho_columnas.get(columna, 100), anchor="center")
        tree.heading(columna, text=columna)
