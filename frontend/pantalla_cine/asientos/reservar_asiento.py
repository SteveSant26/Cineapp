import customtkinter as ctk
from tkinter import messagebox
from frontend import utils
from fpdf import FPDF
import datetime
from . import crear_asientos_img as CAI
from . import utils_asientos as UA
from . generar_asientos import actualizar_asientos

def obtener_asiento(frame_sala, fila, columna):
    """Obtiene el asiento de la grilla en la posición dada."""
    return frame_sala.grid_slaves(row=fila, column=columna)[0]

def generar_pdf_asientos(asientos_seleccionados, usuario):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    pdf.cell(200, 10, txt="Confirmación de Reservación de Asientos", ln=True, align='C')
    pdf.cell(200, 10, txt=f"Usuario: {usuario}", ln=True, align='L')
    pdf.cell(200, 10, txt="Asientos Reservados:", ln=True, align='L')
    
    for asiento in asientos_seleccionados:
        fila, columna = asiento
        pdf.cell(200, 10, txt=f"Fila: {fila}, Columna: {columna}", ln=True, align='L')
    tiempo_actual = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    pdf.output(f"tickets\\Asientos_Reservados({usuario})_{tiempo_actual}.pdf")
    messagebox.showinfo("PDF Generado", "Se ha generado un PDF con los asientos reservados.")

def reservar_asientos(base: ctk.CTk) -> None:
    """Reserva los asientos seleccionados en la sala de cine."""
    if base.mejor_asiento:
        base.asientos_seleccionados.add(base.mejor_asiento)
        fila, columna = base.mejor_asiento
        UA.unbind_asiento(obtener_asiento(base.frame_sala, fila, columna))
        base.mejor_asiento = None

    for asiento in base.asientos_seleccionados:
        fila, columna = asiento
        widget = obtener_asiento(base.frame_sala, fila, columna)
        UA.unbind_asiento(widget)
        widget.configure(image=CAI.ASIENTOS_IMAGEN["asiento_reservado"], state="disabled", border_color=("white", "black"))
        if base.tipo_usuario == "cliente":
            widget.configure(image=CAI.ASIENTOS_IMAGEN["asiento_ocupado"], state="disabled", border_color="#C15F44")

    print(base.asientos_habilitados)
    
    UA.agregar_asientos(base.asientos_reservados_id, base.asientos_seleccionados, base.usuario, habilitar=base.asientos_habilitados)
    
    generar_pdf_asientos(base.asientos_seleccionados, base.usuario)
    actualizar_asientos(base)
    
    
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

    for fila, columna in base.asientos_reservados:
        base.asientos_seleccionados.add((fila, columna))
        asiento_reservado = obtener_asiento(base.frame_sala, fila, columna)
        asiento_reservado.configure(image=CAI.ASIENTOS_IMAGEN["asiento_habilitado"], state="normal", border_color="#C15F44")
        asiento_reservado.bind("<Button-1>", lambda event, row=fila, col=columna: click_en_asiento(row, col, base))
        UA.bind_asiento(asiento_reservado, CAI.ASIENTOS_IMAGEN["asiento_libre"], CAI.ASIENTOS_IMAGEN["asiento_habilitado"])

def click_en_asiento(fila: int, columna: int, base: ctk.CTk) -> None:
    """Función llamada cuando se hace clic en un asiento habilitado."""
    if (fila, columna) in base.asientos_reservados:
        if (fila, columna) in base.asientos_seleccionados:
            asiento = obtener_asiento(base.frame_sala, fila, columna)
            asiento.unbind("<Button-1>")
            UA.unbind_asiento(asiento)
            asiento.configure(image=CAI.ASIENTOS_IMAGEN["asiento_libre"], state="normal", border_color="#31AF5D")
            UA.bind_asiento(asiento, CAI.ASIENTOS_IMAGEN["asiento_hover"], CAI.ASIENTOS_IMAGEN["asiento_libre"])
            print(f"Asiento en la fila {fila}, columna {columna} deseleccionado")
            base.asientos_seleccionados.add((fila, columna))
