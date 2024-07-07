import customtkinter as ctk
import json

from backend.database import crear_asientos_reservados,obtener_asientos_reservados,ejecutar_query_obtener,editar_asiento_reservado
from . import crear_asientos_img as CAI

def seleccionar_asiento(fila: int, columna: int, base) -> None:
    """
    Selecciona o deselecciona un asiento en la sala de cine.

    Args:
        fila (int): La fila del asiento.
        columna (int): La columna del asiento.
        vars (dict): Un diccionario con las variables del programa.

    Returns:
        None
    """
    # Si el asiento está reservado, no se puede seleccionar
    # if (fila, columna) in base.asientos_reservados:
    #     return
    
    # Obtener el botón del asiento
    asiento = base.frame_sala.grid_slaves(row=fila, column=columna)[0]
    unbind_asiento(asiento)
    
    
    # Si el asiento ya está seleccionado, se de-selecciona y se quita del set de asientos seleccionados
    if (fila, columna) in base.asientos_seleccionados:
        asiento.configure(image=CAI.ASIENTOS_IMAGEN["asiento_libre"])
        bind_asiento(asiento,CAI.ASIENTOS_IMAGEN["asiento_hover"],CAI.ASIENTOS_IMAGEN["asiento_libre"])

        base.asientos_seleccionados.remove((fila, columna))
    
    elif base.mejor_asiento == (fila, columna):
        asiento.configure(image=CAI.ASIENTOS_IMAGEN["asiento_libre"])
        base.mejor_asiento = None
        
        bind_asiento(asiento,CAI.ASIENTOS_IMAGEN["asiento_hover"],CAI.ASIENTOS_IMAGEN["asiento_libre"])
    
    # Si el asiento no está seleccionado, se selecciona y se agrega al set de asientos seleccionados
    else:
        asiento.configure(image=CAI.ASIENTOS_IMAGEN["asiento_hover"])
        bind_asiento(asiento,CAI.ASIENTOS_IMAGEN["asiento_libre"],CAI.ASIENTOS_IMAGEN["asiento_hover"])
        base.asientos_seleccionados.add((fila, columna))
        


    print(f"Asientos seleccionados: {base.asientos_seleccionados}")
    
def bind_asiento(asiento:ctk.CTkButton, asiento_entrada,asiento_salida)->None:
    """
    Asigna un evento a un asiento.

    Args:
        asiento (ctk.CTkButton): El asiento al que se le asignará el evento.
        vars (dict): Un diccionario con las variables del programa.
        fila (int): La fila del asiento.
        columna (int): La columna del asiento.

    Returns:
        None
    """
    asiento.bind("<Enter>", lambda event, asiento=asiento: asiento.configure(image=asiento_entrada))
    asiento.bind("<Leave>", lambda event, asiento=asiento: asiento.configure(image=asiento_salida))
    
def unbind_asiento(asiento:ctk.CTkButton)->None:
    """
    Remueve el evento de un asiento.

    Args:
        asiento (ctk.CTkButton): El asiento al que se le removerá el evento.

    Returns:
        None
    """
    asiento.unbind("<Enter>")
    asiento.unbind("<Leave>")
    
    
    
def obtener_todos_asientos_reservados(funcion_id:int)->list:

    try:
        asientos_reservados_json = obtener_asientos_reservados(funcion_id)
        if not asientos_reservados_json:
            crear_asientos_reservados(funcion_id) 
        asientos_reservados = json.loads(asientos_reservados_json[0][2])
        return [(fil,col) for usuario in asientos_reservados for fil,col in usuario["asientos"]]
    except:
        return []

def obtener_id_asiento(funcion_id:int)->int:

    try:
        query = "SELECT id FROM asientos_reservados WHERE funcion_id = %s"  
        return ejecutar_query_obtener(query, "asientos_reservados",datos=(funcion_id,))[0][0]

    except:
        return None


def obtener_asientos_por_id(id_asientos:int)->list:
    try:
        query = "SELECT asientos FROM asientos_reservados WHERE id = %s"  
        asientos_json =  json.loads(ejecutar_query_obtener(query, "asientos_reservados",datos=(id_asientos,))[0][0])
        return asientos_json

    except:
        return []
    
def agregar_asientos(id_asientos, nuevos_asientos, usuario,habilitar=False):
    asientos = obtener_asientos_por_id(id_asientos)
    nuevos_asientos_ls = list(nuevos_asientos)  # Convierte el set a lista
    
    try:
        for i in asientos:
            if habilitar == True:
                if i["user"] == usuario:
                    i["asientos"] = nuevos_asientos_ls
                    return editar_asiento_reservado(id_asientos, json.dumps(asientos))
            else:
                if i["user"] == usuario:
                    # Extiende nuevos_asientos_ls con los asientos existentes
                    nuevos_asientos_ls.extend(tuple(asiento) for asiento in i["asientos"])
                    nuevos_asientos_ls = list(set(nuevos_asientos_ls))
                    i["asientos"] = [list(asiento) for asiento in nuevos_asientos_ls]  # Convierte de nuevo a lista
                    return editar_asiento_reservado(id_asientos, json.dumps(asientos))
            
        # Si el usuario no tiene asientos reservados aún, agrega una nueva entrada
        asientos.append({"user": usuario, "asientos": nuevos_asientos_ls})
        
        return editar_asiento_reservado(id_asientos, json.dumps(asientos))
    
    except Exception as e:
        print(f"Error al agregar asientos: {e}")
        


