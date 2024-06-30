from backend.database import obtener_imagen_pelicula_por_id,obtener_id_titulo_pelicula_bd

for id,pelicula in obtener_id_titulo_pelicula_bd():
    print(id,pelicula)