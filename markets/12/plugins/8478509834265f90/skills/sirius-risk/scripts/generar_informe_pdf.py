from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
import textwrap

output_pdf = "/mnt/data/sirius_informe.pdf"

def generar_pdf(texto, path=output_pdf):
    c = canvas.Canvas(path, pagesize=A4)
    width, height = A4

    margin_x = 2 * cm
    margin_y = 2 * cm

    x = margin_x
    y = height - margin_y

    line_height = 14  # un poco más legible

    max_width_chars = 95  # mejor ajuste horizontal

    for paragraph in texto.split("\n"):

        # Línea vacía
        if paragraph.strip() == "":
            y -= line_height
            if y < margin_y:
                c.showPage()
                y = height - margin_y
            continue

        # Ajuste de texto
        wrapped_lines = textwrap.wrap(paragraph, width=max_width_chars)

        for line in wrapped_lines:
            c.drawString(x, y, line)
            y -= line_height

            # Salto de página
            if y < margin_y:
                c.showPage()
                y = height - margin_y

    c.save()