# Markdown Report Fallback

Use for Rapid scans or when the HTML renderer is unavailable or fails once. It is a visual dashboard,
not an essay. Omit sections without decision-changing content.

## Visual language

Use one verdict marker consistently:

- 🟢 **STRONG BUY / BUY**
- 🟡 **BUY IF PPI PASSES / NEGOTIATE**
- 🟠 **HIGH-RISK BUY**
- 🔴 **AVOID**

Use compact confidence labels: **Verified**, **Seller claim**, **Recurring pattern**, **Unknown**.

Do not use decorative emojis elsewhere. Keep paragraphs under three sentences and table cells concise.

## 1. Hero verdict

```markdown
# [Year Make Model Trim]
*[Mileage] · [Location] · [Seller type]*

## [marker] [VERDICT] — [score]/100

[One decisive paragraph: pursue/pass, why, and the condition that could change it.]

| Asking | Fair value | Maximum offer | Confidence | Dealer concern |
|---:|---:|---:|---|---|
| ... | ... | ... | ... | ... |
```

The hero must answer the buying question without scrolling.

## 2. Decision drivers

Use three columns and no more than two lines per cell:

| Mechanical | Financial | Transaction |
|---|---|---|
| Biggest powertrain/maintenance fact | Price versus comps and true cost | Dealer/history/PPI fact |

## 3. Score profile

Show the scoring structure without a dense nine-column table:

| Category | Score | Category | Score |
|---|---:|---|---:|
| Engine/propulsion | x/15 | Transmission/drivetrain | x/15 |
| Maintenance outlook | x/15 | History | x/12 |
| Condition/evidence | x/8 | Repairability | x/10 |
| Value | x/10 | Driving | x/10 |
| Fuel/energy | x/5 | Penalties | −x |

Add one sentence explaining the weakest score and any catastrophic-risk penalty.

## 4. Candidate snapshot

| Item | Finding | Status |
|---|---|---|
| Exact powertrain | ... | Verified/Unresolved |
| Mileage and use | ... | Verified/Seller claim |
| History | ... | Verified/Seller claim/Unknown |
| Tires/brakes | ... | Visible/Unknown |
| Warranty/campaign | ... | Verified/VIN check required |

Include only fields that matter. State identity ambiguity before any reliability conclusion.

## 5. Risk map

Rank by expected money/safety impact. Use 3–6 rows.

| System | Risk and applicability | Likelihood evidence | Cost exposure | Candidate signal |
|---|---|---|---:|---|
| ... | ... | Common/Occasional/Uncertain | ... | Present/Absent/Unknown |

Do not repeat these risks later. Maintenance and PPI sections should reference the row briefly.

## 6. Cost outlook

| Horizon | Expected work | Estimated exposure | Classification |
|---|---|---:|---|
| Before purchase | ... | ... | Immediate/overdue |
| 12 months | ... | ... | Scheduled/wear/reserve |
| 24–36 months | ... | ... | Scheduled/wear/reserve |
| Tail risk | ... | ... | Low-probability, separate |

When annual use is known, state the assumption once. Never mix catastrophic exposure into routine expected cost.
If no defensible local cost basis exists, write **Not credibly estimable before records/PPI** rather than
inventing a range. A clearly labelled planning reserve is allowed, but it is not a repair estimate.

## 7. Price and local market

Show three to five close comps in Standard mode.

| Comparable | Mileage | Asking price | Adjustment |
|---|---:|---:|---|
| ... | ... | ... | Why it is better/worse than candidate |

Then show the bridge:

`clean-market value – immediate work – evidence/risk discount = maximum recommended price`

State advertised asking prices as asks, not sale prices.

## 8. Dealer reputation and transaction risk

Use the compact table from `dealer-reputation.md`. Include licensing/regulator status, written fees, warranty/PPI access, and repeated review themes. End with the concern rating and confidence.

This section is required for dealer listings even when no negative signal is found.

## 9. Driving and practical fit

Use a short line or compact table covering power, transmission behaviour, ride, handling, fuel grade/consumption, cargo, tires, and the buyer's stated priorities. Keep this section proportionate; do not let subjective driving commentary crowd out purchase risk.

Include a **Repairability x/10** call with the two jobs or dependencies that drive it.

## 10. PPI priorities

List 5–8 model-specific checks ordered by severity. Include diagnostic scan targets, cold-start behaviour, leaks, transmission/AWD/battery tests, accident-repair clues, tire/brake measurements, and any campaign verification.

## 11. Seller questions and negotiation

Ask 3–6 evidence-seeking questions. Then provide:

- **Opening offer:** [amount and basis]
- **Target:** [amount]
- **Walk-away:** [amount or condition]

Do not create false precision when history or condition is unknown.

## 12. Walk-away triggers

Give 3–5 observable triggers: title/history contradiction, unresolved warning codes, PPI refusal, structural evidence, missing high-value service proof, or written-fee contradiction.

## 13. Bottom line

Use two sentences: the canonical decision and the single best next action. Add one short sentence that this research does not replace an independent inspection or official title/lien verification.

## Deep-mode additions

Deep reports may add:

- fuller VIN/listing chronology
- 12/24/36-month ownership-cost scenarios
- broader comparable set
- ownership panel from `decision-panel.md`
- negotiation message or inspection handoff

Do not add these to Standard mode merely to make the report longer.
