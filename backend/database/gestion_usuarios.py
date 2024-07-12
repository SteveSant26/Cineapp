from .utils_db import ejecutar_query_obtener, ejecutar_query_agregar, ejecutar_query_editar, ejecutar_query_eliminar

def obtener_usuarios_bd():
    query = "SELECT * FROM usuarios"
    return ejecutar_query_obtener(query, "usuarios")


def agregar_usuario_bd(datos_usuario: tuple):
    query = "INSERT INTO usuarios (nombre, apellido,usuario, contrasena, tipo_usuario) VALUES (%s, %s, %s, %s, %s)"
    return ejecutar_query_agregar(query, datos_usuario, "usuarios")

def editar_usuario_bd(datos_usuario: tuple):
    query = "UPDATE usuarios SET nombre = %s, apellido = %s, usuario = %s, contrasena = %s WHERE id = %s"
    return ejecutar_query_editar(query, datos_usuario, "usuarios")

def eliminar_usuario_bd(id_usuario: int):
    query = "DELETE FROM usuarios WHERE id = %s"
    return ejecutar_query_eliminar(query, (id_usuario,), "usuarios")