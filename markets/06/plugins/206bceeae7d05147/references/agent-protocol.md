# Specialist coordination and verification

## Ownership and order

The council director owns the mandate, plan, canonical assumptions, model versions and final ranking. Specialists own bounded investigations and their evidence. Assign multiple roles to one worker when appropriate; role count is not agent count.

| Stage | Skill / analytical owner | Dependency |
|---|---|---|
| 1 | equity-council / mandate and procedure director | User industry |
| 2 | equity-universe / industry economist and value-chain analyst | Mandate |
| 3A | equity-business / business quality and competition | Screened universe |
| 3B | equity-financials / forensic accountant | Current filings |
| 3C | equity-stewardship / governance and capital allocation | Filings and proxy |
| 3D | equity-risk / macro, financing, regulation and technology risk | Industry map |
| 3E | equity-catalysts / expectations and market structure | Price and business facts |
| 4 | equity-valuation / valuation and probability modeling | Reconciled 3A–3E inputs |
| 5 | equity-red-team / independent thesis challenger | Neutral facts first; draft second |
| 6 | equity-audit / source and calculation verifier | Sources and questions first; draft second |
| 7 | equity-council / investment committee adjudicator | Corrected models and dissent |
| Later | equity-update / forecast accountability | Saved run and new evidence |

## Real delegation

When the host offers subagents and permits their use, delegate independent industry/company investigations, red-team work and verification. Use actual host tools and their current schemas; do not invent an API or create user-owned tasks as a substitute. Inspect available concurrency and queue work in waves. Keep dependent edits sequential. Do not give multiple workers ownership of a shared model file. Workers may write only their assigned dossier/ledger fragments; the director merges by claim ID and resolves conflicts. Do not recursively spawn committees unless a concrete bounded subtask justifies it and capacity permits.

If delegation is unavailable, carry out each specialist pass sequentially, labeling this clearly as a single-agent workflow with separate analytical lenses. Never claim independent agents or independent confirmation in that mode. Run quality controls in either mode. Different agents using the same model/source are correlated, not independent samples of truth.

## Assignment contract

Use this compact payload, populated with real paths and questions:

> You own [specific question] for [industry/company], under [mandate version and cutoff]. Read [skill path] and these source/input IDs: [list]. Deliver [assigned file] with supported claims and direct source locations, assumptions, numerical impacts where supportable, strongest counterevidence, missing data, and what would change the conclusion. Do not select the final winner or infer another worker's conclusion. Do not treat another agent's assertion as a source. Stay within this question and write only the assigned file. Finish when [observable condition]; return incomplete status if [dependency] is missing.

Return every specialist brief with: scope; 3–7 decisive findings; evidence/claim IDs; calculations and units; assumptions/ranges; counterevidence; unresolved questions with decision impact; handoff inputs; confidence rationale; status (complete / conditional / blocked). Small tasks may use fewer findings. Reasoning summaries should explain mechanisms, not expose internal deliberation.

## Reduce anchoring

Collect initial business, financial, and risk conclusions before sharing a favorite. Give the skeptic a neutral evidence packet and the strongest uncertainty first. Give the auditor neutral reconstruction questions and original source locations before revealing draft answers. Then compare outputs. This separation is a workflow precaution, not proof of statistical independence.

Examples of neutral questions: What is the current fully diluted share count? Which period does this cash-flow value cover? What terminal revenue and margin are needed for this entry price? What could prevent shareholders from receiving the forecast cash? Recompute results with code; check source entailment by opening the cited section.

## Resolve differences without voting

Classify each conflict: factual, definition/period, causal, forecast, or preference. Resolve factual disputes from original sources; resolve definitions through the normalization bridge. Preserve alternative coherent forecasts as sensitivity sets. Ask the user only if an unresolved preference materially changes the decision. Record the losing interpretation and why it lost; unresolved dissent stays in the final memo. Agreement does not mechanically increase any probability.

Maintain a checkpoint after each stage: completed tasks, source cutoff, model version, unresolved decision questions, assigned files, next stage. Resume by reading artifacts and reconciling them against the original mandate. Do not treat an earlier narrative summary as verified current data.
