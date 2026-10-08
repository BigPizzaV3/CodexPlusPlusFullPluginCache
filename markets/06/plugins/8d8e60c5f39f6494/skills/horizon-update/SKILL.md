---
name: horizon-update
description: Revisit a saved industry forecast, update probabilities and rankings from new evidence, and score resolved predictions. Use for forecast maintenance, signpost reviews, and calibration reports.
---

# Forecast update and calibration

Read [artifact contracts](../horizon-forecast/references/artifact-contracts.md), [evidence method](../horizon-forecast/references/evidence-method.md), and [calculation interface](../horizon-forecast/references/calculation-interface.md).

1. Load the original forecast, scope, probabilities, assumptions, source ledger, and version history. If absent, ask for its location while preparing the update procedure; do not reconstruct an allegedly original forecast from memory.
2. State the update plan, new as-of date, and what evidence would justify revision. Search fresh data for registered signposts and important unexpected events.
3. Separate genuine new information from duplicate coverage, noise, and changed definitions. Preserve the original deadline unless the user requests a new forecast; a rolling horizon is a separate event.
4. Re-estimate affected assumptions and scenarios. Record previous and revised probabilities, reason, source, and ranking impact. Avoid arbitrary precise likelihood ratios; use Bayesian numerical updating only when the likelihood assumptions are defensible and dependencies handled.
5. Resolve an event only under its predeclared rules using observed outcomes. A revised source series or ambiguous classification may require a pending/ambiguous outcome. Never resolve a missing measurement as failure.
6. For resolved binary events, use the calculator's Brier report. Choose one forecast vintage per event at a comparable lead time, or explicitly define a separate time-weighted evaluation. Show sample size and comparator. Do not claim calibration from a handful of favorable outcomes.
7. Deliver a concise change summary plus an updated full record, unresolved events, observed error patterns, and next signposts. Preserve earlier versions and denominators; report failures as well as successes.

Define monitoring indicators freely; create a recurring automation only if the user asks for it and the host supports it. Normal research updates do not modify global memories or the installed plugin's defaults. For genuine historical validation, use archived information and acknowledge that model training may still contain later outcomes; prospective frozen forecasts are stronger evidence.
