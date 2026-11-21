---
name: jct-contracts
description: JCT SBC/DB/ICD/MW 2016 and 2024 contract knowledge — Relevant Events/Matters,
  EOT, loss and expense (L&E), LADs, and interim payments. Not NEC or FIDIC (own skills).
---

Read `../../shared/openai-runtime.md` before this workflow; it defines tool discovery, resource paths, output handling and data checks for this OpenAI edition.


# JCT Contract Knowledge

Background domain knowledge for JCT (Joint Contracts Tribunal) contracts. This skill provides terminology, clause references, timescales, and commercial procedures that the model can draw on when answering JCT contract questions.

**Important boundary:** This skill provides contract knowledge only. It cannot fetch variation registers, EOT applications, or any live contract administration data from Gather. The Gather MCP provides site diary, labour, progress, and programme data — not contract administration data.

**Editions covered:** JCT SBC 2016, JCT DB 2016, JCT ICD 2016, JCT MW 2016. References are to the 2016 editions unless otherwise stated.

**JCT 2024:** 2024 editions of these forms are now published — see the Edition Differences table below. Confirm which edition applies before citing clause numbers.

**Amended contracts:** JCT contracts are almost always amended by a schedule of amendments, which frequently inserts condition-precedent notice regimes. Always check the contract as executed. This skill is contract-administration guidance, not legal advice.

---

## Topic Index — read only the matching file(s)

| Topic | File |
|---|---|
| EOT, Relevant Events, delay notice (clauses 2.27–2.29) | `references/eot-and-claims.md` |
| Payment, loss and expense, Relevant Matters (clauses 4.8–4.24) | `references/payment-and-loss-expense.md` |
| Variations, Variation Quotations, Valuation Rules (clause 5) | `references/variations.md` |
| Termination (Section 8), disputes (Section 9) | `references/disputes-and-termination.md` |
| Definitions (Section 1), Control of the Works (Section 3), Insurance (Section 6), key dates/periods, JCT vs NEC comparison, common pitfalls | `references/general-and-control.md` |

**Procedure:** Identify the topic from the question; read only the file(s) above that match it before answering.

---

## Edition Differences: JCT 2016 → 2024

| Topic | JCT 2016 | JCT 2024 |
|---|---|---|
| Architect/CA EOT decision period (clause 2.28.2) | 12 weeks from receipt of particulars | 8 weeks from receipt of particulars |
| Relevant Events / Relevant Matters | As listed at 2.29 / 4.22 | Adds epidemics; discovery of unexploded ordnance, asbestos and contaminated material (extending the existing antiquities provisions); changes in law and statutory guidance |

Clause numbering, payment mechanics, and the Final Certificate regime are otherwise materially unchanged in the 2024 editions.

---

## Key Terminology Glossary and Contract Forms Comparison

See `references/general-and-control.md` for the full SBC/DB/ICD/MW glossary and forms comparison table.

---

## Commercially Decisive Rules (SBC 2016)

The rules below most often decide commercial outcomes. Full clause detail, including the complete Relevant Events and Relevant Matters lists, is in the reference (see next section).

- **Delay notice (clause 2.27.1):** If and whenever it becomes reasonably apparent that the progress of the Works is being or is likely to be delayed, the Contractor shall forthwith give written notice to the Architect/CA of the material circumstances, including the cause or causes of the delay, and shall identify in the notice any event which in his opinion is a Relevant Event.
- **EOT decision (clause 2.28.2):** The Architect/CA must notify their decision as soon as is reasonably practicable and in any event within 12 weeks of receipt of the required particulars. (JCT 2024 shortens this period to 8 weeks.)
- **Loss and/or expense (clauses 4.20-4.24):** The Contractor must make a written application as soon as it has become, or should have become, reasonably apparent that regular progress has been or is likely to be materially affected by a Relevant Matter, including an initial assessment updated at monthly intervals. The Architect/CA (or QS) must notify the ascertained amount within 28 days of receipt of the Contractor's initial assessment and information, and within 14 days of each subsequent update (clause 4.21).
- **Time and money are separate mechanisms:** Under NEC, a single compensation event covers both time and cost. Under JCT, time (EOT via Relevant Events, clause 2.29) and cost (Loss & Expense via Relevant Matters, clause 4.22) are separate mechanisms with different triggers. Some events give time only (e.g., weather), some give time and money, and some are arguable.

---

## What's in Each Reference File

Use the Topic Index above to pick the file(s); read only what the question needs before citing specific provisions.

- `eot-and-claims.md` — the thirteen Relevant Events (clause 2.29) in full; extension of time procedure (clauses 2.27-2.28): best endeavours, concurrent delay, the retrospective review
- `payment-and-loss-expense.md` — payment chain (clauses 4.8-4.12): Interim Valuation Dates, due dates, Interim Certificates, pay less notices, retention; Final Certificate and conclusivity (clauses 4.26, 1.9.3, 1.9.4); loss and expense procedure and the Relevant Matters (clause 4.22) and common heads of claim (clauses 4.20-4.24)
- `variations.md` — Variations, Variation Quotations (clause 5.3 / Schedule 2), and the Valuation Rules (clauses 5.6-5.10)
- `disputes-and-termination.md` — Section 8 termination, Section 9 disputes
- `general-and-control.md` — definitions, Control of the Works, insurance of the works (clause 6.7 / Schedule 3), key timescales table, JCT vs NEC comparison, common pitfalls

---

## Practical Guidance for QSs

1. **Give notice early.** Although JCT has no strict time bar like NEC's 8-week rule, prompt notice is essential. Delays in notifying weaken the Contractor's position and may be argued as prejudicial to the Employer.

2. **Separate time and money.** EOT and loss & expense are separate applications. An EOT does not automatically mean loss & expense is due, and vice versa. Make separate applications with separate substantiation.

3. **Keep contemporaneous records.** Site diaries, resource records, and photographs are critical evidence for both EOT and loss & expense claims. Gather data supports this — use `$diary`, `$labour`, and `$narrative-search` for evidence.

4. **Value variations correctly.** Use contract rates where applicable. Only move to fair rates where the work is not of similar character or conditions. Always document why contract rates are or are not applicable.

5. **Understand Practical Completion.** This is the Architect/CA's decision, not the Contractor's. It triggers the Rectification Period, releases half the retention, and stops LADs running. Push for certification as soon as the works are practically complete.

6. **Watch the Final Certificate.** Once issued, it is conclusive evidence unless challenged within 28 days. Review it immediately and raise any disputes within the window.

7. **Record disruption carefully.** Loss & expense for disruption is notoriously hard to prove. A measured mile analysis comparing productivity in disrupted and undisrupted periods is the strongest methodology — use `$measured-mile`.

---

## Related Skills

- `$delay-analysis` — Build a delay register from site records to support EOT applications
- `$measured-mile` — Quantify productivity disruption for loss & expense claims
- `$labour` — Labour hours data for prolongation cost calculations
- `$commercial-report` — Period commercial reporting
- `$programme` — Programme status and milestone tracking
