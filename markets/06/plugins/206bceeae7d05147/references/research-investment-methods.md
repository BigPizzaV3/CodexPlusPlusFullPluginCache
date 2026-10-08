# Investment methodology research memo

Checked: 2026-09-15. Scope: design of a multi-expert public-equity research plugin, not recommendations of particular securities. Sources below are primary research, regulator documentation, or the organization defining an industry metric. The workflow and implementation rules are design recommendations inferred from these sources; they are not a validated investment strategy.

## Central design decision

“Highest probability of success” and “highest return” are separate objectives and generally identify different candidates. Do not disguise their trade-off with a single impressive-looking score. Define success before screening: instrument, entry price and timestamp, horizon, currency, dividends, costs, benchmark, and minimum acceptable return. Keep four outputs separate: estimated success probability, expected total return, severe-loss exposure, and confidence in the evidence/model. A research-quality score is never a probability.

Use a Pareto frontier: a company is dominated only when another is at least as attractive on the selected objectives and strictly better on one. Then apply a declared ranking policy to the remaining candidates. A practical default is: meet evidence and survivability gates; disclose any user-imposed downside constraint; rank the feasible group by expected annualized wealth growth under several plausible probability sets; show adjacent-rank ties when uncertainty exceeds the difference. Also show separate probability-first and upside-first tables. The chosen utility or ranking policy is a user preference/design assumption, not an empirical law.

## Evidence architecture

### 1. Make data lineage part of each input

Each material fact should carry issuer identity, exchange/share class, CIK or equivalent local identifier, currency, units, period start/end, publication/acceptance date, retrieval time, filing accession, source URL and section, and whether reported, calculated, estimated, or assumed. Build a source ledger and a contradiction ledger before narrative synthesis. Distinguish different publications repeating the same management claim from independent evidence.

The SEC companyfacts APIs expose standard taxonomy, entity-wide facts; custom/segment metrics may be absent. Frames align approximately to calendar periods, which can conceal different fiscal dates. Therefore check the original statement and notes before comparing critical ratios; match tags, units, duration versus instant, and period boundaries. Do not sum cumulative nine-month cash flows with stand-alone quarters. Do not use the latest restatement in a point-in-time historical test. [S1, S2]

### 2. Normalize economics without erasing unfavorable costs

Create a GAAP-to-adjusted bridge, retaining recurring restructuring, stock compensation, maintenance capex, working-capital consumption, leases, acquisition economics, and dilution where relevant. Explain every adjustment and apply comparable definitions across peers. SEC guidance identifies misleading exclusions and emphasizes that free cash flow lacks one uniform definition; CFO minus capex does not automatically equal discretionary owner cash. [S3]

For each candidate, reconcile current shares, diluted share count, option/convertible obligations, cash, debt and minority interests. Treat forecast stock compensation consistently: either model its economic expense or resulting dilution/repurchase cost coherently; avoid charging both mechanically. Verify currency consistency between cash flows and discount rates. These are proposed model controls, not SEC-prescribed valuation rules.

## Valuation and expectation analysis

Use at least two genuinely different lenses when applicable: fundamental cash-flow valuation and economically comparable valuation multiples. Do not call two multiples derived from the same forecast independent confirmation.

Build a reverse valuation first: solve which sales growth, steady-state margin, reinvestment, or return on capital is consistent with the current price, holding other assumptions explicit. A price implies a family of assumptions, not a unique growth forecast. Compare that family with historical/peer reference classes and the company's operational capacity. Damodaran's examples directly demonstrate solving growth from price. [S4]

Then model coherent scenarios, linking growth to reinvestment and competitive fade. Match FCFF with WACC and FCFE/dividends with cost of equity. Show terminal-value share, discount-rate/terminal-growth sensitivity, and the assumptions that reverse the top ranking. For terminal perpetuities require discount rate above terminal growth. Include failure or refinancing outcomes where material, with explicit recoveries, timing, and dilution; do not assume perpetual survival.

Banks and insurers need equity-focused methods because debt and reinvestment are economically different from those of nonfinancial businesses. Use distributable capital, regulatory constraints, normalized ROE and an equity model rather than automatically applying industrial EV/EBITDA and CFO-minus-capex templates. [S5]

## Return and probability mechanics

For scenario s over T years, define terminal shareholder wealth W_s, including distributions under an explicit reinvestment convention, net of stated costs, in the investor's currency. Then R_s = W_s / P0 - 1 and CAGR_s = (W_s / P0)^(1/T) - 1. With mutually exclusive exhaustive scenario weights p_s summing to one:

- Expected total return = sum(p_s * R_s).
- Success probability = sum(p_s * I[R_s clears the predeclared hurdle]).
- Probability of terminal loss = sum(p_s * I[R_s < 0]).
- Annualized expected terminal wealth = (sum(p_s * W_s) / P0)^(1/T) - 1.
- Expected scenario CAGR = sum(p_s * CAGR_s), which generally differs from the previous quantity.

Do not call terminal loss a maximum drawdown estimate. Drawdown requires a price path; permanent impairment is a separate economic judgment. Benchmark outperformance requires matched benchmark scenarios or another explicit relative-return model; comparing a stock scenario to an unsupported fixed benchmark return manufactures certainty.

Three to five named scenarios are useful communication devices, not an empirically observed distribution. Label weights subjective unless supported by a documented estimation and validation procedure. If weights cannot be defended, publish an unweighted scenario envelope and rank conditionally; leave success probability unavailable. Report probability bands or rounded estimates with reference class, sample, horizon and adjustment rationale. Do not turn a confidence adjective or weighted checklist into “87% success.”

Separate ordinary uncertainty from structural ignorance. Stress alternate weights and joint assumptions; allow revenue growth, margins, financing conditions and terminal multiples to worsen together. A Monte Carlo model is optional and only useful when distributions and dependence are justified. Additional simulated paths do not create information about unknown parameters.

Bessembinder finds a strongly skewed historical stock-return distribution: a small fraction of companies accounts for aggregate net wealth creation over Treasury bills. Use this to demand tail-aware analysis and an explicit comparison with diversified alternatives, not to assume a today's candidate has a 4% chance of winning. Historical population statistics are not company-specific forward probabilities. [S6]

French's factor documentation supplies observable size, value, profitability and investment portfolio constructions. Use these as an attribution/control vocabulary so the plugin distinguishes a company-specific thesis from familiar factor exposures. They do not certify alpha or a universal scoring formula. [S7]

## Forecast accountability and validation

Save pre-outcome forecasts with immutable event definitions, horizon, as-of data, forecast probabilities, intervals and model version. Score resolved binary events using mean (p-y)^2, and use an appropriate proper score for full distributions or intervals. Proper scoring rules encourage honest probability statements; a good retrospective explanation is not a substitute for a forecast recorded beforehand. Show sample size and event dependence before claiming calibration. [S8]

Use a forward paper ledger before performance claims. If backtesting, preserve delisted names, splits, distributions, publication lags, transaction costs and historical universe membership. Record every material strategy/weight variation tried; repeated selection against the same “out-of-sample” history consumes its independence. Bailey and colleagues show why ordinary hold-out validation can be inadequate for investment backtests and propose an overfitting assessment framework. Do not imply that a single hold-out, a beautiful equity curve, or a high Sharpe ratio validates the plugin. [S9]

## Sector routing and material tangents

Require a sector specialist to replace generic ratios with relevant economics. Evidence-backed examples:

- Banks: test uninsured funding concentrations, deposit behavior, liquidity, asset/liability duration, unrealized losses and credit losses together. FDIC's First Republic review illustrates that reported regulatory capitalization can coexist with severe funding and interest-rate fragility. [S10]
- Drug developers: distinguish trial stages, clinical endpoints, statistical evidence, regulatory review, commercialization and funding runway. FDA describes different phase purposes; its broad stage-transition figures must not be copied as an asset-specific approval probability. Construct a conditional event tree and source indication/modality-specific reference classes separately. [S11]
- REITs: reconcile GAAP income and Nareit FFO; examine recurring property capex, leasing costs, occupancy, lease expirations and refinancing separately. Nareit FFO is a supplemental operating measure, not a complete shareholder cash-flow model. [S12]

Additional design checklists requiring live sector sources in each run: commodities (mid-cycle price, cost curve, depletion, reserves and sustaining capex); software (cohort retention, unit economics, sales efficiency, capitalization, dilution); semiconductors (cycle, utilization, export controls, customer concentration and committed capex); utilities (rate base, allowed versus earned return, financing, regulatory lag); insurers (reserve quality, combined ratio, investment book and catastrophe exposure).

Make tangential research causal and bounded: record the proposed chain “external development -> operating driver -> cash flow/balance-sheet effect -> valuation/return impact,” magnitude range, timing, confidence, evidence, and whether it can change the ranking. Investigate energy, water, supply chains, trade policy or technology substitution only when this chain is plausible. Park attractive but decision-irrelevant topics. Stop expansion when new evidence no longer changes decisions, with residual unknowns disclosed.

## Expert procedure and quality gates

1. Planner fixes the decision contract, universe definition, evidence map, sector modules, work products, dependencies and stopping rules before research.
2. Universe analyst finds candidates and an exclusion log, including less obvious adjacent beneficiaries; disclose coverage limitations instead of claiming every listed company was examined.
3. Evidence/accounting analyst builds auditable normalized inputs.
4. Industry specialist maps economics, competitive behavior and causal tangents.
5. Valuation analyst builds current-price expectations and coherent shareholder scenarios.
6. Probability/risk analyst builds reference classes, stress cases, dependencies and ranking sensitivity.
7. Independent skeptic receives facts and a bounded challenge before seeing consensus ranking; produces strongest countercase, thesis-breaking tests, and omitted alternatives.
8. Adjudicator resolves disputes by evidence quality, preserves consequential minority views, and computes ranking only after data/model checks.
9. Verification checks arithmetic, security identity, source entailment, dates, currencies, dilution, weighting totals, point-in-time consistency and formula labels.
10. Final report leads with ordered candidates and trade-offs, then detailed dossiers, scenarios, assumption sensitivities, failure conditions, price-dependent entry logic and a forecast/update ledger.

Do not force a winner. Permitted outcomes: credible ranking, tied tier, conditional winner, watchlist pending evidence, or no sufficiently supported opportunity. A long answer is justified by additional decision-relevant evidence, not repetition or claims of exhaustive thinking.

## Verified source register

All checked 2026-09-15. Sources S1-S5 and S7-S12 were opened successfully with the web tool. S6's SSRN record was retrieved in search with its author, abstract and revision date; direct opening returned an internal tool error, so the verified publisher abstract URL is also the selected direct source below (retrieved in search).

| ID | Primary source and direct URL | What it supports / limitation |
|---|---|---|
| S1 | [SEC: EDGAR APIs](https://www.sec.gov/search-filings/edgar-application-programming-interfaces) | API scope, taxonomy/entity limitations, unit arrays, calendar frame caveats. Documentation last reviewed April 8, 2025. |
| S2 | [SEC: Financial Statement Data Sets](https://www.sec.gov/dera/data/fsds.pdf) | As-filed data, amendments, duplicate/inconsistent records, metadata fields; original filings remain essential. |
| S3 | [SEC: Non-GAAP Financial Measures](https://www.sec.gov/rules-regulations/staff-guidance/corporation-finance-interpretations/non-gaap-financial-measures) | Recurring-cost exclusions, reconciliation, nonuniform FCF; document states last update December 13, 2022. |
| S4 | [Damodaran: Valuation Examples](https://pages.stern.nyu.edu/~adamodar/pdfiles/dcfveg.pdf) | Implied-growth solution, PDF pages 6-8; historical teaching example, not current valuation inputs. |
| S5 | [Damodaran: Valuing Financial Service Firms](https://pages.stern.nyu.edu/~adamodar/pdfiles/country/finsvce.pdf) | Cash-flow/discount-rate consistency, regulatory overlay, equity focus, especially PDF pages 11-13. |
| S6 | [Bessembinder (2018): Do stocks outperform Treasury bills?](https://www.sciencedirect.com/science/article/pii/S0304405X18301521) | Original research abstract, JFE 129(3), 440-457, DOI 10.1016/j.jfineco.2018.06.004; historical US sample, not a present forecast. |
| S7 | [Kenneth French: Developed-market five-factor construction](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/Data_Library/f-f_5developed.html) | Factor definitions and data construction; attribution vocabulary, not promised future premiums. |
| S8 | [Gneiting and Raftery (2007): Strictly Proper Scoring Rules, Prediction, and Estimation](https://sites.stat.washington.edu/people/raftery/Research/PDF/Gneiting2007jasa.pdf) | Proper scoring foundations; binary Brier score and distribution/interval scores. |
| S9 | [Bailey et al.: The Probability of Backtest Overfitting](https://www.davidhbailey.com/dhbpapers/backtest-prob.pdf) | Repeated trials, selection bias and hold-out limitations; framework is not a turnkey validation of this plugin. |
| S10 | [FDIC OIG: First Republic material loss review](https://www.fdicoig.gov/news/summary-announcements/material-loss-review-first-republic-bank) | Funding concentration, duration and liquidity interactions; a case study, not universal default probabilities. |
| S11 | [FDA: Step 3, Clinical Research](https://www.fda.gov/patients/drug-development-process/step-3-clinical-research) | Phase purposes and broad transition descriptions; not sufficient for company-specific clinical forecasts. |
| S12 | [Nareit: Funds From Operation](https://www.reit.com/glossary/funds-operation-ffo) | Industry-defined supplemental FFO measure and adjustments. |
