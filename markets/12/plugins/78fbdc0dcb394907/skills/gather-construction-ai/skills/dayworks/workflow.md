---
name: dayworks
description: Build a signature-ready daywork (T&M) sheet — labour, plant, materials
  on an instructed task, priced at daywork rates. Not subbie verification (use subcontractor-check)
  or plain labour/plant analysis (use labour/plant-report).
---

Read `../../shared/openai-runtime.md` before this workflow; it defines tool discovery, resource paths, output handling and data checks for this OpenAI edition.


# Daywork Sheet Builder

Build the daywork sheet a QS would otherwise write by hand: pull the shift records for the
instructed task's date(s), attribute labour, plant and materials to that task **conservatively**,
price at the commercial profile's daywork rates, and produce a signature-ready sheet.

Follow the shared patterns: `../../shared/patterns/02-date-range-parsing.md` (date parsing); `../../shared/patterns/03-empty-data-handling.md` (empty data handling); `../../shared/patterns/04-pagination-rate-limits.md` (pagination).

---

## Step 1: Resolve Project, Task, Dates and Instruction Reference

1. Resolve the project using **Pattern 1** in `../../shared/patterns/01-project-resolution.md`.
2. Parse `the user’s request` for the **task description** (what was instructed), the **date(s)** worked,
   and an optional **instruction/CE reference**.
3. Parse the date(s) using **Pattern 2**. Dayworks are tied to specific worked dates, not an open
   period — if none is given, ask rather than defaulting to "last 4 weeks".
4. If the task description is missing or too vague to attribute resources against in Step 4, ask
   for it first — conservative attribution is impossible without knowing what was instructed.
5. If no instruction/CE reference was given, record "no instruction reference supplied" in the
   header rather than inventing one.

---

## Step 2: Gather Shift and Delivery Records for the Date(s)

Call `getShiftRecords` for the project and stated date(s), then `getShiftRecord` per matching
record for narrative, worker lists, and any plant/material list fields — follow **Pattern 4** for
pagination and confirm first if more than 5 records need detail fetches. Also locate delivery-note
data for the same date(s) using the same lookup order as `$delivery-notes` Step 2: a
delivery-capable report via `getReportSchemas` first, else mined from shift-record list fields and
narratives (`dashboardResourceMaterial` is usage, not delivery, and is not the source here).

If no shift records exist for the date(s), follow **Pattern 3**: state plainly that none were
found for that project and those dates, suggest checking the date(s) or project, and offer retry.

---

## Step 3: Identify Labour, Plant and Materials Present

Build three raw lists for the stated date(s) — every resource recorded on site that day, not yet
the daywork sheet:

- **Labour** — name, trade/role, hours, and the shift(s) they appear on
- **Plant** — item, hours or days recorded in use
- **Materials** — description, quantity, unit, delivery note reference

---

## Step 4: Attribute Conservatively — the Guardrail

This is the skill's signature discipline. For each entry from Step 3, check whether the shift
narrative(s) explicitly **tie that resource to the stated task**:

- **Tied by narrative** (named trade/plant/material working on, or delivered for, the described
  task) → include in the priced tables (Step 5).
- **Present that day but not tied** (no mention, or a general narrative that doesn't distinguish
  this task from other work that day) → do **not** price it. List it under **"Attribution
  unconfirmed — confirm in/out"** for the user to resolve before the sheet is finalised.

Never include a resource on presence alone. An ambiguous narrative covering multiple tasks without
separating hours is treated as unconfirmed, never split by guesswork.

---

## Step 5: Price the Attributed Resources

Check for a commercial profile (`commercial-profile.md` or the project-slugged variant) per
**Pattern 14**; a profile whose `project` doesn't match is ignored (say so).

- **Labour** — confirmed hours × the trade's `labour_daywork_rates` entry. No matching rate →
  quantities-only for that row ("rate not in commercial profile").
- **Plant** — confirmed hours/days × the item's `plant_rates` entry, in the rate's own unit
  (day/week — never convert hours to days without a stated shift length). No matching rate →
  quantities-only.
- **Materials** — delivered quantity at **delivered cost** (from the delivery note, or
  user-supplied this session — Gather itself carries no financial data) **plus** the commercial
  profile's materials handling/overhead percentage where one is stated. Missing cost and/or
  percentage → quantities-only for the missing part, e.g. "delivered cost only — no handling
  percentage in commercial profile".

Every priced line cites its source ("rate per commercial profile" / "user-supplied this
session"). No profile at all → the whole sheet runs quantities-only, pointing once to
`$commercial-profile` (Pattern 14 rule 2) — never a blocker.

---

## Step 6: Contract Note

Resolve the contract type per **Pattern 5** if not already known, and include exactly one line
(never both, never an invented clause):

- **NEC:** "Dayworks value a compensation event only where the Project Manager and Contractor
  agree to use them instead of Defined Cost (clause 63.2) — the default CE assessment remains
  Defined Cost + Fee (see `nec-contracts`). This sheet is a factual daywork record, not itself a
  CE assessment unless such agreement exists."
- **JCT:** "Where instructed work cannot properly be valued by measurement, it is valued as
  daywork under the Valuation Rules (clause 5.7, alongside 5.6–5.10)."
- **Unknown/other:** state the contract type hasn't been confirmed and valuation mechanics vary by
  form — ask, or proceed noting the sheet is a factual record pending confirmation.

---

## Step 7: Build and Present the Daywork Sheet

Assign **Ref: DW-[NNN]** per **Pattern 8** (increment if a prior DW ref exists this conversation,
else `001`). Present in chat:

```
DAYWORK SHEET — [Project Name]
Ref: DW-[NNN]                      Sheet No: [NNN]
Date(s): [date or date range]
Instruction/CE Ref: [ref, or "none supplied"]
Task: [task description]
```

**LABOUR** — | Name | Trade | Hours | Rate | Basis | Value |
**PLANT** — | Item | Hours/Days | Unit | Rate | Basis | Value |
**MATERIALS** — | Material | Qty | Unit | Delivered Cost | +% | Value |

**TOTALS** — Labour / Plant / Materials / **Sheet Total** (state currency; "rate not in
commercial profile" rows excluded from the priced total and called out separately).

**Attribution unconfirmed — confirm in/out** — | Type | Name/Item | Hours/Qty | Why unconfirmed |

**Contract note** — the single line from Step 6.

**Signature block**

| Prepared By (QS) | Agreed By (PM / Client Agent) |
|---|---|
| _______________ Date: _____ | _______________ Date: _____ |

**Evidence appendix** — every shift record ID and delivery note reference used, one row per
record: | Record Type | ID | Date | Relevance |

Always include: "This sheet is a factual record from Gather site data. It requires QS commercial
review and PM/Client agreement before it has contractual effect. Ref: DW-[NNN] is a session-local
sequence number for cross-referencing."

---

## Step 8: Shareable HTML Daywork Sheet (Generated by Default)

Generate the HTML sheet automatically after presenting the chat version, unless the user asked
for chat-only output or declines when told a file is about to be written.

1. Read `../../shared/templates/ce-submission-template.html`.
2. Build the run's data as a single JSON object matching the template's schema, with
   `typeLabel: "DAYWORK RECORD"` (added to the template in parallel with this skill) so the
   header band reads "DAYWORK RECORD" rather than a CE label. Map `ref`/`projectName`/
   `contractLine`/`date` from Step 7's header; `parties.from`/`parties.to` from the preparing
   party and the PM/Client agent; `sections` — one entry per Step 7 block (Task Description,
   Labour, Plant, Materials, Attribution Unconfirmed, Contract Note) as
   `{heading, paragraphs, table?, list?}`; `evidence` from the Evidence Appendix; `assumptions`
   from any pricing basis stated in Step 5 (omit if none); `notes` from the Step 7 caveat line;
   `signature.preparedBy`/`signature.reviewedBy` left `""` unless names were supplied.
3. Splice this JSON between the `/*__CE_SUBMISSION_DATA__*/` and `/*__END_CE_SUBMISSION_DATA__*/`
   markers with a plain string split on those literal tokens (not a regex) — locate the opening
   marker, locate the closing marker, replace everything between with `JSON.stringify` of the
   object from step 2. Keep both markers in place around the data.
4. Write the result to `<ref>-daywork.html` in the working directory with the Write tool — one
   self-contained file, zero external requests.
5. State the file path, and note it opens in any browser, prints to A4 portrait, and is safe to
   circulate standalone.

**Fallback:** if the template cannot be read, say so plainly and present the chat sheet from
Step 7 only — do not hand-build a substitute HTML file.

---

## Related Skills

- `$commercial-profile` — capture daywork/plant rates and materials handling percentage
- `$subcontractor-check` — verify a subcontractor's own daywork claim against records
- `$labour` — broader labour analysis beyond a single instructed task
- `$delivery-notes` — fuller delivery search if materials evidence needs more context
