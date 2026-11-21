---
name: nec-deadlines
description: NEC deadline clock — clause 61.3 time bar, deemed acceptance, 61.4 PM
  reply, 62.3/62.6 quotation, 64/50.9/53 deadlines, from user-supplied dates. "Have
  we missed the 8 weeks"; time bar; deadline.
---

Read `../../shared/openai-runtime.md` before this workflow; it defines tool discovery, resource paths, output handling and data checks for this OpenAI edition.


# NEC Deadline and Deemed-Acceptance Clock

Given whichever dates the user can supply, compute every NEC deadline that is currently live and flag any deemed-acceptance clock that has started or could be started today.

**No Gather MCP data is needed or used** — this skill works entirely from dates the user types in. If the user asks it to go and find the event, notification, or reply dates from site records, do not guess them: point to `$delay-analysis` (event register) or `$ce-builder` (event narrative and notification drafting) to establish the dates first, then return here.

The timescales table in Step 3 below is self-contained for every clock this skill computes — do not read the whole of `nec-contracts` to get it. Only if the question needs clause detail beyond a bare timescale (grounds, mechanism, commercial significance) read the single matching `../nec-contracts/references` topic file: `ce-and-early-warning.md` for 61–66 and early warning, `programme-and-time.md` for 31.3, `payment-and-defined-cost.md` for 50.9/53, `general-clauses-and-guidance.md` for the Key Timescales summary, or `short-forms.md` for ECS/ECSC/ECSS. Apply Pattern 2 (dates, `../../shared/patterns/02-date-range-parsing.md`), Pattern 6 (notification compliance, `../../shared/patterns/06-notification-compliance.md`), and Pattern 13 (contract profile, `../../shared/patterns/13-contract-profile.md`).

---

## Step 1: Gather Inputs

Take whichever of the following the user has supplied (do not demand all of them). Where
`correspondence/correspondence-register.md` (Pattern 17) or `ce-register.md` carries a
**confirmed** date for one of these, offer it and cite it ("notified 2026-01-12 per
[COR-003]") — a register-cited date beats an asserted one; an UNCLASSIFIED correspondence
item is flagged as a candidate, never treated as the notice itself.

- Date of awareness of the event
- CE notification date (Contractor → PM, clause 61.3)
- PM reply date to the CE notification (clause 61.4), or its absence
- Quotation instruction date (clause 62.1/62.3)
- Quotation submission date
- Programme submission date (clause 31.1/31.2, NEC4 only for the deemed-acceptance leg)
- Defects Certificate date (or termination certificate date, clause 53)
- Any other stated trigger date (e.g. a Defined Cost finalisation submission under 50.9, or a failure-to-reply notification the Contractor has already sent)
- Which 60.1 ground the event falls under, if known — needed to check the 61.3 exclusion list

**As-of date:** this skill will not guess. If the user has not stated the date the clocks are to be assessed against, ask for it — do not default to "today" silently, since a deadline reading is often run retrospectively or for a specific status date. This overrides Pattern 2's general default-without-confirmation rule, because a silently wrong as-of date makes every downstream deadline wrong.

Missing dates simply mean the clocks that depend on them are reported as "— not yet triggered", not blockers to producing the rest of the table.

---

## Step 2: Determine the Contract Basis (Pattern 13)

Check the working directory for `contract-profile.md` (or `contract-profile-<project-slug>.md`).

- **If found and it matches the project:** amended periods in `z_clause_amendments` override every default period below. Every output line drawing on an amended period is labelled "per the contract profile (as amended)". Do not re-derive or question profile values.
- **If found but `project` does not match:** ignore it and say so.
- **If not found:** assume the standard, unamended **NEC4 ECC**, state this assumption prominently at the top of the output, and add the one-line pointer: "Run `$contract-profile` to capture project-specific amendments." Note any NEC3 difference from the table in Step 3 as it becomes relevant.
- **Short forms (ECS/ECSC/ECSS):** only use the short-form periods below if the contract profile (or the user) states the contract is an ECS, ECSC, or ECSS. Never default to a short form.

---

## Step 3: Compute Each Live Clock

Standard **NEC4 ECC** periods (both editions unless marked). Encode exactly — do not round or approximate.

| Clock | Clause | Trigger | Standard period | Notes |
|---|---|---|---|---|
| CE time bar | 61.3 | Date of awareness | 8 weeks (56 days) | Does **not** apply to grounds 60.1(1), (4), (7), (8), (15), (17) — events the PM should have notified. If the stated ground is one of these, report the row as "— not applicable (PM-notifiable ground)", not a deadline. An early warning **notified** on the event does not stop or reset this clock — say so explicitly if an EW was notified. |
| PM reply to CE notification | 61.4 | CE notification date | 1 week (7 days) (or a longer agreed period stated in Contract Data) | Both editions. |
| — failure-notification deemed acceptance | 61.4 | Date Contractor notifies the PM's failure to reply | 2 weeks (14 days) | Only starts once the Contractor has notified the failure (not automatic on the 1-week deadline passing). Silence to expiry = event deemed a CE + instruction to submit quotations. |
| Quotation submission | 62.3 | Quotation instruction date | 3 weeks (21 days) (or agreed longer) | |
| PM reply to quotation | 62.3 | Quotation submission date | 2 weeks (14 days) | |
| — failure-notification deemed acceptance | 62.6 | Date Contractor notifies the PM's failure to reply to the quotation | 2 weeks (14 days) | Both editions. Silence to expiry = quotation (cost **and** time) deemed accepted. NEC3 excludes quotations for a proposed instruction/changed decision from this route — note if relevant. |
| PM's own assessment | 64.1/64.4 | Date the 64.1 obligation arose (quotation deadline missed, PM rejects the quotation, no programme submitted, or no Accepted Programme for a stated reason) | Same period the Contractor had for the quotation (3 weeks default, or as amended) | If it is unclear which of these triggered 64.1, ask; do not assume. |
| — failure-notification deemed acceptance | 64.4 | Date Contractor notifies the PM's failure to assess | 2 weeks (14 days) | Both editions (NEC3 via the April 2013 amendment). Silence to expiry = Contractor's **original** quotation deemed accepted — even where the PM had rejected it to assess independently. |
| Programme response | 31.3 | Programme submission date | 2 weeks (14 days) | **NEC4 only** for the deemed-acceptance leg below; NEC3 31.3 has no deemed acceptance — if NEC3, stop at "PM must accept or give reasons" and state there is no deemed-acceptance fallback. |
| — failure-notification deemed acceptance | 31.3 | Date Contractor notifies the PM's failure to respond | 1 week (7 days) | NEC4 only. Silence to expiry = programme deemed accepted. |
| Defined Cost finalisation review | 50.9 | Date Contractor submits records for finalisation | 13 weeks (91 days) | **NEC4, Options C–F only.** If the PM requests further records within the review, add 4 weeks (28 days) from that request for the Contractor to supply them, then a further 4 weeks (28 days) final review from supply. Silence at the end of whichever window is current = records deemed accepted (no separate failure-notification step). |
| Final Assessment | 53 | Defects Certificate date (or termination certificate date) | 4 weeks (28 days) from Defects Certificate; 13 weeks (91 days) from a termination certificate | **NEC4 only** — no NEC3 equivalent. |

**Short forms — only if the profile/user confirms the contract is ECS, ECSC, or ECSS:**

| Form | Time bar | Reminder window | Quotation deemed acceptance |
|---|---|---|---|
| ECS | 7 weeks | 3 weeks | Same reminder-then-silence mechanism as ECC |
| ECSC | 4 weeks | 3 weeks | **Instant** on a missed reply — no reminder step |
| ECSS | 3 weeks | 3 weeks | Same reminder-then-silence mechanism as ECC |

---

## Step 4: Date Arithmetic Discipline

NEC counts **calendar days**, not working days — every period above is weeks × 7 calendar days added to the trigger date. Any working-day convention is a Z-clause matter and can only come from the contract profile; state this once per output if no profile is present.

For every deadline shown, write the arithmetic out before presenting the table row, in the form:

```
<trigger date> + <N> days = <deadline date> (<weekday>)
```

Then compare the deadline against the as-of date to derive status:
- **✅ met on \<date\>** — the relevant reply/submission/notification was recorded on or before the deadline
- **⏳ N days remaining** — deadline is after the as-of date; state N = deadline − as-of date
- **⚠️ PASSED N days ago** — deadline is before the as-of date and nothing was recorded against it; state N = as-of date − deadline
- **— not yet triggered** — the trigger date for this clock has not been supplied or has not yet occurred

Double-check every calculation independently before writing the final table — an off-by-one week error here directly costs or saves the Contractor money.

---

## Step 5: Output

```
NEC DEADLINE AND DEEMED-ACCEPTANCE CLOCK
Ref: TB-[NNN]
Project: [name]
As of: [as-of date]
Basis: [Standard, unamended NEC4 ECC — run $contract-profile to capture amendments]
        OR [Per the contract profile (as amended): <amendments applied>]

| Clock | Clause | Trigger date | Deadline | Status |
|---|---|---|---|---|
| [clock] | [clause] | [date] | [date, weekday] | [✅/⏳/⚠️/—] |
...

ACTIONS AVAILABLE NOW
- [Only reminder-notification opportunities that would START a deemed-acceptance clock today, e.g.:
  "PM reply overdue since <date> — notifying the failure today starts the two-week deemed-acceptance
  clock, expiring <date> (<weekday>)."]
- [Repeat for each overdue reply/assessment that has not yet had its failure notified.]
- [If nothing is overdue, state: "No reminder-notification action is currently available — no clock is
  overdue."]

Notes:
- Ref: TB-[NNN] is a session-local sequence number for cross-referencing (increment from any prior
  TB-report in this conversation; start at 001 otherwise).
- NEC counts calendar days throughout; a Z-clause working-day convention would only apply per the
  contract profile.
- Z-clause amendments change these periods — this is contract administration guidance, not legal
  advice. Where entitlement is disputed or significant sums are at stake, take professional legal advice.
```

Use UK English throughout. An early warning is always **notified**, never "raised".

---

## Related Skills

- `$delay-analysis` — establish event dates from site diary evidence
- `$ce-builder` — draft the CE notification or quotation once dates are confirmed
- `$contract-profile` — capture Z-clause amendments so this skill applies the contract as executed
