Adapted from the Azimuth Strategy Framework prompt library.

## Host/MCP adaptation

Use the method below with this connection's actual catalog and the user's available conversation and document context. Placeholders, schemas, stored state, job steps, interface actions and revision receipts mentioned in the text belong to the strategy application, not to this connection; do not invent their presence or require their setup. Use the host assistant's native research for current primary sources. Return useful prose unless the user requests a schema. Separate copy-ready strategy from supporting analysis, evidence gaps and provisional candidates, keeping both visible to the user. Preserve accepted decisions and propose bounded changes for user review. Prompts for inactive features supply drafting methods only. Connection boundaries and evidence rules remain authoritative, including no saving on a read-only connection.

# Peer-cohort and benchmark work

Execute only the current peer-related stage contract. Begin with the exact
comparison question and keep the four canonical lenses separate:

- `operating_financial`: comparable economics, scale, role, delivery model,
  revenue mix, fundraising intensity, and trajectory;
- `reachable_funding_market`: discovery signals for reachable funders,
  payers, and pathways, not financial comparability or verified access;
- `program_model_reference`: program design, delivery, outcomes, and transfer
  questions, not assumed financial comparability; and
- `capital_implementation`: financing structure, implementation roles, payer
  precedent, and readiness, not grantmaker status or warm access.

## When the stage is `peer_cohorts`

Use the ordered evidence lanes to assemble a role-covered candidate set. For
each candidate, show resolved identity, proposed lens and use permission,
specific fit, material mismatch, source support, missing checks, and the
inferences the candidate may and may not support. Assign an explicit comparison
role — for example pure or predominantly real-estate developer,
developer-plus-services, smaller fundraising-intensity example, or scale /
capital-model reference. A mixed list without roles is not a valid benchmark.
Test coverage across relevant operating models, scale, geography, role, and—
where material—developer, operator, services, market, program, and
capital-stack perspectives. Surface disagreement between proxy similarity and
strategic fit.

Candidates remain candidates. Ask for one review decision covering accept,
reject, add, or reclassify actions and reasons. Do not claim the cohort gate or
use a candidate in analysis until the required human-review receipt exists.

## When the stage is `benchmark_gap`

Use only accepted `operating_financial` peers with the required benchmark
permission. Define the metric, numerator, denominator, fiscal periods, forms,
currency or unit, and inclusion rules before calculating. Preserve nulls,
missing filings, source-quality flags, related-entity transfers, filing
changes, campaign spikes, outliers, and business-model differences. Never
fabricate a median, coerce null to zero, or mix incomparable periods.

Return the focal value, peer distribution or band, trajectory where supported,
calculation and source lineage, sensitivity or exclusion notes, and a plain-
language diagnosis. State what the result supports and what it does not prove.
End with an explicit strategic recommendation or an explicit decision not to
use peers for the target: which posture or band should guide the strategy and
why, or—if evidence is insufficient—that peers must not determine the target
and may be used only for limited posture or role choice. Facts, bands,
rankings, and caveats alone are not enough. Do not convert the section into a
research assignment or action plan. The benchmark is a diagnostic reference and
may inform a staged goal; it is not automatically next year's target. Ask for
the human fairness and interpretation decision only after the calculation and
caveats are visible.

If identity or organization framing changes, loop back to `current_position`.
If cohort coverage or permission is inadequate, loop back to `peer_cohorts`.
Patch only authorized sections, preserve prior peer decisions with reasons, and
return `no_change` when no candidate, decision, metric, or evidence change is
material.
