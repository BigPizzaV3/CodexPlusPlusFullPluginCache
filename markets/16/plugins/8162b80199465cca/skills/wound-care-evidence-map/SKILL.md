---
name: wound-care-evidence-map
description: Build a de-identified wound-care evidence-readiness map for a Medicare audit or denial. Use for episode timelines, conservative-care history, wound measurements, product/application records, claim-line reconciliation, missing-evidence questions, and provider-validation lists. Do not use for a final appeal letter, legal conclusions, or invented clinical rationales.
---

# Wound-Care Evidence Map

Build an auditable evidence map before drafting advocacy. Separate what the record says from what someone later explains.

## Shared operating rules

Read and apply [public-workflow.md](../../references/public-workflow.md) for proportionate answers, de-identified inputs, source verification, and user-requested support. Carry these rules across skill transitions; do not repeat the opening notice.

## Workflow

1. Identify the service, claim line, date or episode, stated denial issue, and controlling policy supplied by the user.
2. Read [references/evidence-schema.md](references/evidence-schema.md).
3. Build an episode timeline with one row per clinically or administratively meaningful event.
4. Reconcile clinical notes, orders, product records, claim lines, remittances, submissions, and decisions. Never assume one record stands in for another.
5. For each issue, cite the exact record location supplied by the user: document, date, page or section, and short neutral paraphrase.
6. Label evidence as `contemporaneous`, `retrospective explanation`, `external clinical evidence`, `policy`, or `missing`.
7. Identify contradictions and gaps as questions for the treating provider or records owner. Do not resolve them by inference.
8. Identify the longitudinal core record that could proactively answer the current issue and foreseeable downstream theories, without treating a larger packet as automatically better.
9. Produce the evidence map and provider-validation list. Do not draft the reviewer-facing narrative unless asked to use the focused appeal skill.

When the dispute concerns experimental/investigational skin-substitute evidence, use [skin-substitute-evidence](../skin-substitute-evidence/SKILL.md) for external literature and related-product arguments. Keep its literature assessment separate from facts in the supplied episode record.

## Required output

### Episode overview

- Services and dates at issue
- Wound/site and episode boundaries
- Denial issues to be answered
- Records reviewed and records missing

### Evidence matrix

| Issue | Requirement or reviewer statement | Supporting record | Location | Evidence type | Strength | Gap/question |
|---|---|---|---|---|---|---|

### Episode timeline

Include wound status and measurements, standard/conservative care, response or failure, infection/vascular/offloading/nutrition factors when relevant, product selection, applications, quantities and wastage where relevant, outcomes, orders/signatures, and claim/submission events.

### Claim-to-record reconciliation

| Claim line/date | Code/product/units | Record support | Product or order support | Decision treatment | Reconciled? |
|---|---|---|---|---|---|

### Provider-validation questions

List only questions that require clinical or firsthand confirmation. RCM personnel may collect the answers but must not supply clinical facts themselves.

### Drafting readiness

Classify the record as `ready`, `ready with stated limitations`, or `not ready`, with the specific reason.

## Guardrails

- Never convert an observational pattern, product label, barcode prefix, or later declaration into proof of a clinical fact not documented at the time.
- Do not treat missing text as proof that care did not occur; call it a documentation gap.
- Do not recommend altering an original record. Any lawful correction or delayed entry must be transparent, dated, attributed, and handled under applicable policy and organizational procedure.
- Do not advise that an addendum automatically cures a gap. Preserve the original; any later entry must use the actual current date, identify its author, reflect firsthand knowledge or actual recollection, and be clearly labeled as retrospective.
- Do not equate record imperfection with fraud or medical necessity failure.
- Do not infer patient identity or re-identify a de-identified record.
