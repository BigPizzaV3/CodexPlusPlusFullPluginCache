---
name: ololand-dd-playbook-recall
description: "Use when the user asks to run the OloLand ololand-dd-playbook-recall\
  \ workflow. Pull your firm's playbook for deals like this \u2014 what worked, what\
  \ didn't, what got missed in similar past deals. Wraps cross-deal learning + per-deal\
  \ outcome metadata."
---


# Workflow for ololand-dd-playbook-recall

Follow the OloLand command instructions below when the user asks for `ololand-dd-playbook-recall` or the equivalent workflow.

# Playbook Recall

Surfaces your firm's institutional memory on deals like this one. For each similar past deal, returns the playbook moves that worked, the moves that didn't, the risks that were correctly flagged, and (most usefully) the risks that were missed and materialized post-close.

## Usage

```
ololand-dd-playbook-recall <deal_id>
```

## Arguments

- `deal_id` (required) — The current deal to recall playbooks for. Similarity is computed against industry (35%), size (25%), deal type (20%), and margin profile (20%).

## Execution

1. Call `find_similar_deals` from the MCP server with the `deal_id`. Returns up to 8 most similar past deals.
2. **If the response is `status: "no_usable_corpus"`** — stop here. Tell the user explicitly that institutional memory cannot support this deal yet (strict deal-type / sector-family / size-ratio filters couldn't form a usable cohort). Do NOT fabricate a cohort from looser matching.
3. For each similar deal in a usable cohort, walk the `outcome` / `learning_insights` blocks that `find_similar_deals` returns directly:
   - The risk categories that were flagged during DD vs. the risks that materialized post-close
   - The accuracy patterns (where projections were systematically optimistic / pessimistic)
   - The valuation ranges that closed vs. the underwritten range
4. For deeper context on specific past deals, use `get_deal`, `get_deal_risks`, and `get_evidence_links` on the historical deal IDs returned in step 1.
5. Synthesize into a structured playbook recall:

   - **What worked** — moves that recurred across multiple similar deals with positive outcomes
   - **What didn't** — moves attempted but with poor outcomes; treat as anti-patterns
   - **What was missed** — risks that *weren't* flagged during DD but materialized post-close. This is the most valuable section: it surfaces the systematic blind spots in your firm's prior reads of this deal type.
   - **Calibration** — for each metric the current deal is presenting (revenue growth, EBITDA margin, leverage), the historical accuracy of similar deals' projections vs. realizations.

## Why this matters

This is the institutional-memory wedge. A general-purpose AI doesn't have access to your firm's deal history; it can only tell you industry averages. This command tells you what *your firm* learned the last 14 times you saw a deal shaped like this one — including the patterns that consistently get missed in DD and bite later.

## Example

```
ololand-dd-playbook-recall deal_acme_2026
```

Returns: "Across 6 similar industrial-services rollups your firm closed in 2022-2024: revenue projections were overestimated by avg 15%, customer concentration was flagged in 5/6 deals and materialized in 3, integration cost overruns averaged 1.4x management's estimate. Recommended DD pivots: deeper customer interviews, integration cost stress test at 1.5x management base case."

## Related commands

- `ololand-dd-similar-deals` — raw similarity output without playbook synthesis
- `ololand-dd-calibrate-vs-history` — applies historical accuracy patterns to adjust the current deal's projections


## OpenAI execution requirements

Use the connected MCP server's current tool schemas. Do not invent tool arguments, job-status endpoints, inputs, or outputs. If a referenced tool is unavailable, explain the limitation and request the needed connection or data. Invoke writes only when the user has requested the corresponding action. Do not initiate purchases or payments. An unrun, unsupported, or unavailable procedure is a gap, never a passing result.


OpenAI cannot execute local lifecycle hooks. Use the packaged explicit setup/review workflow when requested. Server-side MCP auditing remains authoritative; preserve evidence blockers and human-only approval gates.

Claim-correction submission is unsupported in this OpenAI upload because the current handler records surface=cowork. Do not invoke submit_agent_claim_correction from OpenAI. Explain the limitation and retain proposed correction text for human review without claiming submission. See unsupported-workflows.json for the excluded canonical workflow.
