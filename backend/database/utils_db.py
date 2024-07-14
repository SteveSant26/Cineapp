import os

from .crear_conexion import abrir_conexion
from frontend.utils import mostrar_error


def eliminar_imagen(nombre_imagen: str):
    """
    Elimina una imagen del directorio de portadas de películas.

    Args:
        nombre_imagen (str): El nombre de la imagen a eliminar.

    Returns:
        None
    """
    from frontend.cartelera import corregir_nombre_archivo
    nombre_imagen = corregir_nombre_archivo(nombre_imagen)
    directorio = "frontend\\cartelera\\portadas_peliculas"
    ruta_archivo = f"{directorio}\\{nombre_imagen}.png"
    print(ruta_archivo)
    try:
        if os.path.exists(ruta_archivo):
            os.remove(ruta_archivo)
            print(f"Archivo {ruta_archivo} eliminado exitosamente.")
        else:
            print(f"El archivo {ruta_archivo} no existe.")
    except Exception as e:
        print(f"Error al intentar eliminar el archivo {ruta_archivo}: {e}")


def ejecutar_query_obtener(query:str, tabla:str, datos:tuple=None) -> list:
    """
    Ejecuta una consulta SELECT en la base de datos para obtener datos de una tabla.

    Args:
        query (str): La consulta SELECT a ejecutar.
        tabla (str): El nombre de la tabla en la base de datos.
        datos (tuple, optional): Los datos a pasar como parámetros en la consulta. Defaults to None.

    Returns:
        list: Una lista con los datos obtenidos de la consulta.
    """
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


def ejecutar_query_agregar(query:str, datos:tuple, tabla:str) -> bool:
    """
    Ejecuta una consulta INSERT en la base de datos para agregar datos a una tabla.

    Args:
        query (str): La consulta INSERT a ejecutar.
        datos (tuple): Los datos a insertar en la tabla.
        tabla (str): El nombre de la tabla en la base de datos.

    Returns:
        bool: True si se pudo agregar el dato correctamente, False en caso contrario.
    """
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


def ejecutar_query_editar(query: str, nuevos_datos:tuple, tabla:str)-> bool:
    """
    Ejecuta una consulta UPDATE en la base de datos para editar datos de una tabla.

    Args:
        query (str): La consulta UPDATE a ejecutar.
        nuevos_datos (tuple): Los nuevos datos a actualizar en la tabla.
        tabla (str): El nombre de la tabla en la base de datos.

    Returns:
        bool: True si se pudo editar el dato correctamente, False en caso contrario.
    """
    conexion = abrir_conexion()
    id_query = nuevos_datos[-1]
    try:
        with conexion.cursor() as cursor:
            cursor.execute(f"SELECT * from {tabla} WHERE id = %s", (id_query,))
            datos_actuales = cursor.fetchone()

            if datos_actuales is None and tabla != "asientos_reservados":
                mostrar_error(f"Error al editar {tabla[:-1]}", f"No se ha encontrado la {tabla[:-1]} a editar.")
                return False

            if tabla == "funciones":
                if not verificar_funcion_existente(cursor, nuevos_datos, "editar"):
                    return False
                datos_actuales = (datos_actuales[1], (datos_actuales[2]), str(datos_actuales[3]), datos_actuales[0])
            elif tabla == "salas":
                datos_actuales = (datos_actuales[1], (datos_actuales[2]), (datos_actuales[3]), datos_actuales[0])
                print(datos_actuales)
                print(nuevos_datos)

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
                imagen_actual = datos_actuales[0]
                imagen_nueva = nuevos_datos[0]
                nombre_pelicula = nuevos_datos[1]
                if imagen_actual != imagen_nueva:
                    eliminar_imagen(nombre_pelicula)
            elif tabla == "usuarios":
                datos_actuales = (
                    datos_actuales[1],
                    datos_actuales[2],
                    datos_actuales[3],
                    datos_actuales[4],
                    datos_actuales[0],
                )

            if datos_actuales == nuevos_datos:
                mostrar_error(f"Error al editar {tabla[:-1]}", f"No se ha modificado ningún campo de la tabla {tabla}.")
                return False

            cursor.execute(query, nuevos_datos)
            conexion.commit()

        return True
    except Exception as e:
        mostrar_error("Error al editar funcion", f"No se pudo editar la funcion en la base de datos: {e}")
        return False


def ejecutar_query_eliminar(query:str, id_dato:int, tabla:str) -> bool:
    """
    Ejecuta una consulta DELETE en la base de datos para eliminar un dato de una tabla.

    Args:
        query (str): La consulta DELETE a ejecutar.
        id_dato (int): El ID del dato a eliminar.
        tabla (str): El nombre de la tabla en la base de datos.

    Returns:
        bool: True si se pudo eliminar el dato correctamente, False en caso contrario.
    """
    try:
        conexion = abrir_conexion()
        with conexion.cursor() as cursor:

            cursor.execute(f"SELECT * from {tabla} WHERE id = %s", (id_dato,))
            datos_sala = cursor.fetchone()
            if datos_sala is None:
                mostrar_error(f"Error al eliminar {tabla[:-1]}", f"No se ha encontrado la {tabla[:-1]} a eliminar.")
                return False
            if tabla == "peliculas":
                nombre_pelicula = datos_sala[2]
                eliminar_imagen(nombre_pelicula)

            cursor.execute(query, (id_dato,))
            conexion.commit()
        return True

    except Exception as e:
        mostrar_error(f"Error al eliminar {tabla[:-1]}", f"No se pudo eliminar la {tabla[:-1]} de la base de datos: {e}")
        return False


def verificar_funcion_existente(cursor, parametros:tuple, operacion:str):
    """
    Verifica si ya existe una función en la base de datos con la misma sala y horario.

    Args:
        cursor (Cursor): El cursor de la conexión a la base de datos.
        parametros (tuple): Los parámetros de la función a verificar.
        operacion (str): La operación a realizar ("agregar" o "editar").

    Returns:
        bool: True si no existe una función con la misma sala y horario, False en caso contrario.
    """
    try:
        cursor.execute("SELECT id, sala_id, hora FROM funciones")
        resultado = cursor.fetchall()
        print(f"Resultado: {parametros}")
        for id, sala_id, hora in resultado:
            hora_str = str(hora)
            if operacion == "agregar":
                sala_id_nueva = parametros[1]
                hora_nueva = parametros[2]
                print(f"Sala id nueva: {sala_id_nueva}, hora nueva: {hora_nueva}, sala id: {sala_id}, hora: {hora_str}")
                if sala_id_nueva == sala_id and hora_nueva == hora_str:
                    mostrar_error(f"Error al agregar  la funcion", "Ya existe una función en esa sala y en ese horario.")
                    return False
            elif operacion == "editar":
                id_funcion = parametros[3]
                sala_id_nueva = parametros[1]
                hora_nueva = parametros[2]
                print(f"Sala id nueva: {sala_id_nueva}, hora nueva: {hora_nueva}, sala id: {sala_id}, hora: {hora_str}")
                if sala_id_nueva == sala_id and hora_nueva == hora_str and id_funcion != id:
                    mostrar_error(f"Error al editar la funcion", "Ya existe una función en esa sala y en ese horario.")
                    return False

        return True
    except Exception as e:
        print(f"Error al verificar la función existente: {e}")
        return False