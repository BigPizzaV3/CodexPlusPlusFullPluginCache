# Visible progress and continued delivery

After an authorized start, keep following the same job through translation, host continuity repair (unless opted out), QC and export. Do not end the turn with only “started”, “still processing” or a promise to notify later while the worker is active. Use interim progress messages and continue polling. Respect a user pause/cancel request. If the host actually interrupts or cannot continue, state the exact job and unfinished step, retain successful work and resume that job next turn; never promise a backend-triggered new chat message, start duplicate jobs or schedule a job-specific reminder.

## Read actual evidence

`suba_translate` may return top-level `progress`. Subsequent `suba_get_job` returns `stages.translate.progress`, the stage status, and available `translation_activity` events. Use the latest returned fields, not wall-clock estimates. Activity phases are translating, alignment, summarizing, summary_ready/summary_skipped, terminology, echo and complete. `completed` and `total` refer to translation batches; `batch` is the batch being processed. Only calculate a percentage when total is positive and counts are valid.

Display a short progress update at start and on a meaningful phase/batch change, or after a reasonable interval while work is slow. Include the current step, real counts and the remaining major steps. Do not repeat pricing, whole job IDs, technical disclaimers or large configuration tables on every update. Respect requests not to reveal plot summaries. An activity message is progress evidence, not permission to print its story summary.

Show completed batches as `completed/total (floor(100*completed/total)%, translation batches only)`. That is neither the current model request's internal token progress nor overall delivery completion. A single 100-cue batch has no measured within-batch percentage: show “Batch 1/1 is translating; waiting for the model response”, not an invented increasing percentage. Unknown total means “preparing” or the actual phase, never an invented 0%.

Even at 100% translation batches, terminology/echo checks, host review, QC and export may remain. Never label overall progress 100% until the actual final artifact is available; there is no measured overall percentage across those different operations. For model calls without granular progress, show the phase and last successful status check rather than a fabricated bar, ETA or stall diagnosis. Tool timeouts are not proof of job failure; recheck the same job before deciding.

## Keep the view small

Use a few plain lines or a compact checklist, not ornamental cards/tables or nonfunctional buttons. Derive each state from tools/journal:

- Input/rules: complete only when the upload and validation actually succeeded.
- Translation: actual phase and batch counts. Expose alignment, summary, terminology and echo substeps when active; summary_skipped is a disclosed gap, not a completed successful check.
- Continuity review: not started / running / complete / opted out; include actually reviewed cue coverage when recorded. Merely fetching cues is not evidence all cues were reviewed. Saved corrections are a separate count.
- QC: not started / running / needs review / failed / passed for the checks actually run. Show partial/unsupported coverage honestly; preserve draft access.
- Export: pending / final artifact ready, with the actual delivery or review-draft label and link.

Example only (replace every count/state with actual returned evidence):

> Translation batches: 3/8 complete (37%, batches only).
> Current: translating batch 4/8.
> Next: terminology/echo checks → continuity review → QC → export.

For a one-batch job:

> Current: translating batch 1/1; no within-batch percentage is available.
> Next: terminology/echo checks → continuity review → QC → export.

If queued, show actual ahead/position fields, do not show translation percentage or promise an ETA, and use the parent's slower polling/cancellation flow. Keep phase updates as commentary while working and return the actual deliverable (or retrievable problem draft with concrete remaining issues) at the end.
