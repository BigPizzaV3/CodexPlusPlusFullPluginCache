---
name: track-ribele-campaign
description: Consulta y analiza el estado, los resultados agregados y la evolución temporal de campañas propias de Ribele sin exponer datos personales.
---

# Seguir una campaña de Ribele

Sigue el periodo y el objetivo analítico que pida el usuario; si son ambiguos y cambian materialmente el resultado, acláralos antes de concluir.

## Flujo

1. Localiza la campaña propia con `list_my_campaigns`. Usa `search` y recorre `next_offset` cuando haya más resultados; no supongas que la primera página contiene todas las campañas.
2. Usa `get_campaign` para contextualizar el estado, el objetivo, las fechas, las imágenes y la configuración de la recompensa.
3. Usa `get_campaign_metrics` para totales y evolución diaria. Si el usuario no concreta periodo, usa los últimos 30 días; para comparaciones, consulta intervalos equivalentes por separado. Cada intervalo inclusivo puede abarcar como máximo 366 días.
4. Distingue claramente los totales históricos de los campos prefijados con `period_`. No sumes visitantes únicos diarios para calcular visitantes únicos del periodo.
5. Explica tendencias y ratios con los datos devueltos. Si faltan datos o el periodo es demasiado corto, dilo; no inventes causas, atribución ni objetivos.

## Privacidad y límites

- Las ventas, ingresos y mecenas completados son métricas históricas de solo lectura y cuentan únicamente aportaciones con estado `completed`; este plugin no inicia ninguna venta.
- Informa únicamente de agregados. No solicites ni reveles nombres, correos, direcciones, datos de pago ni otra información personal de mecenas.
- Este flujo es de lectura. No modifiques la campaña salvo que el usuario lo pida expresamente; en ese caso aplica el flujo de preparación y la restricción de estado `draft`.
