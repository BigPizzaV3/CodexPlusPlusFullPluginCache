---
name: search
description: Find hotel day passes on Daypass.com (pool, beach club, spa day, all-inclusive day) with live availability and prices, and give the booking links.
---

Use the `buscar_daypasses` tool from the Daypass.com MCP server whenever someone wants to spend a day
at a hotel, resort, beach club or spa without staying overnight ("day pass", "pase de día", "pasadía").

1. You need a place. If the person did not say where, ask for a city or area before searching.
2. Resolve relative dates yourself ("this Saturday") and send `fecha` as YYYY-MM-DD. If there is no
   date, the tool searches tomorrow and says so: tell the person.
3. Send only the filters the person asked for: every service and vibe must be met by all results.
   Budgets: `precio_maximo` is per person, `presupuesto_total` is for the whole group; never convert
   currencies yourself, send the currency in `moneda_precio`.
4. If the tool says the destination is ambiguous or not found, ask the person; do not guess.
5. Recommend the best two or three options for what they asked and always include each booking link.
   Booking and payment happen on daypass.com.
