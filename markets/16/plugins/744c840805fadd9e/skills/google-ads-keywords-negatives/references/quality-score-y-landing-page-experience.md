# Quality Score y Landing Page Experience

### Los campos de QS: foto de hoy frente a histórico segmentable
- **Tipo**: gotcha de API
- **Por qué**: `ad_group_criterion.quality_info.*` (`post_click_quality_score`, `creative_quality_score`, `search_predicted_ctr`) es foto actual y no acepta `segments.date`.
- **Cómo detectarlo**: con ese campo no se puede afirmar que el LPE "no se ha movido" sin foto previa.
- **Qué hacer**: series con `metrics.historical_quality_score`, `historical_landing_page_quality_score`, `historical_creative_quality_score` y `historical_search_predicted_ctr` sobre `keyword_view`. Enum: 2 = BELOW, 3 = AVERAGE, 4 = ABOVE; 0/1 = sin dato. PMax y App no tienen QS.
- **Evidencia**: Visto en 2-3 cuentas, ago-sep 2026.

### Un QS medio que sube puede ser recambio de keywords
- **Tipo**: error de método
- **Por qué**: si salen keywords de QS bajo y entran de QS alto, la media sube sin que mejore ninguna. Un bloque estructuralmente bajo (competidores, QS 2-3) arrastra la media según su peso.
- **Cómo detectarlo**: like-for-like por texto + match type sobre ventanas comparables, ponderado por impresiones. En un caso, de +1,1 puntos solo +0,34 eran mejora real.
- **Qué hacer**: no reportar QS medio sin separar competidores ni sin el panel de mismas keywords.
- **Evidencia**: Visto en 2-3 cuentas, ago-sep 2026.
