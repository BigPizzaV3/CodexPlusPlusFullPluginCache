## programme-health-check

**Cadence:** Monthly — align to the clause 32.2 revision interval in the contract profile
**Surface:** Desktop
**Prerequisites:** `programme/programme-baseline.md` (from `$programme-import`); `contract-profile.md` optional (the as-amended 32.2 interval); `{{FOLDER}}/routine-state/programme-health-check/last-run.md`
**Priority:** Standard

**Instructions:**
```
Run the Programme Advisor health check (Mode 1) for {{PROJECT}}:

- Data-date freshness: the imported baseline's data date vs this run date. If it is older
  than the 32.2 revision interval (per the contract profile; otherwise 4 weeks, stated as an
  assumption), lead with that — a stale Accepted Programme weakens every CE.
- Submission currency: last revision submitted vs the interval; days until the next is due.
- Acceptance position: anything awaiting the PM's reply, and (NEC4 only) whether the 31.3
  notify-the-failure step is available yet.
- Realism spot checks per the 31.3 grounds: TRA shown on critical activities; no planned
  dates still sitting in the past; remaining durations plausible against recorded run rates.
- CE presentation: notified CEs move planned Completion only — the Completion Date moves
  only via implemented CEs.

Read and update {{FOLDER}}/routine-state/programme-health-check/last-run.md — report only
findings that are new or worsened since last month; if all clear, reply in three lines.
Float and criticality are as stored in the import — never recompute the critical path.
```
