from .conseguir_imagen import conseguir_imagen_ctk

BUSQUEDA_RUTA = {
    "busqueda_dark_path": "frontend\\utils\\imagenes\\busqueda_dark.png",
    "busqueda_light_path": "frontend\\utils\\imagenes\\busqueda_light.png",
    "busqueda_seleccion": "frontend\\utils\\imagenes\\busqueda_seleccion.png", }



BUSQUEDA_IMAGEN = {
    "imagen_busqueda": conseguir_imagen_ctk(BUSQUEDA_RUTA["busqueda_light_path"], 20, 20, path_dark=BUSQUEDA_RUTA["busqueda_dark_path"]),
    "imagen_busqueda_hover": conseguir_imagen_ctk(BUSQUEDA_RUTA["busqueda_seleccion"], 20, 20),
}


def enter_hover_boton_busqueda(boton):
    """
    Cambia la imagen del botón a una imagen de hover cuando el mouse entra.

    Parameters:
    boton (tkinter.Button): El botón a modificar.

    Returns:
    None
    """
    imagen = BUSQUEDA_IMAGEN["imagen_busqueda_hover"]
    boton.configure(image=imagen)

def leave_hover_boton_busqueda(boton):
    """
    Cambia la imagen del botón a la imagen predeterminada cuando el mouse sale.

    Parameters:
    boton (tkinter.Button): El botón a modificar.

    Returns:
    None
    """
    imagen = BUSQUEDA_IMAGEN["imagen_busqueda"]
    boton.configure(image=imagen)
