---
name: informe-seo-mensual
description: Úsala cuando el usuario pida un informe SEO mensual, la evolución de posiciones de keywords o oportunidades de Search Console para una marca.
---

Genera un informe SEO claro y accionable para una marca. Todo el flujo es de solo lectura.

1. Llama a `list_brands` y confirma la marca (si no está clara).
2. Llama a `keywords_tracked_list` con `brand_id` para obtener las keywords en seguimiento.
3. Llama a `keywords_snapshots` para la evolución de posiciones en el periodo (por defecto el último mes). Identifica subidas, bajadas y keywords estancadas.
4. Llama a `gsc_top_queries` para las consultas con más impresiones/clics y su posición y CTR.
5. Llama a `keywords_gsc_opportunities` para detectar keywords en posiciones 5–20 con alto potencial de mejora.
6. Redacta el informe con estas secciones:
   - Resumen ejecutivo (2–3 frases: tendencia general del mes).
   - Top movimientos: keywords que más suben y que más bajan, con posición anterior → actual.
   - Rendimiento en Search Console: mejores consultas por clics e impresiones.
   - Oportunidades: keywords a un empujón del top 10 y acciones concretas (contenido, enlazado interno, intención).
   - Próximos pasos priorizados.

Reglas:
- Haz las llamadas MCP de una en una.
- Sé concreto con los números (posiciones, clics, CTR) y no inventes datos: si una tool no devuelve algo, dilo.
