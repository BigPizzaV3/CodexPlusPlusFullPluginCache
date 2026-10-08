---
name: crisphive-emergency-dispatch
description: Handle urgent field-service work with Crisphive — raise a job's priority, find emergency-capable technicians ranked by ETA, and preview then commit a cascade reschedule that safely pushes lower-priority appointments to make room. Use when the user reports an emergency, an urgent job, an SLA at risk, or asks to move or reshuffle scheduled jobs.
---

# Emergency dispatch & rescheduling with Crisphive

Crisphive schedules by a four-level priority model: `p0` (emergency,
interrupt-driven) > `p1` (top, may carry an SLA deadline) > `p2` (standard,
the default) > `p3` (deferrable). Only a `p0` may displace other jobs.

All `start_at` / `sla_deadline` values below are BUSINESS-LOCAL naive
datetimes (`2026-08-04T14:00:00`, no timezone offset) and must be in the
future.

## Environments: sandbox vs production

This skill works identically in BOTH environments — same tools, same fields,
same responses. The credential decides which one you are in:

- **Sandbox** — API key `chsk_test_…`, or an OAuth connection authorized from
  a sandbox dashboard session. Displacements here move only isolated test
  data and notify nobody. Rehearse an emergency flow here first when
  possible.
- **Production** — API key `chsk_live_…`, or an OAuth connection authorized
  from a live session. A committed cascade MOVES REAL customers'
  appointments and the platform notifies them immediately.

You cannot switch environments with a parameter; reconnect with the other
credential. **In production, never call `commitEmergencyReschedule` or
`commitJobRequestMove` without showing the user the full preview (every
displaced job) and getting explicit approval.**

## Raising priority

- `updateJobPriority` with `priority` (required) and optional `note`.
  Escalate to `p0` only for true emergencies (safety issue, no heat in
  winter, active leak) — `p0` work is allowed to push other customers.
- For urgent-but-not-emergency work use `p1`, optionally with `sla_deadline`
  to arm automatic escalation as breach risk grows.

## The emergency insert flow (ALWAYS preview before commit)

1. **Candidates** — `listEmergencyCandidates` with `emergency_job_id`,
   `mode`, and the desired `start_at`. `mode` is the cascade style the
   preview assumes: `overtime` (displaced jobs stay same-day; the technician
   works late) or `next_day` (overflow rolls to the next working day).
   Returns technicians ranked by ETA with per-candidate feasibility.
2. **Preview** — `previewEmergencyReschedule` with the SAME
   `emergency_job_id`/`mode`/`start_at` plus the chosen `technician_id`.
   Optional `displacement_mode`: `reschedule` (default — displaced jobs move
   to new times) or `reassign` (displaced jobs keep their times on alternate
   technicians when possible). **Nothing is persisted by a preview.** The
   response lists exactly which jobs move and to when.
3. **Approve** — show the user the emergency slot AND every displaced job.
   Get explicit approval.
4. **Commit** — `commitEmergencyReschedule` with the SAME
   `emergency_job_id`/`mode`/`start_at`/`technician_id`/`displacement_mode`
   as the preview, plus:
   - `expected_move_ids`: echo the displaced job IDs the preview returned
     (both `days[].moves[].job_id` and `reassignments[].job_id`) — the commit
     fails safe if the schedule drifted since the preview.
   - `emergency_expected_version`: the previewed job's version fence.
   - An `idempotency_key`.
   Displaced customers are notified automatically by the platform — do not
   message them yourself.

## Moving a single job (dispatch-board move)

- `previewJobRequestMove` with the job `id`, `start_at`, `technician_id`
  (the target technician — pass the current one for a time-only move) and
  `mode` (`overtime` | `next_day`, for any jobs the move displaces). Read the
  hard blocks and warnings it returns.
- Then `commitJobRequestMove` with the same fields plus `expected_move_ids` /
  `expected_version` from the preview and an `idempotency_key`. Never commit
  a move that was not previewed.
- Landing on an occupied slot or in the past is rejected — offer the
  preview's alternatives instead.

## Constraints the engine enforces (do not fight them)

- Multi-day jobs and multi-person crew jobs are frozen anchors for the
  emergency cascade — they are never pushed, and a crew job cannot itself be
  the emergency insert (the API rejects it).
- In-progress jobs (the technician already started) cannot be moved.
- Version fences (`expected_version` / `emergency_expected_version` /
  `expected_move_ids`) exist to catch concurrent edits: on a conflict,
  re-read with `getJobRequest`, re-preview, and try again — never bypass by
  omitting them after a conflict.

## Reporting back

After any commit, read `getJobRequestTimeline` for the emergency job and
summarize: who is coming, when, and which other appointments moved. In live
mode remind the user that affected customers have been notified
automatically.
