import customtkinter as ctk
from . import funcion_botones_side_bar as BSB

def crear_side_bar(base: ctk.CTk) -> None:
    """
    Crea una barra lateral en la ventana base dada.

    Args:
        base (ctk.CTk): La ventana base en la que se creará la barra lateral.

    Returns:
        None
    """
    alto = base.winfo_height()
    ancho = 300

    base.toggle_menu = ctk.CTkFrame(base, width=ancho, height=alto, fg_color="transparent")
    base.toggle_menu.place(x=0, y=50)

    separador = ctk.CTkFrame(base, width=2, height=alto, fg_color="black")
    separador.place(x=ancho, y=50)

    base.desplegar_menu_boton.configure(text="x", command=lambda: ocultar_side_bar(base, separador))

    crear_opciones_side_bar(base)

def colocar_boton_inicio(base: ctk.CTk) -> None:
    """
    Coloca un botón en la interfaz para volver al inicio.

    Args:
        base (ctk.CTk): El objeto base de la aplicación.

    Returns:
        None
    """
    from frontend.cartelera import iniciar_hilo_mostrar_peliculas
    boton_inicio = ctk.CTkButton(base.toggle_menu,
                                 text="Inicio",
                                 width=250,
                                 height=40,
                                 border_width=1,
                                 border_color="black",
                                 fg_color="#329ADF",
                                 font=("Arial", 15, "bold"),
                                 hover_color="#31AF9C",
                                 command=lambda: iniciar_hilo_mostrar_peliculas(base))
    boton_inicio.place(x=20, y=30)

def colocar_boton_editar_perfil(base: ctk.CTk) -> None:
    """
    Coloca un botón en la interfaz para editar el perfil del usuario.

    Args:
        base (ctk.CTk): El objeto base de la aplicación.

    Returns:
        None
    """
    boton_editar_perfil = ctk.CTkButton(base.toggle_menu,
                                        text="Editar perfil",
                                        width=250,
                                        height=40,
                                        border_width=1,
                                        border_color="black",
                                        fg_color="#329ADF",
                                        font=("Arial", 15, "bold"),
                                        hover_color="#31AF9C",
                                        command=lambda: BSB.crear_frame_editar_perfil(base))
    boton_editar_perfil.place(x=20, y=90)

def colocar_boton_administrar_peliculas(base: ctk.CTk) -> None:
    """
    Coloca un botón en la interfaz para administrar películas.

    Args:
        base (ctk.CTk): El objeto base de la aplicación.

    Returns:
        None
    """
    boton_administrar_peliculas = ctk.CTkButton(base.toggle_menu,
                                                text="Administrar películas",
                                                width=250,
                                                height=40,
                                                border_width=1,
                                                border_color="black",
                                                fg_color="#329ADF",
                                                font=("Arial", 15, "bold"),
                                                hover_color="#31AF9C",
                                                command=lambda: BSB.crear_frame_administrar_peliculas(base))
    boton_administrar_peliculas.place(x=20, y=150)

def colocar_boton_administrar_salas(base: ctk.CTk) -> None:
    """
    Coloca un botón en la interfaz para administrar las salas.

    Args:
        base (ctk.CTk): El objeto base de la aplicación.

    Returns:
        None
    """
    boton_administrar_salas = ctk.CTkButton(base.toggle_menu,
                                            text="Administrar salas",
                                            width=250,
                                            height=40,
                                            border_width=1,
                                            border_color="black",
                                            fg_color="#329ADF",
                                            font=("Arial", 15, "bold"),
                                            hover_color="#31AF9C",
                                            command=lambda: BSB.crear_frame_administrar_salas(base))
    boton_administrar_salas.place(x=20, y=210)

def colocar_boton_administrar_funciones(base: ctk.CTk) -> None:
    """
    Coloca un botón en la interfaz gráfica para administrar funciones.

    Args:
        base (ctk.CTk): El objeto base de la aplicación.

    Returns:
        None
    """
    boton_administrar_funciones = ctk.CTkButton(base.toggle_menu,
                                                text="Administrar funciones",
                                                width=250,
                                                height=40,
                                                border_width=1,
                                                border_color="black",
                                                fg_color="#329ADF",
                                                font=("Arial", 15, "bold"),
                                                hover_color="#31AF9C",
                                                command=lambda: BSB.crear_frame_administrar_funciones(base))
    boton_administrar_funciones.place(x=20, y=270)

def colocar_boton_cambiar_tema(base: ctk.CTk) -> None:
    """
    Coloca un botón para cambiar el tema en la interfaz gráfica.

    Args:
        base (ctk.CTk): La ventana principal de la interfaz gráfica.

    Returns:
        None
    """
    # Determina el estado inicial del switch basado en el tema actual.
    tema_actual = ctk.get_appearance_mode()

    switch_tema = ctk.CTkSwitch(
        base.toggle_menu,
        width=50, height=30,
        text="Cambiar tema",
        button_hover_color="#31AF9C",
        font=("Arial", 15, "bold"),
        command=lambda: BSB.cambiar_tema(switch_tema)
    )

    # Establece el estado inicial del switch
    if tema_actual == 'Dark':
        switch_tema.deselect()
    else:
        switch_tema.select()
    
    if base.tipo_usuario == "cliente":
        switch_tema.place(x=20, y=150)
    else:
        switch_tema.place(x=20, y=330)

def colocar_boton_cerrar_sesion(base: ctk.CTk) -> None:
    """
    Coloca un botón de salida en la interfaz gráfica.

    Args:
        base (ctk.CTk): La base de la interfaz gráfica.

    Returns:
        None
    """
    boton_salir = ctk.CTkButton(base.toggle_menu,
                                text="Cerrar sesión",
                                width=250,
                                height=40,
                                fg_color="#329ADF",
                                border_width=1,
                                border_color="black",
                                font=("Arial", 15, "bold"),
                                hover_color="#31AF9C",
                                command=lambda: BSB.cerrar_sesion(base))
    if base.tipo_usuario == "cliente":
        boton_salir.place(x=20, y=210)
    else:
        boton_salir.place(x=20, y=390)

def crear_opciones_side_bar(base: ctk.CTk) -> None:
    """
    Crea los botones de opciones en la barra lateral.

    Args:
        base (ctk.CTk): El objeto base de la aplicación.

    Returns:
        None
    """
    botones_comunes = [
        colocar_boton_inicio,
        colocar_boton_editar_perfil,
        colocar_boton_cambiar_tema,
        colocar_boton_cerrar_sesion
    ]

    if base.tipo_usuario == "cliente":
        botones_especificos = []
    else:
        botones_especificos = [
            colocar_boton_administrar_peliculas,
            colocar_boton_administrar_funciones,
            colocar_boton_administrar_salas
        ]

    for boton in botones_comunes + botones_especificos:
        boton(base)

def ocultar_side_bar(base: ctk.CTk, separador: ctk.CTkFrame) -> None:
    """
    Oculta la barra lateral en la aplicación.

    Args:
        base (ctk.CTk): La ventana principal de la aplicación.
        separador (ctk.CTkFrame): El separador que se debe destruir.

    Returns:
        None
    """
    base.toggle_menu.destroy()
    separador.destroy()
    base.desplegar_menu_boton.configure(text="≡", command=lambda: crear_side_bar(base))
