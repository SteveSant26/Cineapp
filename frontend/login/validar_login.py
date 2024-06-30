import customtkinter as ctk
from frontend import utils, cartelera

def validar_login(usuario_entry:ctk.CTkEntry,contrasena_entry:ctk.CTkEntry,base:ctk.CTk)->bool:

    """ Valida el login del usuario"""
    
    #Se obtiene el usuario y contraseña ingresados y se limpian los entrys
    # usuario = usuario_entry.get()
    # usuario_entry.delete(0, "end")
    # contrasena = contrasena_entry.get()
    # contrasena_entry.delete(0, "end")
    usuario = "admin"
    contrasena = "admin123"

    
    if usuario == "admin" and contrasena == "admin123":
        print("Usuario loggeado")
        
    
        utils.configurar_ventana(base)
        
        #Se llama la funcion de Cartelera.py para mostrar las peliculas
        cartelera.iniciar_hilo_mostrar_peliculas(base)
    else:
        utils.mostrar_error("Error de login", "Usuario o contraseña incorrectos")