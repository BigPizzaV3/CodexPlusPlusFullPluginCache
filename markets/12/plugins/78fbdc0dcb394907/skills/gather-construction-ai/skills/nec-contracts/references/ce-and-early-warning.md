# NEC3/NEC4 Contract Reference

Detailed clause reference for the NEC Engineering and Construction Contract. This document covers the core clauses that are most relevant to commercial management and quantity surveying.

> **Note:** This reference covers the standard form. Project-specific Z-clauses, secondary options, and contract data entries may modify these provisions. Always check the specific contract.

> **Provenance:** clause citations verified 2026-07 against NEC commentary, including the official neccontract.com FAQs and practitioner commentary specific to NEC3 (e.g. gmhplanning.co.uk's clause-by-clause guidance notes and Alistair Blakey's NEC3 "Clauses 60 to 64" commentary), confirming the clause 61.4 and 62.6 deemed-acceptance mechanisms exist in both NEC3 and NEC4 wording. Additionally cross-checked 2026-07 against the full GMH Planning / CECA NEC4 bulletin library (bulletins 1–66), NEC4 ECC Practice Note 1 (Oct 2017), the official NEC4 amendment schedules (Jan 2019, Oct 2020, Jan 2023) and GMH's NEC3→NEC4 clause-by-clause comparison — see `references/gmh-ceca-index.md` for the topic index and `docs/nec4-source-review.md` in the repository for the review record. Items that could only be verified against secondary sources are hedged in the text. Report suspected errors via the repository issue tracker.

---

## Core Clause 6: Compensation Events

This is the most commercially significant section of the NEC contract.

### Clause 60 — Compensation Events

**Clause 60.1** lists the grounds for compensation events. The key grounds are:

| Ground | Description | Common Examples |
|--------|-------------|-----------------|
| 60.1(1) | PM gives an instruction changing the Scope (Works Information) | Variation order, design change, additional work |
| 60.1(2) | Employer does not allow access by the access date | Late possession, access restriction |
| 60.1(3) | Employer does not provide something by the date for providing it | Information, materials, approvals |
| 60.1(4) | PM gives an instruction to stop or not to start work | Stop instruction, suspension |
| 60.1(5) | Employer or Others do not work within the conditions stated, or carry out work not in the Works Information | Third party interference, utility diversions |
| 60.1(6) | PM does not reply within the period for reply | Failure to accept programme, design, etc. |
| 60.1(7) | PM gives an instruction for dealing with an object of value or historical interest | Archaeological finds |
| 60.1(8) | PM or Supervisor changes a decision previously communicated | Changed instruction |
| 60.1(9) | PM withholds an acceptance for a reason not stated in the contract | Unreasonable rejection of programme |
| 60.1(10) | Supervisor instructs searching for a Defect and no Defect found | Abortive testing/inspection |
| 60.1(11) | A test or inspection causes unnecessary delay | Testing delay |
| 60.1(12) | Physical conditions within the Site which an experienced contractor would have judged at the Contract Date to have such a small chance of occurring that it would have been unreasonable to allow for them | Unforeseen ground conditions |
| 60.1(13) | A weather measurement is recorded within a calendar month which, by comparison with the weather data, is shown to occur on average less frequently than once in ten years | Exceptional weather — the "once in 10 years" test. Requires actual meteorological data compared against historical records; only qualifying weather triggers a CE, and only the **excess over the one-in-ten-year value** is compensable, not the whole month. Only the measurements stated in Contract Data can found a CE (standard four: cumulative rainfall, days rainfall >5mm, days min temp <0°C, days snow lying) — wind, fog etc. count only if added at tender |
| 60.1(14) | Employer risk event | Events listed in clause 80.1 |
| 60.1(15) | PM certifies take over of part of the works before Completion | Partial possession |
| 60.1(16) | Employer does not provide materials, facilities, or samples for tests | Missing test materials |
| 60.1(17) | PM notifies a correction to an assumption about a CE | Changed assumption |
| 60.1(18) | A breach of contract by the Employer | Any other Employer breach |
| 60.1(19) | An event which stops the Contractor completing the works (or completing by the date shown on the Accepted Programme), which neither Party could prevent, and which an experienced contractor would have judged at the Contract Date to have such a small chance of occurring that it would have been unreasonable to have allowed for it | Prevention event |

**NEC4 additions:** NEC4 keeps 60.1(1)-(19) with essentially identical numbering and adds two further grounds: **60.1(20)** (the PM notifies the Contractor that a quotation for a proposed instruction is not accepted — compensating abortive quotation cost) and **60.1(21)** (additional compensation events stated in the Contract Data).

**Options B and D only — quantity/BoQ grounds (60.4–60.7):** a difference between the final measured quantity and the BoQ quantity is a CE only where it changes the Defined Cost per unit **and** the rate × BoQ quantity exceeds 0.5% of the total of the Prices at the Contract Date (60.4 — e.g. on a £1m contract a line item must be worth more than £5,000; below the threshold the BoQ rate simply applies to the measured quantity). Quantity changes that delay Completion are a CE even if individually below the threshold (60.5). A correction of a mistake in the BoQ (departure from the method of measurement, or an ambiguity/inconsistency) is a CE (60.6), and in assessing it the Contractor is deemed to have taken the BoQ as correct (60.7).

### Clause 61 — Notifying Compensation Events

**61.1** For compensation events arising from the PM or Supervisor giving an instruction or changing an earlier decision, the PM notifies the Contractor of the compensation event at the time of that communication. In practice, PMs often issue instructions without notifying them as CEs — the Contractor must then notify under 61.3.

**61.3** The Contractor notifies the PM of a compensation event which has not been notified by the PM. **The Contractor must notify within 8 weeks of becoming aware of the event.** If the Contractor fails to notify within 8 weeks, the Contractor is not entitled to changes in the Prices, the Completion Date, or the Key Dates — unless the event arises from the PM or Supervisor giving an instruction, issuing a certificate, changing an earlier decision, or correcting an assumption (i.e., events the PM should have notified: grounds **60.1(1), (4), (7), (8), (15) and (17)**). The bar therefore applies to the Contractor-notifiable grounds — e.g. 60.1(2) access, 60.1(12) physical conditions, 60.1(13) weather.

Notifying an **early warning does not stop or extend the 61.3 clock** — an EW is not a substitute CE notification. If a matter first flagged as an EW crystallises into a CE, the 8 weeks runs from awareness of the CE, and a separate CE notification is still required.

**61.4** The PM decides whether the event is a compensation event and notifies the Contractor within one week of the Contractor's notification (both NEC3 and NEC4, or a longer period agreed with the Contractor). The PM's response either **accepts it is a CE** (and instructs the Contractor to submit quotations) or notifies that the Prices, Completion Date and Key Dates are not to be changed because the PM decides the event:
1. **Arises from a fault of the Contractor**
2. **Has not happened and is not expected to happen**
3. **Has no effect on Defined Cost, Completion, or meeting a Key Date**
4. **Is not one of the compensation events stated in the contract**

(In practice PMs also reply that the notification was out of time — but the time bar operates under 61.3, not as a 61.4 decision ground.)

If the PM fails to reply, the Contractor may notify the failure; if the PM still does not reply within two further weeks, this is treated as acceptance that the event is a compensation event and an instruction to submit quotations (deemed acceptance under 61.4 — both NEC3 and NEC4).

**61.6** Where the effects of a CE are too uncertain to forecast reasonably, the PM may state assumptions on which the quotation is to be based; if an assumption later proves wrong, the PM notifies a correction, which is itself a compensation event (60.1(17)).

**Commercial significance:** The 8-week notification rule is the single most important timescale in NEC contracts. A genuine compensation event that is not notified within 8 weeks is time-barred (unless it is an event the PM should have notified). QSs must maintain a register of potential CEs and ensure timely notification.

### Clause 62 — Quotations for Compensation Events

**62.1** After discussing with the Contractor different practicable ways of dealing with the compensation event, the PM may instruct the Contractor to submit alternative quotations.

**62.3** The Contractor submits quotations within three weeks of being instructed (unless the PM agrees a longer period). The PM replies within two weeks of the submission.

**Quotation content:** a CE quotation must include:
1. **Changes to the Prices** — the proposed adjustment to the contract price
2. **Delay to the Completion Date** — the proposed change to the Completion Date (if any)
3. **Delay to any Key Dates** — proposed changes to Key Date conditions
4. **Details of the assessment** — a breakdown showing how the quotation was built up from Defined Cost + Fee

**62.6** (both NEC3 and NEC4) If the PM does not reply to a quotation within the time allowed, the Contractor may notify the PM of the failure; if the PM still does not reply within a further two weeks, the quotation is treated as accepted. Deemed acceptance is not automatic — it requires the Contractor's notification and the further two weeks of silence — and in NEC3 it does not apply to a quotation for a proposed instruction or a proposed changed decision (in NEC4, proposed instructions are dealt with separately under clause 65).

If the Contractor does not submit a quotation within the time allowed, or the PM does not accept it, the PM may assess the compensation event under clause 64.1.

### Clause 63 — Assessing Compensation Events

**63.1** The changes to the Prices are assessed as the effect of the compensation event on **Defined Cost** plus the **Fee**.

CEs are assessed as actual Defined Cost for work already done and forecast Defined Cost for work not yet done — never by waiting for outturn cost. Both editions fix the point of the actual/forecast split early in the CE's life (see below); it does not drift to whenever the assessment is eventually carried out. This is a fundamental principle of NEC assessment.

**NEC4 dividing date (63.1):** Defined Cost is assessed as **actual** Defined Cost for work done by the dividing date and **forecast** Defined Cost for work not yet done at the dividing date. The dividing date itself depends on how the event arose:
- For a CE that arises from the PM or Supervisor giving an instruction or notification, issuing a certificate, or changing an earlier decision — the dividing date is the date of **that communication**.
- For **other compensation events** (e.g. 60.1(2) Client not allowing access, 60.1(3) something not provided, 60.1(13) weather) — the dividing date is the date the **compensation event is notified** (typically by the Contractor under 61.3).

In practice this means a quotation can (and should) use **actual records for impact already incurred before the dividing date — e.g. recorded standing time from site diaries — and forecast Defined Cost for the ongoing impact after it, including time risk allowances in the forecast** (risk allowances for matters with a significant chance of occurring are the Contractor's entitlement under 63.8 NEC4 / 63.6 NEC3).

**NEC3 fixes the same divide differently (63.1):** "the date when the Project Manager instructed or should have instructed the Contractor to submit quotations divides the work already done from the work not yet done." NEC4's change was to make "dividing date" a defined term and re-anchor it to the date of the PM/Supervisor communication or of the CE notification. Under both editions, therefore, the actual/forecast split is fixed by an event early in the CE's life — **not** by when the assessment happens to be carried out. A CE assessed late — or retrospectively in adjudication — is still valued on the forecast as it stood at the dividing date/line, not on hindsight outturn cost.

Two consequences of the fixed divide:
- A CE arising from a PM instruction (e.g. a 60.1(1) Scope change) is assessed on **forecast Defined Cost only** — the dividing date is the instruction itself, so no compensable work precedes it. Even if actual costs become known before the CE is agreed, they must not be used to adjust the assessment in either direction, and neither party gains from delaying agreement to "wait and see".
- **63.9 NEC4 (63.7 NEC3)** underpins this: the assessment assumes the Contractor reacts **competently and promptly** to the event and that Defined Cost is reasonably/properly incurred — a Contractor cannot improve its position by delaying notification so that inefficient actual costs replace a forecast.

**Forecast vs actual across the main Options:**
- Under Options A and B: CEs are assessed based on **forecasts** made at the time of assessment. Actual cost is irrelevant once the CE is implemented. This is a deliberate incentive mechanism — the Contractor benefits from efficiency and bears the risk of inefficiency.
- Under Options C, D, and E: The assessment adjusts the target or Prices, but the Contractor is paid actual Defined Cost regardless. The CE assessment affects the target (and therefore the pain/gain calculation) but not interim payments.

**Defined Cost under each Option:**

| Option | Defined Cost Means |
|---|---|
| A | Forecast change to Defined Cost (Shorter Schedule of Cost Components — "Short Schedule" in NEC4) |
| B | Forecast change to Defined Cost (Shorter SCC); BoQ rates and lump sums may be used if the PM and Contractor agree |
| C, D | Forecast impact on the target — based on Defined Cost (SCC or SSCC) |
| E | Actual Defined Cost (SCC or SSCC) |

**63.3 (NEC3) / 63.5 (NEC4)** The delay to the Completion Date is assessed as the length of time that, due to the compensation event, planned Completion is later than planned Completion shown on the Accepted Programme. **NEC4 (63.5) anchors this explicitly: the comparison uses the Accepted Programme current at the dividing date** (see 63.1 above for how the dividing date is fixed — for a 60.1(2) access event, for example, it is the date the Contractor notifies the CE). The same rule applies to Key Dates and Sectional Completion Dates.

**The January 2019 amendment to 63.5** added that the assessment "takes into account events which have happened between the date of the Accepted Programme and the dividing date" (folding NEC's October 2017 Practice Note 1 into the contract wording). In practice this is a **two-programme method**: (1) bring the Accepted Programme current at the dividing date up to date with actual progress, other CEs already in the system, and non-CE delays up to the dividing date, and reschedule — fixing where planned Completion stood immediately before the new event; (2) add the new CE, logic-linked, and reschedule — the further movement of planned Completion is the entitlement. Include both (filtered) programmes in the quotation, plus the time-related (preliminaries) cost of the extension. This assessment mark-up is **not** a clause 32.2 programme revision and is not itself submitted for acceptance. A regularly Accepted Programme keeps step (1) small and objective; months of unaccepted programmes make it subjective and contentious.

**Basis of assessment:**
- **NEC4:** the Accepted Programme **current at the dividing date** (63.5), updated to the dividing date as above.
- **NEC3:** the Accepted Programme referred to in 63.3 — the edition does not say which one, and in practice the latest Accepted Programme at the 63.1 dividing line is used (the debate NEC4 resolved expressly).
- **If the Accepted Programme is stale, unsubmitted, or a recent submission was rejected** (NEC4 Practice Note 1): the parties should first try to **agree** a programme to use for the assessment — where the PM's non-acceptance reasons do not bear on the CE, that can be the Contractor's submitted-but-unaccepted programme. Only failing agreement does the PM assess under clause 64, based on the previous Accepted Programme. Do not jump straight to "no Accepted Programme = PM assesses unilaterally".

**Concurrency:** NEC has no concurrent-delay doctrine to import. Overlapping events are resolved by **chronological sequencing**: each CE is assessed against the programme current at (and updated to) its own dividing date, in order. Whichever event first moved planned Completion has consumed the time; float legitimately eaten by one party's earlier delay is simply gone when the later event is assessed. Multiple CEs arising in a short period may be bundled by agreement, but the default is sequential, separate, prospective assessment.

**63.5 (NEC3) / 63.7 (NEC4)** If the PM has notified under clause 61.5 that the Contractor did not give an early warning which an experienced contractor could have given, the event is assessed as if the Contractor had given the early warning.

**Commercial significance:** The assessment is based on Defined Cost + Fee, not the rates in the Activity Schedule or Bill of Quantities (BoQ/Activity Schedule rates may be used only by agreement, 63.2). For Options A and B, this means CE assessments may differ from the original pricing basis. Under Options A/B the cost of **preparing** the quotation is excluded from it; under Options C–E it is included. The use of the Accepted Programme is critical — a missing or unaccepted programme pushes the assessment toward the PM's own view (via the Practice Note 1 agree-first process above, then clause 64), which is rarely more generous than the Contractor's quotation.

### Clause 64 — The Project Manager's Assessments

**64.1** The PM assesses a CE if:
- The Contractor has not submitted quotations within the required timescale
- The PM decides the Contractor has not assessed correctly (and does not instruct a revised quotation)
- The Contractor has not submitted a programme required by the contract
- The PM has not accepted the Contractor's latest programme for a reason stated in the contract

**64.4 — deemed acceptance of the Contractor's quotation:** the PM must make their own assessment within the same period the Contractor had for the quotation. If the PM does not, the Contractor may notify the failure; a further **two weeks** of silence means the Contractor's **original quotation is treated as accepted** — even though the PM had rejected it to make their own assessment. This exists in both editions (NEC3 via the April 2013 amendment) and completes the deemed-acceptance family: programme 31.3 (NEC4 only), CE notification 61.4, quotation 62.6, PM's own assessment 64.4, and Defined Cost finalisation 50.9 (NEC4, Options C–F). Outside these mechanisms there is **no** deemed acceptance — PM silence on a design submission, acceleration quotation or proposed-instruction quotation just stalls the matter (at most a 60.1(6) CE); the Contractor must not treat silence as acceptance and proceed.

### Clause 65 (NEC3) / Clause 66 (NEC4) — Implementing Compensation Events

**65.1** The PM implements each compensation event by notifying the Contractor of the quotation accepted or the PM's assessment.

**65.2** The assessment of a CE is not revised if a forecast is shown to be wrong (NEC3) — this locks in the assessment at the time it is made.

**Commercial significance:** Clause 65.2 is crucial. Once a CE is implemented, the financial assessment is final even if actual costs differ. This means the Contractor bears the risk of underestimating and benefits from overestimating the impact at the time of assessment.

---


---

## Early Warning — Clause 16 (NEC3) / Clause 15 (NEC4)

### Clause 16 (NEC3) / Clause 15 (NEC4) — Early Warning

**16.1 (NEC3) / 15.1 (NEC4)** The Contractor and the PM give an early warning by notifying the other as soon as either becomes aware of any matter which could:
- Increase the total of the Prices
- Delay Completion
- Delay meeting a Key Date
- Impair the performance of the works in use

The matter is recorded in the **Risk Register** (NEC3) / **Early Warning Register** (NEC4).

**16.2 (NEC3) / 15.2 (NEC4)** Either Party may instruct the other to attend a **risk reduction meeting** (NEC3) / **early warning meeting** (NEC4).

**NEC4 kick-off timescales (15.2/15.4):** the PM issues the first Early Warning Register within **one week** of the starting date and instructs the Contractor to attend the first early warning meeting within **two weeks** of the starting date; Contract Data states the interval for subsequent meetings. Note there is **no contractual obligation to reply to an early warning notification** and no period-for-reply attaches to it (a common misconfiguration in contract-administration platforms) — the response mechanism is the meeting, not a reply.

**16.3 (NEC3) / 15.3 (NEC4)** At the meeting, those who attend co-operate in:
- Making and considering proposals for reducing the effects of the risk
- Seeking solutions that will bring advantage to all parties
- Deciding on actions

**Sanction for failure to warn:** If the Contractor did not give an early warning which an experienced contractor could have given, the PM notifies this when notifying the CE decision (clause 61.5) and the CE is assessed as if the early warning had been given — clause 63.5 (NEC3) / 63.7 (NEC4). This may reduce the compensation.

**Commercial significance:** Early warnings are not just good practice — they are contractual obligations. Failure to give an early warning can reduce the compensation for a CE under clause 63.5 (NEC3) / 63.7 (NEC4), applied via a PM notification under clause 61.5. QSs should maintain an early warning register alongside their CE register.

---
