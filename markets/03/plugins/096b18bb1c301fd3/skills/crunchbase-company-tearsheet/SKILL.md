---
name: crunchbase-company-tearsheet
description: Resolve a private-market entity and prepare a concise Crunchbase-grounded company tearsheet, brief, or snapshot for meeting preparation, including asking for the company when an explicit Crunchbase tearsheet or brief request omits its identity. Use only when the user explicitly asks for Crunchbase, selects Crunchbase as the data source, or follows up on an active Crunchbase company tearsheet or brief. Do not use for broad landscapes, recent-round screens, market-wide capital analysis, saved-list operations, public-equity research, Crunchbase pricing or account support, or generic company research when Crunchbase was not requested.
---

# Crunchbase Company Tearsheet

Prepare a focused company snapshot for meeting preparation. Do not present it as full commercial, technical, or investment diligence.

## Clarification contract

1. Before calling Crunchbase, require a company name, user-supplied domain, or previously resolved company identity. If none is present, make no Crunchbase call and ask for the company. Treat meeting purpose, audience, and investment mandate as optional unless the user explicitly requests tailoring that depends on them.
2. Bundle all blocking inputs into one concise question, ask no more than three items, and offer a recommended assumption or default the user can accept in one reply. Do not drip questions across turns or attribute the question to Crunchbase coverage.
3. Do not ask for optional preferences; prepare a general investor brief when meeting context is omitted. If the user says “just run it” or “use the defaults,” proceed with disclosed assumptions unless identity, scope, authorization, or another prerequisite remains genuinely blocking.
4. When identity evidence is supplied, use the resolver as specified below. Ask the user to choose only after the minimum resolution call reveals multiple credible candidates. Ask again only when the user's answer introduces a new blocking ambiguity.

## Operating contract

1. Resolve the named company first with `cb_expert_resolve_entity`, using the narrowest collection, concise situational context, and `cb_entity_get: null` for identity-only resolution. It is the only allowed expert tool; never call another tool whose basename contains `expert`.
2. Use a confident resolver match directly. When the resolver returns several credible candidates, show linked choices and ask the user to select. Use `cb_entity_autocomplete` only when the resolver errors or returns no usable match or candidates.
3. Pass a domain only when the user supplied it or it came from a previously resolved record. Never invent or infer a domain from model memory. A supplied domain is identity evidence, not permission to browse it.
4. Retrieve the profile separately with `cb_entity_get`, explicit top-level fields, and only decision-relevant cards. Never request default cards.
5. Use `cb_reference` before any structured competitor search. Reuse returned similar organizations and search projections; keep the query set bounded.
6. Keep this skill read-only. Never call a `cb_list_*` write tool.
7. Use neutral record language in every user-visible message. Show `—` for a null and explain it only as “— indicates no value was returned for that field.” For an empty search, say “No records matched the stated filters.” Never characterize source coverage, completeness, ingestion behavior, fields, or records as missing or stale.
8. Link the canonical company and competitors to organization profile URLs. Include the as-of date and state that the brief is Crunchbase-grounded. Separate facts, interpretation, risks, and questions to test. Resolve every bundled `references/...` path relative to the directory containing this `SKILL.md`. Never mention skill folders, skill or reference files, instruction loading, plugin or package paths, caches, or attempts to locate bundled resources in any user-visible message.
9. On authentication, permission, metering, or service errors, report the state neutrally and stop. Do not substitute external research unless the user requested it.

## Procedure

1. Read `references/entity-resolution.md` before resolving identity.
2. Read `references/company-snapshot.md`, `references/query-core.md`, and `references/output-contract.md` before profile retrieval and composition.
3. Retrieve only the company, financing, team, event, and peer fields needed for the requested meeting context.
4. End with the strongest counterinterpretation or question that could materially change the assessment.
