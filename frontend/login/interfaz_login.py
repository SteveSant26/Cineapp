import customtkinter as ctk
from . import validar_login as VL
from . import nueva_cuenta as NC
from . import crear_login_img as CLI

def crear_login(base: ctk.CTk) -> ctk.CTkFrame:
    """ Se crea un frame para login en la ventana principal de la aplicación."""

    
    #Se crea el frame de login
    frame_login = ctk.CTkFrame(base, border_color="black", border_width=2)
    frame_login.pack(pady=10, padx=10,expand=True)

    #Se crea el titulo del login
    titulo_login = ctk.CTkLabel(frame_login, text="INTERCINES", font=("Arial", 30, "bold"), image=CLI.LOGIN_IMAGENES["imagen_login"], compound="bottom")
    titulo_login.pack(padx=10, pady=10)


    # Añadir entrybox para el nombre de usuario
    usuario_label = ctk.CTkLabel(frame_login, text="Usuario:", font=("Arial", 16))
    usuario_label.pack(padx=10, pady=5)

    usuario_entry = ctk.CTkEntry(frame_login, width=200)
    usuario_entry.pack(padx=10, pady=5)

    # Añadir entrybox para la contraseña
    contrasena_label = ctk.CTkLabel(frame_login, text="Contraseña:", font=("Arial", 16))
    contrasena_label.pack(padx=10, pady=5)
    
    contrasena_frame = ctk.CTkFrame(frame_login, fg_color="transparent")
    contrasena_frame.pack(padx=10, pady=5,expand=True)
    
    contrasena_entry = ctk.CTkEntry(contrasena_frame, width=200,show="*")
    contrasena_entry.pack(padx=(35,0), pady=5,side="left")

    CLI.boton_mostrar_contrasena(contrasena_frame,contrasena_entry)


    # Botón para iniciar sesión
    iniciar_sesion_boton = ctk.CTkButton(frame_login, 
                                 hover_color="#31AF9C",
                                 fg_color="#329ADF",
                                 text="Iniciar Sesión",
                                 font=("Arial", 16,"bold"),
                                 command=lambda:VL.validar_login(usuario_entry,contrasena_entry,base))
    iniciar_sesion_boton.pack(padx=10, pady=(20,10))
    
    
    crear_cuenta_boton = ctk.CTkButton(frame_login,
                                hover_color="#31AF9C",
                                fg_color="#329ADF",
                                text="Crear cuenta",
                                font=("Arial", 16,"bold"),
                                command=lambda:NC.crear_frame_crear_cuenta(base))
    crear_cuenta_boton.pack(padx=10, pady=(10,20))
    

