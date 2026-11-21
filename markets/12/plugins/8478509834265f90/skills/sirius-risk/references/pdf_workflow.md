# Informe y PDF — ejecución condicionada al entorno

Después de acceso válido y evidencia suficiente, entregar el informe final en el chat y conservar exactamente ese texto en `informe_texto`.

Solo si hay ejecución Python real, `reportlab`, escritura en `/mnt/data/` y descarga de artefactos disponibles, cargar `scripts/generar_informe_pdf.py` y llamar `generar_pdf(informe_texto)`. No asumir que empaquetar el archivo habilita Code Interpreter. No instalar servicios externos ni enviar el informe al MCP.

El helper original usa ReportLab: A4, márgenes de 2 cm, líneas de 14 puntos, ajuste a 95 caracteres y saltos de página. No resumir ni alterar el texto. No cambiar biblioteca ni ruta en operación normal. Comprobar que `/mnt/data/sirius_informe.pdf` existe y es un PDF legible antes de enlazarlo.

Cuando el entorno soporte realmente enlaces sandbox y el archivo exista, conservar la salida original:

✅ Informe listo  
📥 Descargar PDF: (sandbox:/mnt/data/sirius_informe.pdf)

Si Python, reportlab, ruta o descarga no están disponibles, no ejecutar un flujo ficticio ni afirmar que se creó PDF. Mantener el informe en chat y responder literalmente:

“No pude generar el PDF en esta ejecución. Puedo reintentar la generación si lo pides.”

No introducir otra tool ni generación PDF en el MCP. El helper original usa la fuente estándar y textwrap: no garantiza emojis, tipografía Unicode completa ni conservación exacta de espacios al extraer texto de PDF. Si el informe requiere caracteres no renderizables, declarar esa limitación sin reemplazar silenciosamente contenido. NO DISPONIBLE ACTUALMENTE EN LA SKILL / PREPARADO PARA SOPORTE FUTURO cuando el entorno carezca de estas capacidades.
