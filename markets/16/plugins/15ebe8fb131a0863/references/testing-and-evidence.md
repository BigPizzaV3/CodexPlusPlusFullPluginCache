# Evidence and release gates

Evidence categories:
- `designed`: a specification exists.
- `implemented`: source code/assets created and inspected.
- `static-checked`: lint/compile/schema checks ran and passed.
- `runtime-checked`: executable or scene started and logged behavior.
- `interactive-checked`: actual inputs and end-to-end game loop were exercised.
- `export-checked`: packaged build installed/launched on a target.
- `human-playtested`: people actually played and provided subjective feedback.

Do not promote one category to another without recorded evidence. Required trace: command/test, environment, outcome, artifact path, error and follow-up.

Minimum new playable slice: launches, visible objective, effective input, challenge, feedback, win/lose/restart, no blocking errors. Also check asset licenses, focus/resize, pause and sound where applicable.

Automated tests should cover deterministic game rules separately from graphics/physics integration. A screenshot does not prove game controls; a build succeeds does not prove fun or playability.

Use `../../templates/evidence-report.md`; in root references this path is `../templates/evidence-report.md`.
