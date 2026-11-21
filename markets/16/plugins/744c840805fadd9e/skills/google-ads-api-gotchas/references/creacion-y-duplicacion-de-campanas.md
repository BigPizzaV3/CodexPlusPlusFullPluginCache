# Creación y duplicación de campañas

### `contains_eu_political_advertising` es obligatorio al crear campaña
- **Tipo**: gotcha de API
- **Por qué**: desde el reglamento europeo de publicidad política el campo es requerido, también en cuentas fuera de la UE. Sin él, `field_error: REQUIRED`.
- **Cómo detectarlo**: el error en el create.
- **Qué hacer**: `campaign.contains_eu_political_advertising = client.enums.EuPoliticalAdvertisingStatusEnum.DOES_NOT_CONTAIN_EU_POLITICAL_ADVERTISING`.
- **Evidencia**: Visto en 2-3 cuentas, ago-sep 2026, v24.

### `ad_serving_optimization_status` ya no se puede fijar en el create
- **Tipo**: gotcha de API
- **Por qué**: devuelve `CANNOT_SET_AD_ROTATION_MODE` ("ad rotation mode at campaign is deprecated").
- **Cómo detectarlo**: el error en el create.
- **Qué hacer**: quitar el campo. Sale `OPTIMIZE` solo.
- **Evidencia**: Visto en 2-3 cuentas, ago-sep 2026, v24.

### Un budget compartido no admite Maximize Conversions a nivel de campaña
- **Tipo**: gotcha de API
- **Por qué**: devuelve `Bidding strategy type is incompatible with shared budget`.
- **Cómo detectarlo**: el error sobre `campaign_budget` en el create.
- **Qué hacer**: budget propio por campaña, repartiendo el total, o estrategia de portfolio.
- **Evidencia**: Visto en 1 cuenta, sep 2026, v24.

### Una campaña creada por API nace sin tracking y pujando a todas las conversiones de cuenta
- **Tipo**: gotcha de API
- **Por qué**: `tracking_url_template` y `url_custom_parameters` nacen vacíos. `conversion_goal_campaign_config.goal_config_level` nace en `CUSTOMER`, con todas las categorías biddables. Con tROAS, el target deja de significar lo mismo que en el resto.
- **Cómo detectarlo**: comparar la campaña nueva con una de referencia: tracking, parámetros, nivel de objetivo y categorías biddables.
- **Qué hacer**: tres mutates: nivel `CAMPAIGN`, releer y fijar `biddable` por categoría con ruta manual en la máscara, y tracking. La UI rellena esto sola y la API no.
- **Evidencia**: Visto en 2-3 cuentas, sep-nov 2026, v24.

### El config de objetivos de campaña es update, no create, y el custom goal deja restos
- **Tipo**: gotcha de API
- **Por qué**: el config nace con la campaña. Su resource name es `customers/{cid}/conversionGoalCampaignConfigs/{campaign_id}`. Tras fijar un custom goal por API, las categorías de cuenta pueden seguir biddables y no se limpian ni mutando `biddable` ni reaplicando el config.
- **Cómo detectarlo**: la UI enseña el set real de la campaña en una línea. Un custom goal vacío con nivel `CAMPAIGN` falla con "override goals but has no goals configured".
- **Qué hacer**: usar `ConversionGoalCampaignConfigService` con operación update. Tras cada alta, revisar el set en la UI y quitar las categorías sobrantes a mano.
- **Evidencia**: Visto en 2-3 cuentas, ago-nov 2026, v24.

### Duplicar por API no copia UTMs, assets ni exclusiones, pero sí los ajustes de red
- **Tipo**: gotcha de API
- **Por qué**: la copia no lleva `final_url_suffix`, `tracking_url_template`, assets de campaña y ad group, exclusiones de audiencia, brand lists ni labels. Sí arrastra `network_settings`.
- **Cómo detectarlo**: diff de configuración origen contra réplica antes de activar.
- **Qué hacer**: replicar los seis elementos con dry-run y `partial_failure`. Las brand lists no se admiten en una campaña Search solo exacta.
- **Evidencia**: Visto en 2-3 cuentas, ago-sep 2026, v24.

### Fechas de campaña: centinela de fin, hora de inicio y arranque que no se mueve
- **Tipo**: gotcha de API
- **Por qué**: en v24 los campos son `start_date_time` y `end_date_time`. Sin fecha de fin es `2037-12-30 23:59:59`; con otra hora falla. Un inicio de hoy a las 00:00 se graba con la hora de la mutación. Un inicio ya pasado da `CANNOT_MODIFY_START_DATE_IF_ALREADY_STARTED`, aunque nunca haya servido.
- **Cómo detectarlo**: `validate_only` caza los dos primeros casos.
- **Qué hacer**: controlar el arranque de un vuelo activando la campaña ese día, no con la fecha.
- **Evidencia**: Visto en 2-3 cuentas, ago-sep 2026, v24.

### Los resource names temporales no resuelven en todos los recursos
- **Tipo**: gotcha de API
- **Por qué**: dentro de un `MutateGoogleAdsRequest`, `ad_group`, criterios de ad group y anuncios resuelven `customers/X/campaigns/-2`. Un `campaign_criterion` de `LOCATION` y un `ASSET` referenciado desde `ad_group_ad` devuelven `RESOURCE_NOT_FOUND`.
- **Cómo detectarlo**: el error solo en esas operaciones dentro del lote atómico.
- **Qué hacer**: crear assets y campaña en un mutate previo, y añadir geo y anuncios con IDs reales en un segundo mutate.
- **Evidencia**: Visto en 2-3 cuentas, ago 2026, v24.
