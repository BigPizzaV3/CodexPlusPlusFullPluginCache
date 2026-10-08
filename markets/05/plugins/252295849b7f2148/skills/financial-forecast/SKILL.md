---
name: financial-forecast
description: "Assemble the assumptions behind a revenue or valuation forecast: population, penetration, pricing, timing, and competitive erosion, each with its evidence. Use when someone is building a model, for example 'what assumptions should I use for X', 'help me forecast peak sales'. Returns assumptions, not a finished spreadsheet or narrative. Use size-market when only sizing is wanted."
---

# Financial Forecast

## Using this skill

Use the connected Maven Bio MCP server at `https://mcp.mavenbio.com/`. Follow the user's explicit scope, depth, and output preferences; the workflow and output structure below are defaults. Report coverage limits instead of silently narrowing an explicitly requested set.

Hyphenated primitive names refer to other skills in this Maven Bio bundle. Consult the relevant skill when composing its workflow. Use the available MCP tool schemas for arguments; pass document identifiers to `read_document` through `ids`, and include a claim-specific `query` when using `format="citations"`.

This workflow is for forecast intelligence, not spreadsheet rendering.

## Primary Primitives

- `size-market`
- `identify-analogs`
- `enumerate-entities`
- `trace-events`
- `synthesize-evidence`
- `profile-entity`

## Optional Primitives

- `benchmark-assets`

## Output Contract

Return a forecast assumption package that can include:

- market assumptions
- analog references
- asset-specific development or competitive assumptions
- scenario caveats
- evidence ratings and citations for material assumptions
- unresolved forecast sensitivities

## Workflow Rules

- treat structured MCP outputs as the starting assumption stack, not the final forecast truth
- use document augmentation for pricing, analog, catalyst, and competitor assumptions that materially affect the package
- if host web fetch is blocked, use `search_documents` and `read_document` as the fallback path before declaring a gap
- For independent evidence workstreams, follow the [evidence research procedure](references/evidence-research.md) for each scoped pass, then reconcile the claims before synthesis. Run passes sequentially, or in parallel when the host supports it and the task authorizes it.
