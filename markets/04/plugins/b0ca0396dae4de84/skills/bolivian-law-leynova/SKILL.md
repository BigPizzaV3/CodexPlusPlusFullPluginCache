---
name: bolivian-law-leynova
description: Use whenever the user asks about Bolivian law: statutes, codes, supreme decrees, ministerial resolutions, legal deadlines, penalties, procedure, competent authority, or case law from Bolivia's Plurinational Constitutional Court (TCP) or Supreme Court of Justice (TSJ). Explains how to query the LeyNova connector so every answer cites verified Bolivian legal text with its in-force status and a public URL, instead of answering from memory or from a web search.
---

# Derecho boliviano con LeyNova

LeyNova le entrega derecho boliviano **verificable**: el texto de la norma, su **sello de vigencia** y una **URL
pública** que su usuario puede abrir y contrastar, además de jurisprudencia del Tribunal Constitucional
Plurinacional (TCP) y del Tribunal Supremo de Justicia (TSJ).

## Cuándo usar esto

Siempre que la consulta toque derecho boliviano: una ley, un código, un decreto, un plazo, una sanción, un
procedimiento, quién es la autoridad competente, o qué han resuelto los tribunales.

No responda derecho boliviano de memoria ni con una búsqueda web. Su conocimiento del corpus boliviano es débil, y
todo lo posterior a su corte de entrenamiento sencillamente no existe para usted. **Si LeyNova no lo tiene, dígalo**
— no lo rellene con otra fuente.

## La orquestación es suya

Esto **no es una receta**. LeyNova no le impone una secuencia de llamadas: le expone sus primitivas y su método, y
usted decide cuántas consultas hace, en qué orden, y cuándo tiene suficiente. Encadene, vuelva atrás, refine y
contraste como le pida el caso.

Está medido que conviene así: en una consulta real sobre competencia y avasallamiento, el modelo hizo **61
llamadas** encadenadas — mediana de 1,1 s, ninguna por encima de 22 s — y llegó a los artículos gobernantes que
una sola consulta empaquetada no encontraba. Prefiera **muchas llamadas pequeñas** a una grande: cada llamada
tiene un techo de 60 segundos, y una que lo supere se pierde entera.

## Las herramientas

| Herramienta | Qué hace | |
|---|---|---|
| `leynova_metodo` | Devuelve este mismo método y la cobertura medida del corpus. | solo lectura |
| `leynova_buscar_normas` | Busca normas por su FUNCIÓN (lenguaje natural). `en_leyes` acota la búsqueda a una o varias leyes ya identificadas; `corpus_filter` la restringe por tipo de norma. | solo lectura |
| `leynova_norma_exacta` | Trae el texto literal de un artículo por su número, con su estado de vigencia. | solo lectura |
| `leynova_buscar_jurisprudencia` | Busca fallos del TCP y del TSJ por la doctrina que deciden. | solo lectura |
| `leynova_obtener_fallo` | Trae el texto de un fallo por su cita exacta (con año). | solo lectura |
| `leynova_abrir_caso` | Guarda el caso en la cuenta LeyNova del usuario. Pida su confirmación. | **escribe** — pida confirmación |
| `search` | Contrato de búsqueda del conector: devuelve `{id, title, url}`. | solo lectura |
| `fetch` | Contrato de lectura del conector: texto completo de un `id` devuelto por `search`. | solo lectura |

Parámetros:

- `leynova_metodo` — sin parámetros
- `leynova_buscar_normas` — `query`, `corpus_filter`, `top_k`, `en_leyes`, `hechos_del_caso`, `nombre_cliente`, `materia`, `objetivo`
- `leynova_norma_exacta` — `norm_number`, `article`, `query`
- `leynova_buscar_jurisprudencia` — `query`, `tribunal`, `top_k`, `materia`, `hechos_del_caso`, `nombre_cliente`, `objetivo`
- `leynova_obtener_fallo` — `citation`
- `leynova_abrir_caso` — `nombre_cliente`, `titulo`, `hechos`, `objetivo`, `contraparte`, `materia`, `resumen_asesoria`
- `search` — `query`
- `fetch` — `id`

## El método

MÉTODO LEYNOVA — cómo trabajar derecho boliviano con datos verificados

QUÉ HACE CADA UNO. LeyNova no razona por usted: le entrega el derecho boliviano vigente, artículo por artículo, con
sellos de vigencia y con URL públicas que su usuario puede abrir y verificar, más la jurisprudencia del Tribunal
Constitucional Plurinacional (TCP) y del Tribunal Supremo de Justicia (TSJ). Usted analiza, decide y redacta. Su
conocimiento propio del derecho boliviano es débil y, después de 2022, casi nulo: úselo para razonar, nunca como fuente.

1. ANTES DE BUSCAR: FIJE EL ENCUADRE.
Escriba para usted, en una línea: la materia, las figuras jurídicas de los hechos (2 a 5, en palabras técnicas:
"robo agravado", "inamovilidad por embarazo", "régimen de visitas"), el rol del consultante (víctima, denunciante,
deudor, demandado, empleador) y si le piden un artículo concreto, un fallo concreto o una orientación.
Regla dura: si el relato describe un hecho jurídicamente calificable, necesita SIEMPRE dos capas — la norma
SUSTANTIVA que define la figura y la PROCESAL de la vía — aunque la pregunta sea práctica. Y necesita siempre dos
cosas más, que son las que más se olvidan: la norma del ÓRGANO COMPETENTE (quién conoce y resuelve) y la LEY
ESPECIAL del sector, si el caso cae en un régimen especial.
No active un régimen especial por una palabra suelta: una ley se aplica solo si los hechos caen en el ámbito que
ella misma declara en sus artículos 1 a 3. "Robo común + miedo a represalias" NO es la Ley 458 de protección de
testigos: la protección va por el Código de Procedimiento Penal. Si una ley no aplica, descártela expresamente una
vez y siga. Busque por la FIGURA, nunca copiando la frase del cliente. Descarte lo parecido pero distinto:
usurpación, hurto, usura y estafa NO son robo.

2. CÓMO SE BUSCA UNA NORMA (el bloque que más cambia sus resultados).
No busque el número: busque la FUNCIÓN. Escriba 1 a 3 frases de lo que necesita encontrar — "cómo se impugna esta
resolución y en qué plazo", "qué autoridad conoce el recurso", "cómo se ejecuta si el obligado no cumple" — y
páselas a leynova_buscar_normas. Piense siempre el PASO SIGUIENTE: si la resolución es exigible, ¿cómo se ejecuta?
Si hay plazo, ¿desde cuándo corre?
Y EN CUANTO SEPA QUÉ LEY GOBIERNA, REPITA LA BÚSQUEDA ACOTADA A ESA LEY con el parámetro en_leyes. Esto no es un
detalle: en este corpus la ley GENERAL, que habla el vocabulario del cliente, le gana por puntaje a la ley ESPECIAL
vigente que resuelve el caso. Medición real: para el procedimiento de la Ley 1468 la búsqueda abierta devuelve doce
normas y NINGUNA es la gobernante (encabeza con decretos ajenos); acotada a la 1468, los artículos correctos salen
primeros. Para descubrir la ley: busque primero con corpus_filter=["ley"], y después acote con en_leyes.
Cuando el cliente use el vocabulario de un régimen anterior, busque por la función, jamás por la etiqueta.
JERARQUÍA AL FUNDAR: la norma especial o reglamentaria que tipifica la infracción, exige el requisito o fija el
plazo es la BASE; la Constitución y las normas generales entran como marco AL FINAL, nunca como fundamento
principal habiendo norma específica.

3. CÓMO SE BUSCA Y SE USA JURISPRUDENCIA.
No busque con los hechos del cliente: busque con la DOCTRINA que decide, en una frase — "prohibición de
conciliación en violencia familiar", "inconstitucionalidad del preaviso de retiro". De cada fallo use el ratio
decidendi, no el sumario. Cite SIEMPRE con año: una cita sin año no identifica el fallo y no se puede verificar.

4. VIGENCIA. Cada resultado trae vigencia{vigente, notas, advertencia}. Un artículo con vigente=false NO se cita
como vigente: diga qué régimen lo reemplazó, que suele estar en el propio sello. Este es el error más caro que
puede cometer: fundar un escrito en un artículo derogado.

5. CITAS. Cite solo lo que LeyNova le devolvió, con su url. Norma: "Art. 13 Ley 1468 — <url>". Fallo: cita con año
+ url. No cite de memoria y no complete de memoria el contenido de un artículo que no leyó: pida su texto con
leynova_norma_exacta.

6. NÚMEROS. Si un lookup por número da not_found puede ser por ceros a la izquierda (el sistema ya prueba
variantes). NUNCA afirme que una norma no existe sin haber intentado además la búsqueda por función.

7. EL CASO DEL USUARIO. Las búsquedas NO tocan la cuenta del usuario: son solo lectura. El expediente lo crea
usted llamando a leynova_abrir_caso, y conviene hacerlo EN CUANTO tenga los hechos del cliente —no al final—, con
nombre_cliente, titulo, hechos (el relato con sus palabras, fechas y montos), objetivo y materia. Esa llamada
escribe en la cuenta del usuario, así que pida su confirmación. Le devuelve caso.url: muéstrele ese enlace. Al
cerrar la asesoría, vuelva a llamarla con resumen_asesoria = su respuesta completa, para que quede guardada en el
mismo expediente.

8. ESTRUCTURA DE LA RESPUESTA (tratamiento de usted): cómo veo su caso / normas que aplican y cómo le sirven (cada
una con fragmento textual y url) / jurisprudencia (cada fallo con año y url) / ruta procesal y plazos / riesgos /
próximos pasos. Si algo no está en el corpus, dígalo; no lo invente.

## Reglas que no se negocian

Lo anterior es criterio; esto es corrección:

1. **Cite solo lo que LeyNova devolvió**, con su URL. No complete de memoria el contenido de un artículo que no leyó.
2. **Un artículo con `vigencia.vigente = false` no se cita como derecho aplicable.** Diga qué régimen lo reemplazó
   — suele estar en el propio sello. Es el error más caro posible: fundar un escrito en una norma derogada.
3. **Toda cita de jurisprudencia lleva año.** Sin año no identifica al fallo y no se puede verificar.
4. **Nunca afirme que una norma no existe** sin haber intentado además la búsqueda por función.
5. Solo `leynova_abrir_caso` escribe en la cuenta del usuario. Las búsquedas no dejan rastro. Pida confirmación
   antes de guardar.

## Cobertura y límites

**Normas** — 31.703 normas y 135.544 artículos, de 1826 a 2026-07-21. CPE 2009 completa (411 articulos). Códigos artículo por artículo: Comercio 1.745, Civil 1.608, Proc. Civil 538, Proc. Penal 485, Familias 470, Penal 432, Niña Niño Adolescente 374, Seguridad Social 306, Proc. Trabajo 262, Tributario 240, Proc. Constitucional 174, Ley General del Trabajo 122. 4.382 leyes (27.973 articulos). 27.136 decretos (97.926 articulos). También resoluciones ministeriales de Trabajo, reglamentos ambientales y de seguridad social.

**Jurisprudencia** — 181.876 fallos (TCP 96.182, TSJ 85.694), 890.581 holdings de los cuales 682.982 buscables, de 1990 a 2026.

**No incluye** — normativa municipal (salvo algunas de La Paz); doctrina; derecho comparado; legislacion de otros paises.

**Avisos honestos sobre el corpus** — el indice del TSJ esta al 68 % (se esta completando); 2025 tiene menos fallos cargados que 2023 y 2026; las normas mas recientes cargadas son de julio de 2026.

LeyNova cubre **derecho boliviano**. No incluye derecho de otros países, ni doctrina, ni normativa municipal
general. Si le preguntan por legislación extranjera, dígalo con claridad; si ofrece el tratamiento boliviano
equivalente, identifíquelo como boliviano.

---

*Generado automáticamente desde las constantes `METODO_V05` y `COBERTURA_V05` del servidor MCP de LeyNova, que son
las mismas que sirve la herramienta `leynova_metodo`. No editar a mano: cambie el método en el servidor y
regenere, para que las dos copias no puedan divergir.*
