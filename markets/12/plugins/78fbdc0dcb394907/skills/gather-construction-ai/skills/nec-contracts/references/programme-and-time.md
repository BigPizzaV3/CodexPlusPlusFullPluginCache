# NEC3/NEC4 Contract Reference

Detailed clause reference for the NEC Engineering and Construction Contract. This document covers the core clauses that are most relevant to commercial management and quantity surveying.

> **Note:** This reference covers the standard form. Project-specific Z-clauses, secondary options, and contract data entries may modify these provisions. Always check the specific contract.

> **Provenance:** clause citations verified 2026-07 against NEC commentary, including the official neccontract.com FAQs and practitioner commentary specific to NEC3 (e.g. gmhplanning.co.uk's clause-by-clause guidance notes and Alistair Blakey's NEC3 "Clauses 60 to 64" commentary), confirming the clause 61.4 and 62.6 deemed-acceptance mechanisms exist in both NEC3 and NEC4 wording. Additionally cross-checked 2026-07 against the full GMH Planning / CECA NEC4 bulletin library (bulletins 1–66), NEC4 ECC Practice Note 1 (Oct 2017), the official NEC4 amendment schedules (Jan 2019, Oct 2020, Jan 2023) and GMH's NEC3→NEC4 clause-by-clause comparison — see `references/gmh-ceca-index.md` for the topic index and `docs/nec4-source-review.md` in the repository for the review record. Items that could only be verified against secondary sources are hedged in the text. Report suspected errors via the repository issue tracker.

---

## Core Clause 3: Time

### Clause 30 — Starting and the Completion Date

**30.1** The Contractor does not start work on the Site before the starting date.

**30.3** The Contractor does the work so that the Condition stated for each Key Date is met by the Key Date.

**Key Date liability (25.3):** if the Condition for a Key Date is not met by the Key Date, the Contractor pays the additional cost the Client incurs — but only cost incurred **in carrying out work** on the same project or **paying others to do work** (plant hire, storage, re-mobilisation and the like). Pure time-related/preliminaries-type losses are not recoverable via 25.3 — that is what Sectional Completion (X5) with X7 delay damages is for, and claiming both for the same loss risks double recovery. The PM assesses within four weeks of the Condition being met.

**Delay damages:** The core NEC clauses contain no delay damages. Delay damages for late Completion apply only if secondary Option X7 is selected in the Contract Data, at the rate stated there. If X7 is not selected, the Client's remedy for late Completion is unliquidated ("at large") damages proved at common law — omitting X7 does not mean zero liability.

**Acceleration (clause 36):** either party may propose bringing the Completion Date forward (NEC4; under NEC3 only the PM instructs a quotation). The Contractor quotes, and acceleration happens only if the quotation is **accepted — there is no PM own-assessment route for an acceleration quotation** (unlike CEs under clause 64), because its dominant component is the Contractor's risk pricing for committing to the earlier date. Acceleration cannot be imposed (watch for Z-clauses attempting to make it compellable). Note the asymmetry: a PM **can** instruct an earlier Key Date under 14.3 (a CE, and if the quotation is not agreed the PM can impose its own assessment) — effectively compellable acceleration of a Key Date, but not of the Completion Date.

### Clause 31 — The Programme

**31.1** If a programme is not identified in the Contract Data, the Contractor submits a first programme within the period stated.

**31.2** The Contractor's programme shows:
- The starting date, access dates, and Key Dates
- Planned Completion (which may be before the Completion Date)
- The order and timing of work
- Float and time risk allowances
- Health and safety requirements
- Procedures for the work

"Float" here means **total float**; **time risk allowances (TRA)** are a separate requirement and must be shown separately (in practice, a TRA column stating the days allowed within each activity duration). A programme with no or implausible TRA on critical activities is unrealistic and can be rejected under 31.3 on that ground.

**31.3** Within two weeks of the Contractor submitting a programme for acceptance, the PM either accepts it or notifies the Contractor of the reasons for not accepting it. The only reasons for not accepting are that:
- The Contractor's plans which it shows are not practicable
- It does not show the information which the contract requires
- It does not represent the Contractor's plans realistically
- It does not comply with the Works Information (Scope)

**NEC4 addition (31.3):** if the PM does not respond within the time allowed, the Contractor may notify the PM of the failure; if the failure continues for one further week, the programme is treated as accepted. NEC3 has no deemed acceptance of the programme.

**Commercial significance:** The programme is a contractual document under NEC. A rejected programme or failure to submit a programme has serious consequences — including potential assessment of CEs using the PM's own assessment, and **25% of the Price for Work Done to Date may be withheld until a first programme showing the information the contract requires has been submitted (NEC3 50.3 / NEC4 50.5)**.

### Clause 32 — Revising the Programme

**32.1** The Contractor shows on each revised programme the actual progress achieved, how delays will be dealt with, and the effects of compensation events. **Edition difference:** NEC3 32.1 requires the effects of **implemented** CEs (non-implemented CEs enter the programme through the realistic-remaining-work requirement — a notified CE using resources or on the critical path cannot be omitted merely because it is not yet implemented). NEC4 deliberately dropped the word "implemented" — the official rationale was "to avoid any potential misunderstanding that non-implemented compensation events are excluded (which is not the case)". On an NEC4 programme, show the effects of notified/ongoing CEs moving **planned Completion** only; the **Completion Date** moves only when a CE is implemented.

**32.2** The Contractor submits a revised programme at intervals no longer than the interval stated in the Contract Data.

---
