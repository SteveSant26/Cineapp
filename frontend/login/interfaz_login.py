import customtkinter as ctk
from . import validar_login as VL
from . import crear_login_img as CLI

def crear_login(base: ctk.CTk) -> ctk.CTkFrame:
    """ Se crea un frame para login en la ventana principal de la aplicación."""
    
    
    #Se crea el frame de login
    frame_login = ctk.CTkFrame(base, border_color="black", border_width=2)
    frame_login.pack(pady=10, padx=10,expand=True)

    #Se crea el titulo del login
    titulo_login = ctk.CTkLabel(frame_login, text="INTERCINES", font=("Arial", 30, "bold"), image=CLI.LOGIN_IMAGEN["imagen_login"], compound="bottom")
    titulo_login.pack(padx=10, pady=10)


    # Añadir entrybox para el nombre de usuario
    usuario_label = ctk.CTkLabel(frame_login, text="Usuario:", font=("Arial", 16))
    usuario_label.pack(padx=10, pady=5)

    usuario_entry = ctk.CTkEntry(frame_login, width=200)
    usuario_entry.pack(padx=10, pady=5)

    # Añadir entrybox para la contraseña
    contrasena_label = ctk.CTkLabel(frame_login, text="Contraseña:", font=("Arial", 16))
    contrasena_label.pack(padx=10, pady=5)
    contrasena_entry = ctk.CTkEntry(frame_login, width=200,show="*")
    contrasena_entry.pack(padx=10, pady=5)

    # Botón para iniciar sesión
    login_button = ctk.CTkButton(frame_login, 
                                 hover_color="#31AF9C",
                                 fg_color="#329ADF",
                                 text="Iniciar Sesión",
                                 font=("Arial", 16,"bold"),
                                 command=lambda:VL.validar_login(usuario_entry,contrasena_entry,base))
    login_button.pack(padx=10, pady=20)
    
    