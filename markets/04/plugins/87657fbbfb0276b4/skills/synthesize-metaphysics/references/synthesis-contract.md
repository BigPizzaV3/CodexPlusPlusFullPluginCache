# Validated source synthesis contract

The report-v2 contract is system-owned. This procedure compares already validated per-system reports without creating a new report, claim, recommendation, or validation result. Plan 5 owns validated-only cross-method synthesis: the registered `get_cross_method_evidence` tool (backed by `buildCrossMethodEvidenceView`) turns reports validated under one release bundle into a bounded `overlap`/`divergence`/`limitation` evidence view.

## Complete source gate

Accept exactly two or three source validation results from the same current conversation. Every accepted source must have `schemaVersion: omds.interpretation-validation.v1`, `valid: true`, `nextAction: render-validated`, a complete `validatedReport`, and a distinct report system among `liuyao`, `bazi`, and `ziwei`. The validated report must remain byte-for-byte attributable to that validation result, and every source must be validated under the exact same current release bundle -- checked the same way `verifyReleaseBundle` checks any release bundle, never merely assumed from a matching version string.

Reject a source set when any candidate is a facts-only `fallback`, an attempt-one `repair-once` result, an unvalidated draft, raw model prose, remembered content, cross-conversation content, a duplicate system, a report validated under a different release bundle, or a report whose validation-result envelope is absent. If fewer than two sources survive, stop with an explicit limitation and no comparison.

## Bounded comparison

Compare only source-owned material that already shares a bounded question or request type, requested domain, compatible target period and temporal layer, and compatible input/time-basis assumptions. A missing or incompatible boundary is a difference or limitation, never an invitation to infer a bridge.

For each explicit requested domain that two or three systems each contribute a claim to, preserve the source systems and schools, exact source claim IDs, evidence and counter-evidence references, target and temporal layer, support level, and limitations. Label an identical central finding `overlap` and a differing one `divergence`; a domain only one system addressed joins neither. Overlap describes shared wording only: it is not proof, independent confirmation, or a combined conclusion, and it never raises any source claim's own support level. Describe only what the validated source reports already establish. Make no new method claim, chart fact, canonical ID, evidence path, causal explanation, action, or outcome.

## Terminal boundaries

- Call only `get_cross_method_evidence` to produce the comparison itself. Do not call calculation, preparation, validation, chart, or export tools.
- Do not submit a fabricated cross-method system or report to a system validator.
- Do not treat a fallback or unvalidated draft as a validated report, and never cite raw model prose in place of one.
- Do not issue a compatibility verdict, score, probability, prediction, recommendation, professional guidance, or guaranteed outcome.
- Do not use remembered traditional meanings, vote across systems, rank them, suppress disagreements, or treat shared inputs as independent evidence.

Return the bounded evidence view -- its `overlap`, `divergence`, and standing `limitation` sections -- or an explicit not-comparable limitation when fewer than two sources qualify. Do not claim that the output is a validated report or authoritative report widget.
