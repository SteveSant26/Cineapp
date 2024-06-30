from .crear_conexion import abrir_conexion
from frontend.utils import mostrar_error

def ejecutar_query_obtener(query, tabla, datos=None):
    try:
        conexion = abrir_conexion()
        with conexion.cursor() as cursor:
            if datos is None:
                cursor.execute(query)
            else:
                cursor.execute(query, datos)
            datos = cursor.fetchall()
        return datos
    except Exception as e:
        mostrar_error(f"Error al obtener {tabla[:-1]}", f"No se pudo obtener las {tabla[:-1]} de la base de datos: {e}")
        return []
    
def ejecutar_query_agregar(query, datos, tabla):
    try:
        conexion = abrir_conexion()
        with conexion.cursor() as cursor:
            if tabla == "funciones":
                if not verificar_funcion_existente(cursor, datos, "agregar"):
                    return False
            cursor.execute(query, datos)
            conexion.commit()
        return True
    except Exception as e:
        mostrar_error(f"Error al agregar {tabla[:-1]}", f"No se pudo agregar la {tabla[:-1]} en la base de datos: {e}")
        return False

def ejecutar_query_editar(query, nuevos_datos, tabla):
    conexion = abrir_conexion()
    id_query = nuevos_datos[-1]
    try:
        with conexion.cursor() as cursor:
            cursor.execute(f"SELECT * from {tabla} WHERE id = %s", (id_query,))
            datos_actuales = cursor.fetchone()

            if datos_actuales is None:
                mostrar_error(f"Error al editar {tabla[:-1]}", f"No se ha encontrado la {tabla[:-1]} a editar.")
                return False
            
            if tabla == "funciones":
                if not verificar_funcion_existente(cursor, nuevos_datos, "editar"):
                    return False
                datos_actuales = (datos_actuales[1], (datos_actuales[2]), str(datos_actuales[3]), datos_actuales[0])
            elif tabla == "salas":
                datos_actuales = (datos_actuales[1], (datos_actuales[2]), (datos_actuales[3]), datos_actuales[0])
                
            elif tabla == "peliculas":
                datos_actuales = (
                datos_actuales[1], 
                datos_actuales[2], 
                datos_actuales[3], 
                datos_actuales[4], 
                (datos_actuales[5]), 
                str(datos_actuales[6]), 
                str(datos_actuales[7]),   
                datos_actuales[0], 
            )
            if datos_actuales == nuevos_datos:
                mostrar_error("Error al editar funcion", "No se ha modificado ningún campo de la funcion.")
                return False

            cursor.execute(query, nuevos_datos)
            conexion.commit()
        return True
    except Exception as e:
        mostrar_error("Error al editar funcion", f"No se pudo editar la funcion en la base de datos: {e}")
        return False



def ejecutar_query_eliminar(query, id_dato, tabla):
    try:
        conexion = abrir_conexion()
        with conexion.cursor() as cursor:
            
            cursor.execute(f"SELECT * from {tabla} WHERE id = %s", (id_dato,))
            datos_sala = cursor.fetchone()
            if datos_sala is None:
                mostrar_error(f"Error al eliminar {tabla[:-1]}", f"No se ha encontrado la {tabla[:-1]} a eliminar.")
                return False
            
            cursor.execute(query, (id_dato,))
            conexion.commit()
        return True
    
    except Exception as e:
        mostrar_error(f"Error al eliminar {tabla[:-1]}", f"No se pudo eliminar la {tabla[:-1]} de la base de datos: {e}")
        return False



def verificar_funcion_existente(cursor, parametros,operacion):
    try:
        cursor.execute("SELECT id, sala_id, fecha_hora FROM funciones")
        resultado = cursor.fetchall()

        for id,sala_id, fecha_hora in resultado:
            fecha_hora_str = str(fecha_hora)
            if operacion == "agregar":
                sala_id_nueva = parametros[2]
                fecha_hora_nueva = parametros[3]
                if sala_id_nueva == sala_id and fecha_hora_nueva == fecha_hora_str:
                    mostrar_error(f"Error al agregar {operacion}", "Ya existe una función en esa sala y en ese horario.")
                    return False
            elif operacion == "editar":
                id_funcion = parametros[3]
                sala_id_nueva = parametros[1]
                fecha_hora_nueva = parametros[2]
                print(id_funcion,sala_id_nueva, fecha_hora_nueva, id, sala_id, fecha_hora_str)
                if sala_id_nueva == sala_id and fecha_hora_nueva == fecha_hora_str and id_funcion != id:
                    mostrar_error(f"Error al editar {operacion}", "Ya existe una función en esa sala y en ese horario.")
                    return False
        
        return True
    except Exception as e:
        print(f"Error al verificar la función existente: {e}")
        return False