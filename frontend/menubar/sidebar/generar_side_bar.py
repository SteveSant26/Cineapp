import customtkinter as ctk
from . import funcion_botones_side_bar as BSB


def crear_side_bar(base: ctk.CTk):
    """
    Crea una barra lateral en la ventana base dada.

    Args:
        base (ctk.CTk): La ventana base en la que se creará la barra lateral.

    Returns:
        None
    """
    alto = base.winfo_height()
    ancho = 300

    base.toggle_menu = ctk.CTkFrame(
        base, width=ancho, height=alto, fg_color="transparent")
    base.toggle_menu.place(x=0, y=50)

    separador = ctk.CTkFrame(base, width=2, height=alto, fg_color="black")
    separador.place(x=ancho, y=50)

    base.desplegar_menu_boton.configure(
        text="x", command=lambda: ocultar_side_bar(base, separador))

    crear_opciones_side_bar(base)


def crear_opciones_side_bar(base: ctk.CTk):

    colocar_boton_inicio(base)
    colocar_boton_administrar_peliculas(base)
    colocar_boton_administrar_funciones(base)
    colocar_boton_administrar_salas(base)
    colocar_boton_cambiar_tema(base)
    colocar_boton_salir(base)


def colocar_boton_inicio(base: ctk.CTk):
    from frontend.cartelera import mostrar_peliculas
    boton_inicio = ctk.CTkButton(base.toggle_menu,
                                 text="Inicio",
                                 width=250,
                                 height=40,
                                 border_width=1,
                                 border_color="black",
                                 fg_color="#329ADF",
                                 font=("Arial", 15, "bold"),
                                 hover_color="#31AF9C",
                                 command=lambda: mostrar_peliculas(base))
    boton_inicio.place(x=20, y=30)


def colocar_boton_administrar_peliculas(base: ctk.CTk):
    boton_administrar_peliculas = ctk.CTkButton(base.toggle_menu,
                                                text="Administrar peliculas",
                                                width=250,
                                                height=40,
                                                border_width=1,
                                                border_color="black",
                                                fg_color="#329ADF",
                                                font=("Arial", 15, "bold"),
                                                hover_color="#31AF9C",
                                                command=lambda: BSB.crear_frame_administrar_peliculas(base))
    boton_administrar_peliculas.place(x=20, y=90)


def colocar_boton_administrar_funciones(base: ctk.CTk):
    """
    Coloca un botón en la interfaz gráfica para administrar funciones.

    Parameters:
        base (obj): Objeto base de la interfaz gráfica.

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
    boton_administrar_funciones.place(x=20, y=150)


def colocar_boton_administrar_salas(base: ctk.CTk):
    """
    Coloca un botón en la interfaz para administrar las salas.

    Parameters:
    - base: La base de la interfaz donde se colocará el botón.

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


def colocar_boton_cambiar_tema(base: ctk.CTk):
    """
    Coloca un botón para cambiar el tema en la interfaz gráfica.

    Args:
        base (ctk.CTk): La ventana principal de la interfaz gráfica.

    Retorna:
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
        command=lambda: BSB.cambiar_tema(switch_tema, base)
    )

    # Establece el estado inicial del switch
    if tema_actual == 'Dark':
        switch_tema.deselect()
    else:
        switch_tema.select()

    switch_tema.place(x=20, y=270)


def colocar_boton_salir(base: ctk.CTk):
    """
    Coloca un botón de salida en la interfaz gráfica.

    Args:
        base (ctk.CTk): La base de la interfaz gráfica.

    Retorna:
        None
    """
    boton_salir = ctk.CTkButton(base.toggle_menu,
                                text="Salir",
                                width=250,
                                height=40,
                                fg_color="#329ADF",

                                border_width=1,
                                border_color="black",
                                font=("Arial", 15, "bold"),
                                hover_color="#31AF9C",
                                command=lambda: BSB.salir(base))
    boton_salir.place(x=20, y=330)


def ocultar_side_bar(base: ctk.CTk, separador):
    """
    Function to hide the side bar in the application.

    Parameters:
    - base: The main application window object.
    - separador: The separator object to be destroyed.

    Returns:
    None
    """
    base.toggle_menu.destroy()
    separador.destroy()
    base.desplegar_menu_boton.configure(
        text="≡", command=lambda: crear_side_bar(base))
