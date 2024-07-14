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



# [{"user": "Bryan26", "asientos": [[2, 4], [3, 4], [2, 6], [3, 6], [2, 5], [3, 5]]}, 
#  {"user": "SteveSant", "asientos": [[3, 8], [2, 7], [3, 7], [2, 8]]}, 
#  {"user": "Saori", "asientos": [[2, 7], [3, 7], [2, 6], [3, 6], [2, 5]]}]