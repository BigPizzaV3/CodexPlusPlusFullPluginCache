---
name: fidic-contracts
description: FIDIC Red/Yellow/Silver 2017 and 1999 contract knowledge — claims under
  20.2, the 28-day notice bar, DAAB disputes, and variations. Not NEC or JCT (own
  skills).
---

Read `../../shared/openai-runtime.md` before this workflow; it defines tool discovery, resource paths, output handling and data checks for this OpenAI edition.


# FIDIC Contract Knowledge

Background domain knowledge for FIDIC (Fédération Internationale Des Ingénieurs-Conseils) contracts. This skill provides terminology, clause references, timescales, and commercial procedures that the model can draw on when answering FIDIC contract questions.

**Important boundary:** This skill provides contract knowledge only. It cannot fetch claim registers, variation orders, or any live contract administration data from Gather. The Gather MCP provides site diary, labour, progress, and programme data — not contract administration data.

**Caveat:** Outputs based on this skill are contract-administration guidance, not legal advice. FIDIC contracts are routinely amended by Particular Conditions and are governed by varying national laws — the enforceability of time bars in particular is jurisdiction-sensitive. Always check the Particular Conditions and the governing law.

**Editions covered:** FIDIC 2017 (Second Edition) as the primary reference, with key differences from FIDIC 1999 (First Edition) noted where significant. The three main books are covered: Red Book (Construction), Yellow Book (Plant & Design-Build), and Silver Book (EPC/Turnkey).

---

## Topic Index — read only the matching file(s)

| Topic | File |
|---|---|
| Claims (clause 20), disputes and DAAB (clause 21) | `references/claims-and-disputes.md` |
| Variations (clause 13), payment (clause 14) | `references/variations-and-payment.md` |
| Commencement/delays/suspension (clause 8), termination (15, 16), care of the works (17), Exceptional Events (18) | `references/delays-and-termination.md` |
| General provisions (clause 1), the Engineer (clause 3), the Contractor (clause 4), Taking-Over (clause 10) | `references/general-engineer-contractor.md` |
| Key timescales table, common pitfalls | `references/key-timescales-and-pitfalls.md` |

**Procedure:** Identify the topic from the question; read only the file(s) above that match it before answering.

---

## Key Terminology Glossary and FIDIC Books Comparison

See `references/general-engineer-contractor.md` for the full Employer/Engineer/Cost glossary and the Red/Yellow/Silver Book comparison table.

---

## Edition Differences: FIDIC 1999 → 2017 (Quick Reference)

Renumbering between editions is a frequent source of error. When the user does not state the edition, ask or infer, and cite the right sub-clause.

| Topic | FIDIC 1999 | FIDIC 2017 |
|---|---|---|
| Extension of Time | Sub-clause 8.4 | Sub-clause 8.5 |
| Advance Warning | Not provided | Sub-clause 8.4 (took the old EOT number) |
| Force majeure / exceptional events | Clause 19 (Force Majeure) | Clause 18 (Exceptional Events) |
| Claims procedure | Clause 20.1 (brief) | Sub-clause 20.2 (structured, fixed timescales) |
| Fully detailed claim deadline | 42 days | 84 days |
| Late-notice screening / relief | None — time bar absolute on its face | 14-day Engineer screening (20.2.2); late-notice valve (20.2.5) |
| Interim claims (continuing events) | Monthly — expressly required | Monthly (unchanged, 20.2.6) |
| Final claim (continuing events) | 28 days after end of effects | 28 days (unchanged, 20.2.6) |
| Engineer's response | 42 days (approval or disapproval) | 42 days for agreement, then a further 42 days for determination (3.7.3); silence = deemed determination rejecting the Claim |
| Engineer's role | Determination only | Agreement or determination (clause 3.7) |
| Employer claims | Separate procedure (sub-clause 2.5) | Same symmetrical 20.2 procedure |
| Dispute board | Standing DAB (Red); ad hoc DAB appointed when a dispute arises (Yellow/Silver) | Standing DAAB from commencement (all books, with dispute-avoidance role) |
| DAB/DAAB decision period | 84 days | 84 days (unchanged) |
| Notice of dissatisfaction | 28 days | 28 days (unchanged) |
| Amicable settlement period | 56 days | 28 days |
| Programme obligations | Less detailed | More detailed requirements |
| Advance payment | Typically 10-15% | Same, but with more detailed repayment schedule |

The **28-day Notice of Claim condition precedent is unchanged** between editions (20.1 in 1999, 20.2.1 in 2017).

---

## Commercially Decisive Rules (2017 Edition)

- **Notice of Claim — 28 days (20.2.1).** The claiming party must give a Notice of Claim within **28 days** of becoming aware (or when it should have become aware) of the event or circumstance. **This is a condition precedent** — no notice, no entitlement to additional payment or EOT for that event (subject only to sub-clause 20.2.5). Screening: if the Engineer considers the Notice time-barred, it must say so within **14 days** of receipt, failing which the Notice of Claim is deemed valid (20.2.2). Valve: a late Notice of Claim or late fully detailed claim may be accepted where the circumstances justify it (20.2.5).
- **Fully detailed claim — 84 days (20.2.4).** The fully detailed claim must be submitted within **84 days** of becoming aware; otherwise the Notice of Claim is deemed to have lapsed (subject to 20.2.5).
- **Advance Warning — 8.4 (2017 only).** Each Party must advise the other Party and the Engineer in advance of any known or probable future events or circumstances which may adversely affect the work, increase the Contract Price, or delay execution — the FIDIC analogue of NEC's early warning. **Renumbering trap:** in the 1999 edition, sub-clause 8.4 is the EOT clause; in 2017 EOT moved to 8.5 and 8.4 is Advance Warning.

The full 20.2.1–20.2.7 walk-through (contemporary records, continuing-effect claims, the Engineer's 42-day/42-day agreement-or-determination mechanics under 3.7.3) lives in the reference file below.

---

## What's in Each Reference File

Use the Topic Index above to pick the file(s); read only what the question needs before citing specific provisions.

- `claims-and-disputes.md` — full claims procedure (sub-clauses 20.2.1 to 20.2.7); disputes and the DAAB (clause 21)
- `variations-and-payment.md` — variations, clause 13 (13.3.1 instruction, 13.3.2 request for proposal) and valuation 12.3; payment chain — Statement 14.3, IPC 14.6, payment 14.7, retention 14.9
- `delays-and-termination.md` — programme 8.3, Advance Warning 8.4, EOT 8.5, delay damages 8.8, suspension 8.9–8.12; termination (clauses 15 and 16), care of the works and indemnities (clause 17), Exceptional Events (clause 18)
- `general-engineer-contractor.md` — general provisions (clause 1); the Engineer's agreement or determination (sub-clause 3.7, 42 + 42 days, deemed rejection); the Contractor (clause 4), including Unforeseeable Physical Conditions 4.12 (and the Silver Book's "Unforeseeable Difficulties"); Taking-Over (clause 10)
- `key-timescales-and-pitfalls.md` — key timescales table and common pitfalls

---

## Practical Guidance for QSs

1. **The 28-day notice is critical.** Under FIDIC, it is a condition precedent — miss it and the claim is barred. At 28 days, FIDIC's notice period is the strictest of the three main forms: shorter than NEC's 8 weeks, and JCT has no time bar at all. Set up a weekly review process to identify potential claims and ensure notices are issued in time.

2. **Submit detailed claims on time.** The 2017 edition allows 84 days for the fully detailed claim (up from 42 days in 1999) — but miss it and the Notice of Claim is deemed to have lapsed (subject to 20.2.5). Prepare the claim while the evidence is fresh. Do not wait until the event is over.

3. **Keep contemporary records.** FIDIC sub-clause 20.2.3 requires the claiming party to keep "contemporary records", and the fully detailed claim under 20.2.4 must include them. Site diaries, photographs, resource records, and weather data from Gather are exactly the type of evidence needed.

4. **Understand Cost vs Cost Plus Profit.** "Cost" under FIDIC includes overheads but not profit. "Cost Plus Profit" adds the profit margin. Check whether the applicable clause entitles Cost or Cost Plus Profit — this varies by clause.

5. **Know which book you are working on.** The Silver Book gives no relief for unforeseeable physical conditions (clause 4.12 is replaced by "Unforeseeable Difficulties") and does not have an independent Engineer. These are fundamental differences that affect the Contractor's risk profile and claim entitlements.

6. **Programme is a contractual document.** Under clause 8.3, the Contractor must submit a programme within 28 days of commencement and update it when required. Under the 2017 forms, failure to submit required documents (including the programme) is among the grounds on which the Engineer may withhold amounts in an IPC (sub-clause 14.6 — check the exact sub-paragraph in your edition).

7. **Use the DAAB for dispute avoidance.** The 2017 edition's standing DAAB provides an informal dispute avoidance mechanism. This can resolve issues before they escalate to formal adjudication.

8. **Variations require proposals.** Under clause 13.3.2, the Engineer may request a proposal before instructing a Variation. Always respond promptly with a detailed proposal including programme and cost impact.

---

## Related Skills

- `$delay-analysis` — Build a delay register from site records to support EOT claims
- `$measured-mile` — Quantify productivity disruption for claim substantiation
- `$labour` — Labour hours data for cost calculations
- `$commercial-report` — Period commercial reporting
- `$programme` — Programme status and milestone tracking
