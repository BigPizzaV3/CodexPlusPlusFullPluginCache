# NEC3/NEC4 Contract Reference

Detailed clause reference for the NEC Engineering and Construction Contract. This document covers the core clauses that are most relevant to commercial management and quantity surveying.

> **Note:** This reference covers the standard form. Project-specific Z-clauses, secondary options, and contract data entries may modify these provisions. Always check the specific contract.

> **Provenance:** clause citations verified 2026-07 against NEC commentary, including the official neccontract.com FAQs and practitioner commentary specific to NEC3 (e.g. gmhplanning.co.uk's clause-by-clause guidance notes and Alistair Blakey's NEC3 "Clauses 60 to 64" commentary), confirming the clause 61.4 and 62.6 deemed-acceptance mechanisms exist in both NEC3 and NEC4 wording. Additionally cross-checked 2026-07 against the full GMH Planning / CECA NEC4 bulletin library (bulletins 1–66), NEC4 ECC Practice Note 1 (Oct 2017), the official NEC4 amendment schedules (Jan 2019, Oct 2020, Jan 2023) and GMH's NEC3→NEC4 clause-by-clause comparison — see `references/gmh-ceca-index.md` for the topic index and `docs/nec4-source-review.md` in the repository for the review record. Items that could only be verified against secondary sources are hedged in the text. Report suspected errors via the repository issue tracker.

---

## Main Options Summary

| Option | Type | Pricing Basis | Risk Profile |
|--------|------|---------------|--------------|
| **A** | Priced contract with activity schedule | Lump sum prices for each activity | Contractor bears cost risk. Payment on completion of activities. |
| **B** | Priced contract with bill of quantities | Rates and quantities | Contractor bears rate risk, Employer bears quantity risk (re-measurement). |
| **C** | Target contract with activity schedule | Target price from activity schedule; actual payment on Defined Cost + Fee | Shared risk via pain/gain mechanism. |
| **D** | Target contract with bill of quantities | Target price from BoQ; actual payment on Defined Cost + Fee | Shared risk via pain/gain mechanism. |
| **E** | Cost reimbursable | Defined Cost + Fee | Employer bears all cost risk. |
| **F** | Management contract | Defined Cost + Fee for subcontracted work + management fee | Employer bears cost risk through subcontracts. |

### Pain/Gain Mechanism (Options C and D)

The Contractor's share percentage is stated in the Contract Data. At Completion:
- If actual Defined Cost + Fee < final target price → the Contractor receives a share of the saving (gain)
- If actual Defined Cost + Fee > final target price → the Contractor bears a share of the overrun (pain)

The target is adjusted for implemented compensation events, so the risk sharing only applies to cost variance within the Contractor's control. Two subtleties: realised Contractor risk within Defined Cost is still paid by the Client as it is incurred (the pain/gain wash-up comes later), and X20 KPI payments sit **outside** Defined Cost/PWDD, so they do not enter the pain/gain calculation.

---

## Secondary Options (Selected)

Selected in Contract Data part 1; check which apply before advising. The commercially significant ones:

| Option | Subject | QS-critical point |
|---|---|---|
| X1 | Price adjustment for inflation | Also adjusts CE assessment: Defined Cost at the dividing date is deflated to base-date levels via the Price Adjustment Factor (X1.5); people/Equipment use base-date levels from Contract Data |
| X2 | Changes in the law | A change in the law after the Contract Date is a CE |
| X5 / X6 / X7 | Sectional completion / early-completion bonus / delay damages | **Omitting X7 does not mean no liability** — damages become unliquidated "at large"; a genuine nil rate must be drafted expressly |
| X11 (NEC4) | Termination by the Client | Restores the Client's terminate-for-any-reason right that NEC4 removed from the core; Contractor gets Fee on removed work |
| X13 / X16 | Performance bond / retention | X16.2: retention halves at the first assessment after Completion |
| X15 | Contractor's design — reasonable skill and care | **Omitting X15 leaves the Contractor with a fitness-for-purpose design obligation**, which professional indemnity insurance typically does not cover |
| X18 | Limitation of liability | X18.6 cuts off liability for matters not notified before the end of the liability period; X29 Performance Table payments are excluded from the cap |
| X20 | Key Performance Indicators | Client may **add** KPIs/payments but never delete or reduce one already stated; KPI payments sit outside Defined Cost/PWDD and the pain/gain share |
| X21 (NEC4) | Whole life cost | Contractor proposals to reduce operating cost |
| X22 (NEC4) | Early Contractor Involvement | Two-stage single contract (intended for Options C/E). **Hard CE cut-off: Stage One events must be captured in the Stage Two proposals — nothing can be notified for Stage One after the Notice to Proceed to Stage Two.** A decision not to proceed to Stage Two is not a CE and not termination; no lost-fee entitlement for Stage Two. Budget incentive is asymmetric (share of underspend only) |
| X29 (2023 amendments) | Climate change | Requires a climate change plan (submitted for acceptance); Performance Table payments; its own early-warning and CE interactions |
| Y(UK)1 / Y(UK)2 / Y(UK)3 | Project Bank Account / HGCRA / third-party rights | Y(UK)2 carries the UK Construction Act payment machinery (pay-less notices; a Contractor application can become the default payment notice if the PM fails to certify); Contractor suspension for non-payment under Y(UK)2 is itself a CE |
| W1 / W2 / W3 | Dispute resolution | W2 where the UK Construction Act applies; W3 (NEC4) is a standing Dispute Avoidance Board; NEC4 adds a senior-representatives negotiation step before adjudication |
| Clause 16 (NEC4 core) | Contractor's proposals | Not a secondary option but easily confused: NEC4 clause 16 is **value engineering** (Contractor proposes a Scope change to reduce cost; PM replies within 4 weeks; saving shared via the Contract Data percentage). NEC3's clause 16 was early warning — always disambiguate by edition |

---

---

## Main Options A-F (Compact)

The choice of main option fundamentally affects payment, risk allocation, and CE assessment. Full descriptions are in the reference.

| Option | Basis | Who carries cost risk | Typical use |
|---|---|---|---|
| A | Priced, Activity Schedule (lump sums per activity) | Contractor | Well-defined scope; most common in UK infrastructure |
| B | Priced, Bill of Quantities (re-measured) | Client (quantities), Contractor (rates) | Uncertain quantities (earthworks, groundworks) |
| C | Target, Activity Schedule — Defined Cost + Fee with pain/gain | Shared via share percentages | Collaborative major projects (standard for most Network Rail / National Highways work) |
| D | Target, Bill of Quantities | Shared | Target contracts with uncertain quantities |
| E | Cost reimbursable (Defined Cost + Fee, no target) | Client | Emergency or highly uncertain scope |
| F | Management contract | Client | Professional management layer over subcontract packages |

Key CE distinction: under A/B the CE assessment is the final price (forecast-based; actual cost irrelevant once implemented); under C/D the CE adjusts the **target**, while payment remains actual Defined Cost + Fee.

---
