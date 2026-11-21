---
name: build-tam-list
description: "Find target companies and build B2B prospect lists by location, industry and custom customer criteria. Use for new company discovery or TAM sourcing, across the user’s chosen markets and company segments (Firmenrecherche, Zielkundenliste). Reading an existing list or explaining prospecting concepts does not require sourcing."
---

# Find target companies in Compelling

Source companies that match the user's customer criteria into a fresh Compelling list.

For DACH requests, resolve DACH to Germany, Austria and Switzerland. Research can cover
Mittelstand, industrial companies, consultancies and IT service providers; preserve the user's
actual geography and segment, including markets outside DACH. Keep custom criteria such as
SAP usage, ISO 13485 certification or hiring activity explicit and distinguish required
criteria from optional signals. Do not treat missing evidence as a confirmed match.

## Workflow

1. **Confirm the workspace** with `compelling_get_workspace` and tell the user which workspace you are operating in before touching data.
2. **Mint a fresh list** with `compelling_create_list` — never source into an existing list unless the user explicitly asks. Share the returned link so the user can open the list in Compelling.
3. **Clarify the TAM definition** before spending credits. You need:
   - a natural-language `search_prompt` (e.g. "Machinery manufacturers in Germany, 100-500 employees, that use SAP")
   - at least one per-company match `criteria` (each becomes a checkable column, e.g. "has a mobile app", "sells to enterprises")
   - a `target_size` (how many fully-matched companies the user wants, max 500)
4. **Offer a cost preview** with `compelling_estimate_credits(action='find_companies')` — sourcing costs 5 credits + criteria cost per company. Ask whether the user wants the estimate; do not price every run automatically.
5. **Start sourcing** with `compelling_find_companies`. It runs asynchronously.
6. **Wait server-side, don't busy-poll**: pass `wait_seconds` on the call, or check `compelling_find_companies_status` with `wait_seconds` up to 60 — one long-poll call instead of sleeping and retrying.
7. **Read results** with `compelling_read_list(record_type='accounts')` — that is ground truth, counters in status responses settle a few seconds late.

## Pitfalls

- `prompt_ambiguous` status means the search prompt was too broad — refine it with the user and restart rather than retrying unchanged.
- Do not stack unrelated segments into one list; one TAM definition per list keeps criteria columns meaningful.
- After sourcing, the natural next steps are contacts and enrichment — see the `enrich-contacts` skill — and scoring, see `rank-by-icp`.

## Scope and authorization

An estimate-only request does not authorize creating a list or starting sourcing. Stay within
the requested company count, criteria and authorized budget. Reuse existing authorization
for the same scope; do not repeat paid runs solely to improve an answer.
