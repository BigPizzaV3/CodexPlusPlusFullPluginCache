---
name: rea-evidence-and-reporting
description: Interpret REA results and prepare a reviewable report that separates observations, inferences, unknowns, and coverage limits; use for analysis summaries, feature traces, comparisons, and handoffs.
---

# Evidence and reporting

## Evidence ledger

For each conclusion, record the claim; actual evidence ID(s) and source/artifact/version; whether it is direct observation, inference, or unknown; confidence and why; coverage boundary, failed/unsupported routes, and relevant environment; and the narrowest next check if uncertain.

Retain inline Evidence when no durable reference exists. Use stable same-session references when available. Do not invent evidence IDs, cite omitted details, or refer to evidence from another session without proof.

## Interpretation rules

- A string, symbol, import, filename, route, decompiled fragment, or graph edge can suggest a hypothesis; alone it does not prove behavior.
- Static analysis describes the inspected artifact and analysis coverage. It does not show that a code path executed.
- Runtime observation supports only the observed target, state, environment, and interval; it does not establish universal behavior.
- A difference between versions may come from build/configuration or incomplete coverage. Attribute it only when evidence identifies the cause.
- Preserve raw addresses, offsets, selectors, and original carrier details where relevant. Keep inferred values labeled as candidates.
- “Not found” means not found within the stated search boundary, not absent everywhere.

## Suggested report

### Answer
One sentence with confidence and scope.

### Evidence
Bullets keyed by actual Evidence IDs, with what each result directly establishes.

### Interpretation
Clearly labeled inferences and alternatives.

### Limits and unknowns
Provider/tool limitations, target/version/environment, unsearched regions, and missing runtime confirmation.

### Next step
One minimal follow-up tied to an unresolved checklist item.

For evidence bundles, write only to a user-selected path. Before sharing a report externally, remove credentials, private binary paths, proprietary artifacts, personal data, and unrelated local details.
