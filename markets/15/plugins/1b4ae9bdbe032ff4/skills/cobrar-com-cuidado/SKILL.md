---
name: cobrar-com-cuidado
description: Help the user follow up on money still to receive and record payments. Use when the user asks who owes them, what is overdue, wants to remind a client to pay, or says a client paid.
---

1. Call `get_receivables` with `today`. Present clients with an open balance, overdue first, showing amounts per currency (never add different currencies together).
2. To remind a client, call `get_client` to get the message language and the user's saved templates, then draft a short, friendly message with the exact amount and what it refers to. Do not send it; the user sends it themselves.
3. When the user says they received money, find the item (appointment or period charge) in `get_receivables`, then call `record_payment` WITHOUT `confirmation_id` to show the preview (balance before and after). Only after the user agrees, call it again with `confirmation_id`.
4. If the amount is higher than the balance, point it out before confirming.
5. Combinado never moves money; it only records what the user received.
