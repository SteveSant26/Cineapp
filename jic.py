from backend.database import ejecutar_query_obtener, editar_asiento_reservado, obtener_asientos_reservados, crear_asientos_reservados
import json

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
            if asientos_usuario:
                valor_retornar[usuario] = asientos_usuario

        return valor_retornar
    except Exception as e:
        print(f"Error al obtener los asientos reservados: {e}")
        return {}

def obtener_asientos_por_usuario(asientos_reservados: list, usuario: str) -> list:
    try:
        for usr in asientos_reservados:
            if usr["user"] == usuario:
                return [(fil, col) for fil, col in usr["asientos"]]
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
            return editar_asiento_reservado(id_asientos, json.dumps(asientos_actuales))
            

        asientos_usuario = next((resultado for resultado in asientos_actuales if resultado["user"] == usuario), None)
        if asientos_usuario:
            nuevos_asientos_ls.extend(tuple(asiento) for asiento in asientos_usuario["asientos"])
            nuevos_asientos_ls = list(set(nuevos_asientos_ls))
            asientos_usuario["asientos"] = [list(asiento) for asiento in nuevos_asientos_ls]
            return editar_asiento_reservado(id_asientos, json.dumps(asientos_actuales))

        asientos_actuales.append({"user": usuario, "asientos": [list(x) for x in nuevos_asientos_ls]})
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

# obtener_todos_asientos_reservados(31, "SteveSant", "admin")
print(agregar_asientos(177, [(5, 7)], "SteveSant"))

