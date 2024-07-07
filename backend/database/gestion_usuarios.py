from .utils_db import ejecutar_query_obtener, ejecutar_query_agregar

def obtener_usuarios_bd():
    query = "SELECT * FROM usuarios"
    return ejecutar_query_obtener(query, "usuarios")


def agregar_usuario_bd(datos_usuario: tuple):
    query = "INSERT INTO usuarios (nombre, apellido,usuario, contrasena, tipo_usuario) VALUES (%s, %s, %s, %s, %s)"
    return ejecutar_query_agregar(query, datos_usuario, "usuarios")