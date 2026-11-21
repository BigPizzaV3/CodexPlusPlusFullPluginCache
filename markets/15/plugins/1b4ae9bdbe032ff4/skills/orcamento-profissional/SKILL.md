---
name: orcamento-profissional
description: Prepare a clear, professional quote (estimate) in Combinado for a service the user describes. Use when the user asks to quote, estimate, budget or "fazer um orçamento" for a client or a new contact.
---

Use this skill to turn the user's description of a job into a draft quote in Combinado.

1. Identify the client. If the user names one, call `list_clients` with the name and use the matching id. If there is no match, use the name (and phone, if given) as a new contact. Never invent contact details.
2. Collect what the quote needs: the service in a few words (title), what is included, the price and how it is charged (fixed total, per hour, day, week or month). If the price is missing, ask; never guess a price.
3. When the job has several parts with their own prices, use `items` (fixed total). Otherwise use `amount` with `price_mode`.
4. Put conditions the client should see (payment terms, materials, travel, validity) in `conditions`, and private remarks in `notes`.
5. Call `create_quote_draft`. It creates a DRAFT only; nothing is sent to the client.
6. Reply with a short summary (service, total, validity) and remind the user they can review and send it from the Combinado app. Offer to draft the message to the client in the client's language (`get_client` returns it).

Do not promise dates, discounts or conditions the user did not state.
