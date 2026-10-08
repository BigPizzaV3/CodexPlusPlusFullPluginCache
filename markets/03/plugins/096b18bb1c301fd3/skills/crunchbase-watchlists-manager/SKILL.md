---
name: crunchbase-watchlists-manager
description: Inspect, monitor, create, append, replace, or reconcile company watchlists stored as Crunchbase saved lists and their private-company membership, including asking for the operation or identifiers when an explicit Crunchbase watchlist or saved-list request omits them. Use when the user explicitly asks to work with a Crunchbase watchlist or saved list, selects Crunchbase for a saved-list task, or follows up on an active watchlist or saved-list workflow. Do not use for creating a list as part of a new thesis landscape, capital analysis that merely reads a list as its confirmed universe, recent-round sourcing, single-company briefs, public-equity research, Crunchbase pricing or account support, or generic CRM/list work outside Crunchbase.
---

# Crunchbase Watchlists Manager

Treat saved lists as persistent company universes. Keep membership operations distinct from analysis of organization fields over time.

## Clarification contract

1. Before acting, require the requested operation and its essential identifiers: an existing-list identity for inspect, monitor, append, remove, or replace; a list name for create; and a list name plus company set for save. Require explicit write intent before any membership change.
2. When a required input is absent, make no Crunchbase call. Bundle all blocking inputs into one concise question, ask no more than three items, and offer a recommended assumption or default the user can accept in one reply. Do not drip questions across turns or attribute the question to Crunchbase coverage.
3. Do not ask for optional preferences. If the user says “just run it” or “use the defaults,” proceed with disclosed assumptions only for read-only work; never infer a list identity, company identity, membership operation, replacement authorization, or write intent.
4. When an approximate list or company identity is supplied, make only the minimum list-query or entity-resolution call needed to expose credible choices, then ask once. Ask again only when the user's answer introduces a new blocking ambiguity.

## Operating contract

1. Use `cb_list_query` to identify a list and `cb_list_get` to retrieve or reconcile membership. If similar list names remain credible, show candidates and ask the user to choose.
2. Monitoring, current-state review, comparison, and proposing changes are read-only. Write only when the user explicitly asks to create a list, save a supplied set, append resolved entities, or update membership.
3. Resolve every named company first with `cb_expert_resolve_entity`. It is the only allowed expert tool; never call another tool whose basename contains `expert`. Use returned candidates directly and ask when several remain credible. Use `cb_entity_autocomplete` for a named company only after the resolver errors or returns no usable match or candidates.
4. Use only domains supplied by the user or returned by a resolved record. Never invent or infer a domain from model memory.
5. Before the first write, preview the intended operation, collision-free list name when creating, canonical linked companies, and confirmed/ambiguous/unresolved counts.
6. After create, add confirmed organization UUIDs and call `cb_list_get`. After append, call `cb_list_get`. Once reconciliation succeeds, make no further tool calls and render the final result immediately.
7. A remove request does not authorize a replacement list. If in-place removal is unavailable, preview the retained set and versioned replacement, then wait for explicit approval in a later user turn before any write.
8. Use `cb_reference` before any structured organization search. Use explicit profile fields and cards; never request default organization cards.
9. Use neutral record language everywhere. Show `—` for a null and explain it only as “— indicates no value was returned for that field.” For an empty search, say “No records matched the stated filters.” Never characterize source coverage, completeness, ingestion behavior, fields, or records as missing or stale.
10. Link company names to organization profile URLs. Include the as-of date, list ID/name, requested and persisted counts, and any outcome requiring attention. Resolve every bundled `references/...` or `scripts/...` path relative to the directory containing this `SKILL.md`. Never mention skill folders, skill or reference files, instruction loading, plugin or package paths, caches, or attempts to locate bundled resources in any user-visible message.
11. On authentication, permission, metering, or service errors, report the state neutrally and stop. Do not substitute another data source unless requested.

## Procedure

1. Read `references/pipeline-monitoring.md`, `references/saved-lists.md`, and `references/output-contract.md`.
2. Read `references/entity-resolution.md` when company identities must be resolved.
3. Read `references/query-core.md` and `references/organization-search.md` before a structured organization query.
4. Read `references/calculation-spec.md` and use `scripts/derive_metrics.py` only when monitoring calculations are requested.
5. Preserve the requested operation exactly: inspect, monitor, create, append, or propose a replacement. Do not silently substitute one operation for another.
