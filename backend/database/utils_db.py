from .crear_conexion import abrir_conexion
from frontend.utils import mostrar_error

def ejecutar_query_obtener(query, tabla):
    try:
        conexion = abrir_conexion()
        with conexion.cursor() as cursor:
            cursor.execute(query)
            datos = cursor.fetchall()
        return datos
    except Exception as e:
        mostrar_error(f"Error al obtener {tabla[:-1]}", f"No se pudo obtener las {tabla[:-1]} de la base de datos: {e}")
        return []

def ejecutar_query_agregar(query, parametros, tabla):
    try:
        conexion = abrir_conexion()
        with conexion.cursor() as cursor:
            cursor.execute(query, parametros)
            conexion.commit()
        return True
    except Exception as e:
        mostrar_error(f"Error al agregar {tabla[:-1]}", f"No se pudo agregar la {tabla[:-1]} en la base de datos: {e}")
        return False

def ejecutar_query_editar(query, parametros, tabla):
    conexion = abrir_conexion()
    id_query = parametros[-1]
    try:
        with conexion.cursor() as cursor:
            cursor.execute(f"SELECT * from {tabla} WHERE id = %s", (id_query,))
            datos_actuales = cursor.fetchone()

            if datos_actuales is None:
                mostrar_error(f"Error al editar {tabla[:-1]}", f"No se ha encontrado la {tabla[:-1]} a editar.")
                return False
            if tabla == "funciones":
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
            if datos_actuales == parametros:
                mostrar_error("Error al editar funcion", "No se ha modificado ningún campo de la funcion.")
                return False

            cursor.execute(query, parametros)
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
            print(datos_sala)
            if datos_sala is None:
                mostrar_error(f"Error al eliminar {tabla[:-1]}", f"No se ha encontrado la {tabla[:-1]} a eliminar.")
                return False
            
            cursor.execute(query, (id_dato,))
            conexion.commit()
        return True
    
    except Exception as e:
        mostrar_error(f"Error al eliminar {tabla[:-1]}", f"No se pudo eliminar la {tabla[:-1]} de la base de datos: {e}")
        return False


