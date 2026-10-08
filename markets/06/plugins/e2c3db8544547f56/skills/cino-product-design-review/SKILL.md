---
name: cino-product-design-review
description: Perform read-only, evidence-backed product-design and frontend UX audits of websites and web applications. Use when the user asks to inspect visual quality, hierarchy, typography, spacing, responsiveness, accessibility, interaction states, design consistency, or whether an interface looks generic or AI-made. Produce P0/P1/P2 findings tied to exact routes, states, widths, components, evidence, fixes, and verification. This skill audits and specifies repairs; it does not itself authorize product or code changes.
---

# Cino Product Design Review

Audit the interface the user actually has, not an imagined redesign. Prioritize user harm and task completion over taste, preserve settled product rules, and make every serious finding independently verifiable.

## Operating boundary

- Treat every audit as read-only unless the user separately and explicitly asks for implementation.
- When implementation is authorized, finish the audit first and hand its repair brief to the appropriate implementation workflow. Do not silently broaden this skill into a redesign or code-editing mode.
- Review presentation and interaction quality. Do not claim that a visual audit validates calculations, permissions, data integrity, legal compliance, or business logic.
- Respect existing product, brand, content, and business decisions unless the evidence shows that their presentation causes user harm.
- State when access, routes, data, states, or viewport coverage are missing. Never fabricate unseen behavior.

## Required references

Read [finding-format.md](references/finding-format.md) for every audit.

Read [audit-criteria.md](references/audit-criteria.md) when evaluating visual design, interaction design, accessibility, content presentation, or design-system consistency.

Read [responsive-testing.md](references/responsive-testing.md) when the product has responsive layouts, constrained app containers, multiple device classes, or width-related claims.

Read [validation.md](references/validation.md) only when testing or revising this skill itself. Do not load a known answer key before a blind validation pass.

## Audit workflow

### 1. Establish authority and coverage

Identify the product purpose, primary user, core task, required journey, brand constraints, authoritative design system, target routes, target states, and required widths. Inspect supplied requirements and source artifacts before applying personal preferences.

Ask only for missing information that would materially change the audit. If the target is accessible and the user asked for a broad review, begin with reasonable coverage and record assumptions.

### 2. Inspect real rendered states

Prefer the live or locally running interface at exact routes, states, and widths. Use browser evidence, screenshots, DOM/accessibility information, and relevant source code when available. Source code can explain a symptom but does not replace rendered evidence for a visual claim.

Exercise the core task before polishing peripheral pages. Include consequential states such as loading, empty, error, disabled, validation, success, focus, hover, overflow, and realistic dense or long data when they exist.

Do not infer that a state works merely because a component exists. Do not infer that a component is broken merely because its source looks unusual.

### 3. Separate systemic and local problems

Classify repeated faults in typography, spacing, color, controls, grids, or responsive behavior as system findings, then cite representative instances. Classify isolated faults against their exact page and component. Avoid duplicating one root cause as many page findings.

### 4. Rank by harm

Assign P0, P1, or P2 using [finding-format.md](references/finding-format.md). Task blockage, concealed material information, dangerous ambiguity, and serious accessibility barriers outrank style inconsistency. Do not issue a P0 for aesthetics alone.

### 5. Write a repairable report

For each serious finding, give enough location, state, evidence, cause, repair direction, and verification detail that another person can reproduce and fix it without guessing. Label the basis as observed, directly inferred, or unverified.

### 6. Close with a decision

Return one audit result:

- **PASS** — required coverage is complete and no material P0 or P1 remains.
- **PASS WITH CORRECTIONS** — no P0 remains, but one or more material P1 fixes are required.
- **FAIL** — one or more P0 findings block the stated task or release standard.
- **INCOMPLETE EVIDENCE** — required access or coverage is missing, so a reliable decision is not possible.

The result must follow the evidence. Do not soften it to be agreeable or inflate it to sound rigorous.

## Output order

1. Audit result and one-sentence reason
2. Coverage: routes, states, widths, artifacts, and explicit gaps
3. System findings
4. Page-specific findings
5. Prioritized repair brief
6. Verification plan
7. Assumptions and untested areas

Keep P0 and P1 findings complete. Consolidate lower-value P2 polish so it does not bury consequential work.

## Quality guardrails

- Evidence over taste.
- User task over visual novelty.
- Exact context over vague claims.
- Root causes over duplicate symptoms.
- Brand adaptation over generic uniformity.
- Accessible clarity over decorative motion.
- Explicit uncertainty over invented certainty.

Do not use a fixed blacklist of gradients, rounded cards, large headings, or other fashionable patterns as proof of “AI design.” Flag a pattern only when it is generic, inconsistent, inaccessible, poorly matched to the product, or harmful to the user journey.
