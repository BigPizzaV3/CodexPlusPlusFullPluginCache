---
name: ce-radar
description: Proactive sweep for unnotified compensation-event candidates — half-filled
  and conflicting records graded, not discarded, cross-checked against ce-register.md,
  clocked against notification time bars. Candidates for review, never asserted entitlement.
---

Read `../../shared/openai-runtime.md` before this workflow; it defines tool discovery, resource paths, output handling and data checks for this OpenAI edition.


# CE Opportunity Radar (Ref OF-NNN)

Every other skill in this plugin assumes you already know the event exists: `ce-builder` drafts
the notification, `ce-evidence` compiles its proof, red-team attacks the draft, `nec-deadlines`
clocks it. This skill hunts for the event you haven't noticed — because under NEC clause 61.3
(8 weeks from awareness, as amended by the contract profile) an unnoticed event is a wasting
asset: every week unread in a diary is a week closer to time-barred. It reads records the way an
incoming claims consultant would on day one — sceptically, completely, never discarding the
half-finished entry or the record that contradicts another.

Follow the shared patterns: `../../shared/patterns/02-date-range-parsing.md` (date parsing); `../../shared/patterns/04-pagination-rate-limits.md` (pagination).

**Local files this skill reads (never writes):**
- **`ce-register.md`** — cross-check: is a candidate already notified? Base schema is
  Ref/Event description/dates/Status, commonly extended with a Ground column (see
  `final-account`'s note on this file) — read whatever columns are present. Absent → every
  candidate in Step 4 is treated as NEW, and the output says the register wasn't found.
- **`contract-profile.md`** (Pattern 13) — as-amended notification periods. Absent → clocks use
  the unamended standard form, and **every clock line carries the caveat** "unamended [form]
  period assumed — run `$contract-profile`."
- **`correspondence/correspondence-register.md`** (Pattern 17), if present — a local file, not
  an API call; treated as an additional signal source in Step 2, never as the notice itself
  unless an item is already classified there.

**This skill writes nothing.** Proposed `ce-register.md` rows are presented for the user to add
— the register is never edited by this skill, the same discipline `correspondence-import`
applies to its own register proposals.

---

## Step 1: Scope

1. Resolve the project using **Pattern 1**.
2. Resolve the period from `the user’s request`, or ask, using **Pattern 2**.
3. **Review date** — today, unless the user states one. The clock arithmetic in Step 4 uses this
   date; state plainly which date was used, since a retrospective run and a live run reach
   different weeks-remaining figures.
4. Read `ce-register.md` and `contract-profile.md` in the working directory. State plainly which
   of the two were found (a project mismatch on either is ignored — say so, per Pattern 13
   rule 4).
5. State the contract form in use: from the profile, or the user, or — absent both — "unknown,
   NEC4 unamended assumed for clock purposes" (flagged, and carried into every Step 4 clock line).

---

## Step 2: Signal sweep

State the call plan before running it (**Pattern 4** pacing): parallel `getCachedReport` calls
for `dashboardNarrative`, `dashboardAccessPossession`, `dashboardResourceLabour`,
`dashboardResourcePlant` (idle plant where recorded), and `dashboardShiftTable` (weather fields —
per `weather-impact` Step 2, the primary weather source; fall back to
`getShiftRecords`/`getShiftRecord` only if the dashboard carries none, per Pattern 12, pacing at
2 requests/second and warning of the wait over 10 records). Read
`correspondence/correspondence-register.md` if present — a local file, not an API call.

**Signal-phrase table** — the wording that means money. Scan every narrative and access record
for these phrases (case-insensitive; this list is a working superset of Pattern 10's canonical
keywords, tuned for records nobody has flagged yet):

| Phrase family | Example wording |
|---|---|
| Standing / waiting | "stood down", "waiting on", "waiting for", "standing time" |
| Access | "no access", "late handover", "late possession", "possession not granted" |
| Information | "awaiting a design answer", "RFI outstanding", "query outstanding", "not received" |
| Instruction | "instructed to", "redesign", "rework" |
| Physical clash | "clash" |
| Weather | "flooded", "standing water" |

Every hit becomes a **raw signal**: record id, date, source, and the wording quoted verbatim —
never paraphrased at this stage.

---

## Step 3: Candidate build — the verdicts

Group raw signals into candidate events. Each candidate gets exactly one **record-basis
verdict**:

| Verdict | Meaning | Action |
|---|---|---|
| **SUPPORTED** | Dated, attributed records; corroborated across ≥2 sources where a second source exists (e.g. a narrative stand-down is consistent with the labour report's recorded hours for that shift). | Proceed to Step 4 clock/ranking. |
| **PARTIAL** | The signal exists but key fields are missing — list exactly which (e.g. an access report shows a late handover but the diary narrative for that date is blank). | Complete the record in Gather now, while memories are fresh. A late entry is labelled as a late entry, never dressed up as contemporaneous. |
| **CONFLICTING** | Records disagree. Cite both sides verbatim and stop there. | Resolved by the site team in Gather, never by this skill picking a side — a conflict can itself be the tell that something happened. |
| **RECORDS GAP** | The pattern suggests an event but no record substantiates it. | "No recorded evidence" is a recording gap, never "nothing happened" — and equally never asserted as "something happened." |

**Two figures, two sources, never blended.** Where two sources give different numbers for the
same event (e.g. a 3h40m late handover in the access report and a 3.5-hour stand-down in the
diary), cite **both**, each to its own source. Never average, never blend into one number.

**Noise discrimination.** Trivial, self-resolved items — a 15-minute jammed gate noted "no
material impact", waiting on concrete cure between pours as a normal sequence step — are listed
once in a "reviewed and set aside" line with the reason (Step 5, Section 4), never built into a
candidate.

**Candidate contract head.** Each candidate carries a *candidate* head, e.g. "candidate NEC4
60.1(2) (late access)", "candidate 60.1(3)/60.1(6) family (Others/PM does not reply — the
contract skills confirm the precise head)", "candidate 60.1(13) (weather — measurement
incomplete, see below)". Every head carries the standing line that selection is confirmed via
the relevant contract-knowledge skill (`nec-contracts`, `jct-contracts`, `fidic-contracts`) and
the facts — **nothing here asserts entitlement.**

**Weather candidates stay PARTIAL until tested.** Clause 60.1(13) turns on comparison against
weather data with a stated return period (the one-in-ten-year test) measured at the place stated
in Contract Data, per calendar month. Site records alone cannot run that test — obtain the
comparison data (`$weather-impact`); the candidate stays PARTIAL until then, however
compelling the narrative.

**Indicative quantum signal.** Recorded hours only — and a £ figure only where a rate source the
plugin already recognises exists (Pattern 14's commercial profile). Otherwise hours stay hours.
Never an invented rate.

---

## Step 4: Register cross-check + the clock

Check each candidate against `ce-register.md`:
- **IN REGISTER** — cite the CE/EW entry; no further action beyond noting status.
- **NEW** — proceed with the clock below.

For each **NEW** candidate:
1. **Awareness date** = the earliest record showing the event was known on site.
2. **Clock** = the notification period from awareness — the contract profile's amended period if
   present (cite it, "per the contract profile (as amended)"), otherwise the unamended standard
   form with the caveat from Step 1.
3. Report the **expiry date** and **weeks remaining at the review date** (Step 1).

**NEC framing, exact:**
- Early warnings are **notified**, never "raised."
- The 61.3 bar is 8 weeks from awareness of the event, unless the PM should have notified the
  event to the Contractor (the PM-notifiable grounds — Pattern 6). The discipline is
  conservative: notify within the period regardless of that exclusion; arguments that the bar is
  disapplied are fallback positions, not plans.

**Ranking:** time-bar urgency first, then record strength (SUPPORTED > PARTIAL > CONFLICTING >
RECORDS GAP), then indicative quantum signal.

---

## Step 5: Report

Header per **Pattern 8**: `Ref: OF-[NNN]`, session-local, incrementing on any prior OF ref in the
conversation.

```
CE OPPORTUNITY RADAR — [Project Name]
Ref: OF-[NNN]
Period: [start] to [end]
Review date: [date used for the clock arithmetic]
Contract basis: [profile as-amended / unamended [form] assumed — flagged]
ce-register.md: [found / not found]
```

### 1. SUMMARY
[n] candidates ([n] new / [n] in register); the most urgent clock, named and dated.

### 2. OPPORTUNITY REGISTER
Ranked table (time-bar urgency, then record strength, then quantum):

| # | Candidate | Date(s) | Records cited | Verdict | Candidate head | Clock (expiry / weeks remaining) | Indicative signal |
|---|---|---|---|---|---|---|---|
| 1 | [short description] | [date] | [record ids] | [SUPPORTED/PARTIAL/CONFLICTING/RECORDS GAP] | [candidate head] | [expiry date, N weeks remaining / N/A — in register] | [hours, and £ only if sourced] |

### 3. DETAIL (per candidate)
Signals verbatim (quoted, with record ids); corroboration across sources or its absence; what's
missing (for PARTIAL); both sides verbatim (for CONFLICTING); next move — one of: notify an
early warning, run `$ce-builder`, run the CE Evidence agent, complete the record now
(labelled late), obtain the weather comparison data, or watch.

### 4. REVIEWED AND SET ASIDE
The noise line — every trivial, self-resolved item considered and why it was not built into a
candidate.

### 5. PROPOSED REGISTER ROWS
Rows formatted to `ce-register.md`'s schema, clearly marked **PROPOSED — not applied**. This
skill never writes to `ce-register.md`; these are for the user to add themselves.

### 6. GAPS AND CAVEATS
Contract profile absent/assumed periods; sources not swept this run; period-boundary effects
(a signal just inside/outside the window).

**Standing caveat — verbatim, always included:**

> These are candidate events identified from the records, ranked for commercial review —
> nothing in this report asserts entitlement, and a candidate's absence from the records is a
> recording gap, not proof nothing happened. Notification decisions and contract-head selection
> are yours, made with the relevant contract-knowledge skill and, where it matters, professional
> advice. Ref: OF-[NNN] is a session-local sequence number.

---

## Hard Rules

1. Candidates are never asserted as entitlement.
2. Conflicts are cited both-sides — never resolved by this skill picking a side.
3. Per-source figures for the same event are never blended or averaged.
4. Recording gaps are never asserted as absence, nor as presence — a gap is a gap.
5. `ce-register.md` and Gather itself are never written to — proposals only.
6. Completing a record now means labelling it a late entry, never dressing it up as
   contemporaneous.
7. No invented rates, no invented values, no settlement predictions.
8. Early warnings are **notified**, never "raised."
9. UK English throughout.

---

## Related Skills

- `$events` — register of well-formed events; the radar feeds candidates into it
- `$delay-analysis` — master delay register, for a fuller lost-time picture
- `$nec-deadlines` — clock a notified CE precisely, once out of this skill's hands
- `$ce-builder` — draft the notification once a candidate is ready to go
- `$contract-profile` — capture as-amended notification periods, stop assuming
- `$correspondence-import` — imports the paper trail read locally here
- CE Evidence agent — compile the full substantiation pack behind a SUPPORTED candidate
- Time & Claims Advisor agent — broader delay/claims strategy once triaged
