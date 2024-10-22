import customtkinter as ctk
from . import sidebar as SB


def crear_menu_bar(base: ctk.CTk) -> None:
    """
    Crea la barra de menú de la aplicación.

    Args:
        base (ctk.CTk): El objeto base de la aplicación.

    Returns:
        None
    """
    base.menu_bar_frame = ctk.CTkFrame(base, fg_color="transparent", height=50)
    base.menu_bar_frame.pack(side="top", fill="x")
    base.menu_bar_frame.pack_propagate(False)

    base.desplegar_menu_boton = ctk.CTkButton(base.menu_bar_frame,
                                              fg_color="transparent",
                                              hover=False,
                                              text="≡",
                                              text_color=("black", "White"),
                                              font=("Arial", 40, "bold"),
                                              width=20, height=20,
                                              command=lambda: SB.crear_side_bar(base))
    base.desplegar_menu_boton.pack(side="left", padx=10)

    base.desplegar_menu_boton.bind("<Enter>", lambda e: enter_hover_text(base))
    base.desplegar_menu_boton.bind("<Leave>", lambda e: leave_hover_text(base))

    titulo_app = ctk.CTkLabel(base.menu_bar_frame, text="INTERCINES", font=("Arial", 30, "bold"))
    titulo_app.pack(side="left", padx=10)
    

    separator = ctk.CTkFrame(base, height=2, fg_color="black")
    separator.pack(side="top", fill="x")

def enter_hover_text(base: ctk.CTk) -> None:
    """
    Cambia el color del texto del botón al pasar el ratón por encima.

    Args:
        base (ctk.CTk): El objeto base de la aplicación.

    Returns:
        None
    """
    base.desplegar_menu_boton.configure(text_color="#31AF9C")

def leave_hover_text(base: ctk.CTk) -> None:
    """
    Restaura el color del texto del botón al quitar el ratón de encima.

    Args:
        base (ctk.CTk): El objeto base de la aplicación.

    Returns:
        None
    """
    base.desplegar_menu_boton.configure(text_color=("black", "White"))
