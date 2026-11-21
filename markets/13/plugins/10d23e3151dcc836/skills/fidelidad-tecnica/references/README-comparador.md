# Comparador de fidelidad entre prompt e informe

Versión 1.0.0. Programa Python independiente, sin red, servidor, OAuth, MCP, Node ni paquetes externos. Requiere Python 3.10 o posterior. El prompt revisado por la persona usuaria es la única fuente de verdad. No calcula posiciones, no deduce aspectos a partir de grados, no consulta reglas de regencia ni compara cartas entre sí.

El programa separa Tropical, Memoria inconsciente y Sideral, extrae declaraciones reconocibles y compara las afirmaciones reconocibles del informe con esa referencia. No incorpora nombres ni reglas de un consultante concreto. Los ejemplos y las pruebas son ficticios.

## Archivos y uso

Guardar el prompt original como `datos_originales.txt` y el texto íntegro del informe como `informe_final.txt`, ambos en UTF-8. Se conservan literalmente los saltos CRLF/LF, espacios, tildes y contenido original. El programa no escribe sobre los archivos de entrada ni sobrescribe resultados anteriores.

Desde la carpeta del comparador:

```sh
python comparador_fidelidad.py preparar --prompt datos_originales.txt --salida registro_v1.json
python comparador_fidelidad.py auditar --prompt datos_originales.txt --informe informe_final.txt --registro registro_v1.json --salida auditoria_v1.json
python comparador_fidelidad.py comprobar --prompt datos_originales.txt --informe informe_final.txt --recibo auditoria_v1.json
```

`preparar` produce el registro previo a la redacción. `auditar` vuelve a extraer la referencia desde el original y, si se aporta `--registro`, comprueba que coincide íntegramente. El registro no puede sustituirse silenciosamente por otro JSON modificado. `comprobar` repite el análisis y contrasta el recibo completo con los archivos y el programa actuales.

Después de cualquier edición del informe, ejecutar `auditar` otra vez con un archivo de salida nuevo, por ejemplo `auditoria_v2.json`. Después de una revisión del prompt, generar también un registro nuevo. No retirar del informe frases difíciles de auditar para luego añadirlas después de la comprobación.

Límites: 1.000.000 bytes UTF-8 para cada texto de entrada y 32.000.000 bytes para leer un registro o recibo JSON. Si se supera un límite, queda sin completar la auditoría; no se autoriza dividir el informe para presentarlo como revisado íntegramente. No lee PDF, DOCX, imágenes ni tablas gráficas directamente. Su conversión fiel a texto requiere revisión.

## Resultados y aprobación

| Campo / estado | Significado |
| --- | --- |
| `source.status=ready` | Se extrajeron hechos y no se detectaron pendientes en la gramática del programa. No certifica exactitud astronómica ni extracción exhaustiva. |
| `status=blocked` | Hay discrepancias o no se pudo extraer una referencia utilizable. |
| `fidelityStatus=mismatch` | Una afirmación reconocida contradice un dato expreso del mismo mapa. |
| `fidelityStatus=pending` | Hay ambigüedades, datos no proporcionados, pendientes de la fuente o ninguna afirmación verificable. |
| `fidelityStatus=matched_supported_claims` | Coinciden las afirmaciones reconocidas; no significa que toda la prosa haya sido verificada. |
| `status=requires_manual_review` | Continúa siendo necesaria la revisión humana, incluso cuando coinciden las expresiones reconocidas. |
| `deliveryAllowed=false` | El programa nunca autoriza automáticamente la entrega. No tiene una opción para omitir esta barrera. |

Cada incidencia incluye `reference.quote`, línea y coordenadas del fragmento original. Las discrepancias incluyen `actual`, `expected` y citas `sourceReferences` del prompt. Un dato ausente queda pendiente: no se transforma en un hecho falso ni en una aprobación. Si la fuente declara dos valores diferentes para el mismo campo del mismo mapa, se conservan ambos y se solicita revisión; el programa no elige uno ni modifica el prompt.

Los índices `start/end` son posiciones de caracteres Unicode para cortes de cadenas Python, con extremo final excluido. `byteStart/byteEnd` son posiciones en los bytes UTF-8 originales. `line` empieza en 1. Los contextos de pendientes se limitan a una ventana cercana para evitar duplicar párrafos enormes; el análisis sí recibe el texto completo.

### Códigos de salida

| Código | Preparar / auditar | Comprobar |
| --- | --- | --- |
| 0 | Registro preparado o coincidencia de expresiones reconocidas. **No es aprobación completa.** | El recibo corresponde al contenido actual; puede contener discrepancias. |
| 2 | Discrepancias o ninguna referencia técnica utilizable. | No se usa. |
| 3 | Pendientes de revisión detectados. | No se usa. |
| 4 | Error de entrada, registro/recibo obsoleto, UTF-8 inválido o intento de sobrescribir un archivo. | No pudo comprobarse la vigencia. |

No decidir la entrega solo por el código del proceso, por `current=true` ni por el número de coincidencias. Leer también las incidencias, los pendientes de fuente, el alcance y la revisión humana.

## Expresiones que puede contrastar

Los ejemplos requieren un encabezado inequívoco como `## Sideral`, `A) Tropical:` o `B) Memoria inconsciente:`, o una mención explícita de un único mapa en la frase. Un encabezado general de Síntesis o Comparación no permite adivinar el mapa. Las menciones literarias a «su memoria» no cambian la carta.

| Categoría | Ejemplos reconocidos | Alcance |
| --- | --- | --- |
| Aspectos directos | `Sol conjunción Mercurio`; `El Sol forma un sextil con Mercurio`; `Sol y Mercurio forman un sextil`; `conjunción Sol–Mercurio` | Compara el nombre declarado para ese par y esa carta, sin calcular ángulos. |
| Enumeraciones de un aspecto | `Los sextiles del Sol con la Luna, Venus y Marte`; `Sol mantiene sextiles con Luna, Venus y Mercurio` | Desglosa cada relación, también dentro de un párrafo largo o con saltos de línea. |
| Dos sujetos explícitos | `Los sextiles de Sol y Luna con Mercurio` | Desglosa Sol–Mercurio y Luna–Mercurio; no deduce otras relaciones. |
| Signos y posiciones | `Sol en Aries`; `Sol se encuentra en el signo de Aries` | Compara solo el signo expresamente aportado. |
| Casas | `Sol en casa IX`; `Sol en Aries, en casa 9`; `La casa del Sol es IX` | Números arábigos o romanos I–XII. No calcula casas. |
| Cúspides | `La cúspide de la casa 5 se encuentra en Aries, grado 4º` | Campo propio de la cúspide, separado de la posición de un planeta. |
| Decanato y dodecatemoria por signo | `Sol en Aries, decanato Leo, dodecatemoria Sagitario`; `El decanato del Sol es Leo` | No convierte números de decanato en signos ni aplica fórmulas. |
| Grados, minutos y segundos | `Sol en Aries, grado 12º, minuto 30, segundo 15`; `Sol en Aries 12° 30′ 15″` | Comparación decimal literal, sin redondear ni convertir a longitud absoluta. |
| Regencias explícitas | `Planeta regente del signo solar es Venus`; `Regente de Aries es Saturno`; `Saturno es regente de Aries`; `Regente de la casa IX es Venus` | No asigna regentes por conocimiento astrológico. |
| Ángulo y orbe declarados junto al aspecto | `Sol trígono Mercurio (120º, orbe 2,5º)` | Compara los números con la fuente, aunque no coincidan con una definición astronómica del aspecto. |
| Ausencia explícita | `Saturno no tiene aspectos` | Contrasta una declaración literal. Un inventario incompleto no implica ausencia. |

Aspectos del vocabulario: conjunción, semisextil, semicuadratura, sextil, quintil, cuadratura, trígono, sesquicuadratura, biquintil, quincuncio y oposición, con sus plurales. Se reconocen los doce signos en español y los nombres de puntos enumerados en `BODIES` en el programa. Las tildes, mayúsculas, guiones largos, marcado básico de negrita y variantes decimales `2,50`/`2.5` se normalizan solo para comparar; las citas y las huellas conservan el original.

## Expresiones que requieren revisión humana

- Pronombres o elipsis: `su conjunción con Mercurio`, `sus trígonos`, cadenas con cambio de aspecto y sujeto omitido.
- Comparaciones entre cartas, mapa ausente, varios mapas en la misma frase o cambios de contexto implícitos.
- Negaciones complejas, hipótesis, condicionales y citas de un error: `no forma sextil`, `quizá`, `podría`, `en lugar de`. No se adjudica polaridad por suposición.
- Adjetivos como `ariano`, dignidades, retrogradación, dispositores, patrones y relaciones no incluidas en la gramática; glifos y nombres o idiomas no reconocidos.
- Tablas, diagramas, datos obtenidos por OCR, abreviaturas y formatos numéricos alternativos no documentados. Pueden extraerse fragmentos reconocibles, pero no se certifica el formato completo.
- Paráfrasis libres de regencias, decanatos numerados, conversiones de grados a otras unidades o relaciones deducidas.
- Contenido técnico en paréntesis no reconocido. Etiquetas nativas descriptivas como `Ascendente(Cúspide casa 1)` se tratan como etiquetas de presentación; no se deduce de ellas una posición en casa ni una equivalencia entre puntos.
- Interpretación simbólica, filosófica, biográfica o causal. El programa no determina su calidad ni su fidelidad al método.

El detector de vocabulario tampoco puede encontrar todas las posibles afirmaciones técnicas formuladas de manera desconocida. Por eso incluso `matched_supported_claims` conserva `manualReviewRequired=true` y `deliveryAllowed=false`. La revisión humana debe leer el informe entero, además de los fragmentos señalados.

## Huellas y límites del recibo local

El recibo vincula `promptSha256`, `sourceSha256`, `reportSha256`, `comparatorSha256` y `auditSha256`. Cambiar un espacio, un salto de línea o una tilde cambia la huella. `comprobar` recalcula el resultado completo: editar un campo del recibo no lo convierte en aprobado.

Esto es control de consistencia local, no una firma digital, autenticación, protección contra alguien que pueda modificar también el programa, ni historial inviolable. No acredita quién revisó el prompt o el informe. Tampoco detecta una modificación intermedia si después se restauran exactamente los bytes anteriores. La revisión humana y su identidad se registran por separado; no se inventan ni se deducen de una salida Python. Los JSON contienen fragmentos del caso: conservarlos con la misma privacidad que el informe.

## Pruebas y ejemplos

```sh
python -B -m unittest discover -s . -p test_comparador_fidelidad.py
python comparador_fidelidad.py auditar --prompt ejemplos/prompt.txt --informe ejemplos/informe_incorrecto.txt --salida ejemplo_error.json
python comparador_fidelidad.py auditar --prompt ejemplos/prompt.txt --informe ejemplos/informe_correcto.txt --salida ejemplo_coincidencias.json
python comparador_fidelidad.py auditar --prompt ejemplos/prompt.txt --informe ejemplos/informe_ambiguo.txt --salida ejemplo_pendiente.json
```

El ejemplo incorrecto debe devolver código 2 y `expected=conjuncion` para `Mercury|Sun` en Sideral. El correcto debe devolver 0 con `matched_supported_claims`, sin esa discrepancia, pero con entrega automática deshabilitada. El ambiguo debe devolver 3 y señalar la formulación pendiente.

Ver `COORDINADOR.md` para la incorporación propuesta. No se ha modificado ni instalado el coordinador actual y no se ha probado esta ejecución dentro de una sesión de ChatGPT: las pruebas incluidas se ejecutan en Python local.
