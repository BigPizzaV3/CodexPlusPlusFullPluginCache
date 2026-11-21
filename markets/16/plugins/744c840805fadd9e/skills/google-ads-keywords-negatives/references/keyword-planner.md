# Keyword Planner

### El volumen de Planner ya viene agregado por variantes cercanas
- **Tipo**: gotcha de API
- **Por qué**: varias frases del mismo concepto devuelven el mismo `avg_monthly_searches`. Sumarlas cuenta el mismo mercado varias veces.
- **Cómo detectarlo**: frases distintas con números idénticos. En un caso, la suma bruta inflaba el mercado 1,7 veces.
- **Qué hacer**: canonicalizar (marcas, sinónimos del modificador, ruido navegacional, tokens ordenados) y tomar el máximo por grupo. Publicar un rango: suelo = máximo por concepto, techo = suma de frases canónicas.
- **Evidencia**: Visto en 2-3 cuentas, ago-sep 2026.

### Los lotes grandes de `GenerateKeywordHistoricalMetrics` colapsan la cabecera
- **Tipo**: gotcha de API
- **Por qué**: la API agrupa variantes dentro de cada request y elige un representante. Con lotes grandes puede elegir una errata de cola, y la cabecera vuelve como alias sin serie.
- **Cómo detectarlo**: una marca líder con menos volumen que su cola geográfica. Un término pedido solo dio más de 1.000 veces lo que daba dentro de un lote de 500.
- **Qué hacer**: barrido grande primero y repetir en lotes de ~25 los textos que volvieron como alias, ordenados por hash. Verificar cabeceras pidiéndolas de una en una. `RESOURCE_EXHAUSTED` es rate limit: reintentar con espera, no partir el lote.
- **Evidencia**: Visto en 2-3 cuentas, ago-sep 2026.

### Un escalón en la serie de Planner es una reasignación, no una caída
- **Tipo**: gotcha de plataforma
- **Por qué**: Planner reasigna variantes entre conceptos. El término salta 3x o más y queda plano después.
- **Cómo detectarlo**: `mediana(antes)/mediana(después) ≥ 3` y bloque posterior plano (`(max−min)/mediana ≤ 0,6`, 5+ meses). Los volúmenes van en buckets redondeados: un salto de un bucket es ruido.
- **Qué hacer**: publicar el YoY con y sin esos términos. En un caso, la caída de una campaña pasó de −22% a −14%.
- **Evidencia**: Visto en 1 cuenta, ago 2026.

### `url_seed` devuelve el pool genérico de al lado, no el producto de la página
- **Tipo**: gotcha de API
- **Por qué**: Planner usa la página como contexto amplio. Un título largo en `keyword_and_url_seed` se trata como una sola keyword y devuelve una idea.
- **Cómo detectarlo**: comparar contra el seed del nombre del producto. Inflación de hasta 30.000 veces en el peor caso.
- **Qué hacer**: seed = nombre corto del producto. Segunda pasada con el término que usa la gente si es distinto del nombre del producto. Un cero es "seed equivocado" hasta probar ese término.
- **Evidencia**: Visto en 1 cuenta, sep 2026.

### Un pool genérico de Planner se limpia de intenciones ajenas antes de sumarlo
- **Tipo**: error de método
- **Por qué**: Planner no separa intención. Se cuelan comparadores, otros verticales ("X de segunda mano"), y franquicias homónimas del producto.
- **Cómo detectarlo**: clasificar el universo y cortar cada intención ajena con su cifra. Regex de marca con `\b`.
- **Qué hacer**: no tratar como stopwords los modificadores que cambian la intención. En dos casos, el pool real era el 1% y el 40% del bruto.
- **Evidencia**: Visto en 2-3 cuentas, ago-sep 2026.

### Planner y las impresiones elegibles miden cosas distintas
- **Tipo**: error de método
- **Por qué**: Planner incluye subastas donde no entras y no ve la cola larga. Las elegibles (`impressions / search_impression_share`) solo miden donde compites.
- **Cómo detectarlo**: donde se competía, las elegibles fueron 3-10 veces el volumen de Planner. En 8 cuentas, la marca crecía +59% en elegibles mientras Planner la daba plana.
- **Qué hacer**: dimensionar con los dos y decir cuál es cada suelo. Las elegibles de marca no aíslan demanda: suben con inversión y producto.
- **Evidencia**: Visto en 4+ cuentas, ago-sep 2026.
