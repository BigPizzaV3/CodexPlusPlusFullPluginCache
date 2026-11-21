---
name: resumen-operativo
description: Flujo guiado para generar resúmenes ejecutivos diarios y auditorías operativas en Intrasistema.
---

# Intrasistema Operativo: Resumen Diario y Auditoría

Flujo guiado para generar resúmenes ejecutivos y auditorías operativas en Intrasistema.

## Objetivos
1. Descubrir el contexto y empresas asignadas al usuario activo.
2. Extraer métricas comerciales y logísticas del día (órdenes de venta, stock, facturación e incidencias).
3. Presentar toda la información consolidada en tablas Markdown ejecutivas limpias y legibles.
4. Para cualquier acción mutante o de cancelación, solicitar confirmación humana explícita mostrando el impacto antes de invocar `confirm_action`.

## Secuencia de Interacción
1. **Paso 1: Obtener Contexto**
   - Ejecutar `get_my_context` para identificar usuario, tenant y lista de `accessible_businesses`.
   - Si el usuario tiene un solo negocio, se selecciona automáticamente. Si tiene múltiples y no especificó cuál, consultar o presentar el selector.
2. **Paso 2: Consultar Métricas**
   - Consultar órdenes de venta recientes y su estado.
   - Consultar incidencias o reclamos pendientes.
3. **Paso 3: Formateo de Resultados**
   - Presentar cada bloque en tablas Markdown con columnas claras (ID, Referencia, Estado, Monto, Depósito/Canal).
