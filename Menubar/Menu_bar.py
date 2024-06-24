import customtkinter as ctk

import Menubar.Opciones_menu_bar as OMB

import Menubar.Barra_busqueda.barra_busqueda as BB

import Menubar.side_bar as SB


def crear_menu_bar(base: ctk.CTk, busqueda=True) -> None:
    """
    Crea la barra de menú de la aplicación.

    Args:
        base: El objeto base de la aplicación.

    Returns:
        None
    """
    base.menu_bar_frame = ctk.CTkFrame(base, fg_color="transparent", height=50)
    base.menu_bar_frame.pack(side="top", fill="x")
    base.menu_bar_frame.pack_propagate(False)

    base.desplegar_menu_boton = ctk.CTkButton(base.menu_bar_frame,
                                              text="≡",
                                              fg_color="transparent",
                                              hover=False,
                                              font=("Arial", 40, "bold"),
                                              width=20, height=20,
                                              command=lambda: SB.crear_side_bar(base))
    base.desplegar_menu_boton.pack(side="left", padx=10)

    if ctk.get_appearance_mode() == "Dark":
        base.desplegar_menu_boton.configure(text_color="white")
    else:
        base.desplegar_menu_boton.configure(text_color="black")

    base.desplegar_menu_boton.bind(
        "<Enter>", lambda e: OMB.enter_hover_text(base))
    base.desplegar_menu_boton.bind(
        "<Leave>", lambda e: OMB.leave_hover_text(base))

    titulo_app = ctk.CTkLabel(
        base.menu_bar_frame, text="INTERCINES", font=("Arial", 30, "bold"))
    titulo_app.pack(side="left", padx=10)
    if busqueda:
        BB.crear_barra_busqueda(base)

    separator = ctk.CTkFrame(base, height=2, fg_color="black")
    separator.pack(side="top", fill="x")


