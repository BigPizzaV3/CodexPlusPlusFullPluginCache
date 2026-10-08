---
name: benchmark-assets
description: "Compare named assets side by side on a common set of dimensions and return a structured benchmark with explicit evidence strength. Use for direct comparisons, for example 'how does X compare to the other IL-23s', 'benchmark these four programs'. Use identify-analogs when precedents to reason from are wanted rather than a head-to-head table."
---

# Benchmark Assets

## Using this skill

Use the connected Maven Bio MCP server at `https://mcp.mavenbio.com/`. Follow the user's explicit scope, depth, and output preferences; the workflow and output structure below are defaults. Report coverage limits instead of silently narrowing an explicitly requested set.

Hyphenated primitive names refer to other skills in this Maven Bio bundle. Consult the relevant skill when composing its workflow. Use the available MCP tool schemas for arguments; pass document identifiers to `read_document` through `ids`, and include a claim-specific `query` when using `format="citations"`.

This primitive standardizes comparisons across assets without imposing a final table or slide format.

## Use When

- the user wants side-by-side comparison
- a workflow needs comparable dimensions across multiple assets
- you need a reusable comparison object before synthesis

## Core Tools

- `match_entity`
- `search_entities`
- `research_entity`
- `search_documents`
- `read_document` to read a located document (when a benchmark dimension is approval status, designations, or label content, find the label first with `search_documents(source_types=["fda_filings"])` -- `source_types` is a `search_documents` filter, not a `read_document` one)

Use `match_entity` to canonicalize each named asset before benchmarking. Keep the raw asset name in `name` and put sponsor/company/disambiguating text in `context`. Use `search_entities` when you are discovering the benchmark set by criteria rather than starting from a fixed named list.

## Output Contract

Return benchmark items where each asset has dimensions such as:

- mechanism
- lead indication
- highest stage
- differentiating evidence
- key risks

Each dimension should include:

- `value`
- `evidence_rating`
- `citations`
- optional `notes`

## Scaling the Benchmark

The `research_entity`-per-asset path is the right one for small-N comparisons, where
the user needs deep narrative context per asset rather than just structured dimensions.

For larger sets, do not silently degrade the depth of each row to fit the budget.
Narrow the benchmark set first (tighten the phase, indication, or modality scope via
`search_entities`), or reduce the number of comparison dimensions, and say which of
the two you did. A benchmark of 30 assets at one line each is less useful than a
benchmark of 8 assets that actually supports its claims.
- For independent evidence workstreams, follow the [evidence research procedure](references/evidence-research.md) for each scoped pass, then reconcile the claims before synthesis. Run passes sequentially, or in parallel when the host supports it and the task authorizes it.

## Optional Primitives

- `validate-target` (when a benchmark dimension is target genetic validation or tractability)

## Quality Bar

- keep dimensions comparable across assets
- separate directly supported facts from analytic judgment
- when one asset has missing evidence, preserve the asymmetry rather than smoothing it over
- when benchmarking dimensions touch label content, locate each asset's label with `search_documents(source_types=["fda_filings"])` and read the specific document with `read_document`; prefer `format="sections"` to find the relevant section before pulling full text, and cite the document plus its date on each cell
