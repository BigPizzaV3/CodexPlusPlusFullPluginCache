---
name: ololand-dd-similar-deals
description: "Use when the user asks to run the OloLand ololand-dd-similar-deals workflow.\
  \ Find similar completed deals from your firm's history, or compare a metric across\
  \ an attribute-filtered slice of the pipeline \u2014 transfer learning insights,\
  \ accuracy patterns, and valuation benchmarks."
---


# Workflow for ololand-dd-similar-deals

Follow the OloLand command instructions below when the user asks for `ololand-dd-similar-deals` or the equivalent workflow.

# Similar Deals

Find similar completed deals and extract institutional learning patterns, or run
an attribute-filtered metric comparison across the firm's own pipeline.

## Usage

```
ololand-dd-similar-deals <deal_id>
ololand-dd-similar-deals compare <metric,metric,...> [sector=...] [structure=...] [size_band=...] [min_deal_size=...] [max_deal_size=...]
```

## Arguments

- `deal_id` — The current deal to find comparisons for (first form).
- `compare` mode: one or more `metrics` (e.g. `revenue,ebitda,ebitda_margin`),
  and optional `sector`, `structure`, `size_band` (`small`|`lower_mid`|`mid`|
  `upper_mid`|`large`), `min_deal_size`/`max_deal_size` filters.

## Execution — similarity ranking (`ololand-dd-similar-deals <deal_id>`)

1. Call `find_similar_deals` from the MCP server.
2. **If the response is `status: "no_usable_corpus"`** — stop here. Tell the user that strict similarity filters (deal type, sector family, size ratio) could not form a usable cohort. Do NOT relax filters or invent a cohort.
3. For each similar deal in a usable cohort, present:
   - **Deal profile**: Industry, size, type, outcome
   - **Similarity score**: Breakdown by industry (35%), size (25%), type (20%), margin (20%)
   - **Learning insights**:
     - Accuracy patterns: "Revenue projections were overestimated by 15% in 4/6 similar deals"
     - Common risks: "Customer concentration was flagged in 5/6 deals and materialized in 3"
     - Valuation ranges: "Median EV/EBITDA was 8.2x for similar deals"
4. Synthesize actionable recommendations:
   - Which risk categories to watch most carefully
   - Where historical predictions were systematically biased
   - How to calibrate financial assumptions based on past outcomes

## Execution — attribute comparison (`ololand-dd-similar-deals compare ...`)

Use this instead of the similarity ranking above when the user asks something
like "how does deal X's EBITDA margin compare to our other software deals" or
"show revenue across our mid-size deals" — an attribute-filtered comparison
table over the firm's pipeline, not a ranking against one reference deal. It
does **not** require the firm to have any closed/decided deals: it queries the
deal pool directly, so an all-open pipeline still returns a comparison.

1. Call `compare_deals_by_attribute(metrics, sector, structure, size_band, min_deal_size, max_deal_size, limit)`. `limit` is capped at 50. On an `invalid_metric` response, retry with one of the returned `allowed_metrics`.
2. Note that `structure` is **not** a true deal-structure taxonomy (no lbo/merger/asset-purchase field exists yet) — it matches the closed-deal decision type (`closed`/`passed`/`exited`/`withdrawn`) when the deal has one, else the deal's free-text pipeline stage. A miss on this filter means "no deal has that exact label," not "the firm has no such deals" — do not assert firm-wide absence from an empty result on this filter alone.
3. Compare the returned `matched_total` (all attribute-matching deals) against `deal_count` (the truncated size actually shown) and state whether the table is complete or partial.

## Output — compare mode

Table: Deal | Sector | Structure/Stage | Size band | {metric columns...}, followed by `matched_total` vs `deal_count`.

## Why This Matters

This is institutional intelligence — knowledge that accumulates across your firm's deal history. It's the compounding advantage that a general-purpose AI cannot provide because it doesn't have access to your prior deal outcomes.


## OpenAI execution requirements

Use the connected MCP server's current tool schemas. Do not invent tool arguments, job-status endpoints, inputs, or outputs. If a referenced tool is unavailable, explain the limitation and request the needed connection or data. Invoke writes only when the user has requested the corresponding action. Do not initiate purchases or payments. An unrun, unsupported, or unavailable procedure is a gap, never a passing result.


OpenAI cannot execute local lifecycle hooks. Use the packaged explicit setup/review workflow when requested. Server-side MCP auditing remains authoritative; preserve evidence blockers and human-only approval gates.

Claim-correction submission is unsupported in this OpenAI upload because the current handler records surface=cowork. Do not invoke submit_agent_claim_correction from OpenAI. Explain the limitation and retain proposed correction text for human review without claiming submission. See unsupported-workflows.json for the excluded canonical workflow.
