# Wazu data model and scope

## Scope is a first-class contract

| User-visible scope | Request representation | Persisted evidence |
|---|---|---|
| Personal | `scope_kind=personal` or the Personal selector | `cohort_id=null` |
| Cohort | Authorized cohort UUID | `cohort_id=<uuid>` |

The Personal selector may be returned as `personal` for routing and display. It is not a cohort UUID. `set_active_cohort("personal")` means the active cohort is persisted as null.

Current ingestion requires a real cohort. Never route a write to Personal until the server explicitly supports personal writes.

## Retrieval envelopes

Search-like responses can include:

- `status`
- `results`
- `truncated`
- `elapsed_ms` or equivalent timing
- `meta`
- `_scope`
- billing or metering information

Treat `_scope` as the authoritative statement of where the request ran. Do not infer scope from tags or an isolated chunk.

An evidence result can carry an item ID, cohort hint, dates, sender or source metadata, tags, score, snippets, and media or content locators. Prefer explicit text or hydrated content over display snippets when the two differ.

## Items, chunks, and media

`get_item` is the canonical hydration step for a result or Hive Map node. `get_item_chunks` exposes the indexed pieces and their provenance when the full item is incomplete or a claim depends on a particular passage.

A chunk's `cohort_id` is a storage hint, not an authorization decision. Authorization is established by the resolved request scope.

Fetch media only when the user needs the underlying document, image, audio, or video. Do not expose raw base64 payloads in the response.

## Hive Map

Hive Map results are navigational evidence: nodes, edges, and relationship metadata help discover adjacent items. Hydrate material nodes with `get_item` before using them as authoritative evidence.

## Ingestion lifecycle

A successful write can have distinct stages:

1. accepted and stored
2. replicated
3. enriched or indexed
4. linked into the graph
5. verified through retrieval

Report only the stages the response or a read-after-write check confirms.
