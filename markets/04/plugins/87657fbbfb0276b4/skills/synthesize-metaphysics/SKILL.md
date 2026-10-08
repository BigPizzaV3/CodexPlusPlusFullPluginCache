---
name: synthesize-metaphysics
description: Compare validated Inner Lens system reports, bound to one release bundle, when a user requests a bounded, traceable cross-method evidence view.
---

# Synthesize validated Inner Lens reports

Require separate canonical calculation and validation for each selected system before synthesis: use this Skill only with two or three per-system `validatedReport` payloads returned by `validate_interpretation_report` in the same current conversation. Each source must be `valid: true`, have `nextAction: render-validated`, represent a distinct system among Liuyao, Bazi, and Ziwei, and be validated under the exact same current release bundle. If fewer than two qualifying sources remain, stop with an explicit limitation.

1. Read [the complete synthesis contract](references/synthesis-contract.md).
2. Never treat a facts-only `fallback`, a `repair-once` result, or an unvalidated draft as a validated source. Never cite raw model prose, an invalid report, or a report validated under a different release bundle. Never use remembered traditional meaning or a source from another conversation.
3. Call the registered `get_cross_method_evidence` tool with the exact validated reports and the release bundle each was validated under. Present only its returned bounded `overlap`, `divergence`, and `limitation` sections, already linked to source claim IDs, evidence, and limitations. Preserve the source system, school, reading contract, target period, claim IDs, evidence references, counter-evidence, and limitations without reinterpretation.
4. Do not call `prepare_interpretation` or `validate_interpretation_report` for synthesis, and do not call calculation, chart, or export tools. The report-v2 contract is system-owned; this Skill does not produce its own validated cross-method report v2.
5. No compatibility verdict, score, prediction, recommendation, or remembered traditional meaning. Do not vote, rank, merge conflicting claims, invent a bridge, or claim overlap across systems as independent confirmation.

Plan 5 owns validated-only cross-method synthesis: a bounded, release-bundle-bound evidence view over already validated system reports, never a new divination conclusion.
