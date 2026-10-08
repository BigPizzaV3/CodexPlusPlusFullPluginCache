# Reader-First Research Template

Use **Decision View** unless the user explicitly requests scores, calculations, methodology, full workings, or an audit. Keep the conclusion above process detail. Full Panel depth does not require a long answer. Optimize Decision View for a phone screen: normally no Markdown tables, no more than six headings, and roughly 500–800 words for a Full Panel unless a higher-priority brevity request applies.

## Decision View

### Research conclusion

Open with the strongest research candidate or standardized illustrative model without directing a transaction. State the decisive tradeoff in one sentence. Do not reproduce volunteered personal financial facts or workflow metadata.

### Why this won

Give up to three compact, evidence-backed findings. Prefer:
- valuation / expected return
- quality / portfolio construction
- market, macro, or geopolitical risk compensation

When recent price behavior materially affects the result, include one compact regime sentence using the systematic horizon evidence rather than dumping a return table.

### Alternatives considered

For expanded/open universes, name the wider scout universe briefly and summarize no more than three finalists/models. Standardized model weights must be fixed and illustrative.

### Panel decisions — complete

This exact heading is mandatory before any aggregate vote, split, or statement that a role preferred a candidate.

For each participating voter render one line:

`**Analytical role → Candidate · High/moderate/low conviction.** Decisive reason. **Concern:** main risk.`

A Full Panel requires exactly these six voting lines before the result:
1. Portfolio Manager
2. Global Macro Strategist
3. Geopolitical Risk Analyst
4. Market Strategist
5. Fundamental Research Analyst
6. Portfolio Construction Analyst

For an individual-stock comparison, immediately after the Fundamental Research Analyst line add:

`**Graham growth sensitivity (bear / base / bull):** TICKER $X / $Y / $Z · ...`

Then state:
- **Panel result:** winner, reconciled vote count, overall conviction
- **Strongest dissent:** minority choice and why it matters
- **Chief Risk Officer:** verdict, strongest failure case, practical effect

Never state an aggregate vote before the complete corresponding ledger. Conviction uses words, not decimals.

### Valuation

Include only when it can change the decision. Show compact bear/base/bull value or ETF look-through valuation, current price/as-of date, key market expectation, and method. Detailed assumptions belong in Audit View.

### Risks and what could change the decision

Combine two or three decisive scenarios with the Chief Risk Officer's central concern. If historical/regime analysis mattered, include the observable condition that would change the regime label.

### Decision checklist

Give two or three evidence-based review triggers. For standardized portfolios, label all weights illustrative and disclose fixed assumptions. Do not prescribe recipient-specific sizing or execution.

Append the publisher-conflict statement and exact compact disclosure from `compliance.md`.

## Audit View

Append after the complete Decision View.

### Sequential gate record

| Stage | Analytical role | Candidate | Status | Decisive finding | Effect |
|---|---|---|---|---|---|

### Labeled score matrix

| Analytical role | Candidate A | Candidate B | Candidate C | Preferred | Confidence |
|---|---:|---:|---:|---|---:|

### Aggregation

| Candidate | Weighted mean | Disagreement penalty | Data penalty | Gate penalty | Final score |
|---|---:|---:|---:|---:|---:|

Write each calculation plainly and label every candidate.

### Market-history evidence

Include only when the module was triggered. Show common return definition/as-of date, 1M/3M/6M/YTD/1Y comparison, benchmark-relative returns, relevant extension metrics, regime label, and any history limitations. If an event study ran, show analogue, transmission match, differences, and outcome windows.

### Valuation workings

Use `valuation.md` including assumptions, reverse valuation, sensitivity, and method disagreement.

### Scenario matrix

| Scenario | Candidate A | Candidate B | Winner changes? |
|---|---|---|---|

## Completion check

Before sending:
- conclusion appears first
- all required voter lines precede any vote count
- Chief Risk Officer is separate and not counted as a voter
- raw score arithmetic appears only in Audit View unless explicitly requested
- comparisons use consistent as-of dates and definitions
- young-fund/common-window limitations are disclosed when relevant
- historical analogues are used only when transmission mechanisms match
- no recipient financial facts influence the result or appear in the output
- publisher-conflict statement and exact disclosure are present

On follow-ups, summarize what changed and rerun only affected work. Do not repeat the full report unless requested.
