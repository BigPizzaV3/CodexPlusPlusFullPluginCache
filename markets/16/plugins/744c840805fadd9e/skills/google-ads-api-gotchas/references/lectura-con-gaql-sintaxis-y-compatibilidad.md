# Lectura con GAQL: sintaxis y compatibilidad

### Un segmento usado como filtro tiene que ir también en el SELECT
- **Tipo**: gotcha de API
- **Por qué**: GAQL exige que un `segments.X` del `WHERE` esté seleccionado. Los segmentos de fecha (`segments.date`, `week`, `month`) son la excepción habitual. En vistas que no son `campaign`, filtrar por `campaign.experiment_type` o `campaign.advertising_channel_type` también pidió seleccionarlos.
- **Cómo detectarlo**: un linter previo que compare los `segments.*` del `WHERE` con los del `SELECT`. Un `INVALID_ARGUMENT` en una consulta que "parece correcta" suele ser esto.
- **Qué hacer**: añadir al `SELECT` todo segmento filtrado. Pasar el linter antes de enviar cualquier consulta nueva.
- **Evidencia**: Visto en 4+ cuentas, 2026, v20 a v24.

### `LAST_90_DAYS` no existe y `LAST_N_DAYS` excluye hoy
- **Tipo**: gotcha de API
- **Por qué**: los literales válidos son `TODAY`, `YESTERDAY`, `LAST_7_DAYS`, `LAST_14_DAYS`, `LAST_30_DAYS`, `LAST_WEEK_*`, `LAST_MONTH`, `THIS_MONTH`, `THIS_WEEK_*`. Ninguno `LAST_N_DAYS` incluye el día en curso.
- **Cómo detectarlo**: error de parseo con `LAST_90_DAYS`. Totales que no cuadran con la UI cuando se esperaba incluir hoy.
- **Qué hacer**: usar `segments.date BETWEEN 'AAAA-MM-DD' AND 'AAAA-MM-DD'` calculado en código para cualquier ventana distinta o que incluya hoy.
- **Evidencia**: Visto en 4+ cuentas, 2026, v24.

### `conversion_lag_bucket` solo existe a nivel ad group, keyword y anuncio
- **Tipo**: gotcha de API
- **Por qué**: `segments.conversion_lag_bucket` funciona en `ad_group`, `keyword_view` y `ad_group_ad`. Falla en `campaign` con device, `geographic_view`, `expanded_landing_page_view`, vistas demográficas y `search_term_view`. `segments.slot` y `segments.hour` no se pueden pedir juntos. `segments.device` entra en todas.
- **Cómo detectarlo**: error de incompatibilidad de segmentos al combinar lag con vistas de campaña o geo.
- **Qué hacer**: descomponer la CVR por lag desde `ad_group` o `keyword_view` y cruzar el resto de dimensiones aparte. El bucket `UNKNOWN` pesó cerca del 18% de las conversiones: reportarlo.
- **Evidencia**: Visto en 1 cuenta, oct 2026, v24.

### El impression share perdido por presupuesto no existe en `keyword_view` ni en `ad_group`
- **Tipo**: gotcha de API
- **Por qué**: `keyword_view` admite `search_impression_share`, `search_rank_lost_impression_share` y `search_top_impression_share`, pero no `search_budget_lost_impression_share` (`PROHIBITED_METRIC_IN_SELECT_OR_WHERE_CLAUSE`). El presupuesto es de campaña. Si se piden las tres a la vez, el error solo nombra la de presupuesto.
- **Cómo detectarlo**: probar métrica por métrica antes de concluir que ninguna está disponible.
- **Qué hacer**: derivar `budget_lost = max(0, 1 - SIS - rank_lost)` por keyword. El set completo solo vive en `campaign`.
- **Evidencia**: Visto en 1 cuenta, jul 2026, v24.

### `user_location_view` no da región ni provincia, y `geo_target_region` mezcla niveles
- **Tipo**: gotcha de API
- **Por qué**: la vista solo expone `country_criterion_id` y `targeting_location`. Para bajar de país hay que añadir `segments.geo_target_region`, que devuelve IDs de región, provincia y comarca mezclados.
- **Cómo detectarlo**: con un diccionario fijo de regiones, las regiones pequeñas salen a cero porque su volumen viene a nivel provincia.
- **Qué hacer**: resolver cada ID contra `geo_target_constant` (`name`, `canonical_name`, `target_type`) y agregar parseando `canonical_name`. En otros mercados, `geo_target_province`, `geo_target_state` o `geo_target_city` pueden ser el nivel útil, y `geo_target_state` sale vacío fuera de EE. UU.
- **Evidencia**: Visto en 2-3 cuentas, ago-oct 2026, v24.

### Filtrar `landing_page_view` por impresiones borra casi todo PMax y Demand Gen
- **Tipo**: gotcha de API
- **Por qué**: en `landing_page_view` y `expanded_landing_page_view`, las filas de PMax y Demand Gen traen clics con `metrics.impressions = 0`.
- **Cómo detectarlo**: comparar el coste total por landing con el coste de campaña. En una cuenta el filtro por impresiones escondía el 23% de la inversión.
- **Qué hacer**: usar `metrics.clicks > 0` para coste y clics por landing. `impressions > 0` solo vale en vistas de Search puro.
- **Evidencia**: Visto en 2-3 cuentas, ago 2026, v24.

### Las métricas por asset no salen de `asset`, y `video` solo cubre Video y Demand Gen
- **Tipo**: gotcha de API
- **Por qué**: `FROM asset` con `metrics.*` falla: el recurso es de inventario (`asset.source`, `youtube_video_asset.*`). `FROM video` sí lleva métricas, pero solo de campañas Video y Demand Gen.
- **Cómo detectarlo**: en una cuenta con PMax, `FROM video` devuelve un puñado de filas y parece que no hay tráfico de YouTube.
- **Qué hacer**: rendimiento por asset de PMax desde `asset_group_asset`, siempre con `segments.ad_network_type`. Usar `video` solo como catálogo de duraciones (`video.duration_millis`).
- **Evidencia**: Visto en 2-3 cuentas, ago-sep 2026, v24.

### `asset_group_asset.performance_label` no existe en v24
- **Tipo**: gotcha de API
- **Por qué**: la consulta falla con `UNRECOGNIZED_FIELD`. El único `performance_label` del esquema es `ad_group_ad_asset_view.performance_label`, de Search.
- **Cómo detectarlo**: cualquier script heredado de versiones anteriores que lo pida.
- **Qué hacer**: juzgar assets de PMax con métricas de `asset_group_asset` segmentadas por red, `asset_group.asset_coverage.ad_strength_action_items` (campo `action_item_type`) y `asset_group_asset.primary_status_reasons`.
- **Evidencia**: Visto en 2-3 cuentas, sep 2026, v24.

### La etiqueta LOW/GOOD/BEST de los assets de RSA vuelve siempre `NOT_APPLICABLE`
- **Tipo**: gotcha de API
- **Por qué**: en `ad_group_ad_asset_view`, el 100% de los headlines y descriptions medidos volvió `NOT_APPLICABLE` en 90 días. Un filtro por `LOW` devuelve lista vacía y la cuenta parece sana.
- **Cómo detectarlo**: contar la distribución de `performance_label` antes de usarla como filtro.
- **Qué hacer**: sustituir la etiqueta por un índice de serving (impresiones del asset entre la media de sus pares en el mismo anuncio y `field_type`) y un test z de CTR contra el resto del anuncio. Excluir los assets pineados.
- **Evidencia**: Visto en 4+ cuentas, ago 2026, v24.

### Un nombre de enum inexistente en Python devuelve cero filas sin error
- **Tipo**: gotcha de API
- **Por qué**: la extensión de imagen de Search es `AD_IMAGE`, no `IMAGE`. En GAQL, `IMAGE` da `BAD_ENUM_CONSTANT`. Filtrado en Python, devuelve cero filas y el audit concluye que la cuenta no tiene imágenes.
- **Cómo detectarlo**: validar cada nombre de enum contra `client.enums.<Enum>` antes de usarlo como filtro en código.
- **Qué hacer**: filtrar en GAQL, donde un nombre erróneo falla en voz alta, o comprobar el enum en el script.
- **Evidencia**: Visto en 1 cuenta, sep 2026, v24.

### El enum de red cambia entre versiones
- **Tipo**: gotcha de API
- **Por qué**: en v24 `AdNetworkType` tiene `YOUTUBE`, y ya no existen `YOUTUBE_WATCH` ni `YOUTUBE_SEARCH`. Otros valores: `SEARCH`, `SEARCH_PARTNERS`, `CONTENT`, `GMAIL`, `DISCOVER`, `GOOGLE_TV`, `GOOGLE_OWNED_CHANNELS`, `MAPS`, `MIXED`.
- **Cómo detectarlo**: mapeos de red que dejan YouTube en un cubo "otros" tras subir la librería.
- **Qué hacer**: leer los valores del enum de la versión instalada en vez de mantener una lista fija.
- **Evidencia**: Visto en 2-3 cuentas, sep 2026, v24.

### Antes de decir que un dato "no sale por API", listar los campos con `GoogleAdsFieldService`
- **Tipo**: error de método
- **Por qué**: muchas capacidades que parecen ausentes existen en otro recurso. Ejemplo: el reparto keyword frente a AI Max sale de `keyword_view` con `segments.match_type` (valor `AI_MAX`), y cuadra al céntimo con la UI.
- **Cómo detectarlo**: una afirmación de imposibilidad hecha tras probar un solo campo.
- **Qué hacer**: consultar `GoogleAdsFieldService` (`selectable_with`) o lanzar un `validate_only` y leer el error real antes de afirmar que algo es inmutable o no soportado.
- **Evidencia**: Visto en 4+ cuentas, jun-nov 2026, v23-v24.

### `keyword_view` devuelve también las keywords negativas
- **Tipo**: gotcha de API
- **Por qué**: la vista no expone `ad_group_criterion.negative` y mezcla positivas y negativas con `status = ENABLED`. En una cuenta, 3 de cada 4 filas eran negativas.
- **Cómo detectarlo**: recuentos de keywords absurdos, o marcas ajenas con volumen enorme en Planner y cero impresiones.
- **Qué hacer**: contar inventario desde `ad_group_criterion` con `type = 'KEYWORD'` y `negative = FALSE`. Usar `keyword_view` solo para métricas.
- **Evidencia**: Visto en 1 cuenta, ago 2026, v24.

### El `criterion_id` de una keyword sale del texto y el match type
- **Tipo**: gotcha de API
- **Por qué**: la misma keyword tiene el mismo `criterion_id` en todos los ad groups de la cuenta. La identidad real es `(ad_group_id, criterion_id)`, visible en el resource name `adGroupCriteria/{ad_group_id}~{criterion_id}`.
- **Cómo detectarlo**: un filtro "excluir la propia keyword" por `criterion_id` borra todas sus copias, y el resultado dice que no queda ninguna viva.
- **Qué hacer**: indexar criterios por la tupla. Antes de "mover" una keyword, buscarla en el destino: a menudo ya existe pausada y el movimiento son dos cambios de estado.
- **Evidencia**: Visto en 2-3 cuentas, ago 2026, v24.

### El `ad.id` se repite entre ad groups y campañas cuando el texto es idéntico
- **Tipo**: gotcha de API
- **Por qué**: el recurso `ad` es de cuenta. Pegar el mismo RSA en varios ad groups reutiliza el `ad.id` y solo cambia el `ad_group_ad`. Una mutación de `AdService` sobre ese id edita todas las copias.
- **Cómo detectarlo**: `ad_group_ad` filtrado por `ad.id IN (...)` devuelve más filas que ids.
- **Qué hacer**: indexar por `(ad_group_id, ad_id)` y los assets por `(ad_group_id, ad_id, asset_id, field_type)`. Contar ediciones por ad id único.
- **Evidencia**: Visto en 2-3 cuentas, ago-sep 2026, v24.

### El nombre de un ad group no es único en la cuenta
- **Tipo**: gotcha de API
- **Por qué**: Google solo exige nombre único dentro de la campaña. Un diccionario por nombre se queda con el último y apunta al ad group equivocado sin error. Las campañas se renombran, así que tampoco sirven de clave.
- **Cómo detectarlo**: un dry-run que resuelve un nombre a un ad group con un gasto muy distinto del esperado.
- **Qué hacer**: mutar e indexar historial siempre por ID. Verificar contra el estado vivo que nombre y campaña del ID son los esperados.
- **Evidencia**: Visto en 4+ cuentas, jul-sep 2026, v24.

### Los search terms de PMax están en `campaign_search_term_view`
- **Tipo**: gotcha de API
- **Por qué**: `search_term_view` solo devuelve Search y DSA. `campaign_search_term_view` da términos de PMax con coste, sin keyword ni match type. `campaign_search_term_insight` es otra cosa: categorías.
- **Cómo detectarlo**: un guard de conversiones que solo lea `search_term_view` ve con 0 conversiones términos que convierten en PMax.
- **Qué hacer**: cruzar las dos vistas antes de negativizar. Comparar contra el coste de PMax filtrado a red `SEARCH`. No poner `LIMIT`: en un caso escondía el 97% de los términos.
- **Evidencia**: Visto en 2-3 cuentas, ago-sep 2026, v24.

### PMax devuelve impression share, pero sus impresiones son de todas las redes
- **Tipo**: gotcha de API
- **Por qué**: PMax trae las tres métricas de IS, que cubren solo Search. `metrics.impressions` suma Display, Discover y YouTube. Demand Gen no devuelve IS.
- **Cómo detectarlo**: elegibles derivadas (`impresiones / SIS`) de PMax muy por encima de lo plausible.
- **Qué hacer**: derivar elegibles y agregar IS solo con `advertising_channel_type = SEARCH`. Decir qué parte del gasto queda fuera de la medición.
- **Evidencia**: Visto en 2-3 cuentas, ago-sep 2026, v24.

### El impression share se censura a 0,0999 y el top IS hereda la censura
- **Tipo**: gotcha de API
- **Por qué**: Google reporta por debajo del 10% el valor centinela `0.0999`, que se imprime como "10,0%". `search_top_impression_share` y `search_absolute_top_impression_share` se censuran al mismo valor, así que `top_is / sis` da 1 en esas filas.
- **Cómo detectarlo**: contar filas con `sis <= 0.1001` y su peso en impresiones. En una cuenta el 91% de las elegibles traía el absolute top censurado.
- **Qué hacer**: calcular elegibles fila a fila y sumar. Para posición usar `metrics.top_impression_percentage` y `absolute_top_impression_percentage`, que no se censuran. Dar rangos cuando haya censura.
- **Evidencia**: Visto en 2-3 cuentas, jul-oct 2026, v24.

### Con portfolio, el target de la campaña sale 0
- **Tipo**: gotcha de API
- **Por qué**: `campaign.target_roas.target_roas`, `campaign.maximize_conversion_value.target_roas` y sus equivalentes de CPA devuelven 0 si la campaña usa portfolio. El target vive en la estrategia.
- **Cómo detectarlo**: pedir siempre `campaign.bidding_strategy` junto al target. Si viene poblado y el target es 0, el 0 no es "sin objetivo".
- **Qué hacer**: leer el target desde la estrategia, con la subclave que mande su `type`: en `MAXIMIZE_CONVERSION_VALUE` es `maximize_conversion_value.target_roas`, y `target_roas.target_roas` sale 0 siempre.
- **Evidencia**: Visto en 4+ cuentas, ago-sep 2026, v24.

### `FROM bidding_strategy` no ve los portfolios del manager
- **Tipo**: gotcha de API
- **Por qué**: `bidding_strategy` solo devuelve las estrategias propias de la cuenta. Si el portfolio es de una cuenta gestora, devuelve cero filas sin error. El resource name de la campaña no dice quién es el dueño.
- **Cómo detectarlo**: comparar el recuento de `bidding_strategy` con `accessible_bidding_strategy` en la misma cuenta. Si `accessible_bidding_strategy` devuelve más, hay portfolios de la gestora.
- **Qué hacer**: leer con `accessible_bidding_strategy` (trae `owner_customer_id`) contra la cuenta de la campaña. Mutar con `BiddingStrategyService` contra la cuenta dueña. Un portfolio que no resuelve es un hallazgo, no un "sin objetivo".
- **Evidencia**: Visto en 2-3 cuentas, sep 2026, v24.

### `bidding_strategy.campaign_count` cuenta también las campañas pausadas
- **Tipo**: gotcha de API
- **Por qué**: el contador incluye campañas no activas.
- **Cómo detectarlo**: cruzar el portfolio con las campañas `ENABLED` y con gasto que lo usan.
- **Qué hacer**: medir y revisar un cambio de target sobre todas las campañas que sirven con ese portfolio, no sobre una.
- **Evidencia**: Visto en 1 cuenta, sep 2026, v24.

### Una lista de audiencia que no resuelve desde la cuenta cliente puede estar viva
- **Tipo**: gotcha de API
- **Por qué**: `user_list` consultado desde la cuenta cliente no devuelve las listas auto-creadas por la gestora ni las de Play Store. Un criterio que apunta a ellas parece huérfano.
- **Cómo detectarlo**: sacar el `display_name` desde `campaign_audience_view`, que sí lo trae, y mirar si tuvo impresiones.
- **Qué hacer**: retirar solo lo que no tiene nombre ni filas. Las listas muertas de verdad se ven por `size_for_search = 0` o `membership_status = CLOSED`.
- **Evidencia**: Visto en 1 cuenta, sep 2026, v24.

### `campaign_budget.amount_micros` con `segments.date` devuelve el valor actual
- **Tipo**: gotcha de API
- **Por qué**: la API no da el histórico del budget por día. Segmentar por fecha repite el importe de hoy.
- **Cómo detectarlo**: un budget idéntico en todos los días de una serie donde hubo cambios.
- **Qué hacer**: guardar una foto diaria del budget, o reconstruir cambios desde `change_event` dentro de su ventana.
- **Evidencia**: Visto en 1 cuenta, oct 2026, v24.

### `ENABLED` no significa que la campaña pueda servir
- **Tipo**: gotcha de API
- **Por qué**: campañas con fecha de fin pasada o brazos de experimento terminados quedan `status = ENABLED` con `primary_status = ENDED`. En una cuenta, esos brazos sumaban el 64% de las keywords "activas".
- **Cómo detectarlo**: `SELECT campaign.experiment_type, campaign.primary_status, campaign.primary_status_reasons FROM campaign`.
- **Qué hacer**: filtrar inventario y análisis por `primary_status`, no por `status`. Excluir `experiment_type != 'BASE'` salvo que se analice el experimento.
- **Evidencia**: Visto en 2-3 cuentas, ago-sep 2026, v24.

### Los ajustes de red de Search tienen nombres que confunden
- **Tipo**: gotcha de API
- **Por qué**: la casilla de partners de búsqueda de la UI es `network_settings.target_search_network`. `target_partner_search_network` es la Google Partner Network y vale `False` en cuentas normales. Además, el flag dice qué está permitido, no dónde se sirvió.
- **Cómo detectarlo**: cruzar el flag con coste por `segments.ad_network_type = 'SEARCH_PARTNERS'` en L30D. Una campaña con el flag a `False` gastaba el 38% en partners.
- **Qué hacer**: leer `target_search_network` y verificar siempre por `segments.ad_network_type`. En PMax, gasto en partners no es hallazgo: no se puede apagar.
- **Evidencia**: Visto en 4+ cuentas, sep 2026, v24.

### `campaign_conversion_goal` todo a `biddable = False` no significa "hereda la cuenta"
- **Tipo**: gotcha de API
- **Por qué**: `campaign_conversion_goal` solo lista goals estándar. Si todos salen a `False`, lo normal es que haya un custom goal a nivel campaña. El recurso que manda es `conversion_goal_campaign_config`.
- **Cómo detectarlo**: `SELECT conversion_goal_campaign_config.goal_config_level, conversion_goal_campaign_config.custom_conversion_goal FROM conversion_goal_campaign_config`. Segmentar conversiones por `segments.conversion_action_name` confirma qué acción cuenta.
- **Qué hacer**: interpretar `goal_config_level = CAMPAIGN` con custom goal como decisión deliberada. Un set biddable acotado y distinto del de cuenta es diseño, no error.
- **Evidencia**: Visto en 2-3 cuentas, ago-nov 2026, v24.

### El tope de gasto mensual es 30,4 veces el budget diario
- **Tipo**: gotcha de API
- **Por qué**: una campaña que gasta por encima de su diario llega al tope mensual antes de fin de mes y se frena hasta el día 1. Sale como budget lost IS sin ningún cambio en la cuenta.
- **Cómo detectarlo**: gasto que cae a final de mes con budget lost y sin `change_event`. Comparar el gasto del mes con 30,4 x budget.
- **Qué hacer**: proyectar el día de tope como `30,4 x budget / gasto medio diario`. No diagnosticar mercado ni subasta antes de esta comprobación.
- **Evidencia**: Visto en 1 cuenta, oct 2026, v24.

### Lo que la API no expone
- **Tipo**: gotcha de API
- **Por qué**: varias piezas solo existen en la UI. Auction Insights. Estado de auto-apply de recomendaciones. Placements de campañas App. Opt-out de assets automáticos a nivel cuenta. Toggle de expansión de URL en PMax desde v24. Motivo de rechazo de imágenes. Privacidad de vídeos de YouTube. `campaign.brand_guidelines` no es seleccionable.
- **Cómo detectarlo**: listar el campo en `GoogleAdsFieldService` antes de construir un proceso sobre él.
- **Qué hacer**: usar el rastro que sí sale (por ejemplo, `change_event` para auto-apply, `campaign_asset` para brand guidelines) o un export de la UI. `performance_max_placement_view` solo trae impresiones.
- **Evidencia**: Visto en 4+ cuentas, may-oct 2026, v24.
