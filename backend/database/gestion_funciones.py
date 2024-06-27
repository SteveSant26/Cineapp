from .crear_conexion import abrir_conexion
from frontend.utils import mostrar_error, mostrar_mensaje

def obtener_funciones_bd():
    conexion = abrir_conexion()
    with conexion:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM funciones")
        peliculas = cursor.fetchall()
    return peliculas

def agregar_funcion_bd(datos_funcion: tuple):
    conexion = abrir_conexion()
    query = "INSERT INTO funciones (id, pelicula_id, sala_id, fecha_hora) VALUES (%s, %s, %s, %s)"
    try:
        with conexion:
            cursor = conexion.cursor()
            cursor.execute(query, datos_funcion)
            conexion.commit()
        return True
    except Exception as e:
        mostrar_error("Error al agregar funcion", f"No se pudo agregar la funcion a la base de datos: {e}")


def editar_funcion_bd(datos_funcion: tuple):
    conexion = abrir_conexion()
    query = "UPDATE funciones SET pelicula_id = %s, sala_id = %s, fecha_hora = %s WHERE id = %s"
    try:
        with conexion:
            cursor = conexion.cursor()
            cursor.execute("SELECT pelicula_id, sala_id, fecha_hora FROM funciones WHERE id = %s", (datos_funcion[3],))
            datos_actuales = cursor.fetchone()
            if datos_actuales is None:
                mostrar_error("Error al editar funcion", "No se ha encontrado la funcion a editar.")
                return False
            datos_actuales = (datos_actuales[0], datos_actuales[1], str(datos_actuales[2]))
            # Comparar los datos actuales con los nuevos datos
            nuevos_datos = (datos_funcion[0], datos_funcion[1], datos_funcion[2])
            print(nuevos_datos, datos_actuales)
            if datos_actuales == nuevos_datos:
                mostrar_error("Error al editar funcion", "No se ha modificado ningún campo de la funcion.")
                return False

            # Realizar la actualización si hay cambios
            cursor.execute(query, datos_funcion)
            conexion.commit()
        return True
    except Exception as e:
        mostrar_error("Error al editar funcion", f"No se pudo editar la funcion en la base de datos: {e}")
        return False
        
def eliminar_funcion_bd(id_funcion: int):
    conexion = abrir_conexion()
    query = "DELETE FROM funciones WHERE id = %s"
    try:
        with conexion:
            cursor = conexion.cursor()
            cursor.execute("SELECT pelicula_id, sala_id, fecha_hora FROM funciones WHERE id = %s", (id_funcion,))
            datos_funcion = cursor.fetchone()
            if datos_funcion is None:
                mostrar_error("Error al editar funcion", "No se ha encontrado la funcion a editar.")
                return False
            
            cursor.execute(query, (id_funcion,))
            conexion.commit()
        return True
    except Exception as e:
        mostrar_error("Error al eliminar funcion", f"No se pudo eliminar la funcion de la base de datos: {e}")