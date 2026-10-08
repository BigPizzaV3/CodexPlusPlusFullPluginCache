# Preliminary-review report schema

The final report must contain these sections in order:

1. Executive summary: scope, overall result, material limitations, and count by severity.
2. Document and calculation inventory: every reviewed file, sheet, page, equation, and normalized calculation ID.
3. Findings table: ID, severity, exact source location, condition, evidence, independent result, consequence, and recommended verification.
4. Unit and dimensional audit: conversions, inconsistent dimensions, offset-temperature handling, and unitless assumptions.
5. Assumption and dependency gaps: missing loads, boundary conditions, material properties, system states, safety factors, or upstream results.
6. Citation ledger: citation as written, supplied/public source checked, edition, verification status, and exact evidence. Never add a source that was not checked.
7. Items requiring licensed-engineer judgment: governing criteria, model suitability, load path, failure modes, jurisdiction, and acceptability decisions.
8. Sign-off checklist: source completeness, calculations closed, findings resolved, current references confirmed, and responsible engineer review.

Use severity values exactly: `critical`, `major`, `minor`, `observation`. Clearly separate demonstrated errors from unresolved questions.
