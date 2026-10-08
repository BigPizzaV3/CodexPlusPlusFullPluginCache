# Research artifacts and continuation

Create a unique task-local run directory when file access is available. Keep intermediates in `work/` and user-facing files in `outputs/`, respecting the host's existing conventions. Do not write into the installed plugin. For restricted/read-only sessions, keep equivalent structured tables in the response and disclose persistence limits.

## Required records for a full dossier

| Artifact | Contents |
|---|---|
| research-plan.md | Scope, explicit procedure, stage status, task assignments, evidence gates, departures and completion summary |
| report.md | Finished dossier from the report template |
| rankings.csv | Segment, horizon, metric, growth rating/bounds, overlooked rating/bounds, confidence, event probability if defensible, rank/tier, caveats |
| evidence.csv | Claim/source rows with support or contradiction, original URL/path, date/period, geography, definition, units, lineage and verification status |
| assumptions.md | Critical assumptions, justification, plausible ranges, sensitivity, links to claims and forecast IDs |
| decisions.md | Initial versus revised judgments, disagreement, reviewer findings and resolution |
| calculations/ | Actual JSON inputs, outputs, and any additional economic-model calculations with units |
| forecasts.json | Dated, resolvable forecasts and previous versions preserved |
| state.md | Checkpoint for continuation: current stage, completed files, outstanding questions, tool limitations and next steps |

Adapt formats to the user's needs. Do not create empty boilerplate artifacts just to satisfy a file list; record an explicit omission when a calculation is unsupported or a small task needs less. CSV text fields must be quoted correctly. A source ledger can be a Markdown table for small dossiers.

## Forecast registration

Each forecast should record:

- Stable event ID and version ID; creation date and information cutoff.
- Question with metric, comparison baseline, scope, numerical threshold, and deadline.
- Exact resolution rule and preferred authoritative source; handling of data revisions, discontinuation, publication lag, and boundary changes.
- Subjective probability (0–1) only when defensible, with rounding appropriate to confidence; otherwise a clearly qualitative judgment.
- Reference class, pivotal evidence/assumptions, model/rubric version, and links to calculations.
- Confidence label and reason, separately from probability.
- Signposts with current reading, trigger threshold, expected observation date/source, and how the forecast would change.
- Outcome null until resolvable; resolution source/date; full revision history.

Suggested resolution convention for annual statistics: specify the first regular release after the forecast year plus a chosen revision cutoff, or specify the eventual revised series. Choose one before the outcome. A late publication does not mean the event failed. A changed market classification should trigger documented adjudication rather than an undocumented new target.

Keep the same economic-function boundary across baseline sources, models, report and registered event. Do not exclude a new delivery technology unless the original definition warrants that exclusion. Separate standalone products from bundled services consistently.

For an occurrence-by-deadline event, an observed qualifying occurrence may resolve true early; a failed trial normally cannot resolve the whole event false before the deadline. Define technical success with a named measurement/protocol and acceptance criteria before forecasting it. If those criteria cannot be specified from evidence, keep a qualitative watch item rather than an apparently precise resolvable claim. Missing coverage after the deadline can still leave an outcome unresolved.

The calculator's calibration format is a selected view of this register, with one comparable vintage per event. Preserve richer history in the underlying register.

## Checkpoint and resumption

Update state after each research wave and before a context break. Include absolute/usable artifact paths and the next executable step. On resumption, read the plan, state, outstanding issues, and necessary source records. Continue from completed work; recheck facts only when new time or evidence makes them stale. Never claim that an interrupted assignment finished.

Describe actual execution order, including work done concurrently and departures from the original plan. An independent estimate requires freedom from the preferred conclusion; it does not require the director to postpone all separate arithmetic. Do not retroactively describe parallel work as a completed serial procedure.

## Audit trail without reasoning transcripts

Record evidence, assumptions, decisions, calculations, alternative hypotheses, and concise explanations. Do not preserve private chain-of-thought transcripts. A reviewer should be able to reproduce the result from records and methods without needing internal deliberation.
