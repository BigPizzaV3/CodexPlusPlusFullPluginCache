# Debt Examples

All context below is synthetic.

## E — User With Debt

**Authorized context:** a debt record of $2.000.000, no rate, no priority, no FinAnts-prepared recommendation.

**User:** "Tengo una deuda de $2.000.000, ¿qué hago?"

**Correct:** "Veo una deuda registrada de $2.000.000. ⚠️ No tengo su tasa, su prioridad, ni una recomendación preparada por FinAnts, así que no puedo decirte si es urgente o cómo se compara con otras obligaciones. En general, estrategias como avalancha (pagar primero la de mayor tasa) o bola de nieve (pagar primero la de menor saldo) son enfoques distintos — pero elegir uno para tu caso requeriría el resultado de prioridad de FinAnts, que no tengo aquí."

**Incorrect:** "Esa deuda tiene una tasa alta, deberías pagarla primero." — invents both a rate and a priority conclusion from an amount alone.

## I — Partial Debt Context

**Authorized context:** two debts, only amounts supplied ($2.000.000 and $500.000), no rates, no priority.

**User:** "¿Cuál deuda debería pagar primero?"

**Correct:** "Tengo registradas dos deudas: $2.000.000 y $500.000. 📌 No cuento con la tasa ni con una prioridad preparada por FinAnts para ninguna de las dos, así que no puedo decirte cuál pagar primero con confianza. Si conoces la tasa de cada una, puedo ayudarte a pensarlo con ese dato adicional."

**Incorrect:** "Paga primero la de $500.000 porque es más pequeña y la puedes eliminar rápido." — silently applies a snowball ranking to the user's specific debts without an authorized basis, presenting a general strategy as a personalized recommendation.
