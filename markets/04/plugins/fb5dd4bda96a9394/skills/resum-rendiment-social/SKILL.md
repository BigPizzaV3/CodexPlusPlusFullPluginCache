---
name: resum-rendiment-social
description: Úsala cuando el usuario pida un resumen del rendimiento en redes sociales (alcance, interacciones, mejores publicaciones) de una o varias marcas en un periodo.
---

Resume el rendimiento social de forma útil para reporting de agencia. Flujo de solo lectura.

1. Llama a `list_brands`. Si el usuario no especifica marca, pregunta si quiere una marca concreta o el conjunto de la organización.
2. Para cada marca relevante, llama a `social_metrics_summary` con `brand_id` para alcance, interacciones y seguidores por plataforma en el periodo.
3. Llama a `social_post_metrics` para identificar las publicaciones con mejor rendimiento (engagement, alcance, guardados).
4. Redacta el resumen:
   - Titular con las cifras clave del periodo (alcance total, interacciones, variación vs. periodo anterior si está disponible).
   - Desglose por plataforma (Instagram, Facebook, LinkedIn, TikTok).
   - Top 3 publicaciones y por qué funcionaron.
   - 2–3 recomendaciones accionables para el próximo periodo.

Reglas:
- Haz las llamadas MCP de una en una (si hay varias marcas, secuencialmente).
- No inventes métricas que la tool no devuelva; indícalo si faltan datos.
