import customtkinter as ctk

def inicializar_app():
    """ 
    Inicializa la aplicación de la sala de cines.
    Creo diferentes instancias de base para el manejo mas sencillo de las ventanas.
    
    base.titulo_pelicula
    base.frame_opciones_sala
    base.frame_opciones
    base.frame_sala
    base.filas_sala
    base.columnas_sala
    base.combobox_salas
    base.sala_actual
    base.frame_funciones
    base.botones_funciones':
    base.funciones
    base.funcion_actual
    base.salas
    base.mejor_asiento
    base.frame_peliculas
    base.frame_funciones
    base.menu_bar_frame
    base.toggle_menu
    base.desplegar_menu_boton
    base.boton_barra_de_busqueda
    
    """
    from frontend import login,utils
    
    try:
        utils.configurar_apariencia()

        
        base = ctk.CTk()
        base.title("")

        base.resizable(False, False)
        
        
        #Se configura la apariencia de la ventana
        #Se crea el frame principal de la aplicación
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