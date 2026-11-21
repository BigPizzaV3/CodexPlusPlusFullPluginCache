# Match types y close variants

### La paridad de match types se mide por `(texto, match_type)`
- **Tipo**: regla de decisión
- **Por qué**: una BROAD pausada en origen con solo EXACT en destino es un hueco real de cobertura. Comparar solo por texto lo esconde.
- **Cómo detectarlo**: cruzar por `(lower(text), match_type)` y reportar aparte "texto existe pero falta el match type".
- **Qué hacer**: preservar el match type del origen al consolidar o migrar.
- **Evidencia**: Visto en 2-3 cuentas, 2026.

### Antes de crear la EXACT de una BROAD que convierte, comprobar que el texto se busca tal cual
- **Tipo**: error de método
- **Por qué**: una BROAD convierte por expansión. Su texto en EXACT solo captura la query literal, que a menudo no tiene volumen.
- **Cómo detectarlo**: el texto tiene que aparecer como query literal en `search_term_view`. En una cuenta, las BROAD mayores de una lista de altas no habían convertido nunca con su texto literal. Una negativa EXACT del mismo texto en el ad group confirma que la conversión era expansión.
- **Qué hacer**: filtrar por existencia como query literal antes del alta. En cuentas maduras, la EXACT casi siempre existe ya pausada en el mismo ad group: averiguar por qué antes de reactivar.
- **Evidencia**: Visto en 2-3 cuentas, ago 2026.

### "Limitada por volumen de búsquedas" no es señal de match type
- **Tipo**: gotcha de plataforma
- **Por qué**: `SEARCH_VOLUME_LIMITED` sale en toda campaña cuyo pool no absorbe el budget, también en Brand y en campañas con mayoría de gasto en broad.
- **Cómo detectarlo**: la recomendación `USE_BROAD_MATCH_KEYWORD` estimaba +25% clics, +31% coste y 0 conversiones más. Pedir `recommendation.impact` entero.
- **Qué hacer**: antes de añadir broad, mirar gasto por match type, rank lost contra budget lost, y exact/phrase que convierten sin broad en su ad group. Si el rank lost es alto y el budget lost cero, el volumen se compra con el target.
- **Evidencia**: Visto en 1 cuenta, oct 2026.
