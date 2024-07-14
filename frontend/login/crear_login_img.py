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

def boton_mostrar_contrasena(frame, contrasena_entry):
    """
    Función que crea un botón para mostrar la contraseña en un campo de entrada.

    Parámetros:
    - frame: El marco en el que se colocará el botón.
    - contrasena_entry: El campo de entrada de contraseña.

    Retorna:
    None
    """
    
    boton_mostrar = ctk.CTkButton(frame, fg_color="transparent", 
                                  image=LOGIN_IMAGENES["mostrar_contrasena"],
                                  hover_color="#31AF9C",
                                  text="", width=20, 
                                  command=lambda: mostrar_contrasena(contrasena_entry, boton_mostrar))
    
    boton_mostrar.pack(pady=5, side="left")
    
    
def mostrar_contrasena(contrasena_entry, boton_mostrar):
    """
    Muestra u oculta la contraseña en el campo de entrada de contraseña.

    Parámetros:
    contrasena_entry (tkinter.Entry): El campo de entrada de contraseña.
    boton_mostrar (tkinter.Button): El botón para mostrar u ocultar la contraseña.

    """
    if contrasena_entry.cget('show') == '*':
        contrasena_entry.configure(show='')
        boton_mostrar.configure(image=LOGIN_IMAGENES["ocultar_contrasena"])
    else:
        contrasena_entry.configure(show='*')
        boton_mostrar.configure(image=LOGIN_IMAGENES["mostrar_contrasena"])