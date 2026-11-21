---
name: programme-impact
description: 'Indicative what-if on the imported programme: add a delay or change
  a duration and the deterministic CPM engine shows the movement of planned Completion
  and the critical path, always INDICATIVE-bannered with the self-check % — never
  the Accepted Programme.'
---

Read `../../shared/openai-runtime.md` before this workflow; it defines tool discovery, resource paths, output handling and data checks for this OpenAI edition.


# Indicative Impact Assessment (Ref IA-NNN)

Runs a delay/duration what-if against the imported programme through the deterministic CPM
engine (`scripts/cpm.py`) and reports the movement of planned Completion and the critical path.
This skill is the **flagship consumer** of **Pattern 15's STORED/INDICATIVE doctrine** in
`../../shared/patterns/15-programme-baseline.md` — read it, and the
`cpm.py` docstring (the impact-spec JSON schema lives there), before starting. Also follow
**Pattern 1** (project resolution, `../../shared/patterns/01-project-resolution.md`) and **Pattern 8** (report numbering, `../../shared/patterns/08-report-numbering.md`).

**Scope note:** this skill never reschedules or "corrects" the imported programme, never
invents a change, and never presents an indicative date as the Accepted Programme. Every
output is a delta for the planner to apply in the planning tool (P6/MSP/Asta) — that tool
remains the authority.

**Local files this skill reads (never writes):**
- `programme/programme-baseline.json` — the structured sidecar the engine schedules against
  (Pattern 15). **Required** — without it there is no network to run the engine over.
- `programme/programme-baseline.md` — the human-readable provenance block: self-check
  reproduction %, Accepted-Programme confirmation, revision, data date (Pattern 15). Both files
  are written only by `$programme-import`; a project mismatch on either is ignored (say
  so, Pattern 15 rule 7).

---

## Step 1: Resolve Project and Load the Baseline

1. Resolve the project (Pattern 1).
2. Look for `programme/programme-baseline.json` and `programme/programme-baseline.md` (or their
   `<project>`-slugged variants) whose `project` matches. A mismatch is ignored (say so).
3. **Absent sidecar → degrade per Pattern 15 rule 6:** state the standard limitation ("no
   imported programme baseline — run `$programme-import` first"), and stop. There is no
   network to schedule without the JSON sidecar; do not fall back to run-rate methods here (that
   is `$programme`'s job, not this skill's).
4. Read the md file's provenance block and carry these into **every output header** below:
   - **Self-check reproduction %** (and the matched/compared counts behind it).
   - **Accepted-Programme status** (confirmed yes as at a date / no / not confirmed).
   - Revision and data date, for the "per the imported programme" citation.
   - If the md file does not carry a self-check figure (an older import), compute it live —
     `python3 ../../scripts/cpm.py programme/programme-baseline.json
     --self-check` with no `--impact` — and state plainly that the figure was computed live
     because the baseline md did not carry it.
5. If the user has not confirmed the file as the **Accepted Programme**, say so wherever the
   output would otherwise carry contractual weight (Pattern 15 rule 1) — an unconfirmed import
   is treated as indicative-of-indicative, doubly so.

---

## Step 2: Capture and Translate the Change

1. Take the change from `the user’s request` or ask: a delay/duration change to an existing task, or an
   inserted event requiring a fragnet (new tasks + links).
2. **Identify the task(s).** Use the user-confirmed Gather↔programme mapping (Pattern 15 rule 5)
   where the user names a Gather activity, or match directly against the sidecar's task ID or
   name — **exact match only**. If more than one task could plausibly match, **list the
   candidates and ask** — never guess (the same discipline as `programme-import` Step 4).
3. Translate the change into the engine's **impact-spec JSON** (schema documented in the
   `cpm.py` docstring):
   ```json
   {"changes": [{"task_id": "3", "delay_hours": 80}]}
   ```
   — or `"new_duration_hours"` in place of `"delay_hours"` for a duration change, or a
   `"fragnet"` object (`{"tasks": [...], "links": [...]}`) for an inserted event, in the same
   shape as the sidecar's own `tasks`/`links`.
4. **Show the impact spec back to the user before running it.** Non-interactive: state it as
   the assumption and continue, quoting the JSON (or the file it was written to).
5. Changes come only from what the user describes here — **never invented**. A change the user
   hasn't stated does not get modelled "to be thorough."

---

## Step 3: Run the Engine Twice

CPM arithmetic happens **only in the engine script — never in-model** (Pattern 15 rule 3). Shell
out to `scripts/cpm.py` twice, writing the Step 2 spec to a temporary `spec.json` first:

```bash
python3 ../../scripts/cpm.py programme/programme-baseline.json [--status-date <date>]
python3 ../../scripts/cpm.py programme/programme-baseline.json --impact spec.json [--status-date <date>]
```

- The first call (no `--impact`) is the **baseline run** — the unmodified network.
- The second call is the **impact run** — the Step 2 change applied.
- **The movement is the difference between these two ENGINE runs — never engine-vs-stored.**
  State why: the baseline run and the impact run are the same model, under the same
  assumptions, differing only by the one change — their difference is like-for-like
  arithmetic. Comparing the impact run against the stored (planning-tool) dates instead would
  blend two different models and contaminate the delta with the file's own self-check gap
  (Step 1's reproduction %).
- Pass `--status-date` only where the user supplies one, or one is already agreed earlier in
  this conversation (e.g. carried from a Programme Advisor run); omit it otherwise.
- **python3 unavailable:** degrade per Pattern 15 rule 3 — state "indicative recalculation
  unavailable — python3 not found; stored values unaffected" and stop. Do not attempt the
  arithmetic by hand.

---

## Step 4: Present the Assessment

Apply **Pattern 8** for the `IA-[NNN]` ref (session-local; increment on a prior `IA` ref, else
`001`).

```
INDICATIVE IMPACT ASSESSMENT — [Project Name]
Ref: IA-[NNN]
INDICATIVE recalculation performed outside the planning tool - not the Accepted Programme;
verify in P6/MSP/Asta before relying on it.
Self-check (reproduction %): [X]% ([matched]/[compared] tasks reproduce stored dates exactly)
Accepted Programme: [yes, as at DATE / no / not confirmed] — per programme-baseline.md
Baseline: [revision], data date [date] | Change: [one-line Step 2 description]
```

1. **CHANGE APPLIED** — the Step 2 impact spec restated in words, the JSON itself (or the file
   it came from), and how the task(s) were identified (mapping / exact ID / exact name match).
2. **MOVEMENT OF PLANNED COMPLETION** — baseline-run project finish vs impact-run project
   finish: the delta in working hours, the equivalent working days, and the calendar span.
   Repeat for any Key Date / handback-type milestone whose movement differs from the project
   finish. State plainly: "this is the movement between two engine runs of the same model — not
   a comparison against the stored/Accepted Programme."
3. **CRITICALITY MOVEMENT** — **STORED and INDICATIVE never mix unlabelled** (Pattern 15 rule
   2). One table, every column labelled by class:

   | Task | STORED critical (import, [data date]) | INDICATIVE critical (impact run) | STORED float | INDICATIVE float (baseline run) | INDICATIVE float (impact run) |
   |---|---|---|---|---|---|

   Only list tasks where the INDICATIVE (impact-run) criticality flag differs from the STORED
   flag as the "criticality changed" set — but always show the float columns for every task in
   this table where STORED and INDICATIVE float diverge, even with no criticality change: this
   is a normal consequence of the file's self-check gap and must never be smoothed into one
   unqualified "float" figure. If no task's criticality classification changes, say so plainly.
4. **TASK-LEVEL DELTA TABLE** — for the planner to apply directly in the planning tool:

   | Task | Baseline-run start/finish | Impact-run start/finish | Delta (working hours) |
   |---|---|---|---|

5. **DEGRADE MESSAGES**, if any arose — absent sidecar (Step 1) or python3 unavailable
   (Step 3) — restated here per Pattern 15 rules 3 and 6.

Close every output with the standing caveat, unmodified:

> This is an INDICATIVE recalculation performed outside the planning tool — it is not the
> Accepted Programme and is not itself a programme revision. The planning tool (P6/MSP/Asta)
> remains the authority; verify these figures there before relying on them for any contractual
> purpose. Self-check reproduction: [X]% — [the engine's verdict text]. Ref: IA-[NNN] is a
> session-local sequence number for cross-referencing.

---

## LOGIC TRACE Mode

**Trigger:** the user asks "what feeds [task]" / "what does [task] feed" (or similar), or passes
"trace" in `the user’s request`.

This mode **skips the engine entirely** — it is a pure **STORED** read-out, and the output says
so explicitly at the top: "LOGIC TRACE — stored programme logic only, data date [date]; no
engine run, no what-if."

1. Identify the task using Step 2's matching discipline (exact match; ambiguous → list
   candidates and ask).
2. Read the sidecar's `links` array directly — **no `cpm.py` invocation**.
3. Walk predecessors ("what feeds it") and/or successors ("what it feeds") recursively and
   print the chain, e.g.:
   ```
   [Task] <- [predecessor] (FS, lag 0h) <- [predecessor's predecessor] (FS, lag 0h) <- ...
   [Task] -> [successor] (FS, lag 0h) -> [successor's successor] (FS, lag 0h) -> ...
   ```
4. Alongside each task, print its **STORED** total float (hours, plus the converted day figure
   with the divisor stated) and criticality flag exactly as imported — never recomputed.
5. If the sidecar has no links for the task in the requested direction, say so plainly ("no
   stored predecessors" / "no stored successors") rather than an empty table.

---

## Hard Rules

1. **Engine only via `scripts/cpm.py`.** No in-model CPM arithmetic, ever — not even a "rough"
   estimate (Pattern 15 rule 3).
2. **STORED and INDICATIVE never mix unlabelled.** Every date, float, or criticality figure
   states its class. "The critical path" with no qualifier always means the STORED one.
3. **Changes come from the user, never invented.** An unstated change is not modelled; an
   ambiguous task match is listed as candidates, never guessed.
4. **The stored baseline files are never written by this skill.**
   `programme/programme-baseline.json` and `.md` are read-only here — only
   `$programme-import` writes them (Pattern 15 rule 7). This skill never claims to have
   rescheduled, updated, or corrected them.
5. **The planning tool remains the authority.** Every output says so; an indicative movement is
   a delta for the planner to apply in P6/MSP/Asta, never a substitute programme revision.
6. UK English throughout ("programme", not "program").

---

## Related Skills

- `$programme-import` — writes the baseline sidecar and md this skill reads; run this
  first if absent
- `$programme-compare` — the revision-to-revision counterpart: compares two **STORED**
  imports, where this skill compares two **INDICATIVE** engine runs
- `$ce-quotation` — its clause 63.5 two-programme delay assessment runs the same engine
  for a compensation event's time entitlement
- `$programme` — the run-rate forecast counterpart when no baseline has been imported
- Programme Advisor agent — the monthly update pack that reports actual progress against the
  baseline this skill interrogates
- Red Team agent — stress-tests an impact assessment's assumptions before it is relied on for an
  EOT/CE position
