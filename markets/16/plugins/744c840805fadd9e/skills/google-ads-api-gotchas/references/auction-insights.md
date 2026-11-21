# Auction Insights

### Auction Insights no está en la API: se exporta desde Report Editor
- **Tipo**: gotcha de API
- **Por qué**: no hay recurso de la API que devuelva Auction Insights. El dato solo sale de la UI, desde Report Editor.
- **Cómo detectarlo**: no hay recurso GAQL equivalente.
- **Qué hacer**: exportar el informe desde Report Editor y procesar el CSV.
- **Evidencia**: Visto en 4+ cuentas, jun-oct 2026.

### El Report Editor del manager pierde métricas de Auction Insights
- **Tipo**: gotcha de API
- **Por qué**: desde el manager exporta todas las cuentas de golpe, pero solo con impression share, overlap rate y outranking share. Position above y top of page no salen. La dimensión dominio exige la de cuenta.
- **Cómo detectarlo**: columnas que faltan en el export del manager.
- **Qué hacer**: para position above, abrir el informe en cada cuenta. La cuenta la decide el parámetro `ocid` de la URL, no el customer ID.
- **Evidencia**: Visto en 4+ cuentas, oct 2026.

### Exportar Auction Insights con la UI en inglés
- **Tipo**: gotcha de API
- **Por qué**: las cabeceras del CSV cambian con el idioma de la interfaz. Un parser que busca "Display URL domain" falla con un export en otro idioma.
- **Cómo detectarlo**: el parser no encuentra la fila de cabecera.
- **Qué hacer**: fijar `hl=en` o la UI en inglés. El mes llega como "July 2025" y `segments.month` como "2025-07-01": normalizar antes de unir.
- **Evidencia**: Visto en 2-3 cuentas, jun-ago 2026.

### El cruce del export con la API es por nombre de campaña
- **Tipo**: gotcha de API
- **Por qué**: el CSV no trae IDs. Una campaña renombrada entre el export y el análisis se queda sin filas de competidor.
- **Cómo detectarlo**: campañas con gasto y sin filas de Auction Insights.
- **Qué hacer**: sacar export y pull de la API en la misma ventana. Llevar un mapa de renombres por ID.
- **Evidencia**: Visto en 2-3 cuentas, ago-sep 2026.
