---
name: commercial-profile
description: Capture project rates you control — currency, retention, activity/daywork/plant
  rates, subcontract orders, prelims allowances — so valuation, dayworks etc. price
  outputs, not just quantities.
---

Read `../../shared/openai-runtime.md` before this workflow; it defines tool discovery, resource paths, output handling and data checks for this OpenAI edition.


# Commercial Profile

Capture the project's rates and allowances, once per project, so `$valuation`,
`$subcontractor-check`, `$dayworks`, `$plant-offhire`,
`$material-reconciliation`, and `$prelims-monitor` (being built in parallel) stop
producing quantities-only output for figures the user has already priced elsewhere. This skill
only writes the profile file — it does not itself value a measure, verify a claim, or price a
daywork sheet. Follow **Pattern 14 (Commercial Profile)** in
`../../shared/patterns/14-commercial-profile.md` for the file convention and schema — this
skill is the **producer** of that pattern, every other skill a consumer. See also **Pattern 13
(Contract Profile)** in `../../shared/patterns/13-contract-profile.md`, which this skill defers to for `main_option`. Follow **Pattern 19
(Interview-and-Confirm)** in `../../shared/patterns/19-interview-and-confirm.md`
for the five-step skeleton and Update Mode — this file holds only the question groups and
schema below.

**Sensitive-data warning:** this file holds commercially sensitive rates, order values and
allowances — remind the user at write time and offer a `.gitignore` line; never assume the
repository is private.

---

## Step 1: Resolve the Project

Resolve the project using **Pattern 1** in `../../shared/patterns/01-project-resolution.md`. If the Gather MCP is connected, verify the
name against `getMyProjects` (or `getProjects`) so `project` matches Gather exactly. Without a
connection, proceed with the name the user gives — this skill works without one.

Filename: `commercial-profile.md` for one project in this directory, or
`commercial-profile-<project-slug>.md` (lower-cased, hyphenated) once more than one is worked on
here. If a profile file for this project already exists, switch to **Update Mode** instead of a
fresh interview.

**Contract profile cross-check:** look for `contract-profile.md` (or its slugged variant); if it
exists, read it and prefill `main_option` from it rather than asking, flagging any conflicting
answer at Step 3 rather than picking silently. If no contract profile exists, ask for
`main_option` directly; it is not required.

---

## Step 2: Interview — One Compact Question Set

Ask everything in one grouped message — never twenty separate questions — under headings so the
user can answer in one pass and skip any group; the file will say the corresponding skill runs
quantities-only for a skipped group.

> **Currency & retention** — 1. Currency (default GBP). 2. Retention % held.
>
> **Activity / measure rates** (`$valuation`) — 3. Item, unit, rate for each valued
> activity you want priced in the monthly measure.
>
> **Labour daywork rates** (`$dayworks`, `$subcontractor-check`) — 4. Trade, unit,
> rate, and basis (e.g. "CECA daywork schedule 2025 +12%").
>
> **Plant rates** (`$plant-offhire`, `$dayworks`) — 5. Item, unit, rate, hire type
> (hired/owned), off-hire notice period in days.
>
> **Subcontract orders** (`$subcontractor-check`) — 6. Subcontractor, package, order
> value, rates basis (order number/revision).
>
> **Prelims allowances** (`$prelims-monitor`) — 7. Staff heads allowed on site per tender,
> establishment weekly cost, tender duration in weeks.
>
> **Material waste norms** (`$material-reconciliation`) — 8. Material, unit, waste allowance %.

Accept a partial answer (e.g., just plant rates before an off-hire review) — do not insist on a
full interview. Unanswered groups are simply omitted from the file.

---

## Step 3: Confirm Back as a Table

Per Pattern 19 step 3, marking unanswered groups "not provided (quantities-only downstream)". If
Step 1 found a conflicting main option, show both values side by side and ask which is correct.

---

## Step 4: Write the File

Write the confirmed values to the target filename, following the Pattern 14 schema exactly:

```yaml
project: <Gather project name>
currency: <e.g. GBP>
retention_pct: <number>
main_option: <A-F, cross-checked against contract-profile.md if present>
activity_rates:
  - {item: "<item>", unit: <unit>, rate: <number>}
labour_daywork_rates:
  - {trade: "<trade>", unit: <unit>, rate: <number>, basis: "<basis>"}
plant_rates:
  - {item: "<item>", unit: <unit>, rate: <number>, hire: <hired|owned>, offhire_notice_days: <number>}
subcontract_orders:
  - {subcontractor: "<name>", package: "<package>", order_value: <number>, rates_basis: "<basis>"}
prelims:
  staff_allowance: <number>
  establishment_weekly: <number>
  tender_duration_weeks: <number>
material_norms:
  - {material: "<material>", unit: <unit>, waste_allowance_pct: <number>}
profile_date: <YYYY-MM-DD>
```

Wrap the YAML in a short prose header (project, date, sensitive-data reminder). For every
skipped group, add an inline comment stating the downstream consequence, e.g.
`# plant_rates not supplied — $plant-offhire will report exposure quantities only`.
Never invent a value — omission plus a comment is always correct.

Offer this `.gitignore` line (do not add it yourself unless asked): `commercial-profile*.md`

---

## Step 5: Explain What Happens Next

Per Pattern 19 step 5. Name the consuming skills: `$valuation`,
`$subcontractor-check`, `$dayworks`, `$plant-offhire`,
`$material-reconciliation`, `$prelims-monitor` — they now price lines from it,
citing "rate per commercial profile"; skipped sections stay quantities-only. Repeat the
sensitive-data reminder: keep the file out of shared repositories (`.gitignore`:
`commercial-profile*.md`), and outputs sent to the other party should carry only the priced
lines, not the whole file.

---

## Update Mode

Per Pattern 19 step 1's Update Mode trigger and rules, plus: re-check `contract-profile.md` for
`main_option` and flag any drift before merging changes.

---

## Hard Rules

1. **Never invent a rate.** An omitted field means the affected skill runs quantities-only.
2. **Only this skill writes the file.** Consuming skills read it, never edit it — send the user
   back here even for a rate they give mid-conversation.
3. **Sensitive-data warning is not optional.** In the file header and repeated at Step 5, every
   time, including Update Mode.
4. **`main_option` defers to `contract-profile.md`.** Cross-check every write; flag mismatches,
   never silently overwrite.
5. **A mismatched `project` field is not yours to edit.** Resolve the correct project first
   (Step 1) rather than editing in place.
6. **Quantities-only is a complete answer, never a blocker.** Say what's missing and continue.

---

## Worked Example

**EXAMPLE ONLY — illustrates the output format, not a real project.** An NEC4 ECC Option C
project (option read from an existing `contract-profile.md`) with a few rates per section:

> # Commercial Profile — Westbury Viaduct Renewal
>
> Captured 2026-07-07. Contains commercially sensitive rates and order values — keep this file
> out of shared repositories (`.gitignore`: `commercial-profile*.md`).

```yaml
project: Westbury Viaduct Renewal
currency: GBP
retention_pct: 3
main_option: C                            # per contract-profile.md
activity_rates:
  - {item: "Pier Construction (Piers 3-5)", unit: m3, rate: 385.00}
  - {item: "Deck Steel Fixing", unit: t, rate: 1240.00}
labour_daywork_rates:
  - {trade: "Steel fixer", unit: hr, rate: 38.50, basis: "CECA daywork schedule 2025 +12%"}
plant_rates:
  - {item: "50t crawler crane", unit: wk, rate: 2100.00, hire: hired, offhire_notice_days: 7}
subcontract_orders:
  - {subcontractor: "FormTech Ltd", package: "Falsework", order_value: 480000, rates_basis: "SC order 0042 rev 2"}
prelims:
  staff_allowance: 6
  establishment_weekly: 8500.00
  tender_duration_weeks: 42
material_norms:
  - {material: "C40/50 concrete", unit: m3, waste_allowance_pct: 5}
profile_date: 2026-07-07
```

> Notes: no material norm given for reinforcement — `$material-reconciliation` reports
> delivered/placed quantities only until one is supplied.

---

## Related Skills

- `$valuation` — prices the period measure at `activity_rates`, applies `retention_pct`
- `$subcontractor-check` — reads `subcontract_orders` and `labour_daywork_rates`
- `$dayworks` — prices labour/plant hours at `labour_daywork_rates` and `plant_rates`
- `$plant-offhire` — reads `plant_rates` (rate, hire type, off-hire notice)
- `$material-reconciliation` — reads `material_norms`, prices excess waste
- `$prelims-monitor` — reads `prelims` (staff allowance, establishment weekly, tender duration)
