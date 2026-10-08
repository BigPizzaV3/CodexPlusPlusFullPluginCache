# Routing de capacidades

ChatGPT selecciona la Skill por el producto final. Dentro de la Skill, activar solo capacidades que cambien contenido, riesgo, aceptación o formato.

| Necesidad | Capacidad |
|---|---|
| analizar documentos o PDF | lectura documental/PDF disponible |
| calcular, reconciliar o graficar datos | hoja de cálculo o cálculo determinista |
| crear slides o PPTX | Presentations con `@oai/artifact-tool` |
| editar PPTX | Presentations con `@oai/artifact-tool` |
| inspeccionar visualmente | renderizado y revisión de imágenes |
| obtener datos actuales o fuentes | búsqueda web con fuente verificable, solo con `WEB_COMPLEMENTARY` confirmado |
| crear ilustración | generación de imagen, nunca como evidencia factual |
| profundizar decisión `M3/M4` | H.AMA especializada, si está instalada |

## Reglas

- No invocar una herramienta si instrucciones y referencias bastan.
- No asumir que una capacidad disponible en un entorno existirá en otro.
- Componer varias capacidades únicamente cuando exista dependencia real.
- Verificar la salida de cada herramienta antes de transferirla a la siguiente.
- Aplicar el fallback de producción cuando la capacidad requerida no exista.
- No activar búsqueda web con `FILES_AND_CONTEXT_ONLY`; en tareas que crearán slides, si el modo aún no fue confirmado, mostrar ambas opciones y esperar.
- No producir slides antes de que el brief completo esté confirmado.
- Gamma, Presenton y cualquier generador externo de presentaciones quedan excluidos de la ruta de producción. Si Presentations no está disponible, entregar una especificación/storyboard utilizable y declarar la limitación; no sustituir el motor.
