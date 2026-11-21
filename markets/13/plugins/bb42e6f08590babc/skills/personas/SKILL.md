---
name: personas
description: Talk to Convosight SCP (Social Consumer Panel) personas, simulated consumers built from real social research, to get a persona's own opinion or reaction to a question, concept, ad, copy or product.
---

Use the SCP tools when the user wants a persona's own opinion, reaction or voice on a question, concept, ad, copy or product.

1. If you don't know which persona the user means, call `list_personas` with the user's message as `question`, then stop. The user picks a persona in the widget, and the widget sends their message itself. The pick reaches you as "Persona widget state" carrying `persona_id` and `session_id` (or `selected_persona_id` if no message was pending).
2. Once a persona is established, send every further message meant for it with `ask_persona`, using that `persona_id` and `session_id`. Pass the user's message exactly as written. Do not rephrase, shorten or improve it.
3. Do not call `list_personas` again unless the user asks to switch persona.
4. Follow-ups that stay on topic go to the same persona (same `persona_id` and `session_id`) until the user switches.
5. Present the persona's answer as the persona's own words. Do not add your own opinion on top of it.
6. If the daily quota is exceeded or sign-in has expired, tell the user plainly and give the reset time if one is returned.

Do not use these tools for general research, analytics or reporting questions, or for factual lookups that don't need a persona's perspective.
