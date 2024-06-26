from tkinter import messagebox
import customtkinter as ctk
from tkinter import ttk
def mostrar_error(titulo:str, mensaje:str)->None:
    """ Muestra error en un messagebox y en consola."""
    messagebox.showerror(titulo, mensaje)
    print(mensaje)
    
def configurar_ventana(base: ctk.CTk)->None:
    """ Se configurar la ventana principal de la aplicación."""
    ancho = base.winfo_screenwidth()
    alto = base.winfo_screenheight() - 65
    base.geometry(f"{ancho}x{alto}+0+0")
    
    base.state("zoomed")
    configurar_treeview_oscuro()
    
    
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

def limpiar_widgets_base(base:ctk.CTk)->None:
    """ Esta funcion elimina todos los widgets de la base."""
    for widget in base.winfo_children():
        widget.destroy()
        
def configurar_apariencia()->None:
    """ Se configura la apariencia de la aplicación."""
    ctk.set_appearance_mode("dark")  # light, dark
    ctk.set_default_color_theme("dark-blue")  # blue, green, dark-blue
    
def cambiar_color_texto(boton)->None:
    """ Cambia el color del texto de un widget."""
    if ctk.get_appearance_mode() == "Dark":
        boton.configure(text_color="white")
    else:
        boton.configure(text_color="black")