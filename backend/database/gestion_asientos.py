from .utils_db import ejecutar_query_obtener, ejecutar_query_agregar, ejecutar_query_editar
import json

def obtener_asientos_reservados(funcion_id:int):
    query = "SELECT * FROM asientos_reservados WHERE funcion_id = %s"
    return ejecutar_query_obtener(query, "asientos_reservados",datos=(funcion_id,))

def crear_asientos_reservados(funcion_id:int):
    datos = (funcion_id,)
    query = "INSERT INTO asientos_reservados (funcion_id) VALUES (%s)"
    return ejecutar_query_agregar(query,datos,"asientos_reservados")

def editar_asiento_reservado(id_asientos,asientos:json):
    datos = (asientos,id_asientos)
    query = "UPDATE asientos_reservados SET asientos = %s WHERE id = %s"
    return ejecuwtar_query_editar(query,datos,"asientos_reservados")
