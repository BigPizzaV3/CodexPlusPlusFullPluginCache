<!-- Generated loss-aware reference mirror from God_Level_Public_Company_Financial_Analyst_Job_Guide_V6_99_ALL_SUB70_FIXED.docx. Canonical source remains the bundled DOCX. -->

<!-- Appendix: B | Title: INSTITUTIONAL MODEL BUILD STANDARD -->

# APPENDIX B - INSTITUTIONAL MODEL BUILD STANDARD

| Tab / layer | Required contents | Control |
| --- | --- | --- |
| 00 Cover / Control | Company, ticker, valuation date, model version, scenario, analyst, last filing | No output can be published without current valuation date and source status |
| 01 Sources | URL/accession, date, filing period, table/section, definition notes | Every material historical input maps to a source |
| 02 Historical IS | Reported and normalized income statement | Tie to filed statements and amendments |
| 03 Historical BS | Reported and normalized balance sheet | Assets = liabilities + equity |
| 04 Historical CF | Reported and normalized cash flow statement | Beginning cash + movements = ending cash |
| 05 Segments/KPIs | Segment and operating-driver history | Segments reconcile to consolidated or difference explained |
| 06 Assumptions | All forecast assumptions and scenarios | No hidden constants in forecast formulas |
| 07 Revenue driver | Units/customers/capacity/price/mix build | Historical driver model reconciles to revenue |
| 08 Margin/cost | Variable/fixed/step cost architecture | Incremental margin economically plausible |
| 09 Fixed assets | PP&E/capex/depreciation/intangibles | Beginning + capex/acquisition/FX - depreciation/disposal = ending |
| 10 Working capital | AR, inventory, AP, deferred revenue, contract balances | Driver days/turns calculated consistently |
| 11 Debt/interest | Instrument, maturity, rate, covenants, revolver, lease/debt-like claims | Interest links to average balance and rate |
| 12 Taxes | Book tax, cash tax, NOLs, deferreds, discrete items | Cash tax forecast reconciles to economics |
| 13 Shares/dilution | Basic shares, awards, options, converts, issuance, repurchases | Diluted share roll-forward ties |
| 14 Forecast statements | Integrated IS/BS/CF | BS balance and cash roll-forward pass in every scenario |
| 15 Scenarios | Base, bull, bear, stress, thesis break | Operating drivers change coherently |
| 16 Valuation | DCF, multiples, reverse DCF, SOTP if needed | EV-equity bridge and dilution complete |
| 17 Dashboard | Decision variables, sensitivities, catalysts, risks | No decorative KPI without a decision use |
| 18 Checks | Reconciliation, sign, units, dates, scenario, circularity | All critical checks must be green before distribution |



## Formula engineering rules

- Use one formula pattern across a row when economics are the same. Break the pattern only with a written reason.

- Never hard-code a forecast output inside a formula. All assumptions belong in the assumptions layer or a clearly labeled scenario table.

- Use named ranges sparingly and transparently. A reviewer should be able to trace a formula without a hidden dependency graph.

- Use average balance for ratios that compare a period flow with a balance stock when seasonality or growth makes period-end balances misleading.

- Document intentional circularity and convergence settings. Prefer algebraic solutions when practical.

- Use explicit error flags for #N/A, #DIV/0!, broken source links, missing periods, stale market prices, and scenario inconsistencies.

- Protect reported history from accidental overwrite. Normalize in a separate layer with a reconciliation back to reported data.
