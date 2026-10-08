---
name: asset-profile
description: "Build a full intelligence packet on one named drug or asset: development status, trial evidence, competitive position, catalysts, and risks. Use when someone names a single asset and wants depth, for example 'tell me everything about X', 'profile this drug', 'is X differentiated'. Use profile-entity instead when only a single structured fact sheet is wanted."
---

# Asset Profile

## Using this skill

Use the connected Maven Bio MCP server at `https://mcp.mavenbio.com/`. Follow the user's explicit scope, depth, and output preferences; the workflow and output structure below are defaults. Report coverage limits instead of silently narrowing an explicitly requested set.

Hyphenated primitive names refer to other skills in this Maven Bio bundle. Consult the relevant skill when composing its workflow. Use the available MCP tool schemas for arguments; pass document identifiers to `read_document` through `ids`, and include a claim-specific `query` when using `format="citations"`.

This workflow produces a structured profile for one asset without assuming a final memo or deck format.

## Primary Primitives

- `profile-entity`
- `benchmark-assets`
- `trace-events`
- `synthesize-evidence`

## Optional Primitives

- `identify-analogs`
- `size-market`
- `synthesize-evidence` (when the asset is approved or near-approval and designation, label, or exclusivity claims need to be tied back to specific filings)
- `validate-target` (when the asset's thesis depends on its target's genetic validation)

## Output Contract

Return a structured asset intelligence package that can include:

- asset overview
- development status
- supporting trial or document evidence
- competitive framing
- recent catalysts
- key risks and unresolved questions

## Workflow Rules

- treat entity profiling as the baseline fact pattern, not the final synthesis
- when calling `research_entity`, keep the raw asset name in `name` and put sponsor/company/disambiguating text in `context`
- use document augmentation to strengthen trial, catalyst, forecast, and competitive claims
- if host web fetch is blocked, prefer `search_documents` and `read_document` over repeated blocked fetch attempts
- if a composite asset name fails to resolve, retry with the raw asset name and move sponsor/company details into the optional context hint
- if the asset is approved in any region, include a regulatory timeline (designations, approval dates, label revisions) built from `search_documents` with `source_types=["fda_filings"]` and `read_document`; cite the filing and its date for each milestone, and state exclusivity or LOE timing as a gap when no filing supports it
- For independent evidence workstreams, follow the [evidence research procedure](references/evidence-research.md) for each scoped pass, then reconcile the claims before synthesis. Run passes sequentially, or in parallel when the host supports it and the task authorizes it.
