# Programme acceptance grounds and indicative-run policy

Loaded by Mode 1 (Health Check), Mode 4 (Revision Review), Mode 5 (32.2 Submission Pack), and
whenever an indicative engine run is cited. Full policy prose — the workflow.md body carries only
the short summary and a pointer here.

## Mode 1 — Programme Health Check, full detail

- **Submission currency** — last revision submitted vs the clause 32.2 interval in Contract Data
  (or the profile's amended interval). Data date freshness: a data date months behind today is
  itself a finding.
- **Acceptance position** — is there an Accepted Programme at all? If the first programme was
  never accepted, state the 25% PWDD sanction (NEC3 50.3 / NEC4 50.5). If a submission is
  awaiting response, state the PM's two-week window and, NEC4 only, the 31.3 notify-the-failure
  → one-further-week deemed-acceptance route (NEC3 has no programme deemed acceptance).
- **Realism per the 31.3 grounds** — the only rejection grounds are: not practicable, missing
  information the contract requires, not representing the Contractor's plans realistically, not
  complying with the Scope/Works Information. Check what the imported data can evidence: TRA
  shown per activity (absent or implausible TRA on critical activities is a recognised 31.3
  rejection ground), actuals in the past, remaining durations plausible against Gather-recorded
  output rates (`progress`).
- **CE presentation** — notified/ongoing CEs move **planned Completion** only; the **Completion
  Date** moves only when a CE is implemented (NEC4 32.1 dropped "implemented" so all CE effects
  are shown; under NEC3 non-implemented CEs still enter via realistic remaining work). Flag a
  programme that moves the Completion Date for an unimplemented CE.
- **Reverse direction** — an *incoming* subcontractor programme is reviewed against the same
  31.3 grounds before acceptance, plus interface dates against your own programme's mapped
  activities.

## Mode 4 — Revision Review, full detail

- **31.3 grounds against the delta** — does the new submission remain practicable, does it still
  carry the information the contract requires, does it still represent the Contractor's plans
  realistically, does it still comply with the Scope/Works Information — each judged against
  what actually moved, not restated wholesale from Mode 1.
- **Float and TRA erosion** — report any reduction in total float on critical/near-critical
  activities and any narrowing or disappearance of TRA between the two stored revisions (both
  are STORED-vs-STORED comparisons — never recomputed) with the delta stated in days.
- **CE register cross-reference** — for every activity showing erosion, check the CE register
  (or this conversation's CE-/QT- refs) for a compensation event that would explain it; state
  "no corresponding CE found" plainly where erosion has no matching entry — this is itself a
  31.3-relevant finding, not a gap to smooth over.

## Mode 5 — 32.2 Submission Pack, full detail

- **Progress narrative per mapped activity** — drawn from Gather records over the period, one
  line each.
- **Dormancy evidence** — mapped tasks with no recorded work in the period, per Mode 3.
- **CE schedule with planned-Completion effects** — every live CE this period, cross-referenced
  to its ce-quotation Step 4 movement where one has been run in this conversation.
- **TRA statement from stored values** — TRA as carried in the imported baseline, never
  recomputed.
- **Possession commentary** where tagged — possession-dependent activities per Pattern 15's
  import-time tagging, cross-referenced against `$access` where available.

Emit alongside the narrative pack the **machine-readable actuals table** (the same table Mode 3
produces) so the planner can apply it directly, and note the **round-trip update file**
`$programme-create`'s writer will produce once it ships — until then, the actuals table
is the hand-off artefact.

## Indicative Analyses policy

Where a deterministic recalculation is genuinely useful (float/TRA erosion that Mode 4's STORED
comparison can't resolve on its own, or a what-if the user explicitly asks for), the Advisor may
cite `$programme-impact` runs — **always** with the Pattern 15 INDICATIVE banner and that
file's self-check reproduction %, **never** blended into a STORED table or narrative without
each figure's class being visible (Pattern 15 rule 2). An indicative run never substitutes for,
or upgrades to, an Accepted Programme position.

**Recovery log.** Report `programme/recovery-log.md` (Pattern 15 rule 8) alongside any indicative
or update-pack output: the measure, the **user-stated** expected saving (never computed by this
agent), and actual progress against it from Gather records. This agent never invents or computes
a recovery saving — only reports the user's stated target against what the records show.
