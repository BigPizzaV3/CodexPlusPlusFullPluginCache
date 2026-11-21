# Pattern 15: Programme Baseline (imported from MS Project / P6)

**Canonical caveat (cite this, do not restate it):** the Gather API provides no baseline
programme, logic links, or critical path (CPM) — dates, float, and criticality only exist
where imported from a planning tool, and any recalculation is **INDICATIVE**, never a
substitute for the **STORED** Accepted Programme (see the STORED vs INDICATIVE doctrine below).

The Gather API holds no baseline programme (no planned dates, logic links, or critical path).
Planning tools do. `$programme-import` parses a planning-tool export — **MS Project
MSPDI XML** (File → Save As → XML; `.mpp` cannot be read directly), **Primavera P6 XER**,
**P6 XML**, or **Asta Powerproject's Microsoft Project XML export** (`.pp` cannot be read) — and writes a normalised local cache other skills consume.

**File convention (v2 — sidecar + summary):** row-level data lives in the structured sidecar
`programme/programme-baseline.json`, written ONLY by `scripts/parse_programme.py` (invoked via
`$programme-import`); the human-readable `programme/programme-baseline.md` carries the
provenance block (source filename, format, export/data date, revision, Accepted-Programme
confirmation, parser warnings, **self-check reproduction %**), the headline counts, the
**user-confirmed mapping** between Gather activity names and programme task IDs, and — where
confirmed at import — Key Date / Sectional Completion typing and possession-dependent tags.
**Revisions are versioned, never overwritten:** each import saves
`programme-baseline-<revision>.json` and updates `programme-baseline.json` to the latest; the
md file indexes the revision history (this is what `$programme-compare` diffs).

**The two classes of programme statement — the doctrine every consumer follows:**

- **STORED** — what the export carries: dates, total float, criticality **as computed by the
  planning tool at its data date**. This is the ONLY admissible source for "the Accepted
  Programme says…", and it is never recomputed, adjusted, or blended. Cite as "per the
  imported programme ([revision], exported [date])".
- **INDICATIVE** — output of the deterministic CPM engine (`scripts/cpm.py`: unit-tested in
  CI, stdlib-only, never writes to the sidecar). Every engine result carries the banner
  *"INDICATIVE recalculation performed outside the planning tool — not the Accepted
  Programme; verify in P6/MSP/Asta before relying on it"* and is accompanied by that file's
  **self-check reproduction %** (the engine re-runs the unmodified network and compares
  against stored dates — 100% means the model explains the stored programme; less means the
  file carries calendars/constraints the model lacks, and every indicative figure inherits
  that caveat).

**Rules for consuming skills:**
1. If present and its project matches, use it and cite it (STORED citation form above). If
   the user has not confirmed it as the Accepted Programme, say so wherever contractual
   weight is placed on it.
2. **STORED and INDICATIVE never mix unlabelled.** No table, Gantt, or narrative may blend
   the two classes without each figure's class being visible. "The critical path" with no
   qualifier always means the STORED one.
3. **CPM arithmetic happens only in the engine script — never in-model.** A skill that needs
   a recalculation shells out to `scripts/cpm.py`; if python3 is unavailable, engine-backed
   features degrade with a stated message ("indicative recalculation unavailable — python3
   not found; stored values unaffected") and stored-value features continue.
4. Impact/what-if/63.5 outputs are INDICATIVE dates plus task-level deltas for the planner —
   the planning tool remains the authority, and outputs say so.
5. The Gather↔programme activity mapping is user-confirmed at import; consumers use only
   mapped pairs and list unmapped items separately — never guess a mapping.
6. Absent file → skills state the standard limitation (no baseline/critical-path data; run
   $programme-import) and continue with run-rate/records-only methods.
7. Only `$programme-import` (via the parser) writes the sidecar and md file. A project
   mismatch → ignore it (say so).
8. **Recovery/mitigation log:** `programme/recovery-log.md` — user-maintained (measure, target
   task, expected saving **as stated by the user, never computed**, status); the Programme
   Advisor reports actual progress against it and never invents a saving.
