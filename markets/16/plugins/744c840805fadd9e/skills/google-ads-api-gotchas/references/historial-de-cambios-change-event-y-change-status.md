# Historial de cambios: `change_event` y `change_status`

### `change_event` solo cubre 30 días y `change_status` no trae diffs
- **Tipo**: gotcha de API
- **Por qué**: pedir más de 30 días da `START_DATE_TOO_OLD`. `change_status` exige un rango acotado (`CHANGE_DATE_RANGE_INFINITE` si no) y solo dice qué recurso cambió, no qué campo.
- **Cómo detectarlo**: cualquier reconstrucción de configuración de hace más de un mes.
- **Qué hacer**: para periodos anteriores, exportar el historial de cambios de la UI (CSV, columna `Changes` multilínea). Si se necesita historia, guardar una foto diaria propia.
- **Evidencia**: Visto en 4+ cuentas, 2026, v24.

### `change_event` corta en 10.000 filas por consulta
- **Tipo**: gotcha de API
- **Por qué**: en cuentas con cambios masivos la respuesta se trunca sin aviso.
- **Cómo detectarlo**: una consulta que devuelve exactamente 10.000 filas.
- **Qué hacer**: partir la ventana en dos de forma recursiva hasta quedar por debajo del tope. En días de cambios en bloque, tratar los recuentos como un suelo.
- **Evidencia**: Visto en 4+ cuentas, jul-ago 2026, v24.

### Un límite de fecha `<= 'AAAA-MM-DD'` corta a las 00:00
- **Tipo**: gotcha de API
- **Por qué**: `change_date_time` es un timestamp. Comparar con una fecha sin hora excluye todo lo ocurrido ese día.
- **Cómo detectarlo**: cambios de hoy que no aparecen.
- **Qué hacer**: usar como límite superior el día siguiente.
- **Evidencia**: Visto en 2-3 cuentas, sep 2026, v24.

### Un UPDATE en `change_event` solo trae los campos cambiados
- **Tipo**: gotcha de API
- **Por qué**: `old_resource` y `new_resource` llevan solo `changed_fields`. Pausar una keyword llega sin texto ni match type. `ad_group_criterion.type` y `campaign_criterion.type` salen `UNSPECIFIED`. Los eventos de `AD` y `CAMPAIGN_BUDGET` no traen campaña.
- **Cómo detectarlo**: logs de cambios con entradas tipo "criterio pausado" sin identidad.
- **Qué hacer**: resolver `change_resource_name` contra el recurso vivo. El budget se cruza con `campaign.campaign_budget` y el anuncio con `ad_group_ad`. En CREATE y REMOVE el payload sí trae texto; el recurso borrado va en `old_resource`.
- **Evidencia**: Visto en 4+ cuentas, jul-sep 2026, v24.

### El tipo de un enlace de asset solo está en el sufijo del resource name
- **Tipo**: gotcha de API
- **Por qué**: en eventos de `CAMPAIGN_ASSET` o `AD_GROUP_ASSET`, `field_type` sale `UNSPECIFIED`. El tipo real está en `campaignAssets/<campaign>~<asset>~CALLOUT`. Los eventos de asset traen el ID, nunca el texto.
- **Cómo detectarlo**: un log que dice "asset pausado" sin distinguir un callout de un anuncio.
- **Qué hacer**: parsear el sufijo y resolver el texto contra `asset`. Pausar un enlace de extensión no para el serving: no tratarlo como alarma.
- **Evidencia**: Visto en 2-3 cuentas, jul-sep 2026, v24.

### `change_event` no registra targets de portfolio ni enlaces de listas compartidas
- **Tipo**: gotcha de API
- **Por qué**: ni `change_event` ni `change_status` tienen `BIDDING_STRATEGY`. `change_event` tampoco tiene `CAMPAIGN_SHARED_SET` ni `SHARED_CRITERION`. Además puede omitir cambios de estado que `change_status` sí marca.
- **Cómo detectarlo**: un cambio de tROAS de portfolio o un enlace de lista negativa que no aparece en el log.
- **Qué hacer**: combinar `change_event` (quién y qué), `change_status` (qué recursos) y una foto diaria de `accessible_bidding_strategy` y del estado de recursos.
- **Evidencia**: Visto en 2-3 cuentas, sep-oct 2026, v24.

### Los cambios automáticos de Google se identifican por `user_email`
- **Tipo**: gotcha de API
- **Por qué**: `user_email` lleva texto de sistema sin `@`: `Recommendations Auto-Apply`, `Low activity system bulk change`, `Bulk Actions`. `client_type` separa `GOOGLE_ADS_API`, `GOOGLE_ADS_WEB_CLIENT`, `GOOGLE_ADS_SCRIPTS` y `GOOGLE_ADS_RECOMMENDATIONS`.
- **Cómo detectarlo**: `WHERE change_event.user_email = 'Recommendations Auto-Apply'`. En una cuenta aparecieron eliminaciones de negativas, siempre de madrugada, durante un congelamiento de cambios acordado.
- **Qué hacer**: correr esta consulta al auditar una cuenta nueva. Desactivar auto-apply en la UI. `Low activity system bulk change` es Google pausando keywords sin impresiones: filtrarlo del triaje.
- **Evidencia**: Visto en 4+ cuentas, ago-sep 2026, v24.

### Una edición en bloque escribe un evento por entidad
- **Tipo**: gotcha de API
- **Por qué**: retirar un callout compartido de 50 campañas son 50 eventos casi idénticos. Leídos junto al gasto, parecen una pausa masiva.
- **Cómo detectarlo**: muchos eventos con el mismo timestamp, usuario, tipo de recurso y campos.
- **Qué hacer**: agrupar por `(timestamp, usuario, recurso, campos)` y listar destinos con recuento.
- **Evidencia**: Visto en 2-3 cuentas, sep 2026, v24.

### Las subidas en bloque de la UI dejan `match_type` en `UNSPECIFIED`
- **Tipo**: gotcha de API
- **Por qué**: el match type va en la sintaxis del texto: `[exacta]`, `"frase"`.
- **Cómo detectarlo**: keywords creadas con match type vacío en el payload.
- **Qué hacer**: inferir el match type de los delimitadores del texto.
- **Evidencia**: Visto en 1 cuenta, jul 2026, v24.
