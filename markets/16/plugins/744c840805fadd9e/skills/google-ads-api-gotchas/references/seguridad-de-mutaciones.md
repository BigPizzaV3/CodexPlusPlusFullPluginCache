# Seguridad de mutaciones

### Dry-run por defecto y apply solo tras revisar el diff
- **Tipo**: regla de seguridad
- **Por qué**: una acción "obvia y pequeña" sigue pudiendo mutar el recurso equivocado. Sin revisión humana del plan no hay control.
- **Cómo detectarlo**: un script que muta sin flag explícito.
- **Qué hacer**: el dry-run produce una tabla `entity_type`, `entity_id`, `field`, `current_value`, `new_value`. El apply exige un flag explícito y la aprobación de una persona que haya visto ese diff.
- **Evidencia**: Visto en 4+ cuentas, 2026.

### El dry-run tiene que validar contra el servidor
- **Tipo**: regla de seguridad
- **Por qué**: muchos errores solo aparecen al validar en la API: brand guidelines, topes de assets, políticas, campos obligatorios. Un dry-run local pasa y el apply falla a medias.
- **Cómo detectarlo**: un plan que nunca se ha enviado con `validate_only = True`.
- **Qué hacer**: lanzar cada operación con `validate_only`. Si el dry-run llama a la misma función que el apply, pasarle el flag: un log en modo seco no basta.
- **Evidencia**: Visto en 4+ cuentas, ago-sep 2026, v24.

### `validate_only` con `partial_failure` devuelve todos los errores a la vez
- **Tipo**: gotcha de API
- **Por qué**: la excepción normal enseña el primer error, a veces sin mensaje legible. Con los dos flags, `partial_failure_error` lista cada error con su índice de operación y su campo.
- **Cómo detectarlo**: errores que aparecen de uno en uno en iteraciones sucesivas.
- **Qué hacer**: validar creaciones de varias operaciones con los dos flags y leer `partial_failure_error`.
- **Evidencia**: Visto en 2-3 cuentas, sep 2026, v24.

### Una violación de política tumba el lote entero y la API solo enseña la primera
- **Tipo**: gotcha de API
- **Por qué**: `MutateAdGroupCriteria` es atómico. Un topónimo puede disparar una política de citas. Keywords de salud en ad groups con audiencias disparan `HEALTH_IN_PERSONALIZED_ADS`. `partial_failure` no agrega las violaciones.
- **Cómo detectarlo**: `policy_violation_error: POLICY_ERROR` con `PolicyViolationDetails`.
- **Qué hacer**: biseccionar con `validate_only` hasta listarlas todas. Si `is_exemptible`, reenviar con `exempt_policy_violation_keys` (`policy_name` y `violating_text`). Las no exentables se quitan.
- **Evidencia**: Visto en 2-3 cuentas, ago 2026, v24.

### Mutar por ID y verificar contra el estado vivo antes de construir la operación
- **Tipo**: regla de seguridad
- **Por qué**: nombres repetidos y renombres hacen que una resolución por nombre apunte al recurso equivocado sin error.
- **Cómo detectarlo**: un dry-run que resuelve una entidad con gasto o campaña distintos de los esperados.
- **Qué hacer**: el plan lleva IDs. Antes de mutar, comprobar que nombre y padre del ID coinciden con lo esperado. Si no, abortar.
- **Evidencia**: Visto en 4+ cuentas, jul-sep 2026, v24.

### Un OK de la API no prueba que el cambio se aplicó
- **Tipo**: regla de seguridad
- **Por qué**: hay no-ops silenciosos. Un booleano a `False` con máscara automática. `membership_life_span` forzado. `biddable` bajo custom goal. `create` de una keyword que ya existe. El nombre de un budget propio.
- **Cómo detectarlo**: releer cada entidad tras el mutate con una consulta independiente.
- **Qué hacer**: verificar el valor final, no la respuesta. Fallar el script si no coincide con lo pedido.
- **Evidencia**: Visto en 4+ cuentas, jul-nov 2026, v24.

### La lectura tarda en reflejar una mutación
- **Tipo**: gotcha de API
- **Por qué**: la API de lectura es eventualmente consistente. Un dry-run lanzado 13 segundos después de un apply seguía viendo keywords sin crear.
- **Cómo detectarlo**: un "fallo de carga" que desaparece al repetir la consulta.
- **Qué hacer**: esperar unos 30 segundos antes de verificar, o verificar por recuento.
- **Evidencia**: Visto en 2-3 cuentas, ago-sep 2026, v24.

### Backup completo antes y después de cada apply
- **Tipo**: regla de seguridad
- **Por qué**: sin el estado previo completo no hay restauración posible. `change_event` no guarda pins, ni historia de más de 30 días, ni lecturas.
- **Cómo detectarlo**: un apply sin fichero de backup asociado.
- **Qué hacer**: volcar JSON y CSV de las entidades afectadas antes y después. Registrar script, argumentos, usuario y hora en un log de mutaciones por cliente.
- **Evidencia**: Visto en 4+ cuentas, 2026.

### Los scripts de alta tienen que ser reanudables e idempotentes
- **Tipo**: regla de seguridad
- **Por qué**: si un script crea budget o estrategia y falla después, los recursos quedan creados. Relanzarlo duplica.
- **Cómo detectarlo**: budgets o estrategias huérfanos con `reference_count = 0`.
- **Qué hacer**: buscar lo existente antes de crear, con `status != 'REMOVED'`. Para budgets propios, buscar por cableado (`explicitly_shared = False` y `reference_count <= 1`), no por nombre. Reutilizar un budget solo si es huérfano y tiene el importe esperado.
- **Evidencia**: Visto en 2-3 cuentas, ago-sep 2026, v24.

### Un budget propio no conserva su nombre ni admite renombrarse
- **Tipo**: gotcha de API
- **Por qué**: con `explicitly_shared = False`, Google sustituye el nombre del create por el de la campaña. Un update de `name` falla con `request_error: UNKNOWN`. Al renombrar la campaña, el budget toma el nombre nuevo solo.
- **Cómo detectarlo**: un find-by-name que nunca encuentra el budget y cada relanzamiento crea otro.
- **Qué hacer**: no buscar budgets propios por nombre. En un rename, mutar solo la campaña. Con budget compartido sí hay que renombrar el budget, o un alta posterior lo reutilizará con su importe viejo.
- **Evidencia**: Visto en 2-3 cuentas, sep 2026, v24.

### Pausar, no eliminar
- **Tipo**: regla de seguridad
- **Por qué**: `REMOVED` es terminal. Un recurso eliminado no se reactiva, y `keyword_view` deja de devolver su historia.
- **Cómo detectarlo**: cualquier operación `remove` sobre keywords, ad groups, anuncios o campañas.
- **Qué hacer**: pausar. Reservar `remove` para enlaces (assets, listas) y negativas, con backup.
- **Evidencia**: Visto en 4+ cuentas, 2026.

### Topes por cambio, planes que caducan y revert inmediato
- **Tipo**: regla de seguridad
- **Por qué**: un cambio grande de budget o target, o dos seguidos sobre la misma entidad, impide leer el efecto. Un plan aprobado sobre un estado que ya cambió aplica algo distinto de lo revisado.
- **Cómo detectarlo**: un apply sobre una entidad modificada después de generar el plan.
- **Qué hacer**: topes por cambio (por ejemplo ±30% de budget, ±20% de target) y enfriamiento sobre la misma entidad. El plan caduca y se invalida si la cuenta cambia. Guardar la operación inversa para revertir rápido. Un rechazo por tope no se esquiva partiendo el cambio.
- **Evidencia**: Visto en 4+ cuentas, ago-sep 2026.

### Un portfolio se cambia pensando en todas sus campañas
- **Tipo**: regla de seguridad
- **Por qué**: el target gobierna todas las campañas del portfolio, también de otras cuentas si es del manager. Un ad group nuevo compite dentro del portfolio entero.
- **Cómo detectarlo**: listar las campañas que usan la estrategia antes de tocar el target.
- **Qué hacer**: decidir y medir el cambio sobre el conjunto. Mutar en la cuenta dueña.
- **Evidencia**: Visto en 4+ cuentas, ago-sep 2026, v24.

### Las campañas de Video no admiten mutaciones por API
- **Tipo**: gotcha de API
- **Por qué**: devuelven `MUTATE_NOT_ALLOWED`. Search, PMax y Demand Gen sí se mutan.
- **Cómo detectarlo**: comprobar `advertising_channel_type` antes de construir operaciones.
- **Qué hacer**: abortar antes de tocar una campaña `VIDEO` y hacer el cambio en la UI.
- **Evidencia**: Visto en 4+ cuentas, 2026, v24.

### Los criterios de una campaña eliminada no se pueden borrar
- **Tipo**: gotcha de API
- **Por qué**: devuelve `OPERATION_NOT_PERMITTED_FOR_REMOVED_RESOURCE`. Sin `partial_failure`, el lote entero cae.
- **Cómo detectarlo**: auditorías de inventario que cuentan negativas de campañas eliminadas.
- **Qué hacer**: descontar del alcance lo que cuelga de campañas `REMOVED`. No bloquea ni puja. Lo de campañas pausadas sí se borra, pero vuelven sin él si se reactivan.
- **Evidencia**: Visto en 1 cuenta, sep 2026, v24.

### Positiva y negativa con el mismo texto y match chocan en el ad group
- **Tipo**: gotcha de API
- **Por qué**: comparten `criterion_id`. Crear la segunda da `IMMUTABLE_FIELD`. Con la positiva pausada, crear la negativa da `CANT_UPDATE_NEGATIVE`, que parece "la negativa ya existe".
- **Cómo detectarlo**: consultar el criterio en el ad group antes de interpretar el error.
- **Qué hacer**: cruzar negativas existentes contra el pool de keywords nuevo antes de mutar. Abortar si hay colisión.
- **Evidencia**: Visto en 2-3 cuentas, ago-nov 2026, v24.

### Crear una keyword que ya existe es un no-op que devuelve éxito
- **Tipo**: gotcha de API
- **Por qué**: un `create` de `ad_group_criterion` con el mismo ad group, texto y match type pasa sin error y deja el criterio existente intacto, pausado si lo estaba.
- **Cómo detectarlo**: keywords "añadidas" que siguen pausadas y no generan `change_event`.
- **Qué hacer**: buscar el criterio primero. Si está pausado, update de `status`. Si está activo, no hacer nada. Si no existe, crear con `status = ENABLED` explícito.
- **Evidencia**: Visto en 1 cuenta, jul 2026, v24.

### Una audiencia positiva sin `TargetRestriction` restringe la campaña
- **Tipo**: gotcha de API
- **Por qué**: una campaña de Search sin entrada `AUDIENCE` en `targeting_setting.target_restrictions` está en targeting. Añadir una lista positiva limita el tráfico a esa lista, sin error ni cambio de estado.
- **Cómo detectarlo**: `SELECT campaign.id, campaign.targeting_setting.target_restrictions FROM campaign`. Si ya pasó: impression share que sube mientras las impresiones caen.
- **Qué hacer**: poner `AUDIENCE` con `bid_only = True` y máscara `targeting_setting.target_restrictions` antes de añadir audiencias.
- **Evidencia**: Visto en 2-3 cuentas, sep 2026, v24.

### `membership_life_span` de una lista rule-based no siempre se guarda
- **Tipo**: gotcha de API
- **Por qué**: con dos operandos o sin `lookback_window_days`, pedir 7 días guardó 540. El update del campo devuelve OK y no cambia nada. `basic_user_list` rechaza acciones de GA4 o Firebase con `INVALID_CONVERSION_TYPE`.
- **Cómo detectarlo**: releer `user_list.membership_life_span` tras crear o actualizar.
- **Qué hacer**: si no coincide, crear la audiencia en GA4 con la ventana deseada y exportarla a Ads. Cerrar y renombrar la lista errónea, no borrarla.
- **Evidencia**: Visto en 1 cuenta, sep 2026, v24.

### Los assets `AUTOMATICALLY_CREATED` no se editan ni se enlazan a mano
- **Tipo**: gotcha de API
- **Por qué**: editar da `CANNOT_MODIFY_AUTOMATICALLY_CREATED_ASSET`. Enlazar da `Advertiser links cannot link to automatically created asset`. Los sitelinks automáticos pueden apuntar a la web de otro país.
- **Cómo detectarlo**: barrer `campaign_asset`, `ad_group_asset`, `customer_asset` y `asset_group` con `asset.source`. `landing_page_view` no cubre destinos de sitelink.
- **Qué hacer**: quitar el enlace con `remove`. Quitarlo no apaga la automatización, que puede regenerar otro: vigilarlo de forma recurrente.
- **Evidencia**: Visto en 2-3 cuentas, ago 2026, v24.

### `PromotionAsset`: el porcentaje va en escala de millón y la URL es obligatoria
- **Tipo**: gotcha de API
- **Por qué**: `percent_off` usa 1.000.000 = 100%, así que 5% es 50.000. Un 5.000.000 da `TOO_HIGH`. Sin `asset.final_urls` falla con `REQUIRED_NONEMPTY_LIST`.
- **Cómo detectarlo**: comparar con los promotion assets existentes de la cuenta.
- **Qué hacer**: usar la escala de millón y pasar `final_urls`. `start_date` y `end_date` nativos apagan la promoción sola.
- **Evidencia**: Visto en 1 cuenta, jul 2026, v24.

### El header de un structured snippet no es texto libre
- **Tipo**: gotcha de API
- **Por qué**: Google acepta un conjunto cerrado de headers que depende del idioma. Un header fuera de la lista se rechaza al aplicar.
- **Cómo detectarlo**: validar con `validate_only` antes de una tanda.
- **Qué hacer**: contrastar el header en la UI. Validar en el plan 3 a 10 valores, de 25 caracteres o menos, sin repetir.
- **Evidencia**: Visto en 2-3 cuentas, sep 2026, v24.
