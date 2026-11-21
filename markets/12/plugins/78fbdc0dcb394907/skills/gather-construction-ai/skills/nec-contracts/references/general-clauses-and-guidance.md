# NEC3/NEC4 Contract Reference

Detailed clause reference for the NEC Engineering and Construction Contract. This document covers the core clauses that are most relevant to commercial management and quantity surveying.

> **Note:** This reference covers the standard form. Project-specific Z-clauses, secondary options, and contract data entries may modify these provisions. Always check the specific contract.

> **Provenance:** clause citations verified 2026-07 against NEC commentary, including the official neccontract.com FAQs and practitioner commentary specific to NEC3 (e.g. gmhplanning.co.uk's clause-by-clause guidance notes and Alistair Blakey's NEC3 "Clauses 60 to 64" commentary), confirming the clause 61.4 and 62.6 deemed-acceptance mechanisms exist in both NEC3 and NEC4 wording. Additionally cross-checked 2026-07 against the full GMH Planning / CECA NEC4 bulletin library (bulletins 1–66), NEC4 ECC Practice Note 1 (Oct 2017), the official NEC4 amendment schedules (Jan 2019, Oct 2020, Jan 2023) and GMH's NEC3→NEC4 clause-by-clause comparison — see `references/gmh-ceca-index.md` for the topic index and `docs/nec4-source-review.md` in the repository for the review record. Items that could only be verified against secondary sources are hedged in the text. Report suspected errors via the repository issue tracker.

---

## Core Clause 1: General

### Clause 10 — Actions

**10.1 (NEC3)** The Employer, the Contractor, the Project Manager and the Supervisor shall act as stated in this contract and in a spirit of mutual trust and co-operation.

**NEC4 splits this into two clauses:** 10.1 (act as stated in the contract) and 10.2 (act in a spirit of mutual trust and co-operation) — two distinct, cumulative obligations, not one blended duty. Cite 10.2 for the mutual-trust obligation on an NEC4 contract.

**Commercial significance:** This overarching obligation means both parties must act reasonably and not obstruct each other. It is often cited in disputes where one party argues the other acted in bad faith (e.g., unreasonably rejecting a programme or withholding information). It does **not** justify acting on verbal instructions — a Scope-change instruction must still be given in writing under clauses 13/14.3 before it is acted on.

### Clause 11 — Identified and Defined Terms

Key defined terms QSs must understand:
- **Completion** — when the Contractor has done all the work the Works Information states must be done by the Completion Date and corrected Defects preventing the Employer from using the works
- **Completion Date** — the date by which Completion is required, as adjusted by compensation events
- **Defects Date** — a fixed date stated in the Contract Data, a set period after Completion; distinct from the defect correction period, which is the separate period within which each notified Defect must be corrected
- **Defined Cost** — the cost of the work calculated in accordance with the contract (differs by main option)
- **Fee** — the percentage applied to Defined Cost to cover overheads and profit
- **Key Date** — a date by which a condition must be met (not the same as the Completion Date)
- **Prices** — the lump sums and rates in the Activity Schedule or Bill of Quantities
- **Works Information** — the specification and drawings defining what the Contractor must build (called "Scope" in NEC4)

### Clause 13 — Communications

**13.1** Each communication must be in a form that can be read, copied, and recorded. Every instruction, certificate, submission, notification, and reply must be communicated separately.

**13.7** A notification must be communicated separately from other communications.

**NEC4 13.2:** where the Scope specifies a communication system (e.g. a cloud contract-administration platform), a communication has effect only when communicated through that system — a CE notification sent by email outside the specified system risks having no contractual effect.

**NEC4 13.4:** a reply that does not accept a submission must state reasons in sufficient detail to enable the Contractor to correct and resubmit — grounds to push back on vague, boilerplate rejections. A "holding response" does not satisfy a reply obligation.

**Commercial significance:** The requirement for separate notification is critical for compensation events. A CE notification buried in minutes or emails may not comply with clause 13.

### Clause 14 — The Project Manager and the Supervisor

**14.1** The PM's (or Supervisor's) acceptance of a communication or of work does **not** change the Contractor's responsibility to Provide the Works or its liability for its design. "But the PM accepted it" is not a defence — acceptance is a check for obvious problems, not a transfer of risk. (NEC deliberately says "acceptance", not "approval"; the only "approval" in the contract is the Contractor obtaining design approval from Others under 27.1.)

**14.2** The PM and the Supervisor, after notifying the Contractor, may delegate any of their actions and may cancel any delegation.

**14.3** The PM may give an instruction to the Contractor which changes the Works Information (Scope in NEC4).

**Commercial significance:** Only the PM (or their delegate) can give contractual instructions. Instructions from anyone else are not binding. QSs should verify the authority of anyone giving instructions that change the scope.

---

## Core Clause 2: Contractor's Main Responsibilities

### Clause 20 — Providing the Works

**20.1** The Contractor provides the works in accordance with the Works Information (Scope).

### Clause 21 — The Contractor's Design

**21.2** The Contractor submits design for acceptance. The PM responds within the period for reply.

**Commercial significance:** If the PM fails to respond to a design submission within the period for reply, this may be a compensation event under clause 60.1(6).

### Clause 25 — Co-operation

**25.1** The Contractor co-operates with Others as stated in the Works Information.

### Clause 26 — Subcontracting

**26.1** If the Contractor subcontracts work, the Contractor is responsible for providing the works as if the work had not been subcontracted.

**26.2** The Contractor submits the name of each proposed Subcontractor to the PM for acceptance.

**26.3** The Contractor submits the proposed conditions of contract for each subcontract for acceptance (unless an NEC contract is proposed or the PM has agreed no submission is required).

**Commercial significance:** The Contractor cannot avoid responsibility by pointing to subcontractor failures. Any subcontractor delay or quality issue remains the Contractor's risk.

---


---

## Core Clause 4: Testing and Defects

NEC4 groups this content as Section 4 "Quality Management," clauses 40–46. NEC3 covers the same substance under its own testing-and-defects clauses, but per CECA Bulletin 16 the renumbering is documented only as "broadly the same in substance, just relabelled and reordered" — the source gives no exact clause-by-clause NEC3 mapping, so confirm against the NEC3 print in use before citing NEC3 numbers for 41–46. Clause 40 itself is new to NEC4 — NEC3 has no equivalent.

### Clause 40 (NEC4 only) — Quality Management

**40.1** The Contractor operates a quality management system and submits both a quality policy statement and a quality plan for PM acceptance by a date stated in Contract Data Part 1. The only ground to reject either is that it would not allow the Contractor to Provide the Works in accordance with the Scope.

**Commercial significance:** If the PM instructs correction of a QMS failure, that instruction is expressly **not** a compensation event — a distinct, easily-missed exception to the general rule that a PM instruction changing the Scope is a CE under 60.1(1).

### Clause 41 — Tests and Inspections

The Contractor and the Supervisor each notify the other before carrying out a test or inspection, and share the results afterwards. The Supervisor must not cause unnecessary delay to the works through testing or inspection — such a delay is itself a CE ground (60.1(11)).

### Clause 42 — Testing Before Delivery

Where the Scope requires Plant and Materials to be tested or inspected before delivery, they are not brought into the Working Areas until the Supervisor has notified the Contractor that they have passed.

### Clause 43 — Searching for and Notifying Defects

Only the Supervisor may instruct the Contractor to search for a Defect (uncovering or removing work covering it). If a Defect is found, the cost of the search is the Contractor's. If no Defect is found, the cost of the search is a compensation event (60.1(10)) — **unless** the Supervisor was not given the opportunity to inspect the work before it was covered up, in which case there is no CE.

### Clause 44 — Correcting Defects

The Contractor corrects a Defect whether or not the Supervisor has notified it. The defect correction period is stated in Contract Data Part 1 and may differ by Defect type. It runs from Completion for a Defect notified before Completion, and from notification for a Defect notified after Completion.

### Clause 45 — Accepting Defects

Either the Contractor or the PM may propose a change to the Scope so that a Defect need not be corrected (typically the Contractor offering a cost saving in exchange for leaving non-compliant work as it is). The PM may accept or reject the proposal but **cannot make its own counter-assessment** of the quoted saving — a rejection prompts a revised proposal, not a PM-imposed figure. If the change is accepted, the resulting Scope-change instruction is expressly **not** a compensation event.

### Clause 46 — Uncorrected Defects

If the Contractor is given access but does not correct a Defect within the defect correction period, the PM assesses the cost to the Client of having it corrected by Others, and the Contractor pays that amount at the next payment assessment. If access is **not** given, the PM instead assesses what it would have cost the Contractor to correct the Defect itself, and the Contractor pays that assessed amount instead.

**Commercial significance:** Under Options C–F, only the cost of correcting a Defect **after Completion** (or of correcting a Defect caused by the Contractor not complying with a stated Scope constraint) is Disallowed Cost. The cost of correcting a Defect **before** Completion is an allowed cost, paid to the Contractor as Defined Cost — do not treat all defect-correction cost as automatically disallowed when assessing PWDD.

---


---

## Key Timescales Summary

| Action | Timescale | Clause |
|--------|-----------|--------|
| Contractor notifies CE | Within 8 weeks of becoming aware | 61.3 |
| PM decides if event is a CE | 1 week (NEC3 and NEC4, or longer agreed period) | 61.4 |
| Contractor submits CE quotation | 3 weeks (or agreed longer) | 62.3 |
| PM responds to CE quotation | 2 weeks of submission | 62.3 |
| PM assesses if Contractor doesn't submit | After quotation deadline passes | 64.1 |
| PM's own assessment overdue → deemed acceptance of quotation | Contractor notifies failure + 2 weeks | 64.4 |
| Defined Cost finalisation review (NEC4, Options C–F) | 13 weeks review + 4 weeks further records + 4 weeks final | 50.9 |
| Final Assessment (NEC4) | 4 weeks after Defects Certificate (13 weeks after termination certificate) | 53 |
| PM replies to Contractor's proposal (NEC4 value engineering) | 4 weeks | 16 |
| Programme submission intervals | As stated in Contract Data | 32.2 |
| Period for reply | As stated in Contract Data, both editions (commonly 2 weeks) | 13.3 / Contract Data |
| PM certifies payment | Within 1 week of each assessment date | 51.1 |
| Payment after assessment | 3 weeks of the assessment date, unless a different period is stated in Contract Data | 51.2 |

---

## Practical Guidance for QSs

### CE Register Management
1. Log every potential CE immediately — even before formal notification
2. Track the 8-week deadline from date of awareness
3. Record the notification date, PM response date, quotation submission date
4. Flag any approaching deadlines weekly
5. If the PM has not responded, track the deemed acceptance date

### Programme Management
1. Submit programme updates at the contractual interval
2. Show actual progress alongside planned
3. Show the effect of CEs: implemented CEs move the Completion Date; notified/ongoing CEs move planned Completion only (NEC3 32.1 says "implemented" — non-implemented CEs still enter via realistic remaining work; NEC4 dropped the word so all CE effects are shown)
4. Understand float ownership — terminal float (between planned Completion and the Completion Date) belongs to the Contractor, as do time risk allowances; other float (**total float** on non-critical activities) is shared and available to absorb delay — including by the Client for CE effects. A CE consuming shared float short of planned Completion has a cost effect only; but if the Contractor's own earlier delay has eaten that float, a later CE moves planned Completion and is compensable — order of events matters
5. A rejected programme must be resubmitted — work to resolve the reasons for rejection

### Record Keeping
1. Keep contemporaneous records of all events that may become CEs
2. Photographs, diary entries, and correspondence are the primary evidence
3. Record weather conditions daily
4. Record access/possession times and any restrictions
5. Record PM instructions and the date they were given
6. Record resource levels and hours worked

### Common Pitfalls
1. **Missing the 8-week notification deadline** — the most common and most costly mistake
2. **Not having an Accepted Programme** — this weakens the Contractor's position on time assessments
3. **Assessing CEs on actual cost** — work after the dividing date/line is assessed on the forecast as at that date, not actual outturn (clause 63.1); actuals are only correct for work done **before** the dividing date. The main practical exception is weather (60.1(13)), where the dividing date (notification) usually falls after the calendar month's data confirms the threshold, so the assessment is largely actual-cost by nature
4. **Confusing completion with planned completion** — the Completion Date and the Contractor's planned completion may differ; float sits between them
5. **Not keeping early warning records** — failure to warn can reduce CE compensation under clause 63.5 (NEC3) / 63.7 (NEC4)

---

## Key Terminology Glossary

| Abbreviation | Full Term | Definition |
|---|---|---|
| **CE** | Compensation Event | An event entitling the Contractor to additional time and/or cost under clause 60. The mechanism by which the contract price and Completion Date are adjusted. |
| **EWN** | Early Warning Notice | A notification under clause 16 (NEC3) / clause 15 (NEC4) of a matter that could increase cost, delay Completion, or impair performance. Either party can issue one. |
| **PM** | Project Manager | The person named in the Contract Data who manages the contract on behalf of the Client. Has wide-ranging powers to instruct, accept, and assess. |
| **Supervisor** | Supervisor | The person named in the Contract Data responsible for quality — testing, inspecting, and checking that work complies with the Works Information / Scope. |
| **Client** | Client (Employer in NEC3) | The party who commissions the work. Called "Employer" in NEC3, renamed "Client" in NEC4. |
| **Accepted Programme** | Accepted Programme | The latest programme accepted by the PM under clause 31-32. Used as the basis for assessing time impact of CEs. Critical for delay and disruption claims. |
| **Defined Cost** | Defined Cost | The cost used to pay (Options C-F) and to assess compensation events (all options). Built from the Schedule of Cost Components (C-E) or the Shorter/Short Schedule (A/B CE assessment). **Activity Schedule / BoQ rates are NOT used to value CEs** unless the PM and Contractor agree (clause 63.2). |
| **Fee** | Fee | A percentage added to Defined Cost to cover the Contractor's overheads and profit, stated in the Contract Data. NEC4 has a **single Fee percentage**; NEC3 had separate direct and subcontracted fee percentages. |
| **PWDD** | Prices for Work Done to Date | The cumulative value of work completed, assessed by the PM at each assessment date. Forms the basis of interim payments. |
| **Activity Schedule** | Activity Schedule | A priced list of activities produced by the Contractor (Options A and C). Each activity has a lump sum price. Payment is made when an activity is complete, not proportionally. |
| **BoQ** | Bill of Quantities | A measured schedule of work items with quantities and rates (Options B and D). Payment is based on quantities of work completed multiplied by the rates. |
| **Works Information** | Works Information (NEC3) / Scope (NEC4) | The specification of what the Contractor must do. Called "Works Information" in NEC3 and "Scope" in NEC4. |
| **Site Information** | Site Information | Information about the site provided by the Client — ground conditions, surveys, existing services, environmental data. |
| **Completion** | Completion | The date when the Contractor has done all the work required by the Scope/Works Information, except minor outstanding items that do not prevent the Client from using the works. |
| **Completion Date** | Completion Date | The date by which the Contractor is required to achieve Completion. This can change through CEs — it is not fixed at contract award. |
| **Key Date** | Key Date | A date by which the Contractor must meet a stated condition. Unlike Completion, a Key Date does not trigger delay damages; the Contractor is liable under clause 25.3 for the Client's additional cost — but only **work-type** cost (doing work or paying others on the same project), not time-related/preliminaries losses, assessed by the PM within 4 weeks. |
| **Defect** | Defect | A part of the works not in accordance with the Scope/Works Information, or a part not in accordance with the applicable law or the Contractor's design. |
| **Defects Certificate** | Defects Certificate | Issued by the Supervisor at the later of the Defects Date and the end of the last defect correction period. Either lists notified Defects that the Contractor has not corrected or states that there are none. |
| **Risk Register** | Risk Register (NEC3) / Early Warning Register (NEC4) | Maintained under the early warning procedure (clause 16 NEC3 / clause 15 NEC4). Records all early warning matters, decisions from risk reduction meetings (NEC3) / early warning meetings (NEC4), and actions. |
| **W1 / W2 / W3** | Dispute Resolution Options | W1: standard adjudication procedure. W2: adjudication procedure for use when the Housing Grants, Construction and Regeneration Act 1996 applies (UK). W3 (NEC4): standing Dispute Avoidance Board instead of adjudication (non-UK/non-HGCRA projects). NEC4 also inserts a senior-representatives negotiation step before formal proceedings. |
| **X clauses** | Secondary Option Clauses | Optional clauses selected in the Contract Data: X1 (inflation), X2 (changes in law), X5 (sectional completion), X6 (early-completion bonus), X7 (delay damages — omission means damages "at large", not nil), X11 (NEC4: Client termination for convenience), X13 (performance bond), X15 (design liability limited to reasonable skill and care — omission defaults to fitness for purpose), X16 (retention), X18 (limitation of liability), X20 (KPIs), X21 (NEC4: whole life cost), X22 (NEC4: Early Contractor Involvement — hard Stage One CE cut-off at Notice to Proceed to Stage Two), X29 (climate change, 2023 amendments), Y(UK)1-3 (PBA/Construction Act/third-party rights). See the reference's Secondary Options table. |
| **Z clauses** | Additional Conditions of Contract | Bespoke amendments to the standard form, identified in the Contract Data. Z-clauses commonly change notification periods and other timescales — always check the contract as amended, not just the standard form. |
| **pain/gain** | Pain/Gain Share | Under Options C and D (target contracts), the mechanism for sharing cost overruns (pain) and savings (gain) between the Client and Contractor, based on the share percentages in the Contract Data. |
| **Disallowed Cost** | Disallowed Cost | Cost that the PM removes from Defined Cost when assessing PWDD under Options **C-F**. Includes cost not justified by records, cost that should not have been paid, and the cost of correcting Defects **after Completion** (correcting Defects before Completion is an allowed cost) or Defects caused by not complying with a constraint in the Scope. The Jan 2019 amendments added failure to give an early warning and failure to notify a subcontract dispute as Disallowed Cost heads. |

---
