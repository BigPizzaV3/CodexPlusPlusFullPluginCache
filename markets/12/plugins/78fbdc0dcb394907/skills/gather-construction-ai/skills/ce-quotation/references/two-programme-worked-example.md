# Two-Programme Method — Engine Execution and Worked Presentation Example

Loaded at Step 4, after the Programme baseline check (Pattern 15).

## Engine execution

**If the sidecar exists, python3 is available, and the user confirmed the baseline as the
Accepted Programme — EXECUTE the two-programme method with the engine, do not template it:**

1. **Programme 1 — run the engine, status-dated to the dividing date.** Shell out to
   `scripts/cpm.py` over the sidecar with `--status-date <dividing date>`:
   `python3 scripts/cpm.py programme/programme-baseline.json --status-date <dividing date> --self-check`.
   This fixes actuals (actual_start/actual_finish as recorded) and resumes remaining work at the
   dividing date — exactly the "updated to the dividing date" state clause 63.5 calls for.
   Record the run's `project_finish` as Programme 1's planned Completion.
2. **Programme 2 — the same run, plus the CE.** Re-run the identical command with
   `--impact <impact-spec.json>` added, where the impact spec carries the CE as a **fragnet**
   (linked into the network alongside the affected mapped task(s)) or as a **delay on the
   affected mapped task(s)** (`delay_hours` / `new_duration_hours`) — whichever shape the user
   confirms matches how the CE actually bites; never guess the shape. Record this run's
   `project_finish` as Programme 2's planned Completion.
3. **The EOT movement is Programme 2's `project_finish` minus Programme 1's `project_finish`,
   both engine runs.** This is the only like-for-like arithmetic available: both figures come
   from the same deterministic model under the same calendars and constraints, so the
   subtraction isolates the CE's effect. Never take Programme 1 from the engine and Programme 2
   from the stored programme (or vice versa) — mixing an engine run with a stored date compares
   two different bases and the difference would be partly model error, not CE effect.
4. **Every figure is INDICATIVE-bannered**, each carrying the banner text from Pattern 15
   ("INDICATIVE recalculation performed outside the planning tool — not the Accepted Programme;
   verify in P6/MSP/Asta before relying on it") plus **that file's self-check reproduction %**
   from `programme-baseline.md`'s provenance block (e.g. "self-check: 87% — the network model
   reproduces 87% of the file's stored dates; the other 13% carry calendars/constraints the
   model doesn't capture, and this indicative movement inherits that caveat"). Cite the
   sidecar's revision and export date alongside (Pattern 15 rule 1).
5. Terminal float preservation and the dividing-date fixing rules (Step 1) stand untouched: the
   Completion Date moves by exactly the movement computed above — no more, no less.
6. The rendering below now carries the engine's computed dates instead of bracket placeholders
   — every date and the `+[X] days` movement is labelled **INDICATIVE** inline, not just in a
   caveat paragraph.

**EXPLICIT DEGRADE — no sidecar, or python3 unavailable:** fall back to the descriptive
template exactly as below, with its bracket placeholders, and state plainly in the output:
**"no computation ran — this is a descriptive template; the planner must produce the two
actual programmes in MS Project/P6/Asta and return the planned-Completion dates."** Never
present the descriptive template's bracketed dates as if they were computed.

- **Sidecar exists but NOT confirmed as the Accepted Programme:** say so plainly, run the
  engine anyway if the user wants an indicative view, but do not give the result the
  contractual weight of an Accepted Programme — it stays INDICATIVE either way.
- **python3 unavailable:** state "indicative recalculation unavailable — python3 not found;
  stored values unaffected" (Pattern 15 rule 3) and use the degrade above.
- **Absent sidecar entirely:** state the standard limitation (no baseline/critical-path data)
  and use the degrade above; point to `$programme-import`.

## Presentation

Render both programmes as compact one-line-per-activity text Gantts, then a single Mermaid
chart with two sections, in the shape below.

**When the engine executed** (sidecar + python3 + confirmed baseline, per Step 4's procedure):
every bracketed date is replaced by the engine's computed date and tagged `(INDICATIVE)`
inline — including both "Planned Completion" lines and the `+[X] days` movement; the
self-check % appears once, directly under the pair.

**When the engine did NOT execute** (the degrade case): the brackets stay as unfilled
placeholders and the output states plainly that this is the descriptive template, not a
computed result.

```
Programme 1 — Updated to dividing date ([dividing date])
Scale: [start] ——— [end] (each ▪ ≈ [X] days)
Activity A                  ████████████··················
Activity B                  ····████████████···············
[CE-affected activity]      ········████···················
                                          ▲ Planned Completion: [date] (INDICATIVE)

Programme 2 — With CE impacted, logic-linked and rescheduled
Activity A                  ████████████··················
Activity B                  ····████████████···············
[CE-affected activity]      ········████░░░░[CE]···········
                                              ▲ Planned Completion: [date] (INDICATIVE) (+[X] days)

EOT movement (Programme 2 finish − Programme 1 finish, both engine runs): +[X] working days — INDICATIVE
Self-check (this file): [X]% — [engine reproduces the stored programme / caveat per Pattern 15]
```

```mermaid
gantt
    title Two-Programme Delay Assessment — [Project] — [CE-NNN] — INDICATIVE
    dateFormat YYYY-MM-DD
    axisFormat %d %b
    section Updated to dividing date (INDICATIVE)
    Activity A            :done, p1a, [start], [end]
    Activity B             :active, p1b, [start], [end]
    Planned Completion     :milestone, p1c, [date], 0d
    section With CE impacted (INDICATIVE)
    Activity A            :done, p2a, [start], [end]
    Activity B             :active, p2b, [start], [end]
    [CE] impact            :crit, p2d, [start], [end]
    Planned Completion     :milestone, p2e, [date], 0d
```

If the PM has notified under 61.5 that the Contractor did not notify an early warning an
experienced contractor could have given, note that the CE is assessed as if the early warning
had been notified (63.5 NEC3 / 63.7 NEC4), which may reduce the entitlement above.
