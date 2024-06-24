from frontend.utils import conseguir_imagen_ctk 

RUTA_ASIENTOS = {
                 "asiento_libre_path": "C:\\Users\\Bryan\\OneDrive - ULEAM\\Tareas\\Segundo semestre\\Programacion estructurada\\Cine\\frontend\\Pantalla_cine\\Asientos\\Asientos_img\\asiento_libre.png",
                 "asiento_seleccionado_path": "C:\\Users\\Bryan\\OneDrive - ULEAM\\Tareas\\Segundo semestre\\Programacion estructurada\\Cine\\frontend\\Pantalla_cine\\Asientos\\Asientos_img\\asiento_hover.png",
                 "asiento_mejor_path": "C:\\Users\\Bryan\\OneDrive - ULEAM\\Tareas\\Segundo semestre\\Programacion estructurada\\Cine\\frontend\\Pantalla_cine\\Asientos\\Asientos_img\\asiento_mejor.png",
                 "asiento_reservado_path": "C:\\Users\\Bryan\\OneDrive - ULEAM\\Tareas\\Segundo semestre\\Programacion estructurada\\Cine\\frontend\\Pantalla_cine\\Asientos\\Asientos_img\\asiento_reservado.png",
                 "asiento_habilitado_path": "C:\\Users\\Bryan\\OneDrive - ULEAM\\Tareas\\Segundo semestre\\Programacion estructurada\\Cine\\frontend\\Pantalla_cine\\Asientos\\Asientos_img\\asiento_habilitado.png"}

ASIENTOS_IMAGEN = {
            "asiento_libre": conseguir_imagen_ctk(RUTA_ASIENTOS["asiento_reservado_path"], 50, 50, path_dark=RUTA_ASIENTOS["asiento_libre_path"]),
            "asiento_hover": conseguir_imagen_ctk(RUTA_ASIENTOS["asiento_seleccionado_path"], 50, 50),
            "asiento_mejor": conseguir_imagen_ctk(RUTA_ASIENTOS["asiento_mejor_path"], 50, 50),
            "asiento_reservado": conseguir_imagen_ctk(RUTA_ASIENTOS["asiento_libre_path"], 50, 50, path_dark=RUTA_ASIENTOS["asiento_reservado_path"]),
            "asiento_habilitado": conseguir_imagen_ctk(RUTA_ASIENTOS["asiento_habilitado_path"], 50, 50),
            }