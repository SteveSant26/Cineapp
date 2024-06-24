from tkinter import messagebox
import customtkinter as ctk
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