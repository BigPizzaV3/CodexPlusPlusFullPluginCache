---
name: google-ads-bidding-measurement
description: "Reglas de pujas, Smart Bidding, portfolios, budgets, pacing, objetivos de conversión, tracking, lag y atribución en Google Ads. Usar al leer o cambiar targets de puja, revisar presupuestos y pacing, auditar objetivos y acciones de conversión, o interpretar conversiones que maduran."
---

# Pujas, budgets y medición

Reglas de Fiera para trabajar con cuentas de Google Ads. Cada regla sale de cuentas reales gestionadas a diario.

## Cómo aplicar las reglas

- Si existe `account-context.md` para la cuenta (lo crea la skill `google-ads-account-context`), léelo antes que nada: dice qué vende el negocio, su KPI, sus buckets y lo que no se toca.
- Lee solo el fichero de `references/` que toca a la tarea. El índice de abajo dice qué hay en cada uno.
- Cada regla tiene el mismo formato: **Tipo**, **Por qué** (el mecanismo), **Cómo detectarlo**, **Qué hacer** y **Evidencia**.
- **Evidencia** dice en cuántas cuentas se vio y cuándo. "Visto en 1 cuenta" es una observación: compruébala en la cuenta antes de actuar sobre ella.
- Los gotchas de API indican la versión en la que se comprobaron. Si usas otra, valida con `validate_only` o con `GoogleAdsFieldService` antes de dar la regla por buena.
- Una regla describe un mecanismo, no ordena un cambio. Antes de mutar una cuenta, enseña el plan y espera aprobación.

## Índice (18 reglas)

### `references/atribucion-y-medicion.md`: Atribución y medición
- En Google Ads solo quedan DDA y last click

### `references/budgets-y-pacing.md`: Budgets y pacing
- Las reglas automáticas multiplicativas de budget erosionan la base cada ciclo
- Un Ads Script puede revertir en una hora cualquier cambio de budget hecho por API
- Fin de semana: el CPC y la CVR caen en la misma proporción
- El coste intradía es un suelo
- La moneda de la cuenta no se deduce del mercado
- El recargo por servicios digitales va sobre el gasto de plataforma

### `references/lag-y-maduracion.md`: Lag y maduración
- `conversion_lag_bucket` mide clic a conversión, no el retraso de importación

### `references/mecanica-de-smart-bidding.md`: Mecánica de Smart Bidding
- Smart Bidding ignora los ajustes por horario, geo y audiencia; la cobertura del ad schedule sí apaga
- Desde el 17-ago-2026, una campaña limitada por presupuesto con target puja al target
- "Limitada por presupuesto" tiene dos señales y no coinciden

### `references/objetivos-de-conversion.md`: Objetivos de conversión
- Un goal estándar puede depender de una sola acción primaria; si se rompe, la campaña puja a nada
- Las acciones secundarias solo aparecen en `all_conversions`
- Dos acciones para el mismo evento: duplicado paralelo o relevo con definición distinta
- En cuentas con dos IDs de conversión en el mismo sitio, comprobar a cuál apunta cada tag

### `references/portfolios-donde-vive-el-target.md`: Portfolios: dónde vive el target
- La subclave del target la decide el `type` del portfolio

### `references/simulaciones-y-performance-planner.md`: Simulaciones y Performance Planner
- Las simulaciones salen por tipo de estrategia y los puntos de tROAS vienen ordenados por target

### `references/tracking-y-gclid.md`: Tracking y gclid
- Desde el 15-jun-2026, los imports offline y Enhanced Conversions for Leads nuevos van por Data Manager API
