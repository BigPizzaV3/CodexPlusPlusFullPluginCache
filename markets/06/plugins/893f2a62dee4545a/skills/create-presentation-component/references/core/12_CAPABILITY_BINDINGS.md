# Contrato de capacidades externas

## Naturaleza

Las herramientas y Apps son dependencias de ejecución, no autoridades de diseño. Verificar su disponibilidad antes de usarlas y validar su salida antes de integrarla.

| Capacidad lógica | Entrada | Salida | Fallback |
|---|---|---|---|
| lectura de fuentes | archivo o URL autorizada | contenido y localizadores | solicitar contenido o limitar alcance |
| cálculo/datos | tabla y reglas | valores reconciliados/visual | tabla validada sin gráfico |
| producción de slides/PPTX | brief confirmado, storyboard, plantilla y activos | PPTX editable mediante Presentations + `@oai/artifact-tool` | storyboard/especificación; nunca otro generador |
| renderizado | artefacto | imágenes/PDF de inspección | revisión estructural condicionada |
| búsqueda actual | brief confirmado con `WEB_COMPLEMENTARY`, pregunta y dominio | evidencia citada | archivos/contexto o pendiente, según decisión del usuario |
| generación visual | brief gráfico | activo ilustrativo | composición sin imagen |
| análisis H.AMA | problema `M3/M4` | hallazgos y riesgos | contrato local de materialidad |

No exponer secretos, no transmitir datos fuera del alcance autorizado y no ejecutar acciones externas irreversibles sin autorización aplicable. En tareas de creación, `FILES_AND_CONTEXT_ONLY` prohíbe toda búsqueda web y un modo pendiente prohíbe tanto la web como la producción. Gamma, Presenton y otros generadores externos no son bindings válidos para crear slides.
