import customtkinter as ctk
from tkinter import messagebox
from frontend.cartelera import datos_peliculas as DP
from frontend import utils
from . import crear_asientos_img as CAI
from . import utils_asientos as U

def obtener_asiento(frame_sala, fila, columna):
    """Obtiene el asiento de la grilla en la posición dada."""
    return frame_sala.grid_slaves(row=fila, column=columna)[0]

def reservar_asientos(base: ctk.CTk) -> None:
    """Reserva los asientos seleccionados en la sala de cine."""
    if base.mejor_asiento:
        base.asientos_seleccionados.add(base.mejor_asiento)
        fila, columna = base.mejor_asiento
        U.unbind_asiento(obtener_asiento(base.frame_sala, fila, columna))
        base.mejor_asiento = None

    for asiento in base.asientos_seleccionados:
        fila, columna = asiento
        widget = obtener_asiento(base.frame_sala, fila, columna)
        U.unbind_asiento(widget)
        widget.configure(image=CAI.ASIENTOS_IMAGEN["asiento_reservado"], state="disabled")

    numero_asientos_seleccionados = len(base.asientos_seleccionados)

    U.agregar_asientos(base.asientos_reservados_id, base.asientos_seleccionados, base.usuario, habilitar=base.asientos_habilitados)
    messagebox.showinfo("Asientos reservados", f"Usted ha reservado {numero_asientos_seleccionados} asient{'os' if numero_asientos_seleccionados > 1 else 'o'}")

    print(f"Asientos reservados: {base.asientos_seleccionados}")
    base.asientos_seleccionados.clear()
    base.asientos_habilitados = False
    base.asientos_reservados = U.obtener_todos_asientos_reservados(base.funcion_actual_id)

def preguntar_reservar(base) -> None:
    """Pregunta al usuario si desea reservar los asientos seleccionados."""
    if not base.asientos_seleccionados and not base.mejor_asiento:
        utils.mostrar_error("Sin selecciones", "No ha seleccionado ningún asiento para reservar")
        return

    if messagebox.askyesno("Confirmar Reserva", "¿Desea reservar los asientos seleccionados?"):
        reservar_asientos(base)

def habilitar_reservados(base: ctk.CTk) -> None:
    """Deselecciona los asientos reservados."""
    if not base.asientos_reservados:
        utils.mostrar_error("Sin asientos reservados", "No hay asientos reservados")
        return

    base.asientos_habilitados = True
    for (fila, columna) in base.asientos_reservados:
        base.asientos_seleccionados.add((fila, columna))
        asiento_reservado = obtener_asiento(base.frame_sala, fila, columna)
        asiento_reservado.configure(image=CAI.ASIENTOS_IMAGEN["asiento_habilitado"], state="normal")
        asiento_reservado.bind("<Button-1>", lambda event, row=fila, col=columna: click_en_asiento(row, col, base))
        U.bind_asiento(asiento_reservado, CAI.ASIENTOS_IMAGEN["asiento_libre"], CAI.ASIENTOS_IMAGEN["asiento_habilitado"])

def click_en_asiento(fila: int, columna: int, base: ctk.CTk) -> None:
    """Función llamada cuando se hace clic en un asiento habilitado."""
    if (fila, columna) in base.asientos_reservados:
        if (fila, columna) in base.asientos_seleccionados:
            asiento = obtener_asiento(base.frame_sala, fila, columna)
            asiento.unbind("<Button-1>")
            U.unbind_asiento(asiento)
            asiento.configure(image=CAI.ASIENTOS_IMAGEN["asiento_libre"], state="normal")
            U.bind_asiento(asiento, CAI.ASIENTOS_IMAGEN["asiento_hover"], CAI.ASIENTOS_IMAGEN["asiento_libre"])
            print(f"Asiento en la fila {fila}, columna {columna} deseleccionado")
            base.asientos_seleccionados.add((fila, columna))
