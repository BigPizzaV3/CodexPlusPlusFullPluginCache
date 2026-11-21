# Auditoría de cuenta

- **Cuándo**: al recibir una cuenta nueva, o una vez al año en cuentas activas.
- **Entradas**: Customer ID, MCC, ventana (por defecto 90 días), KPI de negocio y objetivo de CPA o ROAS.

**Pasos**

1. **Universo.** Lista campañas con estado, tipo de canal, estrategia de puja y gasto L30D. Separa las que no sirven y los brazos de experimento.
   ```sql
   SELECT campaign.id, campaign.name, campaign.advertising_channel_type,
          campaign.experiment_type, campaign.primary_status, campaign.serving_status,
          campaign.bidding_strategy_type, campaign.bidding_strategy, metrics.cost_micros
   FROM campaign
   WHERE segments.date BETWEEN '{D-30}' AND '{D-1}' AND campaign.status = 'ENABLED'
   ```
2. **Conversiones (primero, porque invalida todo lo demás).** Por acción: primaria o secundaria, conteo "one" o "every", modelo y valor estático o dinámico. Busca acciones a 0 en 30 días y doble conteo (GTM + GA4 + nativa). Revisa overrides por campaña en `campaign_conversion_goal`.
3. **Targets de puja.** Pide `campaign.bidding_strategy` junto al target. Si la campaña usa portfolio, el target de campaña sale 0: léelo en `accessible_bidding_strategy`.
4. **Estructura.** Convención de nombres, ad groups por campaña, campañas cuyo nombre no describe lo que compran, intenciones mezcladas en un ad group.
5. **Keywords.** Inventario positivo desde `ad_group_criterion` con `negative = FALSE`. Distribución de match types. Keywords de alto gasto con QS bajo y su componente Below.
6. **Negativas a tres niveles.** `shared_criterion`, `campaign_criterion` y `ad_group_criterion` con `negative = TRUE`, más `campaign_shared_set` para saber qué listas aplican dónde. Busca negativas que bloquean positivas propias.
7. **Search terms.** Composición de intención sobre `search_term_view`; economía sobre `keyword_view`. Mide la cobertura del search term view en el segmento.
8. **Presupuesto y restricción.** Budget lost contra rank lost por campaña o pool. Campañas en learning más de 14 días. Pacing: budget diario × 30,4 contra objetivo mensual.
9. **Anuncios y extensiones.** RSAs por ad group, assets por anuncio, uso de pins. Extensiones mínimas por campaña de Search. No uses `performance_label` de assets de texto.
10. **Geo, dispositivo y configuración.** Targeting por "presencia" o "presencia o interés", Display expansion, Search Partners, modificadores de dispositivo accidentales (-100%). Bajo Smart Bidding, los modificadores de franja horaria no operan.
11. **Historial de cambios.** `change_event` de 30 días: quién cambia la cuenta, cuánto es Auto-Apply y cuánto reglas automáticas.
12. **Priorizar.** Arreglos inmediatos (tracking, bloqueos), mejoras rápidas, medio plazo, cambios estratégicos. Cada punto con su cifra y su base.

- **Salida**: informe con resumen ejecutivo, secciones por área y lista priorizada de acciones con impacto estimado.
- **Reglas que aplica** (en las otras skills del paquete):
  - Paso 1: «`ENABLED` no significa que la campaña pueda servir».
  - Paso 2: «`campaign_conversion_goal` todo a `biddable = False` no significa "hereda la cuenta"»; «Las acciones secundarias solo aparecen en `all_conversions`».
  - Paso 3: «Con portfolio, el target de la campaña sale 0»; «`FROM bidding_strategy` no ve los portfolios del manager».
  - Paso 5: «`keyword_view` devuelve también las keywords negativas».
  - Paso 6: «Una negativa solo bloquea en su ámbito; resolverlo antes de medir».
  - Paso 8: «El tope de gasto mensual es 30,4 veces el budget diario».
  - Paso 9: «La etiqueta LOW/GOOD/BEST de los assets de RSA vuelve siempre `NOT_APPLICABLE`».
  - Paso 10: «Los ajustes de red de Search tienen nombres que confunden»; «Smart Bidding ignora los ajustes por horario, geo y audiencia; la cobertura del ad schedule sí apaga».
  - Paso 11: «Los cambios automáticos de Google se identifican por `user_email`»; «`change_event` no registra targets de portfolio ni enlaces de listas compartidas».
