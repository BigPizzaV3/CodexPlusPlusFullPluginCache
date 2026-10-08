<!-- Generated loss-aware reference mirror from God_Level_Public_Company_Financial_Analyst_Job_Guide_V6_99_ALL_SUB70_FIXED.docx. Canonical source remains the bundled DOCX. -->

<!-- Master Lab: 01 | Title: ACCOUNTING MECHANICS, JOURNAL ENTRIES, AND FOOTNOTE RECONSTRUCTION -->

# MASTER LAB 01 - ACCOUNTING MECHANICS, JOURNAL ENTRIES, AND FOOTNOTE RECONSTRUCTION

> Purpose: make the analyst capable of reconstructing the accounting from the transaction level upward. The analyst should be able to explain not only what a reported number is, but what journal entries created it, which estimates sit behind it, where the cash moved, what will reverse, and how the item changes valuation.

## Required outputs

- A clean historical three-statement reconstruction tied to audited filings and amendments.

- A transaction-level bridge for every material accounting area that can alter normalized earnings, cash flow, invested capital, or share count.

- A footnote roll-forward workbook for debt, leases, stock compensation, taxes, goodwill and intangibles, pensions, reserves, and commitments.

- A GAAP-versus-economic adjustment schedule that preserves both reported accounting and the analyst normalization.

- A list of unresolved accounting judgments with sensitivity ranges and source citations.

## Prerequisites

- Basic algebra and percentage change.

- Understanding of debit and credit mechanics at the level of assets, liabilities, equity, revenue, expense, gains, and losses.

- Ability to locate primary statements and footnotes in a 10-K or equivalent annual filing.

## 1. Build the accounting map before reading ratios

Start with the transaction, not the ratio. A ratio can look unusual for many reasons. A transaction map asks what the company sold, what it promised, when control transferred, when cash moved, what asset or liability was created, what estimate was required, and what future reversal is expected. For every material line item, create a six-column accounting map: economic event, debit, credit, income-statement effect, cash-flow-statement effect, and balance-sheet carryforward.

| Economic event | Typical debit | Typical credit | Income statement | Cash flow | Future analytical question |
| --- | --- | --- | --- | --- | --- |
| Cash sale of product | Cash | Revenue | Revenue and related COGS recognized | Operating inflow | Is gross margin sustainable and are returns and rebates accrued correctly? |
| Sale on credit | Accounts receivable | Revenue | Revenue recognized before cash | No collection yet | Are receivables growing faster than sales and why? |
| Cash collected in advance | Cash | Contract liability / deferred revenue | No revenue until performance | Operating inflow | What portion is refundable, cancellable, or tied to future service cost? |
| Capital equipment purchase | PP&E | Cash / payable | Depreciation later | Investing outflow | Maintenance or growth capex, useful life, residual value, capacity added? |
| Stock award vesting | Compensation expense / equity mechanics | APIC / equity | SBC expense | Usually noncash add-back in CFO, tax effects separate | What is the true dilution and repurchase offset? |
| Acquisition | Assets and goodwill | Cash, debt, or equity | Future amortization, integration costs, step-up effects | Investing and financing mix | How much value depends on synergies and purchase accounting? |

## 2. Trial balance to financial statements

A novice often learns the three statements as separate reports. An expert treats them as different views of one ledger. Reconstruct at least one quarter from a simplified trial balance. Confirm that every income-statement item closes into retained earnings, every noncash income-statement item has a balance-sheet counterpart, and every cash movement is classified once in the cash flow statement.

Core identity: Assets = Liabilities + Equity.

Retained earnings ending = Retained earnings beginning + Net income - Common dividends +/- other direct retained-earnings adjustments.

Cash ending = Cash beginning + CFO + CFI + CFF + FX or other cash translation effects.

Do not plug cash to make a model balance. If the model does not balance, find the missing accounting link. Common causes are omitted retained earnings, incorrect share repurchase treatment, debt issuance or repayment omitted from financing cash flow, acquisition consideration not bridged, lease principal classified incorrectly, or a sign error in working capital.

### Mini-ledger drill

1. Record a $100 credit sale with $60 cost of goods sold.

1. Collect $70 of the receivable.

1. Buy $40 of inventory for cash.

1. Buy $120 of equipment with $20 cash and $100 debt.

1. Record $10 depreciation.

1. Pay $5 interest and accrue $3 of unpaid interest.

1. Repurchase $15 of stock and issue $4 of stock compensation.

After the seven entries, rebuild the income statement, balance sheet, and cash flow statement. The drill is complete only when the balance sheet balances without a plug and the change in cash equals the cash flow statement.

## 3. Revenue recognition from contract economics

Revenue is not a demand metric by default. The analyst must separate contract signing, order intake, backlog or remaining performance obligation, billing, cash collection, delivery, acceptance, and revenue recognition. For each material revenue stream, document the performance obligation, transaction price, variable consideration, timing of transfer, cancellation rights, refund rights, renewal behavior, principal-agent presentation, and significant financing components.

| Signal | What it measures | Can lead revenue? | Can mislead? | Required reconciliation |
| --- | --- | --- | --- | --- |
| Bookings / order intake | Signed or accepted orders under company definition | Often | Yes, cancellations, nonbinding orders, multi-year scope | Bookings to backlog or RPO to recognized revenue |
| Billings | Invoice issuance | Sometimes | Yes, billing terms can change | Billings to receivable or deferred revenue to cash |
| Cash collections | Cash received | Sometimes | Yes, prepayments can precede delivery | Cash to contract liability or receivable reduction |
| RPO / backlog | Contracted future performance under issuer definition | Usually | Yes, cancellability and duration vary | Opening balance + additions - recognized or cancelled = ending balance |
| GAAP revenue | Performance recognized under accounting rules | No, it is the reported result | Yes as a demand proxy | Revenue to cash, receivables, contract assets and liabilities, units and price |

For over-time recognition, identify the measure of progress and test whether it can be influenced by cost estimates, milestones, or front-loaded inputs. For point-in-time recognition, identify the control-transfer trigger and whether acceptance clauses, shipment terms, installation, or customer-specific customization delay recognition. For marketplaces and resellers, test gross-versus-net presentation because a presentation change can make reported revenue growth look spectacular while gross profit and economics barely change.

### Revenue quality bridge

Organic revenue growth = Reported growth - acquisition/divestiture scope effect - FX effect - presentation/definition effect.

Contract asset intensity = Contract assets / Revenue. Rising intensity deserves explanation when revenue growth is strong.

Deferred revenue conversion = Revenue recognized from opening deferred revenue / Opening deferred revenue, when disclosed and meaningful.

A revenue conclusion is not finished until it reconciles to at least one physical or contractual driver such as units shipped, seats, customers, megawatts, transactions, subscriptions, procedures, tonnage, capacity, or price per unit.

## 4. Working capital as an operating model, not a ratio plug

Build working capital from the commercial process. Receivables depend on sales timing, billing, payment terms, customer mix, disputes, and collections. Inventory depends on demand, lead times, safety stock, production cycle, product mix, obsolescence, and channel strategy. Payables depend on procurement, supplier terms, bargaining power, purchase timing, and financing programs.

DSO = Average accounts receivable / Revenue x Days in period.

Inventory days = Average inventory / COGS x Days in period.

DPO = Average accounts payable / COGS or purchases x Days in period, using the denominator that best matches the liability.

Cash conversion cycle = DSO + Inventory days - DPO.

Do not mechanically forecast each balance as a percentage of revenue if the business mix is changing. A hardware-plus-service company, a marketplace shifting to gross presentation, or a manufacturer entering a build phase can break historical ratios. Use operational drivers where available and use ratios only as a cross-check.

### Supplier finance and factoring

Supplier finance can improve reported operating cash flow by extending payment timing while economically introducing financing. Factoring can accelerate cash collections while transferring or retaining credit risk. Read the footnotes for program size, outstanding balances, classification, recourse, fees, and cash-flow presentation. Recast when necessary so operating cash generation is comparable through time.

## 5. Capex, depreciation, useful lives, and asset intensity

Separate maintenance capex, growth capex, capitalized software or development, construction in progress, acquired assets, and lease-related asset additions. The maintenance-versus-growth split is an analytical estimate, not a GAAP line. Use physical capacity, age of asset base, depreciation, management disclosures, replacement cycles, and peer economics to constrain the estimate.

Net PP&E ending = Net PP&E beginning + capital expenditures + acquired assets + FX/other - depreciation - disposals - impairments.

Gross investment intensity = Capex / Revenue. Incremental capital intensity = Change in invested operating assets / Change in revenue, measured over a sensible multi-year window.

Useful-life changes can shift earnings without changing near-term cash. Compare disclosed useful lives through time and against peers. If depreciation falls because useful lives are extended, show the counterfactual expense under the prior life. When a company claims asset-light economics, test whether capital expenditure has simply moved into leases, supplier financing, cloud commitments, or acquisition spending.

## 6. Leases and debt-like commitments

Create a lease schedule that separates operating lease cost, finance lease interest, amortization, lease liabilities, right-of-use assets, principal payments, and undiscounted future commitments. For valuation, decide consistently whether leases are treated as operating obligations embedded in EBITDA or as debt-like claims with corresponding earnings adjustments. Do not subtract lease debt from enterprise value while also using an EBITDA denominator that already bears full rental expense without considering comparability.

Approximate lease debt sensitivity: present value of contractual lease payments discounted at a rate consistent with lease risk, when a full reported liability is unavailable.

Also inventory purchase commitments, take-or-pay contracts, cloud commitments, minimum volume commitments, guarantees, securitizations, receivable sales, and off-balance-sheet joint-venture obligations. A liquidity model that includes only funded debt is incomplete.

## 7. Stock-based compensation and diluted share economics

Treat stock compensation in two separate dimensions. First, it is compensation expense that can be economically recurring even when management excludes it from adjusted earnings. Second, it creates dilution or consumes cash when the company repurchases shares to offset dilution. Analyze both.

Net dilution rate = (Ending diluted shares - Beginning diluted shares - shares issued for acquisitions or capital raises where separately analyzed) / Beginning diluted shares.

Buyback offset ratio = Shares repurchased / Gross shares issued or vested from employee equity programs, when share data permit.

Build an award inventory for options, RSUs, PSUs, employee stock purchase plans, and convertibles. For options, use treasury-stock-method mechanics where appropriate. For performance awards, model probable payout ranges. For convertibles, test if-converted treatment and capped-call effects where applicable. The goal is a forward share count that responds to price and award assumptions rather than a flat historical diluted share number.

## 8. Income taxes, cash taxes, and deferred tax mechanics

Separate statutory tax rates, reported effective tax rate, cash taxes, deferred tax expense or benefit, NOLs, tax credits, valuation allowances, uncertain tax positions, discrete items, geographic mix, and withholding taxes. A low effective rate can be durable, temporary, or purely accounting.

Tax provision = Current tax expense + Deferred tax expense, subject to jurisdictional and classification detail.

NOPAT for valuation should use a normalized operating cash-tax concept, not automatically the reported effective tax rate.

Create a tax-rate bridge by jurisdiction and item. Review valuation allowance changes carefully because releasing a valuation allowance can create a large GAAP tax benefit without an equivalent current-period cash inflow. For NOLs and credits, track jurisdiction, amount, expiration, limitations, and expected utilization. If a transaction changes ownership or legal structure, assess whether tax assets remain usable.

## 9. Acquisitions, goodwill, intangibles, and purchase accounting

Rebuild each material acquisition from purchase price to assets acquired and liabilities assumed. Separate consideration paid in cash, debt, equity, contingent consideration, rollover equity, and assumed obligations. Identify identifiable intangibles, useful lives, deferred tax effects, step-ups, restructuring reserves, and goodwill.

Goodwill = Consideration transferred + fair value of prior or noncontrolling interests - fair value of identifiable net assets acquired.

For analysis, create an acquisition cohort table with purchase date, purchase price, revenue or EBITDA acquired, initial synergy claims, actual integration progress, impairments, disposals, and cumulative return on acquired capital. This prevents repeated acquisitions from hiding weak organic economics.

Amortization of acquired intangibles is noncash in the current period but reflects a real acquisition price paid for finite-lived assets. Whether to add it back depends on the analytical question. Never label it economically irrelevant solely because it is noncash.

## 10. Reserves, estimates, warranties, returns, litigation, and restructuring

Any estimate that lets management recognize cost earlier or later deserves a roll-forward. Build beginning reserve + provisions - cash or use + acquisitions, FX, or reclasses = ending reserve. Compare provision rates with underlying activity. A declining warranty reserve while unit volumes and defect indicators rise is different from a declining reserve after genuine product quality improvement.

| Estimate area | Key management judgment | Analyst cross-check | Red flag |
| --- | --- | --- | --- |
| Credit loss | Default probability, loss severity, macro scenario | Charge-offs, delinquency, vintage performance | Reserve ratio falls as credit metrics worsen |
| Warranty | Failure rate, repair cost, product mix | Claims, installed base, recalls, field data | Expense rate falls before evidence of quality improvement |
| Returns / rebates | Return rate, channel inventory, rebate behavior | Sell-through, discounting, channel checks | Reserve rate falls while promotions rise |
| Litigation | Probability and estimable loss range | Court filings, regulator actions, settlements | Repeated not-estimable language despite advancing case |
| Restructuring | Scope, timing, eligible costs | Cash payments, headcount, facility closures | Recurring restructuring excluded from adjusted earnings every year |

## 11. Pension and postretirement obligations

For defined-benefit plans, separate service cost, interest cost, expected or actual asset return, actuarial gains and losses, contributions, benefit payments, funded status, discount rate, asset allocation, and expected future contributions. The accounting can obscure economic leverage.

Funded status = Fair value of plan assets - Projected benefit obligation, subject to the exact plan definition.

Stress discount rates and asset returns, then estimate cash-contribution implications. In enterprise-to-equity valuation, avoid double counting pension deficits if related expense adjustments already change cash flow. For companies with large plans, include pension sensitivity in balance-sheet stress testing.

## 12. Foreign currency and translation

Separate transaction exposure from translation exposure. Revenue translated at a weaker or stronger currency can change reported growth without changing local-currency demand. Transaction exposure can affect gross margin or operating expense depending on where costs and revenues are denominated.

Constant-currency growth should be reconstructed from disclosed local-currency or FX bridge data when possible, not accepted as a black-box non-GAAP metric.

Track balance-sheet translation in accumulated other comprehensive income where relevant. For companies with debt in multiple currencies, test whether hedges match the underlying exposure and whether hedging gains and losses are operating or financing in economic substance.

## 13. Cash flow statement reconstruction

Reconcile CFO from net income through every material noncash item and working-capital movement. Then compare CFO to a direct cash logic: cash collected from customers minus cash paid to suppliers, employees, taxes, and other operating uses. The indirect and direct perspectives should tell the same economic story.

Review classification elections and changes. Interest, taxes, restricted cash, discontinued operations, supplier finance, factoring, acquisition-related costs, and lease payments can create comparability issues across companies and accounting regimes. Normalize for analytical comparability while preserving the reported statement.

Free cash flow is not a single authoritative GAAP measure. Define the exact construction every time and reconcile it to reported cash flows.

A useful analytical stack is CFO, CFO before working-capital changes, capex, maintenance capex estimate, growth capex estimate, cash restructuring, acquisition spending, SBC-related tax and cash effects, and owner-oriented free cash flow. Each answers a different question.

## 14. U.S. GAAP and IFRS comparability

Do not assume two companies using different accounting frameworks are directly comparable because the line-item names look similar. Focus on economic differences that can affect margins, assets, cash flows, leverage, and valuation. Common areas requiring explicit review include development-cost capitalization, inventory costing, impairment reversals, lease presentation, pension accounting, revaluation options, and cash-flow classification.

Build a comparability bridge only for material differences. The goal is not to rewrite one company into the other accounting framework. The goal is to prevent an accounting-policy difference from being mistaken for an economic advantage.

## 15. Footnote reconstruction protocol

1. Create a source index containing filing date, reporting period, accession or document identifier, amendment status, page or section, and link.

1. For each material note, capture the current table and at least two comparable prior periods or prior filing versions.

1. Standardize units, signs, fiscal periods, and definitions before calculating trends.

1. Build roll-forwards for balances that change through additions, usage, remeasurement, acquisitions, FX, and reclassification.

1. Tie every roll-forward ending balance to the balance sheet or disclosed subtotal. Treat unexplained differences as open issues.

1. Mark each input as reported fact, analyst calculation, management claim, external estimate, or judgment.

1. Document every normalization separately from the reported accounting so another analyst can restore the original data.

1. Write one sentence explaining how the footnote could change revenue, margin, cash flow, invested capital, financing, dilution, risk, or valuation.

## 16. Accounting mastery exercises

### Exercise A: deferred revenue versus demand

A software company grows revenue 18%, billings 8%, deferred revenue 3%, and RPO 20%. Build at least four explanations that could produce the pattern. Examples include longer contract duration, billing-frequency change, usage revenue mix, acquisition scope, renewal timing, or weakening new bookings. Identify the additional disclosure required to distinguish them. Do not choose a narrative before reconciling definitions.

### Exercise B: inventory and margins

A hardware company reports gross margin expansion while inventory days rise from 70 to 115. Reconstruct price-volume-mix, purchase commitments, obsolescence reserves, channel inventory, expedite cost, and manufacturing utilization. Quantify a scenario in which margin remains strong but cash conversion deteriorates, and another in which inventory is an intentional buffer ahead of constrained supply.

### Exercise C: acquisition economics

A serial acquirer reports 12% adjusted EPS growth, 2% organic revenue growth, rising goodwill, and recurring restructuring add-backs. Build an acquisition cohort analysis. Recalculate cumulative invested capital, organic versus acquired operating profit, cash acquisition spending, SBC and dilution, and returns on acquired capital. Determine whether EPS accretion reflects value creation or financing and accounting optics.

### Exercise D: cash tax normalization

A company reports a 9% effective tax rate because of stock-compensation windfalls and valuation-allowance release. Build a normalized tax range using jurisdiction mix, statutory rates, durable credits, and expected NOL utilization. Show the impact on NOPAT, FCFF, and DCF value under reported and normalized tax assumptions.

## 17. Accounting completion gate

- Every material balance can be traced to a filing, footnote, roll-forward, or explicit analyst estimate.

- Every normalization has a reversible bridge to reported accounting.

- The three statements reconcile without unexplained plugs.

- Revenue, cash, working capital, capex, debt, tax, and share count are linked through transaction mechanics.

- At least one skeptical accounting interpretation has been quantified for every thesis-relevant judgment.

- The reviewer can change one key accounting assumption and observe the full effect on earnings, cash flow, invested capital, and valuation.
