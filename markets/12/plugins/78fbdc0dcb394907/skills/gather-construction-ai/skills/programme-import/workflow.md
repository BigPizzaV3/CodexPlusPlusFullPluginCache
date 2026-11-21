---
name: programme-import
description: Import the programme from MS Project, Primavera P6 (XER), or Asta Powerproject
  via the deterministic parser script into a JSON sidecar — baseline tasks, float
  and critical path as stored, an engine self-check %, and versioned revision history.
---

Read `../../shared/openai-runtime.md` before this workflow; it defines tool discovery, resource paths, output handling and data checks for this OpenAI edition.


# Programme Import

The Gather API holds no baseline programme — no planned dates, logic links, or critical path.
This skill drives `scripts/parse_programme.py` (a deterministic, stdlib-only parser) over a
planning-tool export — MS Project MSPDI XML, Primavera P6 XER, or Asta Powerproject's MS Project
XML export — and writes the structured sidecar `programme/programme-baseline.json` plus the
human-readable index `programme/programme-baseline.md`. This skill **produces** **Pattern 15
(Programme Baseline)** in `../../shared/patterns/15-programme-baseline.md`
(read it first — it governs the sidecar/md split, STORED/INDICATIVE doctrine, and consuming
skills' rules). Also follow **Pattern 1** (`../../shared/patterns/01-project-resolution.md`) and **Pattern 8** (`../../shared/patterns/08-report-numbering.md`).

**Scope note:** parses and reports the schedule **as exported** (STORED) — never reschedules the
Accepted Programme, never invents a Gather-activity/programme-task mapping. The one engine run
performed, `scripts/cpm.py --self-check`, only calibrates trust in *later* engine-backed features
— its output is INDICATIVE, separately bannered, never a STORED substitute. A recomputation
beyond that self-check: "run `$programme` or the engine with the INDICATIVE banner,"
never a guess made here.

---

## Step 1: Locate the File and Detect Format

Resolve the project (Pattern 1). Then find the programme file: named in `the user’s request`, or a
working-folder scan for `.xer`/`.xml` files with programme-ish names (e.g. containing
"programme", "schedule", "baseline", the project name) — **confirm before using it**, same
discipline as `timesheet-check` Step 1.

**`.mpp` files:** MS Project's native binary format — never parse. Tell the user: "Open in MS
Project, File → Save As → XML, re-run with the `.xml` file." Stop.

**`.pp` files (Asta Powerproject):** also native binary — never parse. Tell the user: "In
Powerproject, File → Export → Microsoft Project XML, re-run with the `.xml` file." Asta's XML
export parses via the MSPDI path; see format-notes.md's Asta section for quirks (`Critical` is
often unpopulated — the parser falls back to `TotalSlack` ≤ 0 and says so).

**Format detection for everything else:**
1. `.xer` extension (or content starting `ERMHDR`) → **P6 XER** — parser-supported.
2. `.xml` extension → sniff the root element: `<Project>` in the
   `http://schemas.microsoft.com/project` namespace, containing `<Tasks>` → **MSPDI** —
   parser-supported. `<APIBusinessObjects>` root → **P6 XML** — **not yet supported** (the parser
   errors on the root-tag check; Step 2 explains the fallback). Neither → say exactly what root
   element/namespace was found and **stop** — never guess a parser for an unrecognised XML shape,
   a wrong parser silently produces wrong dates.

State the detected format in Step 2's report.

---

## Step 2: Parse

**Before running the parser — check for a prior import.** If `programme/programme-baseline.json`
already exists, this is a re-import. Read its `provenance` block and show it back (source
filename, format, data date, revision). Ask the user for the label of the revision now being
superseded (e.g. "Rev C"; non-interactive: use the file's own stated revision, or "unlabelled").
Then copy the existing sidecar, unmodified, to `programme/programme-baseline-<revision>.json`
**before** the parser overwrites `programme-baseline.json`. **Never silently replace it** — that
copy is the only thing `$programme-compare` has to diff against, and the md file's
revision index (Step 6) depends on it existing. No prior sidecar → first import; record and
continue.

Read `references/format-notes.md` for the full
field-by-field map, unit conversions, calendar/constraint handling, and what each export can and
cannot carry — the parser implements exactly those mappings; you don't need to re-derive any of
it by hand.

**Run the parser:**

```
python3 ../../scripts/parse_programme.py <file> --out programme/programme-baseline.json
```

**Multi-project XER:** the script refuses to guess. First list the projects in the file:

```
python3 ../../scripts/parse_programme.py <file> --list-projects
```

Show the returned `proj_id`/name/data-date list, ask the user which project, then re-run with
`--project <id>` added to the command above.

**Present the parser's JSON summary VERBATIM as the parse report** — do not paraphrase, round, or
drop any field: `format`, `project_name`, `data_date`, `baseline_present`, `task_count`,
`milestone_count`, `link_count`, `encoding`, `warnings`, `sidecar`. Surface every warning in full
— especially the **NO BASELINE** warning P6 XER exports carry when only
`target_start`/`target_end` (current planned dates) are present with no real baseline evidence:
state plainly these are *not* a baseline, per Pattern 15's stored-dates discipline. Surface
calendar warnings (e.g. "no usable weekly pattern — 8h/day assumed"), constraint warnings (unknown
codes, ALAP-treated-as-ASAP), and manually-scheduled-task warnings verbatim — every downstream
STORED citation inherits these caveats.

**In-context parsing fallback — narrow, stated, never silent:** parse in-context yourself per
format-notes.md's field tables **only** when python3 is unavailable **and** the file is small
(under ~200 tasks). State plainly this is a fallback, not the deterministic parser, and that no
self-check (Step 3) is possible without python3. For anything larger, or an unsupported **P6
XML** file, **stop**: give install guidance ("install Python 3 — bundled on macOS/Linux, from
python.org on Windows — then re-run") or ask for re-export as P6 XER/MSPDI XML. **Never silently
truncate a big file** to fit an in-context parse.

---

## Step 3: Engine Self-Check

Run the deterministic CPM engine's self-check against the sidecar just written:

```
python3 ../../scripts/cpm.py programme/programme-baseline.json --self-check
```

Its output carries a `self_check` object: `compared`, `matched`, `match_pct`, `verdict`, up to 25
`mismatches`. Report `match_pct`/`verdict` — **not** a schedule to present or act on; the per-file
trust calibrator Pattern 15 defines:

- **100%** — the network model (calendars, constraints, links) fully explains the stored dates;
  any *later* INDICATIVE engine run starts from a fully-verified model.
- **Less than 100%** — the model doesn't fully capture some calendars/constraints (`mismatches`
  shows which tasks diverge). **Every future INDICATIVE figure from this sidecar inherits that
  caveat** and should quote the self-check % alongside it.

Record `match_pct`/`verdict` in the md file's provenance block (Step 6) — the only content Step 3
contributes to the written file.

If python3 was unavailable (Step 2 in-context fallback), self-check cannot run: state "self-check
unavailable — python3 not found; stored values unaffected, no INDICATIVE recalculation available"
and continue.

---

## Step 4: Confirm

Summarise the parse report back and ask — non-interactive runs state as assumptions and continue:

1. Is this the intended programme?
2. Which revision (file name, export date, or user-stated)? — the label for the Step 2 history
   copy and Step 6 revision index.
3. Is this the **Accepted Programme** (contractual term, Pattern 15), and as at what date?

Record the answers into the md file's provenance block (Step 6) verbatim.

**Optional, only if the user wants them recorded — never assumed:**

4. **Key Date / Sectional Completion typing.** Ask whether any milestone is a **Key Date** or
   **Sectional Completion** rather than ordinary, confirmed against Contract Data
   (`contract-profile.md`, Pattern 13, if it exists — cite it; else ask the user). Skip and
   record untyped if declined.
5. **Possession-dependent tagging.** Ask whether any task/milestone depends on a stated
   possession/access date, for `$access` and `$delay-analysis` cross-reference.
   Skip and leave untagged if declined.

Both are optional confirmations written to the md file only — never inferred, never required.

---

## Step 5: Activity Mapping

Pull Gather activity names from `dashboardProgress` (schema-gate per Pattern 12 — if unavailable,
say so and skip to a mapping-free baseline).

Propose Gather-activity ↔ programme-task pairs against the sidecar's task names: (1) exact match,
then (2) contains-matching (either name a substring of the other, case-insensitive — e.g. "Pier
Construction (Piers 3-5)" vs "Pier Construction Piers 3-5"). (3) List, on **both sides**,
anything left unmapped — never silently dropped.

Show the proposed table and ask the user to confirm/correct before writing anything
(non-interactive: state the proposal as assumption). **Never guess a mapping** — an unresolved
pair stays unmapped, never force-matched.

---

## Step 6: Write the Summary File

Write `programme/programme-baseline.md`. **Row-level data (task table, dates, float,
predecessors) lives in the Step 2 sidecar — this md file never repeats it.** Per Pattern 15 v2,
the md file carries only:

- **Provenance block:** source filename, format, data date, revision, Accepted Programme status
  and as-at date, encoding, and the parser's `warnings` list (or a pointer to them).
- **Self-check:** the Step 3 `match_pct` and `verdict`.
- **Activity mapping:** the confirmed Step 5 table, plus both unmapped lists.
- **Revision index:** one line per revision — current (`programme-baseline.json`) and every
  prior sidecar saved at Step 2 (`programme-baseline-<revision>.json`, label + data date) —
  pointing to `$programme-compare` for the diff between any two.
- **Typed milestones (if confirmed at Step 4):** Key Date/Sectional Completion typing and
  possession-dependent tags. Omit entirely if Step 4's optional confirmations were skipped.

If the md file already exists, its revision index is **appended to**, not replaced — history
accumulates across imports, same as the sidecar history from Step 2.

---

## Step 7: Report

At Step 7, read `references/output-template.md`
for the exact report structure (Parse Summary, Activity Mapping, Revision History, What This
Unlocks, Caveat). Apply Pattern 8 for the `Ref: PI-[NNN]` line.

---

## Hard Rules

1. **Engine arithmetic happens only in `scripts/cpm.py` — never in-model.** Never compute float,
   criticality, or dates by reasoning over the file itself.
2. **INDICATIVE is always bannered and never blended unlabelled with STORED.**
3. **Never invent dates or mappings.** Not-found → "not present in this export" (or `warnings`).
   Unconfirmed mapping → stays in the unmapped lists.
4. **`.mpp`/`.pp` are never parsed.** Instruct the XML/export path and stop.
5. **Cite format, data date, and self-check %** in every downstream figure quoted (e.g. "per the
   imported programme, P6 XER, data date 2026-01-26, self-check 96%").
6. **UK English** throughout ("programme", not "program"; "recognised", not "recognized").
7. **Revisions are versioned, never silently overwritten** (Steps 2 and 6).
8. Only `$programme-import` writes the sidecar, its revision copies, and the md file —
   consuming skills read them (Pattern 15 rule 7).

---

## Related Skills

- `$asbuilt-programme` — actual timing vs this baseline
- `$delay-analysis` — cites critical-path flags from this baseline
- `$ce-quotation` — the two-programme method for time-impact quotations
- `$programme` — milestone forecasting against the imported baseline
- `$programme-compare` — diffs revisions saved by this skill's history
- `$contract-profile` — Accepted Programme status and Contract Data for Step 4 typing
