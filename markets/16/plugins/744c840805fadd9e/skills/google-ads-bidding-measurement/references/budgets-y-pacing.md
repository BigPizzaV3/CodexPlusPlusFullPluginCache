# Budgets y pacing

### Las reglas automáticas multiplicativas de budget erosionan la base cada ciclo
- **Tipo**: gotcha de API
- **Por qué**: ×0,80 el sábado y ×1,20 el lunes dejan ×0,96. La base pierde el 4% cada fin de semana, ~15% al mes.
- **Cómo detectarlo**: `change_event.client_type = 'GOOGLE_ADS_AUTOMATED_RULE'` con `user_email = 'Bulk Actions'`.
- **Qué hacer**: usar pares inversos exactos (×0,80 y ×1,25) o fijar importes. Al leer un budget, saber en qué punto del ciclo está.
- **Evidencia**: Visto en 1 cuenta, sep 2026.

### Un Ads Script puede revertir en una hora cualquier cambio de budget hecho por API
- **Tipo**: gotcha de API
- **Por qué**: un script horario reescribe budgets. En `change_event`, `user_email` muestra el correo del dueño del script, así que parece un cambio manual.
- **Cómo detectarlo**: `change_event.client_type = 'GOOGLE_ADS_SCRIPTS'`. Los scripts no se leen ni se editan por API.
- **Qué hacer**: atribuir cambios por `client_type`, no por correo. Pausar el script antes de aplicar un reparto. Si no toca `campaign.status`, pausar sí frena.
- **Evidencia**: Visto en 1 cuenta, ago 2026.

### Fin de semana: el CPC y la CVR caen en la misma proporción
- **Tipo**: regla de decisión
- **Por qué**: coste por conversión = CPC / CVR. Si los dos caen ~13%, el fin de semana sale a paridad o más barato.
- **Cómo detectarlo**: índice intra-semana con IC95 por ventana de 13, 26 y 52 semanas. Excluir App: no produce la conversión web y gasta plano.
- **Qué hacer**: decidir recortes de fin de semana por calidad posterior del lead, no por CPL de plataforma.
- **Evidencia**: Visto en 2-3 cuentas, jul-ago 2026.

### El coste intradía es un suelo
- **Tipo**: gotcha de API
- **Por qué**: Google reporta el coste con retraso y la hora en curso llega a la mitad.
- **Cómo detectarlo**: `SELECT segments.hour, metrics.cost_micros FROM customer WHERE segments.date = 'YYYY-MM-DD'`. `segments.date` no admite `IN`: una fecha por consulta.
- **Qué hacer**: proyectar el día con el acumulado a la misma hora del mismo día de la semana anterior. El viernes no corre a la media de laborables (~0,84 del jueves en un caso).
- **Evidencia**: Visto en 1 cuenta, sep 2026.

### La moneda de la cuenta no se deduce del mercado
- **Tipo**: gotcha de API
- **Por qué**: una cuenta de un mercado puede reportar en la moneda de otro. Los targets y KPIs del cliente pueden estar en otra moneda.
- **Cómo detectarlo**: `SELECT customer.currency_code FROM customer`. Validar contra una fuente externa en moneda conocida: si cuadra al céntimo, misma moneda.
- **Qué hacer**: pedir al cliente el target en la moneda de la cuenta. Un 11% de diferencia decidía si la cuenta estaba en objetivo.
- **Evidencia**: Visto en 1 cuenta, ago 2026.

### El recargo por servicios digitales va sobre el gasto de plataforma
- **Tipo**: gotcha de API
- **Por qué**: Google añade un recargo jurisdiccional que depende del país. El coste facturado es gasto × (1 + tasa).
- **Cómo detectarlo**: consultar la tasa vigente de cada país en la ayuda de Google Ads (recargos por servicios digitales) y compararla con la factura.
- **Qué hacer**: pacear budgets en coste facturado si el presupuesto del cliente lo incluye. Verificar la tasa antes de cada ajuste.
- **Evidencia**: Visto en 2-3 cuentas, jul 2026.
