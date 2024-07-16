import customtkinter as ctk

def inicializar_app() -> None:
    """
    Función para inicializar la aplicación.
    """
    from frontend import login, utils
    
    try:
        utils.configurar_tema_default()

        base = ctk.CTk()
        base.title("")

        base.resizable(False, False)
        
        # Se configura la apariencia de la ventana
        # Se crea el frame principal de la aplicación
        login.crear_login(base)
                
        base.mainloop()
    except Exception as e:
        utils.mostrar_error("Error al inicializar",
                      f"El siguiente error ocurrió al intentar crear la app:\n{e}")



if __name__ == "__main__":
    inicializar_app()