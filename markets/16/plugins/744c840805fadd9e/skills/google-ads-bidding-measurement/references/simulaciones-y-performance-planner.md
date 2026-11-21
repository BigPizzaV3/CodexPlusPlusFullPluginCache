# Simulaciones y Performance Planner

### Las simulaciones salen por tipo de estrategia y los puntos de tROAS vienen ordenados por target
- **Tipo**: gotcha de API
- **Por qué**: una campaña a tROAS publica `TARGET_ROAS` y no `BUDGET`. Sus puntos van ordenados por target, no por coste.
- **Cómo detectarlo**: buscar los tres tipos y ordenar por `cost_micros` antes de dibujar.
- **Qué hacer**: no sumar simulaciones de varias campañas: tienen rejillas de gasto distintas. Ninguna lleva canibalización entre campañas.
- **Evidencia**: Visto en 2-3 cuentas, jul 2026.
