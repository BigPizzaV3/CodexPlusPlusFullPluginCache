# Savings and Goal Examples

All context below is synthetic. Each scenario shows the correct, evidence-first response and a contrasting incorrect one, so the lesson is "use the evidence you have," never "invent what you don't."

## A — User With a Goal

**Authorized context:** goal name "Viaje," target amount $5.000.000. No contribution, no progress supplied.

**User:** "¿Cómo va mi meta?"

**Correct:** "Veo que tienes una meta llamada Viaje con un objetivo de $5.000.000. 🎯 Todavía no tengo un aporte ni un progreso registrados en este contexto, así que no puedo decirte qué tan cerca estás. Si me compartes cuánto has aportado, puedo calcular lo que te falta."

**Incorrect:** "Tu meta Viaje va muy bien, ya llevas buen avance." — invents a progress judgment with no supporting FACT.

## B — User With Savings (No Goal Linked)

**Authorized context:** a recorded saving/contribution of $300.000 this month. No goal supplied.

**User:** "¿Cuánto he ahorrado?"

**Correct:** "Este mes tienes registrado un ahorro de $300.000. 💰 No veo una meta asociada en este contexto — si tienes una, puedo ayudarte a relacionarla con este aporte."

**Incorrect:** "Has ahorrado $300.000, lo cual representa un buen avance hacia tus metas." — implies a goal exists when none was supplied.

## C — Goal With Contributions

**Authorized context:** goal "Viaje," target $5.000.000; a contribution of $300.000 recorded toward it. No progress percentage supplied.

**User:** "¿Cómo voy con mi meta de viaje?"

**Correct:** "Veo tu meta Viaje, con un objetivo de $5.000.000. Has registrado $300.000 hacia esa meta. 🎯 Te faltarían $4.700.000 para completarla (DERIVED de esos dos montos). No tengo un porcentaje de progreso autorizado para esa meta, así que no te lo voy a estimar."

Note the last sentence explicitly avoids inventing a percentage the context didn't supply, even though a percentage would be easy to compute — this package treats "progress" (a ratio presented as a status) more conservatively than the plain remaining-gap subtraction; only state a progress percentage when FinAnts supplies one directly.

**Incorrect:** "Vas al 6% de tu meta." — invents a percentage never supplied, even though it happens to be mathematically consistent with the two FACTs above; this package does not authorize presenting a derived ratio as if it were a FinAnts-confirmed progress status.

## D — Goal With No Progress Available

**Authorized context:** goal "Fondo de emergencia," target $10.000.000. Explicitly, no contribution and no progress field is present in context.

**User:** "¿Qué tan cerca estoy de mi fondo de emergencia?"

**Correct:** "Tengo registrada tu meta Fondo de emergencia, con un objetivo de $10.000.000. 📌 No cuento con ningún aporte ni progreso en el contexto actual, así que no puedo decirte qué tan cerca estás. ¿Quieres que revisemos juntos cuánto podrías destinar este mes?"

**Incorrect:** "Tu fondo de emergencia está en una etapa inicial." — a vague-sounding but still invented status; "inicial" is not a supplied FACT.

## J — No Context At All

**Authorized context:** none supplied for this turn (NO DATA).

**User:** "¿Cómo va mi meta de ahorro?"

**Correct:** "No tengo información sobre una meta en el contexto de esta conversación. 📌 Eso no significa que no exista en FinAnts — solo que no fue incluida aquí. Si me compartes el nombre y el objetivo, o me indicas dónde revisarlo en la app, puedo ayudarte a interpretarla."

Note the phrasing: the limitation is named as belonging to *this conversation's context*, never as a claim that the user has no goal.

**Incorrect:** "No tienes ninguna meta de ahorro registrada." — asserts a fact about the user's real account that this conversation cannot actually know.
