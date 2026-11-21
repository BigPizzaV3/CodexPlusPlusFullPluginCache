# Demand Gen

### `upgraded_targeting = True` bloquea el geo y no se puede cambiar
- **Tipo**: gotcha de API
- **Por qué**: una Demand Gen creada por API sin tocar el campo sale con `True`. Entonces un criterio `LOCATION` falla con `request_error: UNKNOWN` y trigger `OWNED_AND_OPERATED`. El update da `IMMUTABLE_FIELD`.
- **Cómo detectarlo**: el error críptico al añadir geo, igual con país o región.
- **Qué hacer**: crear con `demand_gen_campaign_settings.upgraded_targeting = False` y `network_settings.target_content_network = True`. Si ya está creada, eliminar y recrear.
- **Evidencia**: Visto en 2-3 cuentas, may-ago 2026, v24.

### Los ad groups de Demand Gen funcionan con una sola audiencia compuesta
- **Tipo**: gotcha de API
- **Por qué**: no admiten `user_list` ni `custom_audience` sueltos (`CANNOT_ADD_AUDIENCE_SEGMENT_CRITERION_WHEN_AUDIENCE_GROUPED_IS_SET`). Solo cabe un recurso `Audience` por ad group. Un ad group creado en la UI sin audiencia no acepta una después.
- **Cómo detectarlo**: los errores de "audience grouped" al adjuntar segmentos.
- **Qué hacer**: crear un `Audience` con todos los segmentos y las exclusiones dentro (`exclusion_dimension.exclusions`). Si el ad group nació mal, eliminarlo y recrearlo con la audiencia en el mismo mutate.
- **Evidencia**: Visto en 2-3 cuentas, may-ago 2026, v24.

### Con audiencia compuesta, la demografía va dentro de la audiencia
- **Tipo**: gotcha de API
- **Por qué**: crear `AGE_RANGE` o `GENDER` en el ad group falla. Google materializa después esos criterios solo, y la lectura sugiere que se pueden crear.
- **Cómo detectarlo**: criterios demográficos que aparecen sin haberlos creado.
- **Qué hacer**: excluir edades con `AgeDimension` dentro del `Audience`. `AgeSegment` solo acepta los buckets estándar (18, 25, 35, 45, 55 y 24, 34, 44, 54, 64); un 30-50 da `DIMENSION_INVALID`.
- **Evidencia**: Visto en 2-3 cuentas, ago 2026, v24.

### Límites de creatividad de Demand Gen que la API aplica
- **Tipo**: gotcha de API
- **Por qué**: el anuncio multi-asset admite 20 imágenes en total. El de vídeo, 5 vídeos. Las tarjetas de carrusel exigen `final_urls` en el asset. Las variantes de vídeo autogeneradas ("Square:", "Shortened:", "Vertical:") se rechazan con `request_error: UNKNOWN`.
- **Cómo detectarlo**: validar el anuncio con un vídeo cada vez para aislar el culpable.
- **Qué hacer**: usar solo uploads reales. Crear un `YouTubeVideoAsset` de un vídeo ya existente devuelve el ID existente, sin error. `custom_audience` va por su propio servicio, no en `MutateOperation`.
- **Evidencia**: Visto en 2-3 cuentas, ago 2026, v24.
