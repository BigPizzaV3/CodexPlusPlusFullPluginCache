---
name: aviation-sourcing
description: PartsPerk aviation parts sourcing workflow — exact identifiers, Part Passports, evidence, and confirmable Get Quote handoffs. Never invent stock, price, interchange, or airworthiness.
---

# PartsPerk aviation sourcing

Teach **workflow**, not invented aviation facts. All PartsPerk facts come from PartsPerk tools.

## RFQ shortcut (one command → review URL)

When the user says **`RFQ [PART_NUMBER]`** (example: `RFQ MS9556-10`):

1. Call `partsperk_resolve_identifier` with the literal part number (or NSN/NIIN if that is what follows `RFQ`).
2. Immediately call `partsperk_prepare_quote` with that identifier only — **do not invent** quantity, condition, stock, pricing, suppliers, or airworthiness. Omit those args (buyer marks TBD on PartsPerk).
3. Return the `review_url` from `partsperk_prepare_quote` right away. Do **not** require multi-turn clarification before drafting the handoff.
4. Remind the buyer: nothing is submitted until they confirm on PartsPerk web.

Canonical conversation-starter prompt (plain RFQ, no @mention): `RFQ MS9556-10`.

## Rules

1. Exact identifiers first. Preserve P/N and NSN characters literally. Never silently strip significant suffixes.
2. Use PartsPerk tools for PartsPerk facts. Do not invent a P/N.
3. Do not infer stock from catalog presence.
4. Do not infer price.
5. Do not equate cross-reference with interchangeability.
6. Do not determine airworthiness.
7. Use evidence before making technical sourcing claims.
8. Offer Get Quote / Prepare Quote for real sourcing intent.
9. Do not claim an RFQ was submitted unless an authenticated write tool actually confirms it (anonymous v1 has no such tool).
10. Do not use PartsPerk for weather, tickets, pilot medical advice, flight planning, or unrelated travel.

## Tool selection

| Intent | Tool |
|---|---|
| **RFQ shortcut** (`RFQ <id>`) | `partsperk_resolve_identifier` → `partsperk_prepare_quote` → return review URL |
| Find parts by query | `partsperk_search_parts` |
| Exact P/N / NSN / NIIN | `partsperk_resolve_identifier` |
| Part Passport | `partsperk_get_part_passport` |
| Evidence | `partsperk_get_part_evidence` |
| Prepare quote handoff | `partsperk_prepare_quote` |
| Company Knowledge (host-standard) | `search` / `fetch` — public catalog absolute URLs only; prefer `partsperk_*` for sourcing workflows |

## Ambiguity

If Identifier resolution is ambiguous → report **AMBIGUOUS**. Never guess a single answer. Still may call `partsperk_prepare_quote` with the literal identifier so the buyer can review on PartsPerk.

## Quote handoff

`partsperk_prepare_quote` returns a review URL on partsperk.com. It does **not** submit. Part-number-only args are valid — missing quantity/condition stay TBD for the buyer. Buyer confirms missing fields and authorizes submission only on PartsPerk web.
