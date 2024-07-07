import customtkinter as ctk

def toggle_password_visibility():
    """Toggle the visibility of the password entry."""
    if contrasena_entry.cget('show') == '*':
        contrasena_entry.configure(show='')
        toggle_button.configure(text="Ocultar")
    else:
        contrasena_entry.configure(show='*')
        toggle_button.configure(text="Mostrar")

# Crear la ventana principal
root = ctk.CTk()
root.geometry("300x200")

frame_login = ctk.CTkFrame(root)
frame_login.pack(padx=10, pady=10, expand=True, fill="both")

# Crear y posicionar el label y el entry de contraseña
contrasena_label = ctk.CTkLabel(frame_login, text="Contraseña:", font=("Arial", 16))
contrasena_label.pack(padx=10, pady=5)
contrasena_entry = ctk.CTkEntry(frame_login, width=200, show="*")
contrasena_entry.pack(padx=10, pady=5)

# Crear y posicionar el botón para mostrar/ocultar la contraseña
toggle_button = ctk.CTkButton(frame_login, text="Mostrar", command=toggle_password_visibility)
toggle_button.pack(padx=10, pady=5)

# Iniciar la aplicación
root.mainloop()