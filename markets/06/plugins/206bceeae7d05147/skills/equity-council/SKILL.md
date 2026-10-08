---
name: equity-council
description: Use when a user wants deep multi-expert research to rank publicly traded companies in an industry for long-term investment opportunity, balancing success probability, potential return and downside.
---

# Equity Council

Act as the research director and final adjudicator. Produce a detailed plan, execute it, then deliver a substantial source-backed ranking. Default horizon: 5–10 years. Expert roles are analytical lenses, not claimed credentials. This skill coordinates the bundled specialists; it does not change the host model or create tools.

## Start with the decision contract

Read [operating contract](../../references/operating-contract.md), [agent protocol](../../references/agent-protocol.md) and [report contract](../../references/report-contract.md). Adopt [defaults](../../config/defaults.json) with explicit user overrides. Resolve the industry if absent. State provisional assumptions for optional preferences and continue useful work.

Publish and save the plan **before substantive screening**: industry definition, success event, horizon, universe, benchmark, current-data cutoff, procedures, expert assignments, dependencies, required evidence, rank method and stopping conditions. Initialize a dated run using `../../scripts/new_run.py --help` or equivalent manual files. Then execute the plan without a routine approval pause.

## Execute in dependency order

1. **Map and screen:** use [equity-universe](../equity-universe/SKILL.md). Establish economic exposure and the candidate/exclusion ledger. A useful initial search often discovers 15–30 candidates, but actual industry size and reliable coverage control scope. Do not claim completeness from a familiar ticker list.
2. **Investigate independently:** assign [business](../equity-business/SKILL.md), [financials](../equity-financials/SKILL.md), [stewardship](../equity-stewardship/SKILL.md), [risk](../equity-risk/SKILL.md) and [expectations/catalysts](../equity-catalysts/SKILL.md). Use real subagents where supported, within available slots. Queue independent assignments; reconcile shared inputs centrally. Disclose sequential mode if separate workers are unavailable.
3. **Shortlist by economics and evidence:** normally deepen approximately five finalists plus the closest rejected alternative. Include less obvious value-chain beneficiaries. Do not let missing evidence masquerade as weak fundamentals or exciting narratives substitute for survivability.
4. **Normalize and model:** adopt one source-linked assumptions ledger. Use [equity-valuation](../equity-valuation/SKILL.md) and [ranking method](../../references/ranking-method.md). Produce central and adverse sensitivity sets, plus independently rebuilt 5-/10-year forecasts. Compute with the bundled calculator only when its conventions match and weights are defensible.
5. **Challenge and verify:** use [equity-red-team](../equity-red-team/SKILL.md) and [equity-audit](../equity-audit/SKILL.md). Send neutral source questions before proposed answers where practical. Resolve errors and rerun affected models. Preserve material dissent.
6. **Adjudicate:** apply the predeclared gates, Pareto comparison and ranking policy. Explain why the leader beats the runner-up, the assumptions that reverse that choice and whether the industry offers any attractive absolute opportunity. Present probability-first and speculative-upside alternatives separately. Use tied tiers when uncertainty exceeds apparent differences.
7. **Deliver:** write the long-form report and linked evidence/model artifacts. Reconcile the final output with the original checklist. Save testable forecasts and monitoring triggers; use [equity-update](../equity-update/SKILL.md) on a later requested refresh.

## Decisions that require judgment

Investigate tangents only through a plausible causal effect on cash flows, balance sheets, valuation or failure probability. Prioritize unanswered questions that could change the shortlist or rank. High confidence in an audited historical fact does not imply confidence in its extrapolation. Expert consensus does not calibrate probabilities.

If current sources, a required price or supportable scenario weights are unavailable, finish the useful research with conditional valuations and a watchlist. Say what prevented a supported ranking. Do not manufacture a winner, a success percentage, citations or a claim of exhaustive research. Finish when material questions are answered or transparently bounded and remaining research has low decision value.
