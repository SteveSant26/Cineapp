import customtkinter as ctk
import datetime
from jinja2 import Template
import os
import pdfkit
import re
from tkinter import messagebox
from frontend import utils
import datetime
from . import crear_asientos_img as CAI
from . import utils_asientos as UA
from . generar_asientos import actualizar_asientos

def obtener_asiento(frame_sala, fila, columna):
    """Obtiene el asiento de la grilla en la posición dada."""
    return frame_sala.grid_slaves(row=fila, column=columna)[0]

def corregir_nombre_archivo(filename: str) -> str:
    """
    Replace or remove characters that are invalid in filenames.
    """
    return re.sub(r'[<>:"/\\|?*]', '', filename)

def generar_pdf_asientos(asientos_seleccionados, usuario, titulo_pelicula, funcion) -> None:
    plantilla_html = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Reservación Intercine</title>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Roboto', sans-serif;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
        }
        .ticket-container {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            width: 100vw;
        }
        .ticket {
            background-color: #ffffff;
            border-radius: 10px;
            border: 1px solid #dcdcdc;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
            padding: 20px;
            max-width: 400px;
            width: 100%;
            text-align: center;
        }
        .highlight {
            background-color: #55B7EC;
            color: #ffffff;
            font-weight: bold;
            padding: 10px;
            border-radius: 5px;
            margin-bottom: 20px;
        }
        .content p {
            margin: 10px 0;
        }
        .content strong {
            display: block;
            margin-top: 20px;
            font-size: 18px;
        }
        .movie-details {
            margin-top: 10px;
            font-size: 16px;
            color: #333;
        }
        hr {
            border: none;
            border-top: 1px solid #dcdcdc;
            margin: 20px 0;
        }
    </style>
</head>
<body>
    <div class="ticket-container">
        <div class="ticket">
            <div class="highlight">INTERCINES</div>
            <div class="content">
                <hr>
                <p><strong>¡¡DISFRUTA TU PELÍCULA!!</strong></p>
                <p>--{{ titulo }}--</p>
                <hr>
                <p><strong>Usuario:</strong> {{ usuario }}</p>
                <p><strong>Hora:</strong> {{ hora }}</p>
                <p><strong>Asientos Reservados:</strong></p>
                {% for fila, columna in asientos %}
                    <p class="movie-details">Fila: {{ fila }}, Columna: {{ columna }}</p>
                {% endfor %}
                <hr>
            </div>
            <div class="highlight">Gracias por tu compra</div>
        </div>
    </div>
</body>
</html>
    """

    plantilla = Template(plantilla_html)
    html_renderizado = plantilla.render(usuario=usuario, titulo=titulo_pelicula, hora=funcion, asientos=asientos_seleccionados)

    tiempo_actual = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    titulo_pelicula = corregir_nombre_archivo(titulo_pelicula)
    
    filename = f"tickets\\Asientos_Reservados({usuario})_{titulo_pelicula}_{tiempo_actual}.pdf"
    
    config = pdfkit.configuration(wkhtmltopdf='C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')
    
    options = {
        'enable-local-file-access': None,
    }
    
    try:
        pdfkit.from_string(html_renderizado, filename, options=options, configuration=config)
        utils.mostrar_mensaje("PDF Generado", "Se ha generado un archivo PDF con los asientos reservados.")
        os.startfile(os.path.realpath(filename))
    
    except Exception as e:
        utils.mostrar_mensaje("Error", f"Se ha producido un error al generar el PDF: {str(e)}")



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
    
    if messagebox.askyesno("Descargar ticket de boletos", "¿Desea descargar el ticket de los asientos reservados?"):
        generar_pdf_asientos(base.asientos_seleccionados, base.usuario, base.titulo_pelicula,base.funcion_actual)
    
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
