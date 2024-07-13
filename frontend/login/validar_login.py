import customtkinter as ctk
from backend.database import obtener_usuarios_bd
from frontend import utils, cartelera

def  validar_login(usuario_entry:ctk.CTkEntry,contrasena_entry:ctk.CTkEntry,base:ctk.CTk)->bool:

    """ Valida el login del usuario"""
    try:
        #Se obtiene el usuario y contraseña ingresados y se limpian los entrys
        # usuario = usuario_entry.get()
        # contrasena = contrasena_entry.get()
        
        
        #Admin para pruebas
        # usuario = "SteveSant"
        # contrasena = "bryan123"
        
        #Cliente para pruebas
        usuario = "Bryan26"
        contrasena = "bryan123"
        
        # usuario = "Saori"
        # contrasena = "sao123"

        # usuario = "Luis16"
        # contrasena = "lui123"

        # usuario = "Naomi"
        # contrasena = "nao123"


        for usuario_db in obtener_usuarios_bd():
            if usuario_db[3] == usuario and usuario_db[4] == contrasena:
            
            
                base.usuario = usuario_db[3]
                base.tipo_usuario = usuario_db[5]
                base.usuario_id = usuario_db[0]
                utils.configurar_ventana(base)
                
                usuario_entry.delete(0, "end")
                contrasena_entry.delete(0, "end")
                

                return cartelera.iniciar_hilo_mostrar_peliculas(base)
        else:
            return utils.mostrar_error("Error de login", "Usuario o contraseña incorrectos")
            
    except Exception as e:
        utils.mostrar_error("Error de login", f"Ocurrió un error al intentar validar el login:\n{e}")