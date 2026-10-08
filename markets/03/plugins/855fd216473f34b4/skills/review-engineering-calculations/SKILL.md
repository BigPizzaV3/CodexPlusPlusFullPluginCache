---
name: review-engineering-calculations
description: Preflight engineering calculation memos, spreadsheets, equation sets, assumptions, unit conversions, and user-supplied code excerpts. Use for a preliminary evidence-based calculation review that independently recomputes supported arithmetic and flags dimensional, citation, and engineering-judgment gaps without certifying the work.
---

# Engineering Calculation Preflight

Produce a preliminary calculation-review report. Never claim to seal, stamp, approve, certify, or establish code compliance.

## Required workflow

1. Inventory every supplied file, sheet, equation, input, output, assumption, unit, cross-reference, and cited standard. Preserve exact file, page, cell, section, or equation locations.
2. Read `references/input-schema.md`, `references/report-schema.md`, and `references/safety-boundaries.md` before normalizing calculations or writing findings.
3. Extract supported arithmetic into one JSON package matching `references/input-schema.md`. Do not silently repair source values or equations.
4. Run `python3 scripts/check-calculations.py INPUT.json --output RESULTS.json`. The script uses only the Python standard library and safely parses arithmetic.
5. Reconcile script results with the source. Check signs, bounds, significant figures, spreadsheet references, assumptions, dependencies, and equation-to-result traceability.
6. Verify citations only against documents supplied by the user or public primary sources the host is permitted to access. Record “not verified” when the cited text or edition is unavailable. Never invent a citation, section, or requirement.
7. Write the report using `assets/report-template.md` and all sections required by `references/report-schema.md`.

## Severity

- `critical`: a demonstrated error could materially change a result or design decision, such as a consequential sign reversal or order-of-magnitude error.
- `major`: a material arithmetic, dimensional, reference, or missing-input issue that prevents reliance on the result.
- `minor`: a localized issue unlikely to change the engineering decision by itself.
- `observation`: clarification, traceability, or recommended verification with no demonstrated material error.

Do not assign `critical` or `major` merely because evidence is absent. State the gap and its consequence. Unsupported equations must be identified as unsupported, never guessed.

## Safety boundary

Refuse any request to stamp, seal, certify, approve, or represent the report as a licensed-engineer review. Offer the preliminary preflight plus a sign-off checklist for the responsible engineer. If an apparent condition presents an immediate safety risk, lead with the specific evidence and recommend stopping affected work under the user's established safety and engineering-review procedures.
