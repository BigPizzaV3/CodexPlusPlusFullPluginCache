# Eligibility

Silent gates applied at the end of Stage 1 before any tool call. Any failure → refusal per SKILL.md § Refusal routing.

## Age

Compute `age = floor((startDate − DOB) / 365.25)` at trip start.

| Age at trip start | Action |
| --- | --- |
| < 60 | Continue to Stage 2 |
| ≥ 60 | `HANDOFF-AGE-MEDICAL`, STOP. Never mention age or reason. |

## Province of residence

Allowed 2-letter codes: `ON`, `QC`, `BC`, `AB`, `MB`, `SK`, `NS`, `NB`, `NL`, `PE`, `YT`, `NT`, `NU`.

Anything else → ask for a valid province (do not refuse). Quebec (`QC`) triggers `bill96Consent` in `saveQuotes` — `true` only when the sticky locale is EN, `false` in French — and the QC advisor message after the priced table.

## Citizenship

Canadian citizen or permanent resident = yes → continue. Anything else → `HANDOFF-DEFAULT`, STOP.

## Trip

- `startDate ≤ endDate`, both in the future.
- Trip length ≤ 365 days.
- `tripCost` integer in `0..100000`.
- `tripType` is always `"SINGLE"`. Any multi-trip / annual mention → `HANDOFF-MULTI-TRIP`, STOP.
- One traveller only. Any additional-traveller mention → `HANDOFF-MULTI-TRAVELLER`, STOP.

## Medical / pre-existing conditions

**Never ask.** Only a user-volunteered mention triggers `HANDOFF-AGE-MEDICAL`.
