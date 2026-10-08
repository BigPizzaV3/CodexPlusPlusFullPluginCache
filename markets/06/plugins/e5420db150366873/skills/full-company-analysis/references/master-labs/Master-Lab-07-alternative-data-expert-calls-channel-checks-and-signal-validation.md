<!-- Generated loss-aware reference mirror from God_Level_Public_Company_Financial_Analyst_Job_Guide_V6_99_ALL_SUB70_FIXED.docx. Canonical source remains the bundled DOCX. -->

<!-- Master Lab: 07 | Title: ALTERNATIVE DATA, EXPERT CALLS, CHANNEL CHECKS, AND SIGNAL VALIDATION -->

# MASTER LAB 07 - ALTERNATIVE DATA, EXPERT CALLS, CHANNEL CHECKS, AND SIGNAL VALIDATION

> Purpose: use nontraditional evidence to test public-company hypotheses without confusing noisy correlation with fact or crossing legal and compliance boundaries. Alternative data should reduce uncertainty around a defined question. It should never become a collection of interesting charts with no causal link to revenue, margins, cash flow, or risk.

## 1. Start with the hypothesis and the causal chain

Write the precise hypothesis before collecting alternative data. Example: "North American enterprise demand for Product X is decelerating because renewal-seat contraction is offsetting list-price increases." Then map the causal chain from customer behavior to observable signal to reported KPI to financial statement. A data source is useful only if the chain is plausible and the signal arrives early enough to matter.

Signal value ≈ Expected decision impact x probability the signal resolves uncertainty x timeliness - data cost - false-positive cost - compliance risk.

This expected-value framing prevents expensive datasets from becoming status symbols. A cheap source that resolves a material assumption can be more valuable than a sophisticated feed with weak linkage to the thesis.

## 2. Compliance and MNPI boundary

Alternative-data work must operate within applicable law, contractual terms, privacy rules, platform terms, and the firm compliance program. Do not solicit or use material nonpublic information. Do not encourage an expert to breach an employer confidentiality duty, customer agreement, government restriction, or other obligation. When the line is unclear, stop and escalate to compliance.

- Define prohibited topics before expert calls.

- Use approved expert-network and research procedures where required.

- Avoid asking for unreleased earnings, bookings, customer-specific confidential spend, unannounced product details, material contract awards, or other nonpublic company information.

- Record the source, date, population, and method used to collect a signal.

- Separate public aggregation from information that is nonpublic because of the source or method.

- Respect robots.txt, access controls, rate limits, licensing, and contractual restrictions for web data.

## 3. Expert-call design

Expert calls are hypothesis tests, not fishing expeditions. Build a question tree from broad market structure to specific observable behavior. Ask for process, ranges, comparisons, and examples rather than confidential point estimates. Use multiple independent experts with different positions in the value chain to reduce individual bias.

1. Define the hypothesis and the evidence that would change it.

1. Screen experts for relevant role, geography, customer size, product generation, and time period.

1. Write prohibited topics and conflict notes.

1. Begin with background and definitions so terminology is consistent.

1. Ask open-ended process questions before revealing your hypothesis.

1. Probe contradictions and ask for examples or ranges.

1. At the end, ask what would make the expert wrong and which data source they trust most.

1. Code notes by claim, source role, confidence, and whether the claim is independently corroborated.

### Good versus weak questions

| Weak question | Better question |
| --- | --- |
| Are bookings weak this quarter? | How has the customer purchase process changed over the past six to twelve months, and what public or observable indicators would show that change? |
| What will Company A report? | Which vendors are gaining or losing consideration in current evaluations, and what factors drive the decision? |
| How much did your company spend? | How is budget allocation changing across the category, and what ranges or priorities are observable across customers like yours? |
| Is the new product good? | Compared with the prior generation and alternatives, where does the product perform better or worse on cost, reliability, deployment, and support? |

## 4. Customer research

Segment customers by size, geography, use case, maturity, contract type, and strategic importance. A sample of five enthusiastic early adopters does not represent the installed base. Ask about purchase trigger, procurement cycle, alternatives considered, price paid, implementation effort, realized value, renewal, expansion, churn, and support.

When the company sells through channels, distinguish sell-in from sell-through. Distributor inventory can make supplier revenue look strong while end demand weakens. Track channel inventory, weeks of supply, discounting, return rights, and vendor incentives where observable and compliant.

## 5. Supplier research

Suppliers can reveal order patterns, lead times, capacity, input shortages, redesign activity, customer concentration, and cost pressure. However, one supplier may see only a small program or may be losing share. Weight the evidence by exposure and corroborate with other suppliers, customer commentary, inventory, and company disclosures.

Map whether a supplier is sole-source, dual-source, qualified backup, commodity, or highly specialized. Changes in supplier lead time can reflect demand, capacity expansion, inventory normalization, or bargaining power. Do not assume one cause.

## 6. Job postings and workforce data

Hiring data can indicate growth priorities, geographic expansion, product investment, sales capacity, or restructuring. It can also be noisy because postings are duplicated, evergreen, cancelled, outsourced, or filled internally. Build a baseline and track unique normalized roles, not raw posting counts.

Normalized hiring index = Unique active roles adjusted for duplicate postings, location, function, seniority, and known evergreen behavior.

Map functions to economic drivers. Sales hiring may precede bookings only after ramp and quota attainment. Engineering hiring may signal product investment but not near-term revenue. Manufacturing hiring may be constrained by capacity commissioning. Backtest the lead relationship before using it in a forecast.

## 7. Web traffic, app data, search interest, and engagement

Digital activity can be useful for consumer, marketplace, software, and media businesses, but source methodology often changes. Track data-provider coverage, bot filtering, device mix, geography, panel composition, and historical revisions. A traffic increase can reflect marketing spend rather than monetization or retention.

Monetization bridge example: Revenue = Active users x transactions per user x average transaction value x take rate, or another business-specific decomposition.

Use digital signals to test components of the bridge, not to substitute for it. If traffic rises but conversion and monetization fall, revenue may not follow. If the company shifts activity from web to app, a single-channel series can give a false decline.

## 8. Pricing, promotions, and inventory scraping

Create a product dictionary with SKU, model, region, channel, list price, observed price, discount, availability, delivery time, seller, and timestamp. Preserve raw observations. Separate permanent price change from promotional discount, bundle, financing subsidy, coupon, channel markdown, and mix.

For inventory, distinguish listed availability from actual inventory. E-commerce stock indicators, shipping times, dealer counts, and SKU availability can be proxies. Backtest which measure predicts reported units or channel commentary. Do not interpret one retailer as the whole market.

## 9. Trade, shipment, geospatial, and physical data

Customs, shipping, satellite, foot traffic, power use, construction, and other physical data can be valuable when they map to a real asset or flow. The key risks are classification errors, incomplete geography, transshipment, entity mapping, revisions, and changes in reporting coverage.

Create entity and unit maps before aggregating. A shipment record may be counted by weight, value, containers, or units and can include internal transfers. A satellite observation can show activity but not necessarily ownership or profitability. Triangulate with company capacity and customer demand.

## 10. Survey design

A survey must define the target population, sampling frame, response rate, weighting, question order, and confidence limits. Convenience samples can produce precise-looking but biased numbers. Use neutral wording and separate awareness, consideration, trial, usage, satisfaction, retention, and willingness to pay.

Report the sample and uncertainty with every conclusion. A statistically significant change can still be economically immaterial. Conversely, a small sample can be useful qualitatively when the effect is large and corroborated by other evidence.

## 11. Alternative-data validation protocol

1. Define the exact reported KPI or economic driver the signal is supposed to predict.

1. Freeze the data vintage to what would have been available at the historical decision date.

1. Normalize the signal for methodology changes, coverage, seasonality, and obvious confounders.

1. Backtest lead and lag relationships across multiple periods, including weak periods.

1. Measure false positives and false negatives, not only correlation.

1. Test whether the relationship survives out-of-sample periods or peer companies.

1. Document revisions and whether historical data are restated by the vendor.

1. Set a minimum effect size required before the signal changes the model.

1. Continue tracking signal performance after deployment and retire signals that decay.

A high in-sample correlation is not enough. Measure out-of-sample forecast error, directional hit rate, revision stability, and incremental explanatory power versus the existing model.

## 12. Avoiding look-ahead and survivorship bias

Historical alternative datasets are often cleaner than they were in real time because providers revise entity mapping, remove bad records, or add coverage. A valid backtest uses the vintage available at the time. Survivorship bias appears when failed products, stores, companies, or web properties disappear from the sample. Preserve dead entities and historical coverage where possible.

## 13. Confounders and causal skepticism

Alternative data rarely come from randomized experiments. Search traffic can rise because of a scandal, marketing campaign, product launch, or seasonal event. Job postings can rise because turnover increased. Prices can fall because mix changed. Always list at least two alternative causes and identify a second data source that helps distinguish them.

## 14. Signal weighting and evidence matrix

| Signal | Coverage | Lead time | Historical reliability | Causal proximity | Current direction | Model impact |
| --- | --- | --- | --- | --- | --- | --- |
| Example customer survey | Enterprise buyers, North America | 1-2 quarters | Medium | High | Weakening | Reduce new bookings only after corroboration |
| Example web traffic | Global public web | Weeks | Low-Medium | Low | Rising | No direct model change |
| Example supplier lead time | Critical component | 1-3 quarters | High after backtest | Medium-High | Falling | Test inventory normalization and pricing |

Do not average signals mechanically. Weight by relevance to the specific driver, population coverage, lead time, reliability, and causal proximity. A high-quality primary-source operating KPI should usually outrank a noisy digital proxy.

## 15. Worked channel-check case

A consumer-electronics company reports strong channel shipments and guides to continued growth. Retail scraping shows rising discounting and faster delivery times. Two distributors report higher weeks of inventory, while search interest remains strong. Build competing explanations: healthy demand with supply normalization, or sell-in exceeding sell-through. The next evidence should include retailer sell-through, returns, channel inventory, company receivables, promotional allowances, and production schedules.

Quantify both cases. In the adverse case, model a one-quarter channel correction, lower unit shipments, promotional margin pressure, and working-capital release. In the benign case, model lower lead times with stable sell-through and normalized inventory. Do not change the long-term thesis solely because one high-frequency indicator moves.

## 16. Completion gate

- Every alternative-data source is tied to a defined hypothesis and financial driver.

- Collection method, population, coverage, terms, revisions, and known biases are documented.

- Expert work follows legal and compliance boundaries and does not solicit MNPI.

- Signals are validated against reported outcomes using real-time vintages where possible.

- False positives, false negatives, and methodology changes are tracked.

- No signal changes a material forecast without a pre-defined effect-size threshold and causal explanation.

- Primary-source evidence retains priority when it directly measures the same underlying variable.

- The analyst can explain what would cause the signal relationship to break and when the signal should be retired.
