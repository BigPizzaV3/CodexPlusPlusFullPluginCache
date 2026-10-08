<!-- Generated loss-aware reference mirror from God_Level_Public_Company_Financial_Analyst_Job_Guide_V6_99_ALL_SUB70_FIXED.docx. Canonical source remains the bundled DOCX. -->

<!-- Master Lab: 02 | Title: INTEGRATED THREE-STATEMENT MODEL BUILD FROM RAW FILINGS -->

# MASTER LAB 02 - INTEGRATED THREE-STATEMENT MODEL BUILD FROM RAW FILINGS

> Purpose: teach the complete build process for an auditable public-company model. The target is not a pretty spreadsheet. The target is a model in which a reviewer can trace every historical number to a source, every forecast to an economic driver, every statement through double-entry logic, every scenario through a small set of explicit assumptions, and every valuation output back to the operating model.

## Required model package

- Source log and assumptions register.

- Historical income statement, balance sheet, cash flow statement, and segment/KPI history.

- Driver schedules for revenue, margins, working capital, capex, depreciation, taxes, debt, cash, share count, and material non-operating items.

- Integrated forecast statements with automated balance and cash checks.

- Base, bull, bear, stress, and thesis-break scenarios that change operating drivers rather than only valuation multiples.

- Valuation tabs linked to the operating model, plus a reverse-expectations view.

- Visible model checks, change log, and reviewer sign-off block.

## 1. Workbook architecture and non-negotiable conventions

Use a modular architecture. The exact tab names may change, but the separation of raw source data, standardized historicals, assumptions, operating schedules, statements, valuation, scenarios, and checks should remain clear. Avoid a single giant sheet where inputs, calculations, and outputs are mixed.

| Layer | Typical tabs | Rule |
| --- | --- | --- |
| Control | Cover, Source Log, Assumptions, Change Log | Every material input has owner, source, date, unit, period, and status. |
| Raw data | 10-K, 10-Q, XBRL extracts, KPI extracts | Do not overwrite source data with analyst normalization. |
| Normalized history | Historicals, Segments, KPIs | Reported and adjusted views reconcile through explicit bridges. |
| Operating schedules | Revenue, Costs, WC, Capex, Tax, Debt, Shares | Forecast from drivers and roll-forwards. |
| Statements | IS, BS, CF | No hard-coded forecast subtotals that bypass schedules. |
| Scenarios | Scenario assumptions, sensitivity matrix | One scenario switch or explicit scenario set controls the forecast. |
| Valuation | DCF, Multiples, Reverse DCF, SOTP if needed | Valuation pulls from statements or schedules, never duplicate hard-coded forecasts. |
| Quality control | Checks, Diagnostics | All material reconciliations visible and designed to fail loudly. |

Use consistent sign conventions. One workable standard is positive revenue and expenses shown as negative only where the model logic requires it, or all statement lines shown in presentation sign with cash-flow formulas handling direction explicitly. Whichever standard is chosen, document it and never mix conventions silently.

Separate inputs from formulas visually using your organization standard, but do not rely on color as the only control. A reviewer should identify an input from cell comments, labels, named ranges, or a dedicated assumption block. Every forecast formula should have a readable causal path.

## 2. Build the source layer before the forecast

1. Record the filing and reporting period for every historical column.

1. Capture the audited annual statements first, then reconcile interim periods to annual totals.

1. Store raw values in reported units and retain the filing definition.

1. Map source line items into standardized model line items through a mapping table rather than rewriting the source.

1. Create an exceptions log for recasts, discontinued operations, segment changes, fiscal-year changes, acquisitions, and accounting-policy changes.

1. Lock the reported historical layer after reconciliation so later analyst adjustments cannot silently replace it.

### Source mapping table

| Source label | Model label | Source period | Unit | Normalization | Check |
| --- | --- | --- | --- | --- | --- |
| Net sales | Revenue | FY2025 | USD mm | None | Ties to statement |
| Revenue - Product | Product revenue | FY2025 | USD mm | Segment recast if needed | Segments sum to consolidated |
| Share-based compensation | SBC | FY2025 | USD mm | Reclassified by function if disclosed | Matches cash-flow add-back and footnote |
| Capital expenditures | Capex | FY2025 | USD mm | Separate acquisitions and finance leases | Matches PP&E roll-forward where possible |

## 3. Historical normalization and definition control

Never force historical comparability by deleting reported history. Maintain a reported series and a constant-definition analytical series. If the company recasts segments, changes KPI definitions, acquires a major business, changes fiscal year, or shifts gross-versus-net revenue presentation, document both the company recast and your own analytical bridge.

Constant-definition growth = Comparable current-period measure / Comparable prior-period measure - 1.

For each adjustment, record whether it changes revenue, operating profit, cash flow, invested capital, or only presentation. The model should be able to reproduce published numbers before any analyst normalization is applied.

## 4. Revenue build: forecast the economic engine

Choose the smallest set of drivers that explains the business without hiding risk. A model with 200 product rows can be less useful than a 10-driver model if the 200 rows simply extrapolate historical growth. The correct granularity is the level at which pricing, volume, capacity, customer behavior, or mix can change differently and materially affect value.

| Business type | Primary revenue drivers | Useful cross-checks |
| --- | --- | --- |
| Subscription software | Beginning ARR, new ARR, churn, expansion, price, FX | RPO, billings, deferred revenue, customer count, NRR |
| Semiconductor | Units, wafer starts/capacity, yield, ASP, mix, utilization | Inventory, lead times, design wins, foundry capacity, end-market sell-through |
| Industrial project | Backlog, bookings, conversion, price, scope, execution timing | Book-to-bill, project milestones, working capital, capacity |
| Marketplace | GMV or transactions, take rate, ads/services, buyer/seller activity | Payment volume, active users, cohort behavior, gross-versus-net presentation |
| Bank | Average earning assets, loan growth, securities, yields, deposits, funding cost | NIM, deposit beta, credit losses, capital |
| Commodity producer | Volume, grade/yield, realized price, benchmark differentials | Reserves, cost curve, hedges, sustaining capex |

### Subscription revenue mechanics

Ending ARR = Beginning ARR + New ARR + Expansion ARR - Churn ARR - Contraction ARR + FX or scope effects.

Approximate subscription revenue depends on average in-period ARR and revenue-recognition timing, not simply ending ARR.

Use cohort or installed-base logic when retention is central. For usage-based models, separate committed minimums from variable consumption. For price increases, model realized price after discounting, seat consolidation, downgrade behavior, and churn response rather than applying list-price change directly to revenue.

### Capacity-constrained revenue

Units shipped = MIN(Demand units, Effective capacity units) when capacity is binding.

Effective capacity = Nameplate capacity x Utilization x Yield, adjusted for downtime, mix, and ramp losses where relevant.

If capacity is the binding constraint, a top-down TAM growth rate is not a forecast. Model commissioning dates, ramp curves, equipment lead times, labor, permits, power, upstream supply, yield, and customer qualification. Revenue cannot exceed the physical system unless the definition changes.

## 5. Price, volume, mix, and FX bridge

For businesses with unit data, decompose growth into volume, price, mix, currency, acquisitions, and other scope. Multiplicative interactions mean the components will not always add cleanly. Use a bridge method and keep an explicit residual when disclosure is insufficient rather than forcing a false decomposition.

Revenue = Units x Realized price per unit for a simple single-product case.

For multi-product portfolios: Revenue = SUM(Units_i x Realized price_i). Mix changes when the weights of products or customers change.

A reported price increase is not always pricing power. Separate inflation pass-through, surcharge, scarcity pricing, mix shift, geography, contract repricing, and true willingness-to-pay. Model the margin consequence because price that merely passes through higher cost may lift revenue without improving value.

## 6. Cost and margin architecture

Classify costs into variable, fixed, semi-variable, pass-through, step-function, and discretionary buckets. Then map each major cost to its driver. COGS may depend on units, material input prices, yield, utilization, freight, warranty, depreciation, and mix. Operating expense may depend on headcount, compensation per employee, sales capacity, R&D program count, facilities, and variable commissions.

Contribution margin = Revenue - truly variable operating costs.

Incremental operating margin = Change in operating profit / Change in revenue, over a period where definition and scope are comparable.

Do not extrapolate margin solely from historical percentage trends. Identify where fixed costs step up. A data center, fab, sales organization, or distribution network can create periods of strong incremental margin followed by discrete capacity investment.

### Utilization and absorption

For manufacturing, low utilization can depress gross margin through under-absorbed fixed costs. Model fixed manufacturing cost separately from variable unit cost. When utilization rises, gross margin can improve even without price or product-cost improvement. That effect may reverse if capacity expands ahead of demand.

## 7. Headcount and compensation build

When labor is material, model average headcount by function, hires, attrition, compensation per employee, variable compensation, payroll taxes, and stock compensation. For rapidly scaling companies, ending headcount multiplied by annual compensation can overstate expense because hiring occurs throughout the year. Use average headcount or cohort timing.

Personnel expense ≈ Average headcount x cash compensation per employee + benefits/payroll burden + SBC, with function-specific assumptions where material.

Link sales headcount to bookings capacity only after accounting for ramp time and quota attainment. Link engineering headcount to roadmap capacity cautiously because output is not linear in headcount. Use headcount primarily as a cost and capacity constraint, not a simplistic productivity guarantee.

## 8. Working-capital schedules

Build receivables, inventory, payables, contract assets, deferred revenue, and other material operating balances from their drivers. Use days or turnover ratios only where the denominator matches the economic process and where business mix is stable.

Accounts receivable ending can be modeled from DSO and revenue, but collections and billing schedules are superior when available.

Inventory ending can be modeled from forward COGS and target days, adjusted for lead time, safety stock, seasonality, launch inventory, and obsolescence.

Deferred revenue depends on prebilling and recognition timing, not revenue alone.

Add cash-flow sign checks. An increase in an operating asset generally consumes cash; an increase in an operating liability generally provides cash, subject to classification and specific account economics. Make the schedule show both balance and period change so sign mistakes are visible.

## 9. Capex, depreciation, and asset roll-forward

Separate capital spending into maintenance, growth, capitalized software or development, construction in progress, and acquisition-related asset additions. Build depreciation from asset cohorts or a simplified useful-life schedule when material. A flat depreciation percent of revenue can become wrong quickly when capex cycles are lumpy.

Gross PP&E ending = Gross PP&E beginning + Capex + acquired assets + FX/reclasses - gross disposals.

Accumulated depreciation ending = Beginning accumulated depreciation + depreciation expense - accumulated depreciation on disposals +/- reclasses.

For capacity projects, model spend curve, in-service date, ramp, depreciation start date, and revenue capacity separately. Construction cash can leave years before the asset reaches mature utilization.

## 10. Taxes and NOL schedule

Build pretax book income, permanent differences, temporary differences, jurisdiction mix, NOL usage, tax credits, valuation allowance changes, and cash taxes at the level needed for the thesis. For most companies, a simplified tax schedule can be accurate if the major drivers are explicit. For companies with large NOLs, cross-border structures, or major stock-compensation tax benefits, the schedule must be more detailed.

Cash taxes = Current taxes payable adjusted for payment timing, refunds, settlements, withholding, and material discrete items.

Do not use a single reported effective rate as the perpetual tax rate without examining why the rate differs from statutory. The model should distinguish near-term shield utilization from steady-state tax economics.

## 11. Debt, interest, liquidity, and cash sweep

Create a debt schedule by instrument with opening balance, mandatory amortization, optional repayment, new issuance, maturity, base rate, spread, floor, fixed coupon, hedges, original issue discount where material, and covenant classification. Link cash interest to average debt balance and instrument rate.

Interest expense by instrument ≈ Average debt balance x effective interest rate, plus amortization and fees where material.

Model revolver draws as a liquidity backstop only after defining minimum cash, operating cash needs, covenant capacity, borrowing base, and other restrictions. A model that automatically draws infinite revolver capacity hides distress.

### Circularity control

Interest depends on debt, debt may depend on cash flow, and cash flow depends on interest. Use a controlled circularity switch or an explicit iterative mechanism. The model must converge under all scenarios. If circularity is disabled, use beginning or average balances with an explicit approximation and quantify the error.

## 12. Share count, repurchases, issuance, options, RSUs, and convertibles

Build basic shares, weighted-average shares, awards vesting, option exercise dilution, performance share payout, employee plan issuance, repurchases, acquisition shares, capital raises, and convertible treatment. Distinguish share count for EPS from period-end shares used for market capitalization.

Equity value per share = Equity value / fully diluted forward share count appropriate to the valuation date and award mechanics.

When repurchases are modeled, connect cash spent, average repurchase price, shares retired, and offsetting employee issuance. Avoid using repurchases as a mechanical EPS accretion plug. Capital allocation should be a separate assumption with liquidity and valuation discipline.

## 13. Build the statements only after the schedules

The income statement should pull revenue and cost schedules, not forecast them independently. The balance sheet should pull working capital, PP&E, debt, leases, taxes, acquisitions, equity, and cash schedules. The cash flow statement should calculate from net income and balance-sheet movements, then reconcile ending cash to the balance sheet. This architecture ensures that a driver change flows through all statements.

1. Complete revenue and operating-cost schedules.

1. Calculate operating profit and taxes.

1. Complete working capital and capex/depreciation schedules.

1. Complete debt, interest, and share schedules.

1. Build the income statement.

1. Build the balance sheet excluding ending cash if cash is the balancing output.

1. Build the cash flow statement from net income and schedule movements.

1. Calculate ending cash from beginning cash plus cash flows.

1. Link ending cash to the balance sheet.

1. Run the balance check and investigate any nonzero difference.

## 14. Scenario system design

A scenario is a coherent economic state, not a list of independent optimistic or pessimistic percentages. Write the causal story first. For example, a bear case might combine slower end demand, lower utilization, price pressure, inventory build, delayed capacity expansion, tighter working capital, and reduced capex. Some variables may improve in a bear case, such as growth capex or labor needs. Preserve those causal interactions.

| Scenario | Demand | Price/mix | Margins | Working capital | Capital / financing | Purpose |
| --- | --- | --- | --- | --- | --- | --- |
| Base | Most evidence-supported path | Contract and market assumptions | Normalized execution | Normal operating range | Funded plan | Central underwriting case |
| Bull | Evidence-based upside state | Better mix or pricing where causal | Operating leverage with constraints | May consume more WC | May require more growth capex | Test upside and bottlenecks |
| Bear | Plausible adverse state | Discounting or weaker mix if supported | Under-absorption or cost pressure | Cash conversion often weakens | Liquidity still expected to hold | Downside without thesis break |
| Stress | Severe but plausible shock | Price/volume stress | Fixed-cost and restructuring burden | Adverse WC and collections | Refinancing/covenant pressure | Solvency and liquidity |
| Thesis break | Mechanism proving original thesis wrong | Structural impairment | Lower normalized earnings power | Depends on mechanism | May require recapitalization | Decision exit or full re-underwrite |

## 15. Model checks that must fail loudly

- Balance sheet check equals zero in every historical and forecast period.

- Cash-flow change in cash equals balance-sheet change in cash after FX and reclassification effects.

- Segments plus eliminations reconcile to consolidated revenue and profit.

- Debt ending balances tie to the debt schedule and disclosed maturities.

- Interest expense directionally responds to debt and rate assumptions.

- Share count responds to issuance, repurchases, options, RSUs, and converts.

- Retained earnings roll-forward ties to net income and distributions.

- Tax schedule reconciles reported provision and modeled cash-tax bridge within explained differences.

- No forecast formula contains an unexplained hard-coded plug.

- Scenario switch changes only intended assumptions and does not overwrite historical data.

- Valuation pulls from model outputs rather than duplicate forecasts.

- A sources or last-updated field exists for every material external input.

## 16. Model error taxonomy and debugging sequence

Debug in layers. First check source mapping and units. Second check statement signs and roll-forwards. Third check schedule-to-statement links. Fourth check scenario switches. Fifth check circularities. Sixth check valuation bridges. Do not fix a balance-sheet error by adding a balancing plug because that destroys the diagnostic signal.

| Symptom | Likely cause | First check |
| --- | --- | --- |
| Balance sheet off by constant amount | Opening balance or missing equity item | Historical opening balances and retained earnings |
| Cash mismatch grows each year | Working-capital sign, capex, debt or FX link | Cash-flow statement versus schedule changes |
| Interest explodes or oscillates | Circular debt-cash logic | Circularity switch, minimum cash, revolver formula |
| EPS changes but equity value does not | Share-count or valuation denominator mismatch | Weighted-average versus period-end diluted shares |
| DCF changes when display units change | Unit inconsistency | Currency and scale across FCFF, debt, cash, share count |
| Segment total differs from consolidated | Eliminations or definition change | Segment reconciliation and footnotes |

## 17. Build-from-scratch training case

Use a fictional company with three years of historical statements and two operating segments. Recreate history from source-like exhibits, then forecast five years. Segment A is subscription service driven by beginning ARR, new bookings, churn, and price. Segment B is hardware driven by units, ASP, utilization, and yield. Build shared corporate costs, working capital, capex, taxes, debt, and share count. The case is complete only after the model balances and a change in churn, utilization, or ASP flows through cash and valuation without manual intervention.

### Minimum test changes

- Increase churn by 200 basis points and confirm revenue, deferred revenue, margins, cash flow, and valuation update.

- Delay a capacity project by two quarters and confirm capex timing, depreciation, units, revenue, working capital, and liquidity update.

- Increase interest rates by 150 basis points and confirm floating-rate debt, interest expense, cash, covenant headroom, and equity value update.

- Increase stock compensation grants and confirm expense, cash-flow add-back, dilution, repurchase needs, and per-share value update.

- Turn off all growth after the explicit forecast and confirm terminal value responds through reinvestment and mature economics rather than a hard-coded multiple.

## 18. Reviewer completion gate

- A reviewer can trace any material historical cell to a source and any material forecast cell to a named driver.

- The model can reproduce reported historical statements before normalization.

- All model adjustments are reversible and documented.

- No statement balances through unexplained plugs.

- All five scenarios remain mathematically stable and economically coherent.

- Valuation changes can be traced to operating assumptions rather than hidden overrides.

- The model contains enough visible checks that a material sign, unit, statement, share-count, or circularity error is likely to be detected before publication.
