# Long-form research deliverables

Create a dated run folder in the user's working/output location, separate from installed plugin files. Use `../scripts/new_run.py` to initialize reusable templates when Python is available, or create the same artifacts manually. Never write research output into the plugin installation. Keep private user preferences within the run unless explicitly asked to remember them.

## Files

- `mandate.json`: adopted defaults, user overrides, industry, benchmark, as-of and version.
- `plan.md`: procedure checklist, assignments/dependencies and acceptance criteria, followed by progress.
- `universe.csv`: discovered companies, economic exposure, evidence and exclusion/status reasons.
- `evidence.csv`, `contradictions.csv`, `assumptions.csv`, `tangents.csv`: traceable inputs and open questions.
- `briefs/`: bounded specialist outputs with provenance.
- `scenario-input.json` and `ranking.json`: actual populated model and reproducible calculation output, when weights are supportable. The initializer intentionally does not create a fake model.
- `report.md`: substantial user-facing memo with direct citations near claims.
- `forecast-ledger.csv`: dated testable future events and forecasts.
- `checkpoint.md`: current stage, model version, unresolved issues and next steps.

## Report order

1. **Decision summary:** ranked candidates or tied tiers; best-supported candidate; conditional nature; why the leader beats the runner-up; no-qualifier conclusion when appropriate. Date, universe, price basis, horizon, currency and benchmark are visible.
2. **Ranking table:** ticker/exchange, price/as-of, scenario return range, expected total return, annualized expected terminal wealth, modeled success probability or unavailable, severe-loss exposure, evidence confidence with reasons, frontier/status. Label probabilities conditional and distinguish central vs stress metrics.
3. **Mandate and completed procedure:** objective, policy thresholds, universe coverage, omissions, tools/sources, actual delegation mode, plan changes and important unfinished work.
4. **Industry economics:** demand vs shareholder value capture, value chain, profit pools, competition, cycle and causal tangents. Include adjacent beneficiaries and alternatives that failed screening.
5. **Finalist dossiers:** business model; durable advantage and its limits; normalized finances; reinvestment runway; governance/capital allocation; market-implied expectations; valuations and assumptions; scenarios; strongest countercase; failure conditions; price sensitivity; monitoring tests. Tie every conclusion to causal evidence.
6. **Comparative adjudication:** common assumptions, rank reversals, dissent, tied tiers, alternative probability-first/upside-first orderings, comparison with diversified benchmark exposure. Explain meaningful tradeoffs instead of hiding them in one score.
7. **Risk and evidence limits:** current-data gaps, model uncertainty, terminal-value dependence, tail outcomes, financing/dilution, correlation and what cannot be estimated.
8. **Next evidence and monitoring:** thesis-breaking observations, expected dates and sources, predefined forecast events, when reranking is warranted. No scheduled monitor unless requested.
9. **Appendices:** source ledger, accounting bridges, scenario inputs/calculations, excluded universe, assumption changes and completed checklist.

Show formulas and compact tables where they clarify. Quote sources sparingly; paraphrase with attribution. Include source dates and document locations. The narrative should explain why numbers and risks matter. Do not dump raw tools, fabricate citations, call a qualitative score a probability, or imply a fully tested investing track record.
