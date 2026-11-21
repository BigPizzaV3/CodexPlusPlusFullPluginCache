# Performance Max

### Crear una PMax por API falla en sitios poco obvios
- **Tipo**: gotcha de API
- **Por qué**: `AssetAutomationSetting` es un tipo anidado. `brand_assets.logo_asset` es repetido. Enlazar assets valida el asset group entero, así que textos solos fallan con `NOT_ENOUGH_MARKETING_IMAGE_ASSET`.
- **Cómo detectarlo**: errores que cambian en cada iteración del create.
- **Qué hacer**: enviar textos e imágenes en una sola mutación de `AssetGroupAsset`. Reutilizar budget, campaña y asset group si ya existen. Esperar `primary_status = PENDING` unas horas mientras los assets están en revisión.
- **Evidencia**: Visto en 2-3 cuentas, ago-sep 2026, v24.

### Las redes de una PMax no se pueden apagar
- **Tipo**: gotcha de API
- **Por qué**: mutar `network_settings.target_search_network` a `False` devuelve `CANNOT_TARGET_SEARCH_NETWORK`, en campañas activas y pausadas.
- **Cómo detectarlo**: el error.
- **Qué hacer**: leer el reparto por red con `segments.ad_network_type`. No se controla.
- **Evidencia**: Visto en 1 cuenta, sep 2026, v24.

### La expansión de URL de PMax se corta con exclusiones `WEBPAGE`, no con un flag
- **Tipo**: gotcha de API
- **Por qué**: `campaign.url_expansion_opt_out` no existe en v24. La expansión vive en `campaign.asset_automation_settings` (`FINAL_URL_EXPANSION_TEXT_ASSET_AUTOMATION`) y el toggle es de UI. Lo que sí acepta la API es un `campaign_criterion` negativo de tipo `WEBPAGE`.
- **Cómo detectarlo**: `landing_page_view` con `clicks > 0` agrupado por prefijo de path, y `final_url_expansion_asset_view`.
- **Qué hacer**: excluir con `webpage.conditions = [(URL, CONTAINS, "<fragmento>")]` y `negative = True`. Lo mismo vale para AI Max y DSA en Search. Un path no es una keyword negativa.
- **Evidencia**: Visto en 2-3 cuentas, sep 2026, v24.

### `TEXT_ASSET_AUTOMATION` no se apaga si la expansión de URL sigue activa
- **Tipo**: gotcha de API
- **Por qué**: devuelve `DYNAMIC_TEXT_ASSET_CANNOT_OPT_OUT_WITH_FINAL_URL_EXPANSION_OPT_IN`. Los dos ajustes van juntos.
- **Cómo detectarlo**: el error al hacer opt-out solo del texto.
- **Qué hacer**: decidir los dos ajustes a la vez.
- **Evidencia**: Visto en 1 cuenta, oct 2026, v24.

### Los topes de assets de un asset group cuentan solo los del anunciante
- **Tipo**: gotcha de API
- **Por qué**: los `AUTOMATICALLY_CREATED` conviven por encima del tope. Topes en v24: 15 headlines, 5 descriptions, 5 long headlines. Las imágenes topan en 20 sumando todas las proporciones (`RESOURCE_LIMIT`).
- **Cómo detectarlo**: contar con `asset_group_asset.source = 'ADVERTISER'` y `status != 'REMOVED'`. Un grupo puede enseñar 23 headlines y rechazar el 15.º.
- **Qué hacer**: en un grupo lleno, las bajas van antes que las altas en la misma sesión. Probar el margen con `validate_only`. Para borrar, usar el resource name de la consulta: construirlo a mano dio `BAD_RESOURCE_ID`.
- **Evidencia**: Visto en 2-3 cuentas, sep-oct 2026, v24.

### El tope de 5 vídeos por asset group es de la UI
- **Tipo**: gotcha de API
- **Por qué**: `validate_only` y el apply aceptaron pasar de 5 a 8 vídeos.
- **Cómo detectarlo**: validar el alta antes de plantear borrados.
- **Qué hacer**: no retirar vídeos solo para hacer sitio. Medir por vídeo con `asset_group_asset`, `metrics.*` y `segments.date`.
- **Evidencia**: Visto en 1 cuenta, ago 2026, v24.

### Cambiar todo el copy de un asset group exige un orden de fases
- **Tipo**: gotcha de API
- **Por qué**: cada baja se valida contra el mínimo (`NOT_ENOUGH_HEADLINE_ASSET`), y las altas topan. Los auto-creados cuentan para el mínimo. Un texto idéntico es el mismo asset de cuenta: recrearlo da `CONCURRENT_MODIFICATION`. Quitar y poner el mismo search theme en una petición da `ID_EXISTS_IN_MULTIPLE_MUTATES`.
- **Cómo detectarlo**: errores de mínimo o de tope al intentar un reemplazo en una sola petición.
- **Qué hacer**: bajas hasta 3/1/2 del anunciante, altas que caben, bajas del resto, altas que faltan, y auto-creados al final. Mantener siempre un titular de 15 caracteres o menos y una descripción de 60 o menos. Buscar el texto en `asset` antes de crearlo.
- **Evidencia**: Visto en 1 cuenta, oct 2026, v24.

### Quitar un vídeo de PMax arrastra sus derivados automáticos
- **Tipo**: gotcha de API
- **Por qué**: Google borra después las copias `AUTOMATICALLY_CREATED` ("Shortened", "Square", "Voiceover") del vídeo retirado. El mutate devuelve OK.
- **Cómo detectarlo**: consulta independiente del estado después del mutate.
- **Qué hacer**: contar como cobertura garantizada solo los vídeos `ADVERTISER`. Un asset group sin vídeo no da error: Google genera uno desde la landing.
- **Evidencia**: Visto en 1 cuenta, sep 2026, v24.

### Con Brand Guidelines, logo y nombre de negocio viven en la campaña
- **Tipo**: gotcha de API
- **Por qué**: con `brand_guidelines_enabled = True`, `BUSINESS_NAME`, `LOGO` y `LANDSCAPE_LOGO` van en `campaign_asset`. En `asset_group_asset` quedan los enlaces viejos `REMOVED`. `primary_status_reasons` no lo delata; solo el error al mutar.
- **Cómo detectarlo**: `campaign_asset` filtrado por esos `field_type`.
- **Qué hacer**: no "reparar" assets que no faltan. Validar contra el servidor antes de recrear enlaces.
- **Evidencia**: Visto en 2-3 cuentas, ago-sep 2026, v24.

### `EnablePMaxBrandGuidelines` no tiene dry-run, no se revierte y añade el favicon como logo
- **Tipo**: gotcha de API
- **Por qué**: la RPC no admite `validate_only`. Una vez activo no se desactiva. Aun con `auto_populate_brand_assets = False`, enlaza el favicon de 32 px como `LOGO` automático.
- **Cómo detectarlo**: releer `campaign_asset` con `field_type IN (LOGO, LANDSCAPE_LOGO, BUSINESS_NAME)` tras activar.
- **Qué hacer**: quitar el favicon con `CampaignAssetService` remove. Tratar la activación como irreversible y pedir aprobación explícita.
- **Evidencia**: Visto en 1 cuenta, sep 2026, v24.

### `UNSET` en la automatización de assets no significa opted-in
- **Tipo**: gotcha de API
- **Por qué**: la API solo devuelve `asset_automation_settings` cuando se ha tocado. En una auditoría, las campañas `UNSET` no servían assets automáticos, y algunas `OPTED_OUT` sí los servían.
- **Cómo detectarlo**: `ad_group_ad_asset_view` con `source = 'AUTOMATICALLY_CREATED'` y `field_type IN ('HEADLINE','DESCRIPTION')` en 30 días.
- **Qué hacer**: decidir sobre el serving real, no sobre el ajuste. Leer el estado de AI Max en `campaign.ai_max_setting.enable_ai_max`.
- **Evidencia**: Visto en 4+ cuentas, ago 2026, v24.

### Las exclusiones de placements de PMax solo van a nivel cuenta o lista del manager
- **Tipo**: gotcha de API
- **Por qué**: la API admite exclusiones con `CustomerNegativeCriterionService` o con shared sets `NEGATIVE_PLACEMENTS` del manager. Las listas del manager no bajan a sub-managers. Límites: 20 listas por manager, 250.000 miembros por lista, 20 listas por cuenta.
- **Cómo detectarlo**: `performance_max_placement_view`, que solo trae impresiones.
- **Qué hacer**: excluir con heurísticas conservadoras sobre impresiones. La exclusión se aplica a todas las campañas de la cuenta.
- **Evidencia**: Visto en 1 cuenta, may 2026, v24.
