<!-- Generated loss-aware reference mirror from God_Level_Public_Company_Financial_Analyst_Job_Guide_V6_99_ALL_SUB70_FIXED.docx. Canonical source remains the bundled DOCX. -->

<!-- Master Lab: 14 | Title: FORMULA, MODELING, AND ANALYTICAL REFERENCE ENCYCLOPEDIA -->

# MASTER LAB 14 - FORMULA, MODELING, AND ANALYTICAL REFERENCE ENCYCLOPEDIA

> Purpose: provide a fast desk reference for frequently used calculations while preventing formula worship. Every metric must be defined for the specific company, period, accounting treatment, and analytical question. A formula is only as good as the inputs and definitions supplied to it.

## 1. Growth and margin

| Metric | Construction | Key caution |
| --- | --- | --- |
| Growth | Current / Prior - 1 | Reconcile acquisitions, FX, accounting presentation, and period length. |
| CAGR | (Ending / Beginning)^(1/years) - 1 | Use actual elapsed years and avoid hiding path volatility. |
| Gross margin | Gross profit / Revenue | Gross-versus-net revenue and depreciation classification can change comparability. |
| Operating margin | Operating income / Revenue | Define whether restructuring, SBC, or amortization is included. |
| Incremental margin | Change in operating profit / Change in revenue | Use comparable scope and period; negative revenue change can make interpretation unintuitive. |
| Contribution margin | Revenue - variable costs, divided by revenue if expressed as percent | Requires true variable-cost identification, not accounting line labels. |

## 2. Working capital and cash conversion

| Metric | Construction | Key caution |
| --- | --- | --- |
| DSO | Average receivables / Revenue x Days | Use credit sales if materially different and adjust for factoring where needed. |
| Inventory days | Average inventory / COGS x Days | Forward COGS can be more useful in fast-changing businesses. |
| DPO | Average payables / COGS or purchases x Days | Use denominator matching the payable and identify supplier finance. |
| Cash conversion cycle | DSO + Inventory days - DPO | Not meaningful for all business models; deferred revenue can be a major source of float. |
| Working-capital investment | Change in operating current assets - Change in operating current liabilities | Remove financing items and acquisition/FX effects when material. |
| CFO conversion | CFO / Net income or operating profit measure | Interpret through business model and noncash charges, not as a standalone score. |

## 3. Returns on capital

| Metric | Construction | Key caution |
| --- | --- | --- |
| ROIC | NOPAT / Average invested operating capital | Define operating cash, goodwill, leases, and capitalized intangibles consistently. |
| Incremental ROIC | Change in NOPAT / Change in invested capital | Use multi-year windows when investment and returns are lumpy. |
| ROE | Net income / Average common equity | Leverage and reserve/accounting differences can dominate. |
| ROA | Profit measure / Average assets | Choose profit measure consistent with asset claimant. |
| Reinvestment rate | Operating reinvestment / NOPAT | Intangible investment may be expensed and need analytical adjustment. |
| Growth identity | Approx. reinvestment rate x incremental return | Steady-state relationship, not a mechanical short-term identity. |

## 4. Free cash flow

| Metric | Construction | Key caution |
| --- | --- | --- |
| FCFF | NOPAT + noncash operating charges - operating reinvestment | Keep financing flows out and capture all growth/maintenance investment. |
| FCFE | Net income + noncash charges - capex - working-capital investment + net borrowing +/- other equity cash items | Best when debt policy is modeled explicitly. |
| Simple FCF | CFO - capex | Useful shorthand but can be distorted by working-capital timing, supplier finance, leases, and acquisition spending. |
| Owner-oriented FCF | Normalized operating cash after maintenance investment and recurring economic costs | Requires judgment; preserve bridge to reported cash flow. |

## 5. Capital structure and credit

| Metric | Construction | Key caution |
| --- | --- | --- |
| Net debt | Debt and debt-like claims - excess cash/non-operating liquid assets | Define lease/pension treatment and minimum cash. |
| Net leverage | Net debt / normalized EBITDA or another relevant cash proxy | EBITDA add-backs and cycle normalization can change result sharply. |
| Interest coverage | EBIT or EBITDA / cash or accounting interest | Match numerator to fixed-charge obligations and include leases where relevant. |
| Fixed-charge coverage | Cash earnings before fixed charges / interest + lease + other fixed charges | Definition varies; state exactly. |
| Covenant headroom | Covenant threshold minus contractual metric | Use the legal debt agreement definition, not headline leverage. |
| Liquidity runway | Usable cash + committed capacity + cash generation - mandatory uses | Model timing and restrictions, not only annual totals. |

## 6. Equity and dilution

| Metric | Construction | Key caution |
| --- | --- | --- |
| Market capitalization | Current share price x period-end shares | Not weighted-average shares used for EPS. |
| Enterprise value | Equity value + debt and debt-like claims + minority/preferred claims - excess cash/non-operating assets | Bridge items depend on accounting and chosen operating metric. |
| Net dilution | Change in shares adjusted for capital raises/acquisitions as analytically appropriate | Repurchases can mask gross employee issuance. |
| Buyback yield | Repurchase cash / beginning or average equity value | Does not indicate value creation without repurchase price and dilution. |
| Treasury-stock option dilution | In-the-money option shares less shares theoretically repurchased with exercise proceeds | Valuation-dependent and simplified for some awards. |

## 7. Valuation

| Metric | Construction | Key caution |
| --- | --- | --- |
| EV/Revenue | Enterprise value / Revenue | Needs gross margin, opex, capital intensity, dilution, and mature economics. |
| EV/EBITDA | Enterprise value / EBITDA | Can hide capex and working capital; normalize leases and cycle. |
| EV/EBIT | Enterprise value / EBIT | More sensitive to depreciation policy but often better for asset intensity. |
| P/E | Equity value / Net income | Affected by leverage, tax, non-operating gains, and buybacks. |
| FCF yield | Free cash flow / Equity value | Define FCF and normalize working capital/capex. |
| Terminal value | FCFF next period / (WACC - g) | Requires WACC > g and steady-state cash flow/reinvestment consistency. |
| WACC | E/V x CoE + D/V x after-tax CoD + other capital weights | Use market weights and risk-consistent inputs. |
| Residual income | Book value + PV of future (ROE - CoE) x beginning book | Useful when book capital is economically meaningful. |

## 8. SaaS and recurring revenue

| Metric | Construction | Key caution |
| --- | --- | --- |
| ARR | Annualized recurring contracted or run-rate revenue under issuer definition | Definitions vary on usage, services, FX, acquisitions, and contract start. |
| Gross retention | Beginning cohort recurring revenue retained before expansion / beginning cohort recurring revenue | Logo and revenue retention are different. |
| Net retention | Beginning cohort recurring revenue after churn/contraction/expansion / beginning cohort revenue | Can remain above 100% while gross churn worsens. |
| CAC payback | Customer acquisition cost / annualized new-customer gross profit | Allocation and timing of sales/marketing cost matter. |
| LTV | Expected customer contribution profit over life discounted appropriately | Highly sensitive to churn, expansion, margin, and acquisition cost. |
| Magic-number style sales efficiency | Change in recurring revenue or ARR annualized / prior sales and marketing spend | Useful only with consistent definitions and sales-cycle timing. |

## 9. Semiconductors and manufacturing

| Metric | Construction | Key caution |
| --- | --- | --- |
| Utilization | Actual effective output / effective capacity | Capacity must reflect yield, downtime, mix, and qualified equipment. |
| Yield | Good output / total processed output | Definition varies by wafer, die, module, or system. |
| ASP | Revenue / units | Mix can dominate apparent price change. |
| Inventory days | Inventory / COGS x days | Channel inventory outside the company also matters. |
| Book-to-bill | Orders / billings or shipments under defined period | Definitions and cancellation risk vary. |
| Content per system | Supplier revenue opportunity / end system | Avoid double counting channel markup and components. |

## 10. Banks

| Metric | Construction | Key caution |
| --- | --- | --- |
| NIM | Net interest income / average earning assets | Tax-equivalent adjustments and balance mix vary. |
| Deposit beta | Change in deposit rate / change in market reference rate | Depends on time window, product mix, and cycle. |
| NCO ratio | Net charge-offs / average loans | Lagging credit measure. |
| Allowance coverage | Allowance / loans or nonperforming loans | Portfolio risk and accounting regime matter. |
| CET1 ratio | Regulatory CET1 capital / risk-weighted assets | Use current regulatory definition and transition rules. |
| P/TBV | Price / tangible book value per share | Interpret through sustainable ROE, cost of equity, growth, and asset quality. |

## 11. Insurance

| Metric | Construction | Key caution |
| --- | --- | --- |
| Loss ratio | Incurred losses / earned premiums | Prior-year reserve development can change the reported ratio. |
| Expense ratio | Underwriting expenses / premiums under chosen definition | Acquisition-cost treatment varies. |
| Combined ratio | Loss ratio + expense ratio | Below 100% usually indicates underwriting profit before investment income under common P&C definitions. |
| Reserve development | Current estimate of prior accident-year losses versus prior estimate | Favorable development can support earnings but may not repeat. |
| Float | Policyholder funds held before claim payment, conceptually | Economic value depends on underwriting cost and duration. |

## 12. Resources and projects

| Metric | Construction | Key caution |
| --- | --- | --- |
| AISC | Sector-defined all-in sustaining cost per unit | Definition is non-GAAP and varies; reconcile to cash spending. |
| Reserve life | Recoverable reserves / annual production | Production and reserve classification change. |
| Capacity factor | Actual output / theoretical maximum output | Weather, outage, curtailment, and resource quality matter. |
| Project IRR | Discount rate that sets project NPV to zero | Can hide scale, timing, reinvestment, and terminal assumptions. |
| Project NPV | PV of after-tax project cash flows - initial/incremental capital | Use realistic construction, ramp, closure, and financing assumptions. |

## 13. Analytical unit controls

- Record currency and whether amounts are nominal or real.

- Record scale: units, thousands, millions, billions.

- Record fiscal period and days in period.

- Record whether values are point-in-time, average, or flow.

- Record whether ratios use beginning, ending, or average balances.

- Record whether metrics are GAAP/IFRS, regulatory, company-defined, or analyst-defined.

- Record treatment of acquisitions, FX, discontinued operations, and recasts.

- Record whether per-share metrics use basic, diluted weighted-average, or period-end fully diluted shares.

## 14. Formula completion gate

A formula may be used in published research only when the analyst can identify every input, unit, period, definition, and reconciliation. If the formula is mathematically correct but the denominator does not match the economic exposure, the output is wrong. When in doubt, reconstruct the metric from source components and compare it with the issuer definition before using it in a model or peer table.
