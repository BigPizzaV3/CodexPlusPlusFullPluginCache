# Source and data standards

## Claim ledger

Use `../templates/evidence.csv`. Every material input or claim needs a stable claim ID and source ID. Include direct URL, issuer/security identity, document and section/page/table, event/financial period, publication date, retrieval timestamp, units, currency, accounting basis, original source lineage, and status: reported / management claim / assumption / calculated / unknown. For calculations, list input claim IDs and formula/script version. A URL alone is not support: check that the source entails the claim.

Prefer filings and notes for reported accounts; official regulator sources for applicable rules; issuer releases for management statements; source-dated market data for prices; genuinely independent primary/secondary research for contesting management's story. Issuer forecasts are evidence of management expectations, not verified future facts. Search snippets are discovery aids; open the underlying source for a material claim. If inaccessible, label snippet-only/secondary coverage and do not pretend to have read the original.

Two articles repeating one release have one evidence origin. Track the origin_id field. Distinguish a statement's publication date, the event date and financial period. Preserve data vintages: do not quietly use a later restatement in historical analysis. Check latest annual and interim reports and subsequent material events, even when a database value appears clean.

## Market snapshot

Freeze an as-of timestamp, exchange timezone, return currency and comparable price basis. Default to the latest completed trading session available at research start, refresh before final publication, and disclose any asynchronous quotes. Check splits, spin-offs, rights, special dividends and ADR ratios. A price older than five trading sessions is a default stale-data flag, not a universal market rule; stricter freshness is appropriate after material news. If a decisive current price cannot be verified, remove actionable rank status and show only conditional valuation/entry thresholds.

## Accounting normalization

- Align fiscal periods and duration vs instant values. Derive standalone quarters from consistent cumulative values; do not add nine-month cumulative CFO to annual CFO.
- Confirm USD vs thousands/millions, reporting vs trading currency, stock vs flow, fiscal vs calendar periods, basic vs diluted vs actual shares, continuing vs discontinued operations, and restatements.
- SEC companyfacts may omit custom or segment metrics; a missing tag is not zero. Inspect units, accession and period. SEC frames approximately align calendar periods and can conceal different fiscal calendars.
- Reconcile GAAP/IFRS and adjusted measures with original notes. FCF has multiple definitions. Separate recurring economic costs from genuinely nonrecurring items.
- Build a share-count bridge including issuance, options/RSUs, convertibles, repurchases and acquisition consideration. Do not equate weighted-average EPS shares with the current share base.
- Treat SBC consistently: model economic cost or coherent future dilution/offsetting repurchases; do not mechanically deduct the same cost twice.
- Keep cash flows, discount rates, terminal values and enterprise-to-equity adjustments in compatible currencies and definitions.

## Evidence gates

For every finalist verify: security/price; latest reported financials; cash/debt/maturities; share count and dilution; the two most important thesis claims; material legal/regulatory status; terminal valuation assumptions; benchmark method. A missing mandatory item means conditional/watchlist status when its uncertainty could alter ranking. The human `evidence_eligible` input to the calculator records this decision; the script cannot certify it.

An audit checks all decisive claims for the leading candidates and a risk-based sample of supporting claims. State the coverage actually checked. Do not claim every sentence was independently verified if only a sample was reviewed. Preserve unresolved source conflicts in `contradictions.csv` and state their return/ranking impact.
