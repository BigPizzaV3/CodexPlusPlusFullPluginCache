# Structured Query Core

Use this reference whenever a workflow calls `cb_search_query`.

## Resolve the contract

For each search:

1. Resolve every predicate and order field once per session. Prefer one `cb_reference('entities/<entity>/fields')` call when it exposes the required field contracts.
2. Call `cb_reference('entities/<entity>/fields/<field_id>')` only for a predicate or order field whose operator, enum, identifier form, or value shape was not exposed by the collection-level response.
3. Track successfully completed reference paths and never call the same path twice in one session.
4. Do not call `cb_reference` for projection-only output fields.
5. Copy the returned `operator_id`, enum spelling, identifier form, and value shape.
6. Treat examples in this skill as patterns, never as a substitute for the live field detail.

When a bounded workflow is nearing its call cap, resolve only the fields required for the next valid query. Optional demonstration defaults and enrichment must not prevent the search from running or the response from being rendered.

Field catalogs help discover candidate fields. Field-detail responses authorize their use.

## Build the query

- Use `predicates` for flat AND filters.
- Use `query` only when related-entity subqueries are required; never send `query` and `predicates` together.
- Request `field_ids` explicitly.
- Use absolute `YYYY-MM-DD` dates calculated from the current date.
- Use USD integer values for money predicates when confirmed by the live field detail.
- Resolve category and location identifiers with `cb_entity_autocomplete`; use returned permalinks rather than display labels.
- Remember that multiple values inside an `includes` or text `contains` predicate typically broaden that field. Confirm exact semantics in the field detail.

## Pagination and completeness

The default row limit is not a complete dataset. When the answer depends on totals, medians, trends, membership reconciliation, or a complete universe:

1. Set an explicit limit.
2. Compare the returned `count` with rows received.
3. If more rows remain, pass the last result UUID as `after_id`.
4. Continue until all rows are retrieved or the user explicitly approves sampling.
5. Deduplicate by entity UUID before calculating.

For exploratory discovery, a stated sample is acceptable. Never present a sampled aggregation as complete.

## URLs

The top-level `url` belongs to the entity collection searched. For a `funding_rounds` search it is a round URL, not a company URL. Before rendering a company table, batch-search `organizations` using the funded-organization permalinks and map each organization UUID to its returned profile URL.

## Empty and error responses

For zero results, say: “No records matched the stated filters.” Audit one constraint at a time, beginning with resolved identifier values, then date, stage, geography, category or text, and money boundaries. Stop after identifying the first binding constraint and use no more than three audit queries. Report which constraint changed the count; do not speculate about source behavior.

For a validation error, read the named field or operator, refresh that field through `cb_reference`, correct only the invalid component, and retry. For authentication, permission, metering, or service errors, report the tool state and do not substitute another data source.
