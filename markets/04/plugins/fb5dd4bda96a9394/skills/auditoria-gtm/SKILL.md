---
name: auditoria-gtm
description: Úsala cuando el usuario quiera auditar la salud del contenedor de Google Tag Manager de una marca (etiquetas, GA4, píxeles, consent, problemas).
---

Audita el contenedor de Google Tag Manager de una marca y explica los hallazgos en lenguaje claro. Flujo de solo lectura.

1. Llama a `list_brands` y confirma la marca.
2. Llama a `gtm_list_containers` con `brand_id` y localiza el contenedor.
3. Llama a `gtm_container_overview` para el resumen (versión publicada, número de etiquetas/triggers/variables).
4. Llama a `gtm_audit` para los health checks (etiquetas presentes/faltantes, GA4, píxeles, etiquetas en pausa, Consent Mode, server-side).
5. Redacta la auditoría:
   - Estado general (semáforo: correcto / avisos / fallos).
   - Qué está bien (GA4, píxeles de conversión, etc.).
   - Avisos y fallos, cada uno con qué es, por qué importa y cómo arreglarlo.
   - Recomendaciones priorizadas (empezando por lo que más afecta a medición/privacidad).

Reglas:
- Haz las llamadas MCP de una en una.
- Traduce el detalle técnico a acciones concretas; no te limites a listar el JSON.
