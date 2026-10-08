---
name: crunchbase-market-mapper
description: Discover, segment, screen, and optionally save a Crunchbase market map against an investment thesis, including asking for a thesis anchor when an explicit Crunchbase market-mapping or landscape request omits one. Use only when the user explicitly asks to use Crunchbase, selects Crunchbase as the data source, or follows up on an active Crunchbase market map or landscape. This skill owns compound “build and save” requests. Do not use for a single-company brief, analysis of a user-confirmed company universe, operations on an existing saved list, recent-round-only reviews, public-equity research, Crunchbase pricing or account support, or generic landscapes when Crunchbase was not requested.
---

# Crunchbase Market Mapper

Build a reviewed company universe against an explicit thesis. Segment by buyer, product, use case, or business model; do not treat keyword matches as final relevance decisions.

## Clarification contract

1. Before calling Crunchbase, require a usable thesis anchor such as a market, buyer, product, use case, business model, or category. Treat stage, geography, operating status, and funding cap as optional when the demonstration defaults can answer safely.
2. When a required input is absent or ambiguous, make no Crunchbase call. Bundle all blocking inputs into one concise question, ask no more than three items, and offer a recommended assumption or default the user can accept in one reply. Do not drip questions across turns or attribute the question to Crunchbase coverage.
3. Do not ask for optional preferences. If the user says “just run it” or “use the defaults,” proceed with disclosed assumptions unless identity, scope, authorization, or another prerequisite remains genuinely blocking.
4. Treat a broad but usable thesis such as “healthcare AI” as sufficient for a first pass. Ask again only when the user's answer introduces a new blocking ambiguity.

## Operating contract

1. Use `cb_reference` before every `cb_search_query` to resolve predicate and order fields. Prefer one collection-level field catalog, then request only field details it does not expose. Do not resolve projection-only fields.
2. Resolve categories and locations with `cb_entity_autocomplete`. For named companies, investors, or people, use `cb_expert_resolve_entity` first. It is the only allowed expert tool; never call another tool whose basename contains `expert`. Use autocomplete for a named entity only after the resolver errors or returns no usable match or candidates.
3. Never invent or infer a domain from model memory. Use only domains supplied by the user or returned by a resolved record.
4. Search and analysis are read-only. Call `cb_list_create` or `cb_list_add_entities` only when the user explicitly asks to save or create the discovered landscape. Preview the collision-free list name and linked canonical companies before the first write.
5. Run the first `cb_search_query` no later than the 12th Crunchbase call. Stop resolving optional fields after call 11. Cap a read-only landscape at 16 Crunchbase calls and a build-and-save landscape at 20. Reuse search projections; do not call `cb_entity_get` for fields already returned by the search.
6. After an authorized write, call `cb_list_get` to reconcile persisted membership. Once reconciliation succeeds, make no further tool calls and render the final result immediately.
7. Use neutral record language everywhere. Show `—` for a null and explain it only as “— indicates no value was returned for that field.” For an empty search, say “No records matched the stated filters.” Never characterize source coverage, completeness, ingestion behavior, fields, or records as missing or stale.
8. Link company names to organization profile URLs. Include as-of date, segments, filters, denominator, refinements, and concise exclusions. Resolve every bundled `references/...` or `scripts/...` path relative to the directory containing this `SKILL.md`. Never mention skill folders, skill or reference files, instruction loading, plugin or package paths, caches, or attempts to locate bundled resources in any user-visible message.
9. On authentication, permission, metering, or service errors, report the state neutrally and stop. Do not substitute another data source unless the user requested external research.

## Procedure

1. Read `references/landscape-build.md`, `references/query-core.md`, `references/organization-search.md`, and `references/output-contract.md`.
2. Read `references/entity-resolution.md` when the request names a company, investor, person, parent, or domain.
3. Read `references/calculation-spec.md` when deriving recency or other metrics; use `scripts/derive_metrics.py` when applicable.
4. Read `references/saved-lists.md` only when the same request explicitly asks to save the new landscape.
5. Apply the user's mandate. When omitted, state the demonstration defaults: United States; pre-seed, seed, and Series A; operating and private; under $15M total funding.
6. Propose no more than three segments, search each once, allow at most one audited refinement, deduplicate by organization UUID, review descriptions, and present the candidate universe before any authorized save.
