# Duplicar y crear campañas

### Al crear una campaña, copia los 21 settings de una referencia viva y verifica
- **Tipo**: regla de decisión
- **Por qué**: los defaults de la API difieren de la cuenta. Un `geo_target_type` o un objetivo de conversión distinto hace que la campaña optimice distinto sin error.
- **Cómo detectarlo**: diff setting a setting entre la nueva y la referencia tras crear.
- **Qué hacer**: crear en PAUSED. Comparar puja, budget, redes, ubicaciones con su tipo positivo y negativo, idiomas, horario, dispositivos, objetivos, tracking en los tres niveles, listas y exclusiones. Activar solo sin diferencias.
- **Evidencia**: Visto en 2-3 cuentas, mar 2026.

### Las brand lists no se admiten en una campaña Search solo exact
- **Tipo**: gotcha de API
- **Por qué**: solo se admiten con targeting exclusivo, campañas broad para inclusión o PMax.
- **Cómo detectarlo**: error al replicar la exclusión.
- **Qué hacer**: si el origen tiene broad y la réplica es exact, cubrir la marca con negativas.
- **Evidencia**: Visto en 1 cuenta, ago 2026.

### Clonar ad groups pierde los criterios demográficos si no se piden en el SELECT
- **Tipo**: gotcha de API
- **Por qué**: `AGE_RANGE`, `GENDER`, `INCOME_RANGE` y `PARENTAL_STATUS` llegan con tipo pero sin valor. El clon sale sin segmentación y sin error.
- **Cómo detectarlo**: pedir `ad_group_criterion.age_range.type` y equivalentes.
- **Qué hacer**: pedirlos explícitos. Keywords de salud con audiencias dan `HEALTH_IN_PERSONALIZED_ADS`: reenviar con `exempt_policy_violation_keys`.
- **Evidencia**: Visto en 1 cuenta, ago 2026.
