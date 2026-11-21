# Off-Hire Mode

Triggered by `$plant-offhire [project] [window]`, or when the user explicitly asks for
an off-hire review, idle-plant ranking, or "hire costing money" analysis rather than a full
plant status report. Reuses Step 1 (project/period resolution, default **last 4 weeks**) and
Step 2 data retrieval (same four sources: `dashboardResourcePlant`, `dashboardAllocation`,
`dashboardNarrative`, plus `dashboardShiftTable` for the coverage check below) — do not
re-fetch. Skip Steps 3–8 of the standard report; run the steps below instead.

## Step A: Load the Commercial Profile

Look for `commercial-profile.md` (or `-<project-slug>.md`) per **Pattern 14**. A `project`
mismatch means ignore it and say so.

- Item has a `plant_rates` entry → read `rate`, `hire` (hired/owned), `offhire_notice_days`.
- Item has no entry → hire status and rate unconfirmed; quantities-only for that item.
- No profile, or no `plant_rates` section at all → **whole output quantities-only** (Pattern 14
  rule 2): classes and idle days still computed, hire status unconfirmed throughout, every
  exposure cell reads "rate not in commercial profile" — point once to `$commercial-profile`.

## Step B: Check Plant Recording Coverage

Before naming any candidate, cross-check recording coverage for the same window — same formula
and Poor-band threshold as `$data-quality`'s Resource Recording check:

**Plant Recording Coverage %** = (days with plant data recorded in the window ÷ expected working
days in the window, from `dashboardShiftTable`) × 100.

- **≥ 60%** — adequate; "no recorded use in the window" is a meaningful idleness signal.
- **< 60%** — **thin**. State this in the output header, and for every item with **zero**
  recorded use (not merely low utilisation) downgrade the claim from "idle" to **"no recorded
  use — verify against hire records"** rather than naming an off-hire candidate on that basis
  alone. Items with some recorded use but low utilisation stay a genuine MONITOR signal regardless of coverage.

## Step C: Build Per-Item Metrics

Apply the same **Pattern 12 schema gate** as the standard report's Step 3 (days-on-site vs
days-used; degrade to first-to-last recorded span if the distinction is unavailable).

For each plant item:

- **Last Recorded Use** — latest date used in the window, or "no recorded use in this window".
- **Idle Working Days** — weekdays from the day after Last Recorded Use through the window end
  (inclusive); the full window's weekdays if no use is recorded at all.
- **Utilisation %** = Days Used ÷ Days in window (or recorded span). Render **"n/a"** on a zero
  denominator (Pattern 12) — never 0.

## Step D: Classify and Calculate Exposure

Apply in order (first match wins):

1. **OFF-HIRE CANDIDATE** — Idle Working Days ≥ 5 **and** `hire: hired` per the profile (or
   hire status unconfirmed — label these "hire status unconfirmed").
2. **MONITOR** — Utilisation % < 40% (and not already a candidate).
3. **IN USE** — everything else.

**Exposure** (hired items only) = idle weeks (Idle Working Days ÷ 5, 1 decimal) × the profile
weekly rate, cited "rate per commercial profile". No rate → exposure cell reads "rate not in
commercial profile"; the item still carries its class.

**Owned plant** never carries an exposure figure or an OFF-HIRE CANDIDATE class (nothing to
end) — list it separately, utilisation-only, MONITOR/IN USE only.

## Step E: Ask About Programmed Upcoming Need

Before finalising, ask the user once, listing items currently classed OFF-HIRE CANDIDATE: "Is
there any programmed upcoming need for [items]?" A confirmed need moves that item to IN USE
with a one-line reason, excluded from the action list. Anything not addressed stays a candidate
but marked **"confirm no programmed need before off-hiring"** — carried by every recommendation
regardless of the answer given, not only the unconfirmed ones.

## Step F: Present the Off-Hire Report

```
PLANT OFF-HIRE REVIEW — [Project Name]
Ref: OH-[NNN]
Window: [Start Date] to [End Date]
Generated: [Today's Date]
```

`[NNN]` per **Pattern 8**: increment a prior OH ref in this conversation, else `001`. If Step B
found coverage < 60%, add: "Plant recording coverage for this window is [X]% — below the
reliable threshold. 'No recorded use' below is a records claim, not proof of idleness — verify
thinly-covered items against hire records before acting."

### RANKED TABLE (hired plant, worst exposure first)

| Item | Hire | Rate | Last Recorded Use | Idle Working Days | Utilisation | Class | Weekly Exposure |
|---|---|---|---|---|---|---|---|
| [item] | hired | [rate/wk or "rate not in commercial profile"] | [date or "no recorded use"] | [X] | [X]% / n/a | [OFF-HIRE CANDIDATE / MONITOR / IN USE] | [£X/wk or "rate not in commercial profile"] |

**TOTAL WEEKLY BLEED: £[X]/wk** — sum of Weekly Exposure across priced OFF-HIRE CANDIDATE lines
only (unpriced and MONITOR/IN USE excluded). Source: commercial profile `plant_rates`. If no
lines are priced: "No weekly bleed figure — no plant rates in the commercial profile; see the
quantities-only table above."

### OWNED PLANT (utilisation only, no exposure)

| Item | Last Recorded Use | Idle Working Days | Utilisation | Class |
|---|---|---|---|---|
| [item] | [date] | [X] | [X]% / n/a | [MONITOR / IN USE] |

### ACTION LIST

For each OFF-HIRE CANDIDATE, one line:

> **[Item]** — idle [X] working days, [utilisation]% over the window, exposure [£X/wk or
> "rate not in commercial profile"]. Off-hire notice period: [X days, per commercial profile /
> "not in commercial profile — confirm with the hire company"]. **Confirm no programmed need
> before off-hiring.**

If none: "No off-hire candidates identified this window."

### Caveats

> **Notes:**
> - "No recorded use" is a records claim, not proof of non-use — plant not entered in
>   shift diaries will not appear here regardless of actual status.
> - Financial figures are user-supplied via the commercial profile (Pattern 14), never invented.
> - Ref: OH-[NNN] is a session-local sequence number for cross-referencing.
