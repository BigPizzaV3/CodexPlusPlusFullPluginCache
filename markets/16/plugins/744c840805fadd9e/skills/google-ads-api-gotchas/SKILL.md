---
name: google-ads-api-gotchas
description: "Gotchas de la Google Ads API, GAQL y el cliente Python, y reglas para mutar sin romper la cuenta. Usar al escribir o revisar consultas GAQL, scripts con la librería google-ads, mutaciones (create, update, remove), lecturas de change_event, cuotas y niveles de acceso de la API, creación de campañas, PMax o Demand Gen por API, y exports de Auction Insights."
---

# API de Google Ads, GAQL y mutaciones

Reglas de Fiera para trabajar con cuentas de Google Ads. Cada regla sale de cuentas reales gestionadas a diario.

## Cómo aplicar las reglas

- Si existe `account-context.md` para la cuenta (lo crea la skill `google-ads-account-context`), léelo antes que nada: dice qué vende el negocio, su KPI, sus buckets y lo que no se toca.
- Lee solo el fichero de `references/` que toca a la tarea. El índice de abajo dice qué hay en cada uno.
- Cada regla tiene el mismo formato: **Tipo**, **Por qué** (el mecanismo), **Cómo detectarlo**, **Qué hacer** y **Evidencia**.
- **Evidencia** dice en cuántas cuentas se vio y cuándo. "Visto en 1 cuenta" es una observación: compruébala en la cuenta antes de actuar sobre ella.
- Los gotchas de API indican la versión en la que se comprobaron. Si usas otra, valida con `validate_only` o con `GoogleAdsFieldService` antes de dar la regla por buena.
- Una regla describe un mecanismo, no ordena un cambio. Antes de mutar una cuenta, enseña el plan y espera aprobación.

## Índice (103 reglas)

### `references/auction-insights.md`: Auction Insights
- Auction Insights no está en la API: se exporta desde Report Editor
- El Report Editor del manager pierde métricas de Auction Insights
- Exportar Auction Insights con la UI en inglés
- El cruce del export con la API es por nombre de campaña

### `references/cliente-python.md`: Cliente Python
- `validate_only` y `partial_failure` van en el objeto request, no como kwargs
- `FieldMask` no es un tipo del cliente de Google Ads
- `field_mask(None, obj)` omite los valores por defecto y el update no hace nada
- La ruta de la máscara tiene que ser el subcampo hoja
- En Python 3.11+, `str()` de un enum devuelve el número
- Rarezas de proto-plus que rompen scripts a mitad de lote

### `references/creacion-y-duplicacion-de-campanas.md`: Creación y duplicación de campañas
- `contains_eu_political_advertising` es obligatorio al crear campaña
- `ad_serving_optimization_status` ya no se puede fijar en el create
- Un budget compartido no admite Maximize Conversions a nivel de campaña
- Una campaña creada por API nace sin tracking y pujando a todas las conversiones de cuenta
- El config de objetivos de campaña es update, no create, y el custom goal deja restos
- Duplicar por API no copia UTMs, assets ni exclusiones, pero sí los ajustes de red
- Fechas de campaña: centinela de fin, hora de inicio y arranque que no se mueve
- Los resource names temporales no resuelven en todos los recursos

### `references/cuotas-acceso-y-versiones.md`: Cuotas, acceso y versiones
- El acceso Basic topa en 15.000 operaciones por 24 horas por proyecto de Google Cloud, lecturas incluidas
- El nivel de acceso va con el proyecto de Google Cloud de las credenciales OAuth
- Las listas y portfolios del manager se mutan contra la cuenta dueña
- Tras borrar en una lista del manager, la cuenta hija sigue viendo el criterio unos minutos
- La librería usa la versión de API más alta que trae
- Una caché de lecturas tiene que caducar antes de un día
- Con consent screen Internal, el código OAuth caduca en minutos

### `references/demand-gen.md`: Demand Gen
- `upgraded_targeting = True` bloquea el geo y no se puede cambiar
- Los ad groups de Demand Gen funcionan con una sola audiencia compuesta
- Con audiencia compuesta, la demografía va dentro de la audiencia
- Límites de creatividad de Demand Gen que la API aplica

### `references/experimentos.md`: Experimentos
- Los brazos de un experimento de broad de un clic no salen en la API
- Un brazo de experimento no se puede pausar

### `references/historial-de-cambios-change-event-y-change-status.md`: Historial de cambios: `change_event` y `change_status`
- `change_event` solo cubre 30 días y `change_status` no trae diffs
- `change_event` corta en 10.000 filas por consulta
- Un límite de fecha `<= 'AAAA-MM-DD'` corta a las 00:00
- Un UPDATE en `change_event` solo trae los campos cambiados
- El tipo de un enlace de asset solo está en el sufijo del resource name
- `change_event` no registra targets de portfolio ni enlaces de listas compartidas
- Los cambios automáticos de Google se identifican por `user_email`
- Una edición en bloque escribe un evento por entidad
- Las subidas en bloque de la UI dejan `match_type` en `UNSPECIFIED`

### `references/lectura-con-gaql-sintaxis-y-compatibilidad.md`: Lectura con GAQL: sintaxis y compatibilidad
- Un segmento usado como filtro tiene que ir también en el SELECT
- `LAST_90_DAYS` no existe y `LAST_N_DAYS` excluye hoy
- `conversion_lag_bucket` solo existe a nivel ad group, keyword y anuncio
- El impression share perdido por presupuesto no existe en `keyword_view` ni en `ad_group`
- `user_location_view` no da región ni provincia, y `geo_target_region` mezcla niveles
- Filtrar `landing_page_view` por impresiones borra casi todo PMax y Demand Gen
- Las métricas por asset no salen de `asset`, y `video` solo cubre Video y Demand Gen
- `asset_group_asset.performance_label` no existe en v24
- La etiqueta LOW/GOOD/BEST de los assets de RSA vuelve siempre `NOT_APPLICABLE`
- Un nombre de enum inexistente en Python devuelve cero filas sin error
- El enum de red cambia entre versiones
- Antes de decir que un dato "no sale por API", listar los campos con `GoogleAdsFieldService`
- `keyword_view` devuelve también las keywords negativas
- El `criterion_id` de una keyword sale del texto y el match type
- El `ad.id` se repite entre ad groups y campañas cuando el texto es idéntico
- El nombre de un ad group no es único en la cuenta
- Los search terms de PMax están en `campaign_search_term_view`
- PMax devuelve impression share, pero sus impresiones son de todas las redes
- El impression share se censura a 0,0999 y el top IS hereda la censura
- Con portfolio, el target de la campaña sale 0
- `FROM bidding_strategy` no ve los portfolios del manager
- `bidding_strategy.campaign_count` cuenta también las campañas pausadas
- Una lista de audiencia que no resuelve desde la cuenta cliente puede estar viva
- `campaign_budget.amount_micros` con `segments.date` devuelve el valor actual
- `ENABLED` no significa que la campaña pueda servir
- Los ajustes de red de Search tienen nombres que confunden
- `campaign_conversion_goal` todo a `biddable = False` no significa "hereda la cuenta"
- El tope de gasto mensual es 30,4 veces el budget diario
- Lo que la API no expone

### `references/performance-max.md`: Performance Max
- Crear una PMax por API falla en sitios poco obvios
- Las redes de una PMax no se pueden apagar
- La expansión de URL de PMax se corta con exclusiones `WEBPAGE`, no con un flag
- `TEXT_ASSET_AUTOMATION` no se apaga si la expansión de URL sigue activa
- Los topes de assets de un asset group cuentan solo los del anunciante
- El tope de 5 vídeos por asset group es de la UI
- Cambiar todo el copy de un asset group exige un orden de fases
- Quitar un vídeo de PMax arrastra sus derivados automáticos
- Con Brand Guidelines, logo y nombre de negocio viven en la campaña
- `EnablePMaxBrandGuidelines` no tiene dry-run, no se revierte y añade el favicon como logo
- `UNSET` en la automatización de assets no significa opted-in
- Las exclusiones de placements de PMax solo van a nivel cuenta o lista del manager

### `references/seguridad-de-mutaciones.md`: Seguridad de mutaciones
- Dry-run por defecto y apply solo tras revisar el diff
- El dry-run tiene que validar contra el servidor
- `validate_only` con `partial_failure` devuelve todos los errores a la vez
- Una violación de política tumba el lote entero y la API solo enseña la primera
- Mutar por ID y verificar contra el estado vivo antes de construir la operación
- Un OK de la API no prueba que el cambio se aplicó
- La lectura tarda en reflejar una mutación
- Backup completo antes y después de cada apply
- Los scripts de alta tienen que ser reanudables e idempotentes
- Un budget propio no conserva su nombre ni admite renombrarse
- Pausar, no eliminar
- Topes por cambio, planes que caducan y revert inmediato
- Un portfolio se cambia pensando en todas sus campañas
- Las campañas de Video no admiten mutaciones por API
- Los criterios de una campaña eliminada no se pueden borrar
- Positiva y negativa con el mismo texto y match chocan en el ad group
- Crear una keyword que ya existe es un no-op que devuelve éxito
- Una audiencia positiva sin `TargetRestriction` restringe la campaña
- `membership_life_span` de una lista rule-based no siempre se guarda
- Los assets `AUTOMATICALLY_CREATED` no se editan ni se enlazan a mano
- `PromotionAsset`: el porcentaje va en escala de millón y la URL es obligatoria
- El header de un structured snippet no es texto libre
