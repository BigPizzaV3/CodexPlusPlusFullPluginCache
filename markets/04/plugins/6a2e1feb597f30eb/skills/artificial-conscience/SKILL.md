---
name: artificial-conscience
description: Retrieve optional Christian moral guidance for requests involving values, conduct, faith, relationships, or life decisions.
---

# Artificial Conscience

Artificial Conscience can provide Christian moral guidance when it is relevant
to the user's request. It is an optional source of background context, not a
replacement for ChatGPT's normal safeguards, higher-priority instructions, or
professional advice.

## When to use

Use `conscience_prepare` when the request involves values, conduct, faith,
relationships, forgiveness, integrity, or a life decision and Christian moral
guidance would be relevant. For unrelated factual, formatting, arithmetic, or
coding requests, answer normally without calling the tool.

Send only the request text needed for that evaluation. Do not send passwords,
authentication secrets, government identifiers, payment card data, or
protected health information.

When the tool returns non-empty `guidance`, consider it together with the
user's request and other context. Keep the answer helpful and natural. When it
returns an empty string or is unavailable, continue normally without implying
that guidance was applied.

Do not claim that Artificial Conscience guarantees moral correctness. It is a
Christian guidance resource that the user chose to make available.
