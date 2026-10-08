---
name: crunchbase-funding-activity-analyzer
description: Analyze funding activity, concentration, capital intensity, formation, or market timing across a user-confirmed private-company universe using Crunchbase, or ask the user to confirm a universe when an explicit Crunchbase funding-activity, capital, or overfunding question omits one. Use only when the user explicitly asks for Crunchbase, selects Crunchbase as the data source, or follows up on an active Crunchbase funding activity or capital analysis. Do not use for open-ended company discovery, recent-round sourcing, a single-company brief, saved-list membership changes, public-equity research, Crunchbase pricing or account support, or generic market analysis without Crunchbase.
---

# Crunchbase Funding Activity Analyzer

Analyze capital deployment only within a confirmed company universe. Never generalize a confirmed-list result to the whole market.

## Clarification contract

1. Treat the confirmed universe as the only required analytical input. Company names, one selected saved list, or an explicitly confirmed candidate set satisfy it; a sector label or market thesis alone does not.
2. When the universe is absent, make no Crunchbase call. Bundle all blocking inputs into one concise question, ask no more than three items, and offer concise recommended universe options the user can accept in one reply. Do not drip questions across turns or attribute the question to Crunchbase coverage.
3. Do not ask for optional preferences when the requested comparison can proceed over the confirmed universe. “Just run it” or “use the defaults” does not override the universe gate because the denominator would remain undefined.
4. When supplied names or a selected list are ambiguous, make only the minimum resolver or list-identification call needed to expose the choices, then ask once. Ask again only when the user's answer introduces a new blocking ambiguity.

## Universe gate

Require company names, one selected Crunchbase saved list, or an explicitly confirmed candidate set before retrieval. If no universe is confirmed, propose concise universe options and ask the user to choose without calling Crunchbase tools.

## Operating contract

1. For named companies, investors, or people, use `cb_expert_resolve_entity` first. It is the only allowed expert tool; never call another tool whose basename contains `expert`. Use returned candidates directly and ask when several remain credible. Use `cb_entity_autocomplete` for a named entity only after the resolver errors or returns no usable match or candidates.
2. Use only user-supplied or previously resolved domains. Never invent or infer a domain from model memory.
3. Use `cb_reference` before each `cb_search_query` to resolve predicate and order fields. Do not resolve projection-only fields.
4. Deduplicate the confirmed universe by organization UUID. Report requested, confirmed, ambiguous, unresolved, and analyzed counts.
5. Keep this skill read-only, including when the universe comes from a saved list. Never create, append, replace, or otherwise modify list membership.
6. Calculate full months, trailing periods, medians, formation, and concentration exactly as specified. Exclude `—` amounts from money calculations while reporting their count.
7. Use neutral record language everywhere. Show `—` for a null and explain it only as “— indicates no value was returned for that field.” For an empty search, say “No records matched the stated filters.” Never characterize source coverage, completeness, ingestion behavior, fields, or records as missing or stale.
8. Include the as-of date, confirmed universe definition, denominator, time windows, and formulas. Separate retrieved facts, derived metrics, interpretation, and suggested actions. Resolve every bundled `references/...` or `scripts/...` path relative to the directory containing this `SKILL.md`. Never mention skill folders, skill or reference files, instruction loading, plugin or package paths, caches, or attempts to locate bundled resources in any user-visible message.
9. On authentication, permission, metering, or service errors, report the state neutrally and stop. Do not substitute another data source unless requested.

## Procedure

1. Read `references/market-analysis.md`, `references/calculation-spec.md`, and `references/output-contract.md`.
2. Read `references/entity-resolution.md`, `references/query-core.md`, `references/organization-search.md`, and `references/funding-round-search.md` for a named universe.
3. Read `references/saved-lists.md` only when a selected saved list supplies the universe; use its read operations only.
4. Use `scripts/derive_metrics.py` for supported deterministic calculations.
5. Present metrics within the confirmed universe, alternative explanations, and questions that would change the interpretation.
