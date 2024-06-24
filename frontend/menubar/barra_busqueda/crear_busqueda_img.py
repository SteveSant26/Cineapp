from frontend.utils import conseguir_imagen_ctk

BUSQUEDA_RUTA = {
    "busqueda_dark_path": "C:\\Users\\Bryan\\OneDrive - ULEAM\\Tareas\\Segundo semestre\\Programacion estructurada\\Cine\\frontend\\Menubar\\Barra_busqueda\\imagenes\\busqueda_dark.png",
    "busqueda_light_path": "C:\\Users\\Bryan\\OneDrive - ULEAM\\Tareas\\Segundo semestre\\Programacion estructurada\\Cine\\frontend\\Menubar\\Barra_busqueda\\imagenes\\busqueda_light.png",
    "busqueda_seleccion": "C:\\Users\\Bryan\\OneDrive - ULEAM\\Tareas\\Segundo semestre\\Programacion estructurada\\Cine\\frontend\\Menubar\\Barra_busqueda\\imagenes\\busqueda_seleccion.png", }





BUSQUEDA_IMAGEN = {
    "imagen_busqueda": conseguir_imagen_ctk(BUSQUEDA_RUTA["busqueda_light_path"], 20, 20, path_dark=BUSQUEDA_RUTA["busqueda_dark_path"]),
    "imagen_busqueda_hover": conseguir_imagen_ctk(BUSQUEDA_RUTA["busqueda_seleccion"], 20, 20),
}
