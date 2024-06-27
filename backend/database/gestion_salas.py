from .crear_conexion import abrir_conexion
from frontend.utils import mostrar_error
def obtener_salas_bd():
    conexion = abrir_conexion()
    with conexion:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM salas")
        peliculas = cursor.fetchall()
    return peliculas

def agregar_sala_bd(datos_sala: tuple):
    conexion = abrir_conexion()
    query = "INSERT INTO salas (id, nombre, filas, columnas) VALUES (%s, %s, %s, %s)"
    try:
        with conexion:
            cursor = conexion.cursor()
            cursor.execute(query, datos_sala)
            conexion.commit()
        return True
    except Exception as e:
        mostrar_error("Error al agregar sala", f"No se pudo agregar la sala a la base de datos: {e}")


def editar_sala_bd(datos_sala: tuple):
    conexion = abrir_conexion()
    query = "UPDATE salas SET nombre = %s, filas = %s, columnas = %s WHERE id = %s"
    try:
        with conexion:
            cursor = conexion.cursor()
            cursor.execute("SELECT nombre, filas, columnas FROM salas WHERE id = %s", (datos_sala[3],))
            datos_actuales = cursor.fetchone()
            if datos_actuales is None:
                mostrar_error("Error al editar sala", "No se ha encontrado la sala a editar.")
                return False

            # Comparar los datos actuales con los nuevos datos
            nuevos_datos = (datos_sala[0], datos_sala[1], datos_sala[2])
            if datos_actuales == nuevos_datos:
                mostrar_error("Error al editar sala", "No se ha modificado ningún campo de la sala.")
                return False

            # Realizar la actualización si hay cambios
            cursor.execute(query, datos_sala)
            conexion.commit()
        return True
    except Exception as e:
        mostrar_error("Error al editar sala", f"No se pudo editar la sala en la base de datos: {e}")
        return False
        
def eliminar_sala_bd(id_sala: int):
    conexion = abrir_conexion()
    query = "DELETE FROM salas WHERE id = %s"
    try:
        with conexion:
            cursor = conexion.cursor()
            cursor.execute(query, (id_sala,))
            conexion.commit()
        return True
    except Exception as e:
        mostrar_error("Error al eliminar sala", f"No se pudo eliminar la sala de la base de datos: {e}")