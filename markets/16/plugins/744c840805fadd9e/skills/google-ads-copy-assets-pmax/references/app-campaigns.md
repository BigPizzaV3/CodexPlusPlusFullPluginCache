# App campaigns

### El bucket SEARCH de una campaña App incluye Google Play
- **Tipo**: gotcha de API
- **Por qué**: `AdNetworkType` no tiene valor para Play. SEARCH mezcla la tienda y la unidad de app promo de la búsqueda de Google.
- **Cómo detectarlo**: n/a.
- **Qué hacer**: no concluir que la App ocupa la subasta de texto por su peso en SEARCH. Comparar la firma de precio: CPC y CPM de App en SEARCH frente a Search de texto.
- **Evidencia**: Visto en 2-3 cuentas, jul-sep 2026.

### Las campañas App no tienen informe de placements ni de search terms
- **Tipo**: gotcha de API
- **Por qué**: `detail_placement_view`, `group_placement_view`, `search_term_view` y `campaign_search_term_insight` devuelven 0 filas para `MULTI_CHANNEL`.
- **Cómo detectarlo**: n/a.
- **Qué hacer**: el máximo detalle es `segments.ad_network_type`. Para estimar el peso de Play, usar iOS como control: su SEARCH no incluye la App Store.
- **Evidencia**: Visto en 1 cuenta, jul 2026.

### La canibalización App contra Search se prueba, no se asume
- **Tipo**: error de método
- **Por qué**: Exact no tiene prioridad sobre App; ambas entran en la misma subasta. Que puedan competir no prueba que lo hagan.
- **Cómo detectarlo**: tres lentes. IS y rank lost móvil de Search frente al gasto de App; desktop como control, donde App casi no sirve; correlación temporal del diferencial móvil.
- **Qué hacer**: un escalón de gasto de App es experimento natural. La prueba causal es un geo-holdout. Las conversiones de App suelen ser instalaciones, no el KPI.
- **Evidencia**: Visto en 2-3 cuentas, jul-sep 2026.
