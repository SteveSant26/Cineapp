import customtkinter as ctk

from frontend import utils, cartelera
from backend.database import obtener_usuarios_bd

def validar_login(usuario_entry: ctk.CTkEntry, contrasena_entry: ctk.CTkEntry, base: ctk.CTk) -> bool:
    """
    Valida las credenciales de inicio de sesión ingresadas por el usuario.

    Args:
        usuario_entry (ctk.CTkEntry): El campo de entrada para el nombre de usuario.
        contrasena_entry (ctk.CTkEntry): El campo de entrada para la contraseña.
        base (ctk.CTk): La ventana base de la aplicación.

    Returns:
        bool: True si el inicio de sesión es exitoso, False en caso contrario.
    """
    try:
        # Obtener el nombre de usuario y la contraseña ingresados y limpiar los campos de entrada
        usuario = usuario_entry.get()
        contrasena = contrasena_entry.get()



        #Admin para pruebas
        usuario = "SteveSant"
        contrasena = "bryan123"
        
        #Cliente para pruebas
        # usuario = "Bryan26"
        # contrasena = "bryan123"
        
        # usuario = "Saori"
        # contrasena = "sao123"

        # usuario = "Luis16"
        # contrasena = "lui123"

        # usuario = "Naomi"
        # contrasena = "nao123"
        
        
        for usuario_db in obtener_usuarios_bd():
            if usuario_db[3] == usuario and usuario_db[4] == contrasena:
                # Establecer la información del usuario en la ventana base
                base.usuario = usuario_db[3]
                base.tipo_usuario = usuario_db[5]
                base.usuario_id = usuario_db[0]
                utils.configurar_ventana(base)

                usuario_entry.delete(0, "end")
                contrasena_entry.delete(0, "end")
                if base.tipo_usuario == "cliente":
                    base.title("INTERCINES - Cliente")
                else:
                    base.title("INTERCINES - Administrador")

                return cartelera.iniciar_hilo_mostrar_peliculas(base)
        else:
            return utils.mostrar_error("Error de inicio de sesión", "Usuario o contraseña incorrectos")

    except Exception as e:
        utils.mostrar_error("Error de inicio de sesión", f"Ocurrió un error al intentar validar el inicio de sesión:\n{e}")