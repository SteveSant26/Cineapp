from . import datos_pelicula as DP
from frontend import utils 

from . import crear_asientos_img as CAI
from . import utils_asientos as UA



def encontrar_mejor_asiento(base) -> tuple:
    """
    Encuentra el mejor asiento disponible en la sala de cine empezando por la primera fila.
    Si se desea cambiar el orden de las filas en el que se empieza a mostrar el mejor asiento, 
    simplemente cambiar x[0] a -x[0] en la función lambda, así se mostrará el mejor asiento empezando por la última fila.

    Args:
        vars (dict): Un diccionario con las variables del programa.

    Returns:
        tuple: Las coordenadas del mejor asiento disponible.
    """
    # Se calcula cuál es la columna del medio usando división absoluta
    centro = base.columnas_sala // 2

    # Se crea una lista de tuplas con las coordenadas de los asientos disponibles
    asientos_disponibles = [
        (i, j) for i in range(2,base.filas_sala+2) for j in range(1,base.columnas_sala+1)
        if (i, j) not in base.asientos_reservados
        # Si se desea también excluir los asientos ya seleccionados, descomentar la siguiente línea:
        # and (i, j) not in base.asientos_seleccionados
    ]

    # Si no hay asientos disponibles se muestra un mensaje de error
    if not asientos_disponibles:
        utils.mostrar_error("Sin asientos", "Ya no hay más asientos para seleccionar")
        return

    # Se ordenan los asientos disponibles por fila y por la distancia al centro
    asientos_disponibles.sort(key=lambda x: (x[0], abs(x[1] - centro)))  # Se puede cambiar x[0] a -x[0] para cambiar el orden de las filas

    # Ajustar la fila y columna a los índices correctos (considerando el desplazamiento)


    return asientos_disponibles[0]

def select_mejor_asiento(base) -> None:
    """
    Marca el mejor asiento disponible en la sala de cine.

    Args:
        vars (dict): Un diccionario con las variables del programa.

    Returns:
        None
    """
    
    # Se busca el mejor asiento
    mejor_asiento = encontrar_mejor_asiento(base)

    # Marcar el nuevo mejor asiento si hay uno
    if mejor_asiento:
        base.mejor_asiento = mejor_asiento
        fila, columna = base.mejor_asiento
        asiento = base.frame_sala.grid_slaves(row=fila, column=columna)[0]
        asiento.configure(image=CAI.ASIENTOS_IMAGEN["asiento_mejor"], border_color="#55B7EC")
        UA.bind_asiento(asiento,CAI.ASIENTOS_IMAGEN["asiento_libre"],CAI.ASIENTOS_IMAGEN["asiento_mejor"])