# Objetivos de conversión

### Un goal estándar puede depender de una sola acción primaria; si se rompe, la campaña puja a nada
- **Tipo**: gotcha de API
- **Por qué**: dentro de una categoría, solo las acciones con `primary_for_goal = True` cuentan para el goal estándar. Las demás solo se alcanzan por custom goal.
- **Cómo detectarlo**: `SELECT conversion_action.category, conversion_action.primary_for_goal, conversion_action.name FROM conversion_action`, y volumen semanal de la primaria. En un caso pasó a 0 y se quedó a la mitad.
- **Qué hacer**: mover las campañas afectadas a un custom goal con una acción que siga registrando.
- **Evidencia**: Visto en 1 cuenta, ago 2026.

### Las acciones secundarias solo aparecen en `all_conversions`
- **Tipo**: gotcha de API
- **Por qué**: `metrics.conversions` cuenta lo biddable de cada campaña. Una acción secundaria, o que no es objetivo de esa campaña, sale 0 ahí.
- **Cómo detectarlo**: pedir `metrics.conversions` y `metrics.all_conversions` segmentados por `segments.conversion_action_name`. `metrics.cost_micros` no se puede pedir con ese segmento: dos consultas y join.
- **Qué hacer**: antes de culpar al tag por una landing o campaña a 0,00, comparar las dos métricas. Si la brecha es entera, es objetivo de campaña.
- **Evidencia**: Visto en 2-3 cuentas, ago 2026.

### Dos acciones para el mismo evento: duplicado paralelo o relevo con definición distinta
- **Tipo**: gotcha de API
- **Por qué**: una acción legacy puede correr en paralelo con la de GA4 con conteos casi iguales. Otro caso: dos acciones con el mismo nombre que no se solapan y miden distinto.
- **Cómo detectarlo**: conteo mensual por `conversion_action.id`. Si conviven todo el periodo, es duplicado. Si los periodos son disjuntos, es relevo y el YoY no es comparable.
- **Qué hacer**: filtrar por ID, nunca por nombre laxo. Avisar en todo YoY que cruce un relevo (un -64% aparente era cambio de definición).
- **Evidencia**: Visto en 2-3 cuentas, may-jun 2026.

### En cuentas con dos IDs de conversión en el mismo sitio, comprobar a cuál apunta cada tag
- **Tipo**: gotcha de API
- **Por qué**: las acciones cross-account del MCC registran 0 en una cuenta con tracking propio. Enhanced Conversions puede estar encendido en una cuenta y enviar el dato al otro ID.
- **Cómo detectarlo**: `customer.conversion_tracking_setting.cross_account_conversion_tracking_id`. En el contenedor, el conversion ID del tag de datos de usuario y las etiquetas de cada tag de conversión.
- **Qué hacer**: alinear EC con el ID de la cuenta que puja. Buscar etiquetas placeholder: pueden disparar en producción sin registrar nada.
- **Evidencia**: Visto en 1 cuenta, ago 2026.
