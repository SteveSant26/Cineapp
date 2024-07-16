import customtkinter as ctk
from frontend.utils import crear_icono_busqueda as CBI, enter_hover_boton_busqueda, leave_hover_boton_busqueda, mostrar_mensaje, mostrar_error
from backend.database import ejecutar_query_obtener

busqueda = False
genero_actual = "Todos"

def crear_barra_busqueda(base: ctk.CTk) -> None:
    """
    Crea una barra de búsqueda en la interfaz gráfica.

    Args:
        base (ctk.CTk): La ventana principal de la aplicación.

    Returns:
        None
    """

    # Contenedor para centrar la barra de búsqueda
    busqueda_frame = ctk.CTkFrame(base.menu_bar_frame, fg_color="transparent")
    busqueda_frame.pack(side="left", expand=True,fill="x",padx=(400, 0))

    entry_barra_de_busqueda = ctk.CTkEntry(busqueda_frame, font=(
        "Arial", 20, "bold"), width=200, placeholder_text="Buscar película...")
    entry_barra_de_busqueda.pack(side="left")

    boton_barra_de_busqueda = ctk.CTkButton(busqueda_frame,
                                            image=CBI.BUSQUEDA_IMAGEN["imagen_busqueda"],
                                            text=" ",
                                            font=("Arial", 20, "bold"),
                                            width=10,
                                            border_width=1,
                                            border_color=("black", "white"),
                                            fg_color="transparent",
                                            hover=False,
                                            corner_radius=15,
                                            command=lambda: buscar_peliculas_por_nombre(base, entry_barra_de_busqueda.get()))
    boton_barra_de_busqueda.pack(side="left", padx=(0, 200))

    boton_barra_de_busqueda.bind(
        "<Enter>", lambda e: enter_hover_boton_busqueda(boton_barra_de_busqueda))
    boton_barra_de_busqueda.bind(
        "<Leave>", lambda e: leave_hover_boton_busqueda(boton_barra_de_busqueda))

    generos = obtener_todos_generos()
    generos.insert(0, "Todos")

    

    combobox_generos = ctk.CTkComboBox(busqueda_frame, font=(
        "Arial", 20), values=generos, command=lambda event: buscar_peliculas_por_genero(event, base, combobox_generos))
    combobox_generos.pack(side="right")
    combobox_generos.set(genero_actual)

def obtener_peliculas_bd_por_nombre(nombre_pelicula: str) -> list:
    """
    Obtiene las películas de la base de datos que coincidan con el nombre de la película.

    Args:
        nombre_pelicula (str): El nombre de la película a buscar.

    Returns:
        list: Una lista de películas que coinciden con el nombre de la película.
    """
    query = "SELECT id,titulo FROM peliculas WHERE titulo LIKE %s"
    nombre_busqueda = f"%{nombre_pelicula}%"
    return ejecutar_query_obtener(query, "peliculas", datos=(nombre_busqueda,))


def buscar_peliculas_por_nombre(base: ctk.CTk, nombre_pelicula: str) -> None:
    """
    Busca películas por nombre.

    Args:
        base (ctk.CTk): La ventana principal de la aplicación.
        nombre_pelicula (str): El nombre de la película a buscar.
        busqueda (bool, optional): Indica si se está realizando una búsqueda. Defaults to None.

    Returns:
        None
    """
    global busqueda,genero_actual

    from .interfaz_cartelera import iniciar_hilo_mostrar_peliculas

    if nombre_pelicula == "":
        if busqueda:
            busqueda = False
            genero_actual = "Todos"
            iniciar_hilo_mostrar_peliculas(base)
            return
        return mostrar_error("Error de búsqueda", "Por favor, ingrese un nombre de película para buscar.")

    peliculas_busqueda = obtener_peliculas_bd_por_nombre(nombre_pelicula)

    if not peliculas_busqueda:
        mostrar_error("Error de búsqueda", f"No se encontraron películas con el nombre {
                      nombre_pelicula}")
        return

    peliculas_busqueda
    iniciar_hilo_mostrar_peliculas(base, peliculas=peliculas_busqueda)
    busqueda = True


def obtener_todos_generos_bd() -> list:
    """
    Obtiene todos los géneros de la base de datos.

    Returns:
        list: Una lista con los géneros de la base de datos.
    """
    query = "SELECT DISTINCT genero FROM peliculas"
    return ejecutar_query_obtener(query, "peliculas")


def obtener_todos_generos() -> list:
    """ 
    Obtiene todos los géneros de las películas.
    
    Returns:
        list: Una lista con todos los géneros de las películas.
    """
    listas_generos = obtener_todos_generos_bd()
    todos_generos = set()
    for generos in listas_generos:
        for genero in generos[0].split(","):
            todos_generos.add(genero.strip())

    return list(todos_generos)


def obtener_id_titulo_genero_pelicula_bd() -> str:
    """
    Obtiene el género de una película.

    Args:
        id_pelicula (int): El id de la película.

    Returns:
        str: El género de la película.
    """
    query = "SELECT id,titulo,genero FROM peliculas"
    return ejecutar_query_obtener(query, "peliculas")


def obtener_generos_pelicula(lista_generos: str) -> list:
    """Obtiene los géneros de una película.
    Args:
        lista_generos (str): La lista de géneros de la película.
    Returns:
        list: Una lista con los géneros de la película.
    """

    generos = lista_generos.split(',')
    nueva_lista = []
    for genero in generos:
        nueva_lista.append(genero.strip())

    return nueva_lista


def buscar_peliculas_por_genero(event: object, base: ctk.CTk, combobox_genero: ctk.CTkComboBox) -> None:

    """ Busca películas por género.
    Args:
        event (object): El evento que se produce al seleccionar un género.
        base (ctk.CTk): La ventana principal de la aplicación.
        combobox_genero (ctk.CTkComboBox): El combobox con los géneros de las películas.
        busqueda (bool, optional): Indica si se está realizando una búsqueda. Defaults to None.
        
    Returns:
        None"""
    try:
        global genero_actual, busqueda
        from .interfaz_cartelera import iniciar_hilo_mostrar_peliculas


        if combobox_genero.get() == "Todos":
            if busqueda:
                genero_actual = "Todos"
                iniciar_hilo_mostrar_peliculas(base)
                busqueda = False
                return
            return mostrar_error("Error de búsqueda", "Por favor, seleccione un género para buscar.")
        elif genero_actual == combobox_genero.get():
            return mostrar_mensaje("Mensaje de búsqueda", "Ya se están mostrando las películas de este género.")

        datos_peliculas = obtener_id_titulo_genero_pelicula_bd()
        peliculas = []
        for pelicula_id, pelicula_titulo, genero in datos_peliculas:
            if combobox_genero.get() in obtener_generos_pelicula(genero):
                pelicula = (pelicula_id, pelicula_titulo)
                peliculas.append(pelicula)
                
        if not peliculas:
            mostrar_error("Error de búsqueda", f"No se encontraron películas con el género {combobox_genero.get()}")
            combobox_genero.set("Todos")
            return

        genero_actual = combobox_genero.get()
        iniciar_hilo_mostrar_peliculas(base, peliculas=peliculas)
        busqueda = True
        return

    except Exception as e:
        mostrar_error("Error de búsqueda",
                      f"Ocurrió un error al buscar las películas por género: {e}")
        combobox_genero.set("Todos")
