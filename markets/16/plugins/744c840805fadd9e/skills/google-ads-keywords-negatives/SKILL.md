---
name: google-ads-keywords-negatives
description: "Reglas de keywords, search terms, match types, AI Max, negativas, Keyword Planner y Quality Score en Google Ads. Usar al auditar o añadir negativas, leer search terms, decidir match types, dar de alta keywords, dimensionar demanda con Keyword Planner o interpretar Quality Score."
---

# Keywords, search terms y negativas

Reglas de Fiera para trabajar con cuentas de Google Ads. Cada regla sale de cuentas reales gestionadas a diario.

## Cómo aplicar las reglas

- Si existe `account-context.md` para la cuenta (lo crea la skill `google-ads-account-context`), léelo antes que nada: dice qué vende el negocio, su KPI, sus buckets y lo que no se toca.
- Lee solo el fichero de `references/` que toca a la tarea. El índice de abajo dice qué hay en cada uno.
- Cada regla tiene el mismo formato: **Tipo**, **Por qué** (el mecanismo), **Cómo detectarlo**, **Qué hacer** y **Evidencia**.
- **Evidencia** dice en cuántas cuentas se vio y cuándo. "Visto en 1 cuenta" es una observación: compruébala en la cuenta antes de actuar sobre ella.
- Los gotchas de API indican la versión en la que se comprobaron. Si usas otra, valida con `validate_only` o con `GoogleAdsFieldService` antes de dar la regla por buena.
- Una regla describe un mecanismo, no ordena un cambio. Antes de mutar una cuenta, enseña el plan y espera aprobación.

## Índice (29 reglas)

### `references/ai-max-for-search.md`: AI Max for Search
- El reparto exacto keyword frente a AI Max sale de `keyword_view` con `segments.match_type`
- AI Max puede multiplicar clics sin mover conversiones y contaminar la cuenta
- Dos gotchas de API al activar AI Max

### `references/expansion-y-altas-de-keywords.md`: Expansión y altas de keywords
- Las altas combinatorias en EXACT nacen sin impresiones

### `references/keyword-planner.md`: Keyword Planner
- El volumen de Planner ya viene agregado por variantes cercanas
- Los lotes grandes de `GenerateKeywordHistoricalMetrics` colapsan la cabecera
- Un escalón en la serie de Planner es una reasignación, no una caída
- `url_seed` devuelve el pool genérico de al lado, no el producto de la página
- Un pool genérico de Planner se limpia de intenciones ajenas antes de sumarlo
- Planner y las impresiones elegibles miden cosas distintas

### `references/match-types-y-close-variants.md`: Match types y close variants
- La paridad de match types se mide por `(texto, match_type)`
- Antes de crear la EXACT de una BROAD que convierte, comprobar que el texto se busca tal cual
- "Limitada por volumen de búsquedas" no es señal de match type

### `references/negativas-ambito-y-niveles.md`: Negativas: ámbito y niveles
- Una negativa solo bloquea en su ámbito; resolverlo antes de medir
- El nombre de una lista de negativas no describe su contenido
- Ninguna query puede quedarse sin campaña que la sirva
- Si una lista cancela una positiva en su ámbito, lo normal es que sobre la keyword
- En cuentas con sculpting masivo, la señal limpia es "cancela una positiva activa en el mismo ámbito"
- El script oficial de conflictos de negativas no ve la mayoría de bloqueos
- Negativas genéricas de una o dos palabras son el fallo más repetido
- Listas de topónimos en PHRASE o BROAD bloquean queries legítimas
- En cuentas maduras el recorrido de negativas suele estar agotado

### `references/negativas-semantica-de-match.md`: Negativas: semántica de match
- Las negativas no tienen close variants; las positivas sí
- La negativa no pliega acentos ni símbolos
- Una negativa PHRASE bloquea palabras completas, no subcadenas

### `references/quality-score-y-landing-page-experience.md`: Quality Score y Landing Page Experience
- Los campos de QS: foto de hoy frente a histórico segmentable
- Un QS medio que sube puede ser recambio de keywords

### `references/search-terms-cobertura-y-lectura.md`: Search terms: cobertura y lectura
- Microsoft Ads no oculta search terms por umbral
- Un match literal en español falla por flexión, orden y erratas
