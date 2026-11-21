# Routine Templates

Ready-to-install scheduled-run prompts for the twenty-six customer-facing entries in the routine
catalogue (`docs/routines-and-schedules.md`, "Routine catalogue" section). Each template below
expands one catalogue entry — same prompt core, same rationale — into a self-contained prompt
you can paste straight into a Desktop scheduled task, a cloud routine, or a host-supported automation. The
maintainer-only "contract currency watch" is excluded — it isn't customer-facing.

**Placeholder convention:** `{{UPPER_SNAKE}}` markers are yours to fill in before installing a
routine. `{{PROJECT}}` (the Gather project name) and `{{FOLDER}}` (the Desktop working folder,
e.g. `~/gather-reports/`) are common to almost every template; the rest are per-template and
named in that template's Instructions block — e.g. `{{ASSESSMENT_DAY}}` (month-end-close),
`{{MEETING_DAY}}` (ew-meeting-prep), `{{DEADLINE_DATE}}` (ce-quotation-chaser). Replace every
placeholder before scheduling; an unfilled `{{…}}` in a live prompt means it was installed too fast.

**Two design rules every template below already implements:**

1. **Delta discipline.** Every recurring routine reads its own last output before doing new
   work and reports only what changed. Silence on a quiet run is the feature, not a shortfall.
2. **Action-first endings for contractual routines.** time-bar-sweep, weather-threshold-check,
   and ce-quotation-chaser never stop at the finding — each ends with the specific reminder,
   notification, or drafting action available right now, because a correct finding with no
   next step is a QS problem left for someone else to notice.

---

## Working-folder conventions

Both conventions below apply to **Desktop scheduled tasks** — cloud routines have no persistent
folder across runs (see the Cloud-routine adaptation note at the end).

### `{{FOLDER}}/routine-state/<routine-id>/last-run.md`

Each recurring routine keeps its own state file at this path (e.g.
`{{FOLDER}}/routine-state/time-bar-sweep/last-run.md`). At the **end** of every run, the routine
overwrites this file with a short dated summary of what it found. At the **start** of the next
run, it reads the file back and reports only the material changes since then — that's delta
discipline in practice, not just a slogan.

Format — a date header plus flat bullet findings, nothing fancier:

```markdown
## 2026-07-06

- Coverage 94%, no gap days
- 1 narrative missing (M. Okafor, 07-04)
- No CE candidates aged >4 weeks
```

Rules:
- One `##` date header per run (or simply overwrite — the routine only ever needs the
  immediately previous entry to compute a delta).
- Bullets are findings, not the full report — the full HTML/table output goes to `{{FOLDER}}`
  itself, dated, where the underlying skill produces one.
- If the file doesn't exist yet (first run), say so once and report the full findings that run.

### `{{FOLDER}}/ce-register.md`

The read-only Gather API has no field for "date the Contractor notified the PM of a compensation
event" — that only exists if someone writes it down. `ce-register.md` is that write-down, and it
is the one file in this pack the routines do **not** own.

Schema — a markdown table:

```markdown
| Ref | Event description | Aware date | Notified date | PM reply date | Quotation instructed | Quotation submitted | Status |
|---|---|---|---|---|---|---|---|
| CE-014 | Access denied, Pier 4 causeway | 2026-05-12 | 2026-05-19 | 2026-05-26 | 2026-06-02 | | Awaiting quotation |
```

Rules:
- **Maintained by the user.** This is the Contractor's own record of what was notified when —
  routines cannot see the PM's inbox, so they cannot know a notification happened unless it's
  written here.
- **Routines read it** to cross-check candidate events (from `$events`) and compute
  deadlines (via `$nec-deadlines`) against real notification dates, not assumed ones.
- **Routines may append**, never edit. A routine that spots a likely un-notified CE adds a
  clearly-marked section at the bottom:

  ```markdown
  ## Suggested new row — added by time-bar-sweep, 2026-07-06
  | CE-019? | Rebar delivery short, Deck 2 | 2026-06-18 | | | | | Not yet in register — confirm and add above |
  ```

  Existing rows are never rewritten by a routine, even to fix an apparent typo.

---

## Scheduled-run adaptation

Confirm the scheduler can access the Gather connection, this plugin and required files on each run. Use durable file references supported by that host. Do not assume local folders survive cloud runs. Keep rates in authorised project files where possible. If a future run cannot access a required profile, request an accessible input or use only the template's explicit fallback. Without persistent state, do not promise delta reporting. The cloud markers in the index describe the original template's input needs, not confirmed ChatGPT scheduling support.
