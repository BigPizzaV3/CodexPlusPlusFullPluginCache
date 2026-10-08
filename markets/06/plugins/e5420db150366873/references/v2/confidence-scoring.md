
# Evidence Freshness and Research Confidence

Confidence describes the research package, not the probability that a stock will rise. Calculate it from auditable components and show deductions.

Default research-confidence weights:

- evidence coverage: 25
- source quality and independence: 20
- historical and cross-source consistency: 15
- model reconciliation: 15
- contradiction resolution: 10
- forecast uncertainty discipline: 10
- evidence freshness: 5

Each component is scored from 0 to 100. The weighted total must come from the deterministic scorer. A high score is prohibited when a mandatory gate is open, a key valuation input has no provenance, point-in-time integrity is broken, or a material contradiction is hidden. In those cases cap the score at 59 and label the research incomplete.

Freshness is claim-specific. Assign a shelf-life category and compare the source date with the research cutoff: market data 1 day; filings 120 days unless a newer filing exists; guidance 120 days or until the next update; capital structure 30 days; management roles 30 days; industry structure 365 days; durable accounting policy 730 days unless amended. Override a default only with a written reason.
