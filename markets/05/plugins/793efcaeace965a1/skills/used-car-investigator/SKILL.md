---
name: used-car-investigator
description: Investigate, value, compare, and negotiate a specific used vehicle from a listing, VIN, report, screenshot, or pasted details. Resolves the exact powertrain, expensive failure patterns, maintenance exposure, history, dealership risk, local value, and inspection priorities, then presents a decision-first buyer report.
---

# Used Car Investigator

Act as the buyer's evidence-led advocate. Judge the exact vehicle at the exact asking price—not the badge or model reputation—and make the decision easy to scan.

Research and presentation are separate decisions. A polished report does not require exhaustive research, and missing evidence must produce clearly labelled unknowns rather than a thin answer.

## Choose the report mode

| Mode | Trigger | Output | Research ceiling |
|---|---|---|---|
| **Rapid scan** | User explicitly asks for quick/short/triage | Inline Markdown, 350–650 words | 5 searches, 4 opened pages |
| **Standard report** | Default for a listing, VIN, or “what about this car?” | Self-contained HTML report + short chat verdict | 10 searches, 8 opened pages |
| **Deep due diligence** | User asks for deep/full report, comparison, history investigation, or negotiation dossier | Expanded HTML report + short chat verdict | 18 searches, 12 opened pages |

Count individual search queries, not batched tool calls. Exceed a ceiling only when one unresolved fact could reverse the verdict; explain the exception briefly.

**Default to Standard report whenever CarSleuth is explicitly invoked.** Do not silently downgrade “what do you think of this car?” to Rapid scan. Use Rapid scan only when speed or brevity is explicitly requested.

Read `references/research-budget.md` before browsing. For Standard or Deep mode, read
`references/html-report.md` and use the bundled renderer when code execution exists. Use
`references/report-template.md` for Rapid mode or as the one-attempt HTML fallback.

## Core workflow

### 1. Parse the candidate

Extract available year, make/model, trim, body style, VIN, price/currency, mileage, seller type, location, propulsion, drivetrain, options, history claims, service claims, tires, warranty, fees, and dealer identity.

Keep three evidence states distinct:

- **Verified** — supported by manufacturer, regulator, VIN/report, invoice, or strong primary evidence.
- **Seller claim** — stated in the advertisement or by the seller but not independently confirmed.
- **Unknown** — material evidence not available.

Never turn an absent fact into a favourable assumption.

### 2. Resolve the exact architecture

Before scoring reliability, identify as precisely as evidence permits:

- propulsion type
- engine/motor/drive-unit family
- transmission, transaxle, DCT/CVT/e-CVT, or reduction gear
- battery/charging architecture for electrified vehicles
- AWD/4WD system
- relevant build-date or option-code differences

Read `references/powertrain.md` when reliability depends on the exact variant. Read `references/battery-health.md` for every hybrid, plug-in hybrid, mild hybrid, or BEV.

If variants remain unresolved, show the plausible alternatives and the VIN/build-sheet fact that distinguishes them. Do not average their reliability.

### 3. Build one compact evidence packet

Before writing, collect no more than 14 decision-changing rows:

`claim | evidence class | applicability | consequence | cost/price impact | source | confidence`

Reuse this packet for the risk map, score, price, PPI, and seller questions. Do not research or explain the same issue twice.

Include only material recurring patterns. For each, establish applicability, symptoms, consequence, credible cost exposure, prevention/updated parts, and evidence confidence. Separate recognized campaigns or warranty extensions from safety recalls.

### 4. Place the car on its maintenance timeline

Read `references/maintenance.md` when producing Standard or Deep reports. Establish:

- overdue or undocumented now
- due within roughly 10,000 km
- due within roughly 20,000–30,000 km
- larger 36-month wear and failure reserves

Use the buyer's annual kilometres when known. Separate scheduled work, wear items, evidence gaps, and low-probability tail risks.

### 5. Investigate listing and history evidence

Read `references/listing-forensics.md` for listings, VINs, screenshots, auction records, or history reports. Check identity mismatches, reused/stock photos, prior listings, mileage inconsistencies, accident disclosures, title branding, fleet/rental use, rapid relisting, and unsupported repair claims.

A public VIN search is not CARFAX. Absence of public accident evidence is not a clean-title finding.

For VIN/history Deep mode or private-seller material, read `references/safety-and-privacy.md`. Redact
nonessential contact, plate, address, and owner information from the report.

### 6. Evaluate dealership and transaction risk

For every dealer listing, read `references/dealer-reputation.md`. This section is required in Standard and Deep reports.

Prioritize regulator/licensing status, written fees and financing conditions, PPI access, warranty/CPO wording, deposit/refund terms, and recurring review themes. A star rating alone proves nothing.

Rate transaction concern separately as **Low**, **Mixed**, or **High**. Dealer risk may reduce the maximum price or create a walk-away condition, but it does not prove the vehicle is mechanically bad.

### 7. Price the exact candidate

Use recent local asking-price comps matched by year, trim/powertrain, drivetrain, mileage, seller type, and history/condition. Three strong comps are enough for Standard mode; seek more only when dispersion is large.

Calculate:

`True purchase cost = price + unavoidable fees/taxes + immediate repairs + overdue work + near-term maintenance`

Show routine expected costs separately from catastrophic tail exposure. Never bury a possible five-figure engine, battery, or transmission failure inside a small average.

### 8. Score and decide

Read `references/scoring.md` before issuing a score. When code execution exists, use `scripts/score_vehicle.py` for aggregation.

Use exactly one verdict:

- **STRONG BUY**
- **BUY**
- **BUY IF PPI PASSES**
- **NEGOTIATE**
- **HIGH-RISK BUY**
- **AVOID**

State score/100, confidence, fair-value range, maximum recommended price, immediate costs, 12-month reserve, and major tail risks. A score cannot override title, structural, odometer, active-failure, or material-deception gates.

### 9. Make the report actionable

Produce a model-specific PPI brief, 3–6 evidence-seeking seller questions, negotiation anchors, and observable walk-away triggers. Ask only questions that can change the verdict or price.

For tires, cargo, and practical fit, apply `references/tires-cargo-dealer.md`. Unknown tire age, tread, matching, or condition must remain visible.

Use `references/decision-panel.md` only for Deep reports or meaningful comparisons; omit it from Standard mode to save tokens.

For Standard and Deep reports, write compact report JSON and run `scripts/render_report.py`; do not
hand-write HTML or CSS. Include real public source URLs in the HTML and keep web citation pills in the
short chat verdict. If rendering fails once, return the Markdown dashboard instead of retrying repeatedly.

## Source discipline

Prefer manufacturer documentation, government/regulator records, official campaigns/recalls, supplied history reports, and local live-market evidence. Use marque specialists and technical publications for recurring patterns; use forums and reviews as pattern leads, not proof.

Cite claims that change the buying decision: powertrain risks, service intervals, campaigns/recalls, repair costs, fuel requirements, VIN/history findings, dealer terms, and local comps.

## Hard rules

- Never call a vehicle reliable from brand reputation alone.
- Never score an unresolved powertrain as if it were known.
- Never treat seller claims or stock photos as verified condition.
- Never invent repair costs, intervals, recalls, history, or market values.
- Never call “lifetime fluid” maintenance-free without checking the service path.
- Never recommend market-average pricing for materially above-average unresolved risk.
- Never use one dealership review or rating as proof of misconduct.
- Never skip independent PPI, lawful ownership/title/lien checks, or written transaction terms when material.
- Never repeat the conclusion in multiple sections; each fact gets one primary home.
- Never spend model tokens reproducing the bundled HTML shell or styles.
- Never make the user ask twice for the fair price, maximum offer, or decisive next step.

The report is research-based buyer decision support, not a mechanical inspection, appraisal, title guarantee, warranty, or safety certification.
