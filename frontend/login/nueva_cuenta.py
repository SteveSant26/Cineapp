import customtkinter as ctk
from frontend.utils import mostrar_error,mostrar_mensaje
from backend.database import agregar_usuario_bd,obtener_usuarios_bd
from . import crear_login_img as CLI

def crear_frame_crear_cuenta(base):
    ventana_crear_cuenta = ctk.CTkToplevel(base)
    ventana_crear_cuenta.title("Crear cuenta")
    ventana_crear_cuenta.geometry("450x450")
    ventana_crear_cuenta.resizable(False, False)
    ventana_crear_cuenta.transient(base)
    
    opciones_crear_cuenta(ventana_crear_cuenta)

def opciones_crear_cuenta(ventana_crear_cuenta):
    frame_formulario = ctk.CTkFrame(ventana_crear_cuenta)
    frame_formulario.pack(padx=10, pady=10,expand=True, fill="both")

    
    label_nombre = ctk.CTkLabel(frame_formulario, text="Nombre:", font=("Arial", 16))
    label_nombre.grid(row=0, column=0, padx=15, pady=15,sticky="nsew")
    entry_nombre = ctk.CTkEntry(frame_formulario, width=150)
    entry_nombre.grid(row=0, column=1, padx=15, pady=15,sticky="nsew")
    
    label_apellido = ctk.CTkLabel(frame_formulario, text="Apellido:", font=("Arial", 16))
    label_apellido.grid(row=1, column=0, padx=15, pady=15,sticky="nsew",)
    entry_apellido = ctk.CTkEntry(frame_formulario, width=150)
    entry_apellido.grid(row=1, column=1, padx=15, pady=15,sticky="nsew")
    
    label_usuario = ctk.CTkLabel(frame_formulario, text="Usuario:", font=("Arial", 16))
    label_usuario.grid(row=2, column=0, padx=15, pady=15,sticky="nsew",)
    entry_usuario = ctk.CTkEntry(frame_formulario, width=150)
    entry_usuario.grid(row=2, column=1, padx=15, pady=15,sticky="nsew")
    
    
    label_contrasena = ctk.CTkLabel(frame_formulario, text="Contraseña:", font=("Arial", 16))
    label_contrasena.grid(row=3, column=0, padx=15, pady=15,sticky="nsew",)
    
    contrasena_frame = ctk.CTkFrame(frame_formulario, fg_color="transparent")
    contrasena_frame.grid(row=3, column=1, padx=15, pady=15,sticky="nsew")
    
    entry_contrasena = ctk.CTkEntry(contrasena_frame, width=150, show="*")
    entry_contrasena.pack(pady=5,side="left")
    CLI.boton_mostrar_contrasena(contrasena_frame,entry_contrasena)
    
    
    label_confirmar_contrasena = ctk.CTkLabel(frame_formulario, text="Confirmar contraseña:", font=("Arial", 16))
    label_confirmar_contrasena.grid(row=4, column=0, padx=15, pady=15,sticky="nsew",)
    
    
    confirmar_contrasena_frame = ctk.CTkFrame(frame_formulario, fg_color="transparent")
    confirmar_contrasena_frame.grid(row=4, column=1, padx=15, pady=15,sticky="nsew")
    
    entry_confirmar_contrasena = ctk.CTkEntry(confirmar_contrasena_frame, width=150, show="*")
    entry_confirmar_contrasena.pack(pady=5,side="left")
    
    CLI.boton_mostrar_contrasena(confirmar_contrasena_frame,entry_confirmar_contrasena)
    
    label_tipo_usuario = ctk.CTkLabel(frame_formulario, text="Tipo de usuario:", font=("Arial", 16))
    label_tipo_usuario.grid(row=5, column=0, padx=15, pady=15,sticky="nsew",)
    
    combobox_tipo_usuario = ctk.CTkComboBox(frame_formulario, values=["Admin", "Cliente"], width=150)
    combobox_tipo_usuario.grid(row=5, column=1, padx=15, pady=15,sticky="nsew")
    
    entries = [entry_nombre, entry_apellido, entry_usuario, entry_contrasena, entry_confirmar_contrasena, combobox_tipo_usuario]
    boton_crear_cuenta = ctk.CTkButton(frame_formulario,
                                        hover_color="#31AF9C",
                                        fg_color="#329ADF",
                                        text="Crear cuenta",
                                        height=40,
                                        font=("Arial", 16,"bold"),
                                        command=lambda:validar_datos(entries,ventana_crear_cuenta))
    boton_crear_cuenta.grid(row=6, column=0,columnspan =2, sticky="nsew", padx=30, pady=15)

def validar_datos(entries,ventana_crear_cuenta):
    try:
        nombre = entries[0].get().capitalize().strip()
        apellido = entries[1].get().capitalize().strip()
        usuario = entries[2].get().strip()
        contrasena = entries[3].get().strip()
        confirmar_contrasena = entries[4].get().strip()
        tipo_usuario = entries[5].get()
        
        if nombre == "" or apellido == "" or usuario == "" or contrasena == "" or confirmar_contrasena == "":
            mostrar_error("Error", "Todos los campos son obligatorios")
            return
        
        if contrasena == confirmar_contrasena:
            if usuario.lower() not in [usuario[3].lower() for usuario in obtener_usuarios_bd()]:
                datos = (nombre, apellido, usuario, contrasena, tipo_usuario)
                agregar_usuario_bd(datos)
                mostrar_mensaje("Cuenta creada", f"La cuenta de {tipo_usuario} con el usuario {usuario} ha sido creada exitosamente")
                for entry in entries:
                    if entry == entries[-1]:
                        entry.set("Admin")
                        continue
                    entry.delete(0, "end")
                ventana_crear_cuenta.destroy()
            else:
                mostrar_error("Error", "El usuario ya existe")
                return
        else:
            mostrar_error("Error", "Las contraseñas no coinciden")
            return
    except Exception as e:
        mostrar_error("Error", f"Ocurrió un error al validar los datos: {e}")
        return