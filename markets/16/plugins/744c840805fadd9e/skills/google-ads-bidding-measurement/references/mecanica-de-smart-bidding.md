# Mecánica de Smart Bidding

### Smart Bidding ignora los ajustes por horario, geo y audiencia; la cobertura del ad schedule sí apaga
- **Tipo**: gotcha de API
- **Por qué**: con tCPA, tROAS, Max Conv o Max Conv Value los ajustes de puja no-dispositivo son señal, no multiplicador. Solo device -100% excluye de forma determinista.
- **Cómo detectarlo**: `campaign.bidding_strategy_type` en estrategia automática y `campaign_criterion.bid_modifier` en `AD_SCHEDULE`, `LOCATION` o audiencia. No asumir que -100% en ad schedule excluye.
- **Qué hacer**: para apagar franjas, crear tramos de ad schedule que dejen la franja fuera. Para recortar gasto en una franja, usar el budget diario.
- **Evidencia**: Visto en 2-3 cuentas, jul-ago 2026.

### Desde el 17-ago-2026, una campaña limitada por presupuesto con target puja al target
- **Tipo**: regla de decisión
- **Por qué**: antes, el presupuesto rebajaba la puja y la campaña entregaba por debajo del target. Ahora la puja la fija el target y el presupuesto se respeta por participación. Afecta a Search, Shopping, PMax, Demand Gen y portfolios con presupuesto compartido.
- **Cómo detectarlo**: listar campañas limitadas con target y comparar target contra CPA o ROAS real. El hueco es la exposición: si el CPA real pasa del 50% al 100% del target, a gasto fijo las conversiones caen a la mitad.
- **Qué hacer**: ordenar por hueco × gasto, no por hueco en %. Opciones: bajar el target al real reciente o pasar a Max Conv / Max Conv Value sin target. El "target holgado para explorar" deja de existir.
- **Evidencia**: Visto en 4+ cuentas, ago 2026.

### "Limitada por presupuesto" tiene dos señales y no coinciden
- **Tipo**: gotcha de API
- **Por qué**: `campaign.primary_status_reasons = BUDGET_CONSTRAINED` es una foto de hoy. `metrics.search_budget_lost_impression_share` cubre el periodo, pero Demand Gen y App no lo reportan.
- **Cómo detectarlo**: pedir las dos. En una cuenta, Google marcaba como limitadas muchas menos campañas de las que perdían IS por presupuesto. En otra el flag recaía en UAC, que no compiten en Search.
- **Qué hacer**: usar las dos señales y decir qué canales quedan sin medir.
- **Evidencia**: Visto en 2-3 cuentas, ago 2026.
