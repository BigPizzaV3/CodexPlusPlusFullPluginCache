---
name: google-ads-copy-assets-pmax
description: "Reglas de copy de RSA, extensiones y assets, Performance Max, Demand Gen, campañas App, estructura, geo y landing pages en Google Ads. Usar al escribir o editar anuncios, revisar extensiones, leer o modificar PMax y Demand Gen, crear o duplicar campañas, o configurar geo."
---

# Copy, assets, PMax y estructura

Reglas de Fiera para trabajar con cuentas de Google Ads. Cada regla sale de cuentas reales gestionadas a diario.

## Cómo aplicar las reglas

- Si existe `account-context.md` para la cuenta (lo crea la skill `google-ads-account-context`), léelo antes que nada: dice qué vende el negocio, su KPI, sus buckets y lo que no se toca.
- Lee solo el fichero de `references/` que toca a la tarea. El índice de abajo dice qué hay en cada uno.
- Cada regla tiene el mismo formato: **Tipo**, **Por qué** (el mecanismo), **Cómo detectarlo**, **Qué hacer** y **Evidencia**.
- **Evidencia** dice en cuántas cuentas se vio y cuándo. "Visto en 1 cuenta" es una observación: compruébala en la cuenta antes de actuar sobre ella.
- Los gotchas de API indican la versión en la que se comprobaron. Si usas otra, valida con `validate_only` o con `GoogleAdsFieldService` antes de dar la regla por buena.
- Una regla describe un mecanismo, no ordena un cambio. Antes de mutar una cuenta, enseña el plan y espera aprobación.

## Índice (53 reglas)

### `references/app-campaigns.md`: App campaigns
- El bucket SEARCH de una campaña App incluye Google Play
- Las campañas App no tienen informe de placements ni de search terms
- La canibalización App contra Search se prueba, no se asume

### `references/copy-y-rsas-escribir.md`: Copy y RSAs: escribir
- Valida la longitud de cada asset con código, no a mano
- No pinees assets en los RSA
- Mutar los textos de un RSA reemplaza la lista entera y borra los pins
- Edita headlines y descriptions en el mismo anuncio, no con remove y create
- Un ad group admite 3 RSA ENABLED; el cuarto falla
- La `final_url` de un RSA nuevo es la que ya usan los anuncios vivos del ad group
- Escribe el headline con la palabra que se busca, no con la del producto
- Elige el término por demanda de búsqueda, no por corrección gramatical
- Un anuncio no afirma lo que el producto no hace, y "gratis" siempre lleva objeto
- Una fecha de promo dentro de un RSA no caduca sola
- Sin nombres de competidor en el copy
- DKI capitaliza mal los acrónimos
- No prometas en el anuncio lo que la landing no hace

### `references/copy-y-rsas-medir.md`: Copy y RSAs: medir
- Las métricas por asset de un RSA se multiplican; usa ratios dentro del anuncio
- Un asset con poco serving no es un asset a reescribir
- Un cambio de copy no se lee antes de 2-4 semanas, y Google puede no servirlo
- Las conversiones por asset son participación, no lift aislado

### `references/demand-gen.md`: Demand Gen
- Los custom segments de keywords solo actúan como intención en propiedades propias
- Los lookalikes de DG son señal, no restricción, desde marzo de 2026
- Al crear una DG, la categoría de conversión de App sale biddable
- Las exclusiones de contenido e inventario de DG no se fijan por API
- Antes de proponer DG de prospecting, mira el histórico de la cuenta

### `references/duplicar-y-crear-campanas.md`: Duplicar y crear campañas
- Al crear una campaña, copia los 21 settings de una referencia viva y verifica
- Las brand lists no se admiten en una campaña Search solo exact
- Clonar ad groups pierde los criterios demográficos si no se piden en el SELECT

### `references/estructura-y-naming.md`: Estructura y naming
- No inventes nombres: replica el patrón de la cuenta
- Renombrar una campaña no actualiza su custom parameter de tracking

### `references/extensiones-y-assets.md`: Extensiones y assets
- Los niveles de extensión se suman; el más específico no apaga al general
- Un enlace de extensión PAUSED no es cobertura
- Mira en qué nivel sirven las extensiones antes de leer hallazgos de encaje
- Los assets de extensión del anunciante se editan in place, y el cambio es global
- Lee el contenido de sitelinks, callouts y snippets con `MessageToDict`
- Dos sitelinks al mismo destino en el mismo set: uno pierde siempre
- El idioma de la landing no se puede inferir si el sitio no lleva locale en la ruta
- Al duplicar ad groups, las extensiones temáticas viajan con el texto viejo

### `references/geo.md`: Geo
- Excluir una ubicación que ya es positiva da `IMMUTABLE_FIELD`
- `geo_target_type_setting` se fija para positivos y negativos por separado
- La región de la analítica tiene que casar con la ubicación de Google Ads

### `references/landing-pages.md`: Landing pages
- Una redirección que pierde la querystring borra el `gclid`

### `references/performance-max-assets-y-asset-groups.md`: Performance Max: assets y asset groups
- Imágenes: 20 por asset group sumando todos los ratios
- Un texto idéntico es el mismo asset en toda la cuenta
- Los vídeos auto-creados no cuentan para Ad Strength

### `references/performance-max-expansion-de-url-y-feeds.md`: Performance Max: expansión de URL y feeds
- Cuando una PMax se va de intención, mira el destino antes que las queries
- Page feed y filtro de asset group: reglas de formato
- Un feed con URLs que redirigen con 200 falla en silencio

### `references/performance-max-trafico-y-lectura.md`: Performance Max: tráfico y lectura
- Una PMax "multicanal" suele ser una campaña de Search
- PMax y Search sobre la misma query no son dos subastas
- Tras excluir la marca propia de PMax, la caída de conversiones es reatribución
- El idioma se targetea a nivel campaña, no de asset group
- Una PMax de acciones locales no se juzga por `metrics.conversions`
