from tkinter import messagebox

import customtkinter as ctk

def mostrar_error(titulo:str, mensaje:str)->None:
    """ Muestra error en un messagebox y en consola."""
    messagebox.showerror(titulo, mensaje)
    print(mensaje)
def mostrar_mensaje(titulo:str, mensaje:str)->None:
    """ Muestra mensaje en un messagebox y en consola."""
    messagebox.showinfo(titulo, mensaje)
    print(mensaje)
    
def configurar_ventana_login(base: ctk.CTk)->None:
    """ Se configura la ventana principal de la aplicación para el login."""
    limpiar_widgets_base(base)
    base.geometry("400x700")
    base.state("normal")
    base.resizable(False, False)
    
def configurar_ventana(base: ctk.CTk)->None:
    """ Se configurar la ventana principal de la aplicación para la interfaz principal."""
    from frontend.menubar.sidebar import configurar_treeview_oscuro, configurar_treeview_claro
    
    ancho = base.winfo_screenwidth()
    alto = base.winfo_screenheight() - 65
    base.geometry(f"{ancho}x{alto}+0+0")
    
    base.state("zoomed")
    if ctk.get_appearance_mode().lower() == "light":
        configurar_treeview_claro()
    else:
        configurar_treeview_oscuro()

def limpiar_widgets_base(base:ctk.CTk)->None:
    """ Esta funcion elimina todos los widgets de un widget padre."""
    for widget in base.winfo_children():
        widget.destroy()
        
def configurar_tema_default()->None:
    """ Se configura la apariencia de la aplicación."""
    ctk.set_appearance_mode("dark")  # light, dark
    ctk.set_default_color_theme("dark-blue")  # blue, green, dark-blue
