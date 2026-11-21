# NEC Subcontract and Short Forms: ECS, ECSC, ECSS

Compact reference for the NEC subcontract and short forms a main-contractor QS is most likely
to meet alongside the ECC. This is a supplement to the ECC content in the other `references/` topic files, not a
replacement — always confirm which form is actually in use before applying any figure below.

**When each form is used:**
- **ECS** (Engineering and Construction Subcontract) — the full subcontract counterpart to the
  ECC, used beneath an ECC main contract. It mirrors the ECC's core clause numbering, PM/Supervisor
  roles (performed by the Contractor for the Subcontractor), and Options A–E almost exactly.
- **ECSC** (Engineering and Construction Short Contract) — a simplified main Client-Contractor
  form for lower-complexity, lower-risk projects. **ECSC has no Project Manager or Supervisor** —
  the Client administers the contract directly. It has only **12 compensation event grounds**
  (against the ECC's 19–21) and **no Early Warning Register or early warning meeting machinery**.
  There is no formula for choosing ECC vs ECSC — it is a judgement call on project complexity, and
  practitioner guidance explicitly warns against picking ECSC as an "easy option" for a complex
  project, since it lacks the ECC's procedural safety nets (no Key Dates, no sectional Completion,
  and — if the Scope is silent — the only default programme requirement is a weekly forecast of
  the Completion date).
- **ECSS** (Engineering and Construction Short Subcontract) — the short subcontract counterpart to
  ECSC, sitting beneath either an ECC or ECSC main contract. Same simplified structure as ECSC,
  with "Contractor"/"Subcontractor" in place of "Client"/"Contractor" — no PM/Supervisor equivalent
  either.

## Timescale comparison

| | ECC | ECS | ECSC | ECSS |
|---|---|---|---|---|
| CE notification time bar (61.3) | 8 weeks | 7 weeks (unconfirmed — no source in this review states the ECS figure explicitly; treat as provisional) | 4 weeks | 3 weeks |
| Contractor/Subcontractor quotation period (62.3) | 3 weeks | 2 weeks | 1 week (or with the notification, if the Client notifies the event) | per Subcontract Data (contract-data-driven, not fixed) |
| PM/Client/Contractor reply to quotation (62.3) | 2 weeks | 4 weeks | 2 weeks | per Subcontract Data |
| Missed-reply reminder/deemed-acceptance mechanism | Two-step: notify the failure, then a further period of silence deems acceptance | Two-step, same as ECC (extended reminder window — see below) | One-step: **instantly** deemed accepted, no reminder step | One-step: **instantly** deemed accepted, no reminder step |
| Reminder/further-silence window (62.6-style) | 2 further weeks | Extends to **3 weeks** | None — instant | None — instant |

The ECC/ECS "two-step" deemed-acceptance mechanism (silence, then a Contractor/Subcontractor
reminder, then a further period of silence before the quotation is deemed accepted) does **not**
carry over to ECSC or ECSS: in both short forms, a missed reply deems the quotation accepted
**immediately**, with no reminder step at all. This is a mechanism-level difference, not just a
faster timescale, and is one of the more consequential traps for a QS moving between the ECS and
ECSC/ECSS families.

## The ECSS back-to-back safeguard

The ECSS Subcontract Data forces a back-to-back drafting link that the full ECS does not: the
period for reply is entered not as a standalone duration but as "**X weeks more than the period
for reply in the main contract**" (mirrored for both the Contractor's and the Subcontractor's
reply periods). This is a structural, form-level guarantee — not just best-practice advice — that
the subcontract's notification chain cannot outrun the main contract's own timescales. The full
ECS Contract Data has no equivalent field: a main contractor procuring under full ECS must
manually calculate and insert compatible reply periods, with no form-level prompt to do so.

## ECSC's weather test

ECSC uses a different weather test from the ECC's clause 60.1(13) one-in-ten-year statistical
comparison. Under ECSC, the qualifying test is periods of **at least one full working day**
occurring within the contract, **totalling more than one-seventh of the days between the starting
date and the Completion Date** — a proportion-of-elapsed-time test rather than a historical-data
comparison. Because it depends on the total elapsed period, this test is necessarily
**retrospective**: it cannot be evaluated until enough of the contract period has passed (or
Completion has occurred) to calculate the one-seventh threshold.

## Defined Cost simplification

ECSC (and ECSS) have no Schedule of Cost Components at all — a materially simpler build-up than
the ECC/ECS. Defined Cost is the sum of:
- **People** — at the People Rates stated in the Contract Data;
- **Plant and Materials** — the amount paid by the Contractor/Subcontractor;
- **Subcontracted amounts** — the amount paid to Subcontractors/Sub-subcontractors;
- **Equipment** — at published list rates or open-market rates;
- plus the **Fee** percentage.

## Provenance and caveat

Verified 2026-07 against GMH Planning / CECA user guides and bulletins for ECS, ECSC and ECSS —
see `references/gmh-ceca-index.md` for the topic index. A handful of the figures above (notably
the unconfirmed ECS 7-week time bar, sourced only from a cross-reference in a bulletin covering a
different form) come from secondary summaries rather than the primary contract text for that
specific form. The contract as executed — including any Z-clause or additional-conditions
amendment — always governs; treat every timescale here as a starting point to verify against the
actual Contract Data, not a substitute for reading it.
