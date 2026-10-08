# Retrieval routing

## Choose the smallest sufficient lane

| Intent | Preferred operation |
|---|---|
| Latest, recent, today, newest | `latest_search` |
| Topic, person, tag, phrase | `search` |
| Deep semantic or cross-modal recall | `full_search` |
| Relationships, adjacent evidence, clusters | Hive Map tools |
| Exact item or result hydration | `get_item` |
| Passage-level provenance | `get_item_chunks` |
| Underlying document or media inspection | media retrieval tool |

Do not automatically fall back from an empty `search` to `full_search`. A wider or more expensive lane requires a reason tied to the user's intent.

## Resolve scope before retrieval

Use `list_cohorts` when the user has not identified a scope. If multiple cohort names match, ask the user to choose. Never invent an identifier or infer that the active cohort is correct merely because one exists.

Personal means `cohort_id=null`. A cohort search uses the exact authorized UUID returned by Wazu.

## Paginate intentionally

Start with a bounded result set that can answer the question. Continue only when the response is truncated, the user asks for exhaustive coverage, or the current evidence is insufficient. Preserve server cursors and limits exactly.

## Hydrate before claiming

Search snippets and map nodes are discovery surfaces. Hydrate the most relevant items, inspect chunks when needed, and attach dates and locators to important claims.

Separate:

- facts directly supported by Wazu evidence
- synthesis or inference across items
- evidence not found or not accessible

## Fail accurately

An empty result is not an error. Authorization, entitlement, metering, and transport failures are errors and must not be rewritten as “no evidence found.”
