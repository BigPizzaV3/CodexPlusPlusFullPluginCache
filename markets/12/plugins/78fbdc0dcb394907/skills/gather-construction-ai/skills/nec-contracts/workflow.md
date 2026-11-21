---
name: nec-contracts
description: NEC3/NEC4 ECC contract knowledge — compensation events (CE), early warnings
  (EWN), the 61.3 time bar, the Accepted Programme, Options A-F, and Z clauses. Not
  JCT or FIDIC (own skills).
---

Read `../../shared/openai-runtime.md` before this workflow; it defines tool discovery, resource paths, output handling and data checks for this OpenAI edition.


# NEC Contract Knowledge

Background domain knowledge for NEC3 and NEC4 Engineering and Construction Contracts (ECC). This skill provides terminology, clause references, timescales, and commercial procedures that the model can draw on when answering construction contract questions.

**Important boundary:** This skill provides contract knowledge only. It cannot fetch compensation event registers, early warning notifications, or any live contract administration data from Gather. The Gather MCP provides site diary, labour, progress, and programme data — not contract administration data. If the user asks for a list of CEs or EWNs on their project, explain that this data is not available through Gather and would need to be sourced from the project's contract management system.

**Amended contracts:** NEC contracts are frequently amended by Z-clauses (additional conditions of contract in the Contract Data) that change notification periods and other timescales. Always check the contract as amended, not just the standard form.

**Disclaimer:** This skill provides guidance on contract administration, not legal advice. Where entitlement is disputed or significant sums are at stake, the user should take professional legal advice.

---

## Topic Index — read only the matching file(s)

| Topic | File |
|---|---|
| Compensation events (clauses 60–66), early warning (16/15) | `references/ce-and-early-warning.md` |
| Programme and Time (clauses 30–32) | `references/programme-and-time.md` |
| Payment (clauses 50–53) | `references/payment-and-defined-cost.md` |
| Main Options A–F, pain/gain, Secondary Options (X/Y/W) | `references/main-and-secondary-options.md` |
| Title, Risks and Insurance, Termination (clauses 70, 80–81, 90–93) | `references/disputes-and-termination.md` |
| General/Actions/Communications/PM/Supervisor (clauses 10–14, 20–26), Testing and Defects (40–46), Key Timescales Summary, Practical Guidance for QSs | `references/general-clauses-and-guidance.md` |
| ECS/ECSC/ECSS short-form differences | `references/short-forms.md` |
| GMH Planning / CECA bulletin index (further reading only) | `references/gmh-ceca-index.md` |

**Procedure:** Identify the topic from the question; read only the file(s) above that match it before answering. Read `references/short-forms.md` first if the question concerns an ECS/ECSC/ECSS subcontract. Only read `references/gmh-ceca-index.md` if the user explicitly asks for source bulletins or further reading.

---

## Edition Differences: NEC3 → NEC4

The two editions share most numbering, but several changes matter for disambiguation. When the user does not state the edition, ask or infer, and use the correct terms throughout.

| Topic | NEC3 | NEC4 |
|---|---|---|
| Client party | Employer | Client |
| Scope document | Works Information | Scope |
| Early warning clause | Clause 16 | Clause 15 |
| Early warning register | Risk Register | Early Warning Register |
| Early warning meeting | Risk reduction meeting | Early warning meeting |
| Early-warning sanction | Assessed under 63.5 | Assessed under 63.7 |
| Delay to Completion Date assessed under | 63.3 | 63.5 |
| Implementing a CE | Clause 65 | Clause 66 |
| Compensation event grounds | 60.1(1)–(19) | 60.1(1)–(19) plus 60.1(20) and 60.1(21) |
| Programme deemed acceptance | None | Clause 31.3 (notify the failure, then one further week) |
| Actual/forecast divide for CE assessment | 63.1: the date the PM instructed **or should have instructed** quotations divides work done from work not yet done | 63.1: defined term "dividing date" — date of the PM/Supervisor communication, or of the CE notification for other events |
| Mutual trust obligation | 10.1 (single clause, joined with "act as stated") | Split: 10.1 (act as stated) + 10.2 (mutual trust and co-operation) |
| Fee | Separate percentages (direct fee, subcontracted fee) | **Single Fee percentage** in Contract Data |
| Revised programme shows | Effects of **implemented** CEs (32.1) | "Implemented" dropped — all CE effects shown (non-implemented move planned Completion only) |
| Final account mechanism | None | Clause 53 Final Assessment (conclusive unless disputed) |
| Client termination for any reason | Core clause right | Removed — requires secondary option X11 |
| Termination reasons | R1–R21 | R1–R22 (R22: Corrupt Act) |
| Value engineering | Via 63.11 target protection (C/D) | Clause 16 "Contractor's proposals" (PM replies in 4 weeks) |
| Option B People Rates | Proposed per event as CEs arose | Pre-agreed in Contract Data part 2 at tender |

The **PM reply to a CE notification is one week in both editions** (clause 61.4); the further two-week route to deemed acceptance runs only after the Contractor notifies the PM's failure to reply. There are **five** deemed-acceptance mechanisms: CE notification (61.4), quotation (62.6) and the PM's own overdue assessment (64.4) exist in both editions; the programme (31.3) and Defined Cost finalisation (50.9, Options C–F) are NEC4-only. Outside these five, PM silence is never deemed acceptance — it stalls the matter and is at most a 60.1(6) CE.

**Scope caution — short forms differ:** these ECC timescales must not be applied to the NEC short/sub forms. The ECS time bar is 7 weeks, the ECSC's is **4 weeks**, the ECSS's is **3 weeks**, and under ECSC/ECSS a missed quotation reply is deemed accepted **instantly** with no reminder step. Check which contract the user actually has.

---

## Key Terminology Glossary

See `references/general-clauses-and-guidance.md` for the full CE/PM/Supervisor/Defined Cost/X-and-Z-clause glossary.

---

## Main Options A-F (Compact)

See `references/main-and-secondary-options.md` for the full A-F table and CE-assessment distinction by option.

---

## The Commercially Decisive Rules

The rules below decide most commercial outcomes. Full clause-by-clause detail, the complete 60.1 CE ground list, quotation and assessment procedure, programme requirements, and the timescales table are in the reference (see next section).

- **The 8-week time bar (clause 61.3):** The Contractor must notify a CE within 8 weeks of becoming aware of the event, or loses entitlement to changes in the Prices, the Completion Date, and Key Dates. The bar does **not** apply where the event arises from the PM or Supervisor giving an instruction, issuing a certificate, changing an earlier decision, or correcting an assumption (events the PM should have notified). If in doubt, notify.
- **PM reply and deemed acceptance (clause 61.4):** The PM replies to a CE notification within **one week** (both editions, or a longer agreed period). If the PM does not reply, the Contractor may notify the failure; a further two weeks of silence is treated as acceptance that the event is a CE.
- **Quotations (clause 62):** submit within three weeks of instruction; PM replies within two weeks (62.3); alternative quotations may be instructed (62.1); quotation deemed acceptance after notified failure (62.6); the PM may make their own assessment (64.1) — including whenever there is no Accepted Programme.
- **Early warning (clause 16 NEC3 / 15 NEC4):** either party must notify matters that could increase cost, delay Completion or a Key Date, or impair performance. Failure to warn reduces the CE assessment (61.5 with 63.5 NEC3 / 63.7 NEC4) — it is a reduction, not a bar. An EWN is not a CE notification; they serve different purposes.
- **No Accepted Programme weakens the Contractor's position on every CE.** Practice Note 1's process is agree-a-programme-first (possibly the Contractor's rejected submission), then PM assessment under clause 64 as the fallback — but PM assessments are rarely more generous than quotations, and 25% of PWDD can be withheld with no compliant first programme (50.3 NEC3 / 50.5 NEC4). Keep the programme submitted, updated, and accepted. Terminal float and time risk allowances belong to the Contractor; other (total) float is shared and available to absorb delay.

---

## What's in Each Reference File

Use the Topic Index above to pick the file(s); read only what the question needs before citing specific provisions.

- `ce-and-early-warning.md` — the full clause 60.1 compensation event grounds, (1)–(19) plus NEC4 (20)–(21), with commentary; notification, quotation, assessment, and implementation procedure (clauses 61–66), including PM's assumptions (61.6) and the NEC4 dividing date (63.1); early warning procedure and sanction detail (clause 16 NEC3 / 15 NEC4)
- `programme-and-time.md` — programme requirements and acceptance (clauses 30–32)
- `payment-and-defined-cost.md` — payment assessment and certification (clauses 50–51), NEC4 50.9 Defined Cost finalisation and clause 53 Final Assessment
- `main-and-secondary-options.md` — Main Options A–F in full, the pain/gain mechanism, and a Secondary Options table (X1–X29, Y(UK), W1–W3)
- `disputes-and-termination.md` — title (70), risks and insurance (80–81), termination (90–93 with the Termination Table mechanics)
- `general-clauses-and-guidance.md` — general/communications/PM/Supervisor clauses (10–14), Contractor's main responsibilities (20–26), Testing and Defects (clauses 40–46: QMS, searching, correcting, accepting and uncorrected Defects, and the pre-/post-Completion Disallowed Cost split), the Key Timescales summary table, and practical guidance for QSs
- `references/short-forms.md` — ECS/ECSC/ECSS timescale and mechanism differences (read before answering any subcontract or short-form question)
- `references/gmh-ceca-index.md` — topic index of the GMH Planning / CECA bulletin library; read only if the user asks for source bulletins or further reading

---

## Related Skills

- `$contract-profile` — Capture the contract as executed (edition, option, Z-clause amendments) so timescales here are applied as amended
- `$nec-deadlines` — Compute every live NEC deadline and deemed-acceptance clock from a few dates
- `$ce-builder` — Build the clause 61.3 notification with site-record evidence
- `$ce-quotation` — Build the clause 62 quotation with the dividing-date split and two-programme delay assessment
- `$delay-analysis` — Analyse delay events and their time impact using site diary data
- `$weather-impact` — Assess weather disruption against the clause 60.1(13) threshold
- `$labour` — Labour hours data for building CE cost assessments
- `$commercial-report` — Period commercial reporting across the project
- `$programme` — Programme status and milestone tracking
