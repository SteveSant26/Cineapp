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
        asiento.configure(image=CAI.ASIENTOS_IMAGEN["asiento_libre"],border_color=("black","white"))
        bind_asiento(asiento,CAI.ASIENTOS_IMAGEN["asiento_hover"],CAI.ASIENTOS_IMAGEN["asiento_libre"])

        base.asientos_seleccionados.remove((fila, columna))
    
    elif base.mejor_asiento == (fila, columna):
        asiento.configure(image=CAI.ASIENTOS_IMAGEN["asiento_libre"],border_color=("black","white"))
        base.mejor_asiento = None
        
        bind_asiento(asiento,CAI.ASIENTOS_IMAGEN["asiento_hover"],CAI.ASIENTOS_IMAGEN["asiento_libre"])
    
    # Si el asiento no está seleccionado, se selecciona y se agrega al set de asientos seleccionados
    else:
        asiento.configure(image=CAI.ASIENTOS_IMAGEN["asiento_hover"],border_color="#31AF5D")
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
    
    
    
def obtener_todos_asientos_reservados(funcion_id: int, usuario: str, tipo_usuario: str) -> dict:
    try:
        asientos_reservados_json = obtener_asientos_reservados(funcion_id)
        if not asientos_reservados_json:
            crear_asientos_reservados(funcion_id)
            asientos_reservados_json = obtener_asientos_reservados(funcion_id)
        
        asientos_reservados_str = asientos_reservados_json[0][2]
        if asientos_reservados_str is None:
            return {}

        asientos_reservados = json.loads(asientos_reservados_str)
        valor_retornar = {}
        todos_asientos = [(fil, col) for usr in asientos_reservados for fil, col in usr["asientos"]]
        if todos_asientos:
            valor_retornar["todos_asientos"] = todos_asientos
        
        if tipo_usuario == "cliente":
            asientos_usuario = obtener_asientos_por_usuario(asientos_reservados, usuario)
            valor_retornar[usuario] = asientos_usuario
            
        print("Asientos reservados  a retornar: ", valor_retornar)
        return valor_retornar
    except Exception as e:
        print(f"Error al obtener los asientos reservados: {e}")
        return {}

def obtener_asientos_por_usuario(asientos_reservados: list, usuario_actual: str) -> list:
    try:
        print(f"Usuario actual: {usuario_actual}")
        print(f"Todos los asientos: {asientos_reservados}")
        for usuario in asientos_reservados:
            print(f"Comparing {usuario['user']} with {usuario_actual}")
            if usuario["user"] == usuario_actual:
                return [(fil, col) for fil, col in usuario["asientos"]]
        return []
    except Exception as e:
        print(f"Error al obtener los asientos por usuario: {e}")
        return []

def obtener_id_asiento(funcion_id: int) -> int:
    try:
        query = "SELECT id FROM asientos_reservados WHERE funcion_id = %s"
        id_asiento = ejecutar_query_obtener(query, "asientos_reservados", datos=(funcion_id,))
        if id_asiento:
            return id_asiento[0][0]
    except Exception as e:
        print(f"Error al obtener el id del asiento: {e}")
    return None

def obtener_asientos_por_id(id_asientos: int) -> list:
    try:
        query = "SELECT asientos FROM asientos_reservados WHERE id = %s"
        asientos_json = ejecutar_query_obtener(query, "asientos_reservados", datos=(id_asientos,))
        if not asientos_json or not asientos_json[0][0]:
            return []
        asientos = json.loads(asientos_json[0][0])
        return asientos
    except Exception as e:
        print(f"Error al obtener los asientos por id: {e}")
        return []

def agregar_asientos(id_asientos: int, nuevos_asientos: list, usuario: str, habilitar: bool = False) -> bool:
    try:

        
        asientos_actuales = obtener_asientos_por_id(id_asientos)
        nuevos_asientos_ls = [tuple(asiento) for asiento in nuevos_asientos]

        if habilitar:
            return habilitar_asientos(id_asientos, asientos_actuales, nuevos_asientos_ls, usuario)
        
        if not asientos_actuales:
            asientos_actuales = [{"user": usuario, "asientos": [list(x) for x in nuevos_asientos_ls]}]
            print("Asientos actuales agregar asientos cuando no hay datos actuales: ", asientos_actuales)
            return editar_asiento_reservado(id_asientos, json.dumps(asientos_actuales))

        asientos_usuario = next((resultado for resultado in asientos_actuales if resultado["user"] == usuario), None)
        if asientos_usuario:
            print(asientos_usuario)
            nuevos_asientos_ls.extend(tuple(asiento) for asiento in asientos_usuario["asientos"])
            nuevos_asientos_ls = list(set(nuevos_asientos_ls))
            asientos_usuario["asientos"] = [list(asiento) for asiento in nuevos_asientos_ls]
            print("Asientos actuales agregar asientos cuando ya hay datos actuales: ", asientos_actuales)
            return editar_asiento_reservado(id_asientos, json.dumps(asientos_actuales))

        asientos_actuales.append({"user": usuario, "asientos": [list(x) for x in nuevos_asientos_ls]})
        print("Asientos actuales agregar asientos: ", asientos_actuales)
        return editar_asiento_reservado(id_asientos, json.dumps(asientos_actuales))
    except Exception as e:
        print(f"Error al agregar asientos: {e}")
        return False


def habilitar_asientos(id_asientos: int, asientos: list, nuevos_asientos_ls: list, usuario: str) -> bool:
    try:
        totales = []
        for resultado in asientos:
            usuario_resultado = resultado["user"]
            asientos_resultados = [tuple(asiento) for asiento in resultado['asientos']]
            
            asientos_admins = []
            asientos_clientes = []
            
            for nuevo_asiento in nuevos_asientos_ls:
                if nuevo_asiento in asientos_resultados:
                    if usuario == usuario_resultado:
                        asientos_admins.append(nuevo_asiento)
                    else:
                        asientos_clientes.append(nuevo_asiento)
        
            if asientos_admins:
                totales.append({"user": usuario_resultado, "asientos": asientos_admins})
            if asientos_clientes:
                totales.append({"user": usuario_resultado, "asientos": asientos_clientes})
                
        return editar_asiento_reservado(id_asientos, json.dumps(totales))
    except Exception as e:
        print(f"Error al habilitar asientos: {e}")
        return False