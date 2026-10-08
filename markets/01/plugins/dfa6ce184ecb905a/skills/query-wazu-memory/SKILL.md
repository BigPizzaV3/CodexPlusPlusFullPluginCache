---
name: query-wazu-memory
description: Search, inspect, compare, trace, summarize, or map grounded evidence in the user's authorized Wazu personal or cohort memory. Use when a user asks what Wazu knows, requests recent or topic-based recall, needs full document or media evidence, wants related-item discovery through Hive Map, or asks for an answer grounded in Wazu data.
---

# Query Wazu Memory

Use Wazu as the evidence system of record. Keep scope explicit, choose the narrowest retrieval lane that matches the request, and hydrate evidence before making authoritative claims.

## Load the Wazu contract

- Read [references/wazu-data-model-and-scope.md](references/wazu-data-model-and-scope.md).
- Read [references/retrieval-routing.md](references/retrieval-routing.md).

## Execute the workflow

1. Resolve scope.
   - Call `account_context` first when the connected actor or active scope is unknown.
   - Call `list_cohorts` when scope is missing or ambiguous.
   - Personal memory uses `scope_kind=personal`; it never uses a cohort UUID.
   - Cohort memory uses an authorized cohort UUID returned by Wazu.
   - Report the returned `_scope`, especially when the request depends on the active cohort.
2. Choose the smallest sufficient retrieval lane.
   - Use `latest_search` for recent evidence.
   - Use `search` for a topic, person, tag, or phrase.
   - Use `full_search` only when deep vector or cross-modal recall is necessary.
   - Use Hive Map tools for relationships and adjacent evidence.
   - Use `get_item` for an exact item or to hydrate a search or map result.
3. Hydrate evidence.
   - Call `get_item` before treating a result as authoritative.
   - Call `get_item_chunks` when the hydrated item is incomplete or chunk provenance matters.
   - Fetch media only when the user needs to inspect it.
4. Answer from the returned evidence.
   - Separate facts, reasonable inference, and missing evidence.
   - State the scope searched.
   - Preserve useful item IDs, dates, and source locators.
   - Summarize billing or metering status without exposing private internal identifiers.

## Guardrails

- Never invent a scope, cohort, item, sender, date, tag, or source.
- Never infer authorization from a chunk's `cohort_id`; authorization comes from the resolved request scope.
- Treat tags as classification, not proof of source.
- Treat an empty result as a valid result, not permission to widen scope silently.
- Do not silently switch retrieval lanes or fall back from personal to cohort scope.
- Do not call write or ingestion tools from this skill.
- Stop and report authorization, metering, or transport failures accurately.
