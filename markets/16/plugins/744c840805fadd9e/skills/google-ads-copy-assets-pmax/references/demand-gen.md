# Demand Gen

### Los custom segments de keywords solo actúan como intención en propiedades propias
- **Tipo**: gotcha de plataforma
- **Por qué**: con `ALL_CHANNELS`, parte del gasto reinterpreta las keywords como intereses, sin aviso en el reporting.
- **Cómo detectarlo**: `ad_group.demand_gen_ad_group_settings.channel_controls`.
- **Qué hacer**: `channel_strategy = ALL_OWNED_AND_OPERATED_CHANNELS` si el segmento es de búsqueda.
- **Evidencia**: Visto en 1 cuenta, jul 2026.

### Los lookalikes de DG son señal, no restricción, desde marzo de 2026
- **Tipo**: gotcha de plataforma
- **Por qué**: el sistema puede servir fuera del pool. El opt-out es por formulario; no hay campo de API.
- **Cómo detectarlo**: n/a.
- **Qué hacer**: no usar un lookalike como control de un test.
- **Evidencia**: Visto en 1 cuenta, jul 2026.

### Al crear una DG, la categoría de conversión de App sale biddable
- **Tipo**: gotcha de API
- **Por qué**: `DEFAULT / APP` viene biddable por defecto y mete conversiones de la app en la puja.
- **Cómo detectarlo**: `campaign_conversion_goal` con `biddable = TRUE` tras crear.
- **Qué hacer**: apagarlo explícitamente. El resource name usa nombres del enum: `{campaign_id}~PURCHASE~WEBSITE`.
- **Evidencia**: Visto en 1 cuenta, jul 2026.

### Las exclusiones de contenido e inventario de DG no se fijan por API
- **Tipo**: gotcha de API
- **Por qué**: los 25 `ContentLabelType` se rechazan (`INVALID_EXCLUDED_CATEGORY`). Sí se admiten negativas de canal, vídeo, placement y categoría de app a nivel campaña.
- **Cómo detectarlo**: `validate_only` con `MutateCampaignCriteriaRequest`.
- **Qué hacer**: content exclusions en la UI. Las exclusiones de canal no contienen el inventario: reaparece vídeo a vídeo en cientos de miles de placements.
- **Evidencia**: Visto en 1 cuenta, jul-ago 2026.

### Antes de proponer DG de prospecting, mira el histórico de la cuenta
- **Tipo**: regla de decisión
- **Por qué**: en varias cuentas el prospecting quedó muy por debajo del umbral. Solo el retargeting lo pasó. La receta "custom segment de convertidores más lookalike más in-market" ya se había probado y fallado.
- **Cómo detectarlo**: histórico completo de `DEMAND_GEN` y Discovery con la conversión de negocio, por ad group.
- **Qué hacer**: si el prospecting falló, cambiar la señal de puja o la landing antes de repetirlo. Retargeting es el único bloque defendible por last click.
- **Evidencia**: Visto en 4+ cuentas, 2024-2026.
