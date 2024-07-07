from frontend.utils import conseguir_imagen_ctk
import customtkinter as ctk

LOGIN_RUTAS = {"login_path" : "frontend\\login\\img\\login.webp",
               "mostrar_oscuro_path" : "frontend\\login\\img\\mostrar_oscuro.png",
               "mostrar_claro_path" : "frontend\\login\\img\\mostrar_claro.png",
               "ocultar_oscuro_path" : "frontend\\login\\img\\ocultar_oscuro.png",
               "ocultar_claro_path" : "frontend\\login\\img\\ocultar_claro.png",}

LOGIN_IMAGENES = {"imagen_login":conseguir_imagen_ctk(LOGIN_RUTAS["login_path"], 350, 350),
                  "mostrar_contrasena": conseguir_imagen_ctk(LOGIN_RUTAS["mostrar_claro_path"], 20, 20,path_dark=LOGIN_RUTAS["mostrar_oscuro_path"]),
                  "ocultar_contrasena": conseguir_imagen_ctk(LOGIN_RUTAS["ocultar_claro_path"], 20, 20,path_dark=LOGIN_RUTAS["ocultar_oscuro_path"])}

def boton_mostrar_contrasena(frame,contrasena_entry):
    toggle_button = ctk.CTkButton(frame,fg_color="transparent", 
                                  image=LOGIN_IMAGENES["mostrar_contrasena"],
                                  hover_color="#31AF9C",
                                  text="",width=20, 
                                  command=lambda:mostrar_contrasena(contrasena_entry, toggle_button))
    
    toggle_button.pack(pady=5,side="left") 
    
    
def mostrar_contrasena(contrasena_entry, toggle_button):
    """Toggle the visibility of the password entry."""
    if contrasena_entry.cget('show') == '*':
        contrasena_entry.configure(show='')
        toggle_button.configure(image=LOGIN_IMAGENES["ocultar_contrasena"])
    else:
        contrasena_entry.configure(show='*')
        toggle_button.configure(image=LOGIN_IMAGENES["mostrar_contrasena"])