from . import crear_busqueda_img as CBI

def enter_hover_boton_busqueda(boton):
    """
    Cambia la imagen del botón a una imagen de hover cuando el mouse entra.

    Parameters:
    boton (tkinter.Button): El botón a modificar.

    Returns:
    None
    """
    imagen = CBI.BUSQUEDA_IMAGEN["imagen_busqueda_hover"]
    boton.configure(image=imagen)

def leave_hover_boton_busqueda(boton):
    """
    Cambia la imagen del botón a la imagen predeterminada cuando el mouse sale.

    Parameters:
    boton (tkinter.Button): El botón a modificar.

    Returns:
    None
    """
    imagen = CBI.BUSQUEDA_IMAGEN["imagen_busqueda"]
    boton.configure(image=imagen)
