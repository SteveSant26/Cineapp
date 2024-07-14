import customtkinter as ctk
from tkinter import messagebox
from frontend.login import crear_login_img as CLI, crear_login
from backend.database import ejecutar_query_obtener, editar_usuario_bd,eliminar_usuario_bd
from frontend.utils import mostrar_error, mostrar_mensaje,limpiar_widgets_base,configurar_ventana_login
from frontend.cartelera import iniciar_hilo_mostrar_peliculas


def obtener_usuario_por_id(id_usuario:int)->tuple:
    """ Obtiene un usuario por su id"""
    query = "SELECT * FROM usuarios WHERE id = %s"
    return ejecutar_query_obtener(query, "usuarios",datos=(id_usuario,))[0]

def editar_perfil(base: ctk.CTk):
    frame_editar_perfil = ctk.CTkFrame(base, fg_color="transparent")
    frame_editar_perfil.pack(fill="both", expand=True)
    
    label_titulo = ctk.CTkLabel(frame_editar_perfil, text="Editar Perfil", font=("Arial", 30, "bold"))
    label_titulo.pack(pady=10)
    
    frame_formulario = ctk.CTkFrame(frame_editar_perfil)
    frame_formulario.pack(padx=10, pady=10)

    datos_usuario = obtener_usuario_por_id(base.usuario_id)
    
    label_nombre = ctk.CTkLabel(frame_formulario, text="Nombre:", font=("Arial", 16))
    label_nombre.grid(row=0, column=0, padx=15, pady=15,sticky="nsew")
    entry_nombre = ctk.CTkEntry(frame_formulario, width=150,font=("Arial", 16),)
    entry_nombre.grid(row=0, column=1, padx=15, pady=15,sticky="nsew")
    entry_nombre.insert(0, datos_usuario[1])
    
    label_apellido = ctk.CTkLabel(frame_formulario, text="Apellido:", font=("Arial", 16))
    label_apellido.grid(row=1, column=0, padx=15, pady=15,sticky="nsew",)
    entry_apellido = ctk.CTkEntry(frame_formulario, width=150,font=("Arial", 16),)
    entry_apellido.grid(row=1, column=1, padx=15, pady=15,sticky="nsew")
    entry_apellido.insert(0, datos_usuario[2])
    
    label_usuario = ctk.CTkLabel(frame_formulario, text="Usuario:", font=("Arial", 16))
    label_usuario.grid(row=2, column=0, padx=15, pady=15,sticky="nsew",)
    entry_usuario = ctk.CTkEntry(frame_formulario, width=150,font=("Arial", 16),)
    entry_usuario.grid(row=2, column=1, padx=15, pady=15,sticky="nsew")
    
    entry_usuario.insert(0, datos_usuario[3])
    
    
    label_contrasena = ctk.CTkLabel(frame_formulario, text="Contraseña:", font=("Arial", 16))
    label_contrasena.grid(row=3, column=0, padx=15, pady=15,sticky="nsew",)
    
    contrasena_frame = ctk.CTkFrame(frame_formulario, fg_color="transparent")
    contrasena_frame.grid(row=3, column=1, padx=15, pady=15,sticky="nsew")
    entry_contrasena = ctk.CTkEntry(contrasena_frame, width=150, show="*",font=("Arial", 16))
    entry_contrasena.pack(pady=5,side="left")
    entry_contrasena.insert(0, datos_usuario[4])
    CLI.boton_mostrar_contrasena(contrasena_frame,entry_contrasena)
    
    
    label_confirmar_contrasena = ctk.CTkLabel(frame_formulario, text="Confirmar contraseña:", font=("Arial", 16))
    label_confirmar_contrasena.grid(row=4, column=0, padx=15, pady=15,sticky="nsew",)
    
    confirmar_contrasena_frame = ctk.CTkFrame(frame_formulario, fg_color="transparent")
    confirmar_contrasena_frame.grid(row=4, column=1, padx=15, pady=15,sticky="nsew")
    entry_confirmar_contrasena = ctk.CTkEntry(confirmar_contrasena_frame, width=150, show="*",font=("Arial", 16),)
    entry_confirmar_contrasena.pack(pady=5,side="left")
    entry_confirmar_contrasena.insert(0, datos_usuario[4])
    CLI.boton_mostrar_contrasena(confirmar_contrasena_frame,entry_confirmar_contrasena)
    
    entries = [entry_nombre, entry_apellido, entry_usuario, entry_contrasena, entry_confirmar_contrasena]
    
    boton_guardar = ctk.CTkButton(frame_formulario, text="Guardar",
                                        hover_color="#31AF9C",
                                        fg_color="#329ADF",
                                        height=40,
                                        font=("Arial", 16,"bold"), command=lambda: guardar_cambios(base,entries))
    boton_guardar.grid(row=5, column=0, columnspan=2, pady=15)
    
    boton_eliminar = ctk.CTkButton(frame_formulario, text="Eliminar cuenta",
                                        hover_color="#31AF9C",
                                        fg_color="#329ADF",
                                        height=40,
                                        font=("Arial", 16,"bold"), command=lambda: eliminar_cuenta(base))
    boton_eliminar.grid(row=6, column=0, columnspan=2, pady=15)
    
def guardar_cambios(base,entries):
    """ Guarda los cambios en el perfil"""
    if messagebox.askyesno("Guardar cambios", "¿Estás seguro que deseas guardar los cambios?") == False:
        return
    nombre = entries[0].get().capitalize().strip()
    apellido = entries[1].get().capitalize().strip()
    usuario = entries[2].get().strip()
    contrasena = entries[3].get().strip()
    confirmar_contrasena = entries[4].get().strip()
    
    if contrasena != confirmar_contrasena:
        return mostrar_error("Error", "Las contraseñas no coinciden")
    
    if nombre == "" or apellido == "" or usuario == "" or contrasena == "":
        return mostrar_error("Error", "Todos los campos son requeridos")
    
    
    try:
        datos_usuario = (nombre, apellido, usuario, contrasena, base.usuario_id)    
        if editar_usuario_bd(datos_usuario):
            mostrar_mensaje("Éxito", "Usuario editado correctamente")
            iniciar_hilo_mostrar_peliculas(base)
        else:
            return
    except Exception as e:
        mostrar_error("Error", f"No se pudo editar el usuario: {e}")

def eliminar_cuenta(base):
    """ Elimina la cuenta del usuario"""
    if messagebox.askyesno("Eliminar cuenta", "¿Estás seguro que deseas eliminar tu cuenta?") == False:
        return
    try:
        if eliminar_usuario_bd(base.usuario_id):
            mostrar_mensaje("Éxito", "Usuario eliminado correctamente")
            limpiar_widgets_base(base)
            configurar_ventana_login(base)
            crear_login(base)
        else:
            return
    except Exception as e:
        mostrar_error("Error", f"No se pudo eliminar el usuario: {e}")
