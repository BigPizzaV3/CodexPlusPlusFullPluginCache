---
name: audit-presentation
description: Audit, review, critique, score, evaluate, quality-check, or diagnose an existing presentation without changing it by default. Use for executive review, narrative review, evidence and citation review, design critique, accessibility review, technical PPTX inspection, template compliance, readiness assessment, or prioritized recommendations. Do not use when the primary request is to implement fixes, create a new deck, or produce a single new slide or chart.
---

# Audit presentation

Produce an evidence-backed diagnosis that distinguishes material risks from preferences. Remain read-only unless the user separately requests implementation.

## Workflow

1. Read [governance](references/core/00_GOVERNANCE.md), [semantic model](references/core/01_SEMANTIC_MODEL.md), [materiality](references/core/03_ANALYSIS_MATERIALITY.md), [privacy/security](references/core/13_PRIVACY_SECURITY_COMPLIANCE.md), [audit rubric](references/core/11_AUDIT_RUBRIC.md) and [assurance](references/core/09_ASSURANCE.md).
2. Apply [the audit workflow](references/workflow.md).
3. Load only the applicable modules: [evidence](references/core/06_EVIDENCE_GOVERNANCE.md), [visual/data](references/core/07_VISUAL_DATA_ACCESSIBILITY.md) and [production](references/core/08_PRODUCTION_INTEROP.md).
4. Use [capability routing](references/core/04_CAPABILITY_ROUTING.md) and [bindings](references/core/12_CAPABILITY_BINDINGS.md) when inspection needs tools.

## Behavior

- Establish the deck's intended audience, objective and use before judging it.
- Inspect both overall story and individual critical slides.
- Ground every finding in a slide, object, claim, rendering or missing requirement.
- Classify severity and explain consequence, correction and verification.
- Prioritize the few changes with highest decision/use impact.
- Separate internal quality state from institutional approval.

## Output contract

Lead with readiness and top risks. Then provide findings by severity, strengths worth preserving, prioritized remediation and validation conditions. Give a score only when the rubric and evidence make it meaningful.

## Prohibitions

- Do not call subjective taste a defect.
- Do not infer factual correctness from visual polish.
- Do not claim application-level inspection not performed.
- Do not modify the deck without authorization.
