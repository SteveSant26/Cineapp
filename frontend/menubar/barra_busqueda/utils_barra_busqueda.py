from . import crear_busqueda_img as CBI
def enter_hover_boton_busqueda(boton):
    imagen = CBI.BUSQUEDA_IMAGEN["imagen_busqueda_hover"]
    boton.configure(image= imagen)

def leave_hover_boton_busqueda(boton):
    imagen = CBI.BUSQUEDA_IMAGEN["imagen_busqueda"]
    boton.configure(image=imagen)