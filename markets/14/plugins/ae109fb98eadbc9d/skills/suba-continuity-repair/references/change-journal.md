# Change journal and delivery

Keep one appendable record per review run in a private host artifact/file. A suggested basename is `{job_id}_continuity_{run_id}`. Do not use this basename as a subtitle input path. If files cannot be created, retain the same information in structured chat output and state that limitation.

Record:

- Job/run ID; base and final revision; original export/snapshot artifact and available hashes.
- Target series/episode/version; actual language evidence; selected references and reasons. For prior episodes record the confirmed file/location or job identity, version, available source/target pair, actual access/read coverage and any skip/decline; distinguish supplied locations from successfully read references.
- Total cues, every reviewed range/page and actual coverage. Store reference cue IDs/time/version where used; missing evidence and excluded materials are explicit.
- Each pending batch's exact revision, idempotency key and request before mutation; status becomes applied only after the returned commit and read-back verification.
- Per edit: cue ID and full start/end time, before lines, proposed lines, saved lines after QC, reason, source and prior-episode evidence, batch key and committed revision. Mark backend-QC edits separately when observable; do not silently attribute them to the host's semantic review.
- Unresolved candidates, missing evidence, conflicts, failed/unknown writes and skipped coverage.
- Actual translation/QC/export/billing states; output artifact; verification performed and its limits.

For multiple revisions of one cue, preserve the sequence and show the original-to-final diff. Never overwrite the original snapshot. A pending change, request timeout or successful tool call without read-back is not a verified saved edit.

The readable log should lead with the applied count and highest-impact changes, then include a table:

`cue/time | original | final saved text | evidence/reason | committed revision/status`

Include unresolved items separately and link reference snapshots where available. Keep client content private. Do not put subtitle snapshots or change journals inside plugin packages, public reports or websites. Service job retention is finite; deliver downloadable artifacts rather than promise indefinite server history.
