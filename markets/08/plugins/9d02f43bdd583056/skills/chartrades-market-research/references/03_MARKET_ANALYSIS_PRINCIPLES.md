# Market Analysis Principles

Never claim database facts unless a live Chartrades MCP tool returned them.

Never invent:

- fields
- metrics
- scores
- wallet identities
- journal records
- timestamps
- prices
- endpoint results
- live market conditions

If a field is not returned, do not mention it as fact. If a tool fails, say the tool failed; do not convert a tool failure into market evidence.

## Evidence Grades

Strong evidence:

- fresh internal data
- multiple independent signals agree
- price confirms the read
- no critical freshness or coverage warnings

Medium evidence:

- the main read exists
- several signals agree
- one important confirmation is missing, stale, capped, or sample-limited

Low evidence:

- data is stale, capped, thin, contradictory, missing, or sample-limited

No valid read:

- the tools did not return enough usable data

Do not turn weak evidence into a confident conclusion.

## Price, Flow, And Confirmation

Positive flow without price confirmation is not automatically bullish.

Negative flow without price breakdown is not automatically bearish.

Large flow values need sanity-checking against price reaction, liquidity, coverage, and distortion flags.

Volume spike alone is not a trade signal.

Price movement without volume or flow confirmation is weaker.

Divergence means evidence layers disagree. Divergence is not automatically a reversal.

## Scores

Do not compare scores unless the live API or live docs says they are on the same scale.

Common score families may include:

- direction scores
- raw pressure or magnitude scores
- quality scores
- confidence scores

Quality scores describe data quality, not bullishness or bearishness.

If the score scale is unclear, ask the live API docs through `help` or `get_docs`, or say the scale is unclear.

## Trade Intent And Optional Setups

A directional bias is not the same as an executable setup.

Ordinary market analysis is analysis-only. Do not volunteer entry, stop, target, R:R, tradeable, or no-trade conclusions for an outlook, directional question, scan, mover, flow read, or wallet question.

Only evaluate tradeability after the user explicitly requests a setup or opportunity and the live MCP catalog exposes an appropriate optional-trade tool. If that tool says no trade, no valid setup, stale data, poor structure, thin book, or weak confirmation, report it directly.

Do not manufacture entries, stops, targets, risk-reward, or invalidation levels unless a live tool returned them.

Do not present diagnostic-only values as actionable.

A geometry-cleared setup is not automatically performance-validated. Keep geometry and validation separate, and describe measured positive edge only when the returned validation state supports it.
