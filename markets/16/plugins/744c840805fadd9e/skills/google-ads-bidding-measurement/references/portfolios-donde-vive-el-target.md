# Portfolios: dónde vive el target

### La subclave del target la decide el `type` del portfolio
- **Tipo**: gotcha de API
- **Por qué**: en un portfolio `MAXIMIZE_CONVERSION_VALUE` el target está en `maximize_conversion_value.target_roas`. `target_roas.target_roas` sale 0 siempre en ese tipo.
- **Cómo detectarlo**: leer `type` y elegir campo según él. Si el campo correcto sale 0, sí es literal: valor máximo sin techo de eficiencia.
- **Qué hacer**: mutar con `update_mask = maximize_conversion_value.target_roas` en ese tipo. Lo mismo para `maximize_conversions.target_cpa_micros` frente a `target_cpa.target_cpa_micros`.
- **Evidencia**: Visto en 2-3 cuentas, ago-sep 2026.
