# Lag y maduración

### `conversion_lag_bucket` mide clic a conversión, no el retraso de importación
- **Tipo**: gotcha de API
- **Por qué**: las conversiones importadas (GA4, Firebase, postbacks iOS, offline) llegan tarde pero se fechan al clic. El segmento no ve ese retraso.
- **Cómo detectarlo**: releer una ventana pasada y comparar con la lectura original, con el coste idéntico. Un día leído a 1 día subió 27-50%; una semana leída el lunes, +13% a +25%.
- **Qué hacer**: no publicar el día más reciente como final. Comparar fresco contra fresco (foto guardada) o a misma edad.
- **Evidencia**: Visto en 4+ cuentas, jun-oct 2026.
