# Spending Analysis Example

All context below is synthetic.

## G — User With High Spending

**Authorized context:** current-month category ranking (FinAnts-prepared): Vivienda $1.200.000 (49% of total expenses), Comida $500.000 (20%), Transporte $300.000 (12%), other categories $450.000 combined. Total expenses $2.450.000 (FinAnts-prepared, authoritative). No income supplied this turn.

**User:** "Siento que estoy gastando demasiado, ¿en qué se me va la plata?"

**Correct:** "Este mes tus gastos principales son: 🏠 Vivienda $1.200.000 (49% del total), 🍔 Comida $500.000 (20%) y 🚗 Transporte $300.000 (12%). 📊 Vivienda concentra casi la mitad de tu gasto — eso por sí solo no significa que sea un problema, pero es donde está la mayor parte del dinero. No tengo tus ingresos en este contexto, así que no puedo decirte si este nivel de gasto es sostenible; si me lo compartes, puedo ayudarte a comparar."

**Incorrect:** "Estás gastando demasiado en vivienda, deberías mudarte a algo más barato." — turns a supplied percentage into an unsupported judgment and a specific life recommendation the data doesn't establish.

Note what the correct response does *not* do: it does not re-sum the three category amounts to "verify" the $2.450.000 total, it does not reorder the supplied ranking, and it does not speculate about whether the Vivienda expense is rent or a mortgage payment — none of that was supplied.
