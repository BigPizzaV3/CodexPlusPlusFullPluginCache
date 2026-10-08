---
name: reliable-dashboard-recovery
description: Resume plugin dashboard uploads and scans safely after stalls, timeouts, or browser interruptions.
---

# Reliable Dashboard Recovery

Use this skill whenever a plugin upload, dashboard navigation, validation save, or asynchronous scan appears stuck.

## Checkpoint record

Before every dashboard mutation, record:

- target plugin ID and whether it is an update or a new plugin;
- package SHA-256, version, and local ZIP path;
- current dashboard URL and submission ID when visible;
- stage: upload, metadata, prompts, skills, scan, compliance, or submission;
- retry count and last observed status.

Never resume an update if the target plugin ID cannot be verified. Never use a new-plugin flow as an implicit substitute for an update flow.

## Recovery loop

1. Inspect the current page and status without clicking anything.
2. Wait using bounded backoff: 2, 4, 8, 15, 30, then 60 seconds.
3. Refresh or reopen the same submission URL and inspect again.
4. Check the plugin list for an already-created draft with the same package name, version, or package hash.
5. Resume the next incomplete stage. Do not repeat completed stages.
6. Retry at most three times per stage. If the same failure repeats, classify it as a browser, permission, authentication, or platform issue and request the smallest required user action.

## Safe retry rules

- An upload button click is not evidence of upload completion.
- A disabled button is not evidence of failure.
- An unchanged `Uploading` or `Scanning` label requires polling and a fresh inspection, not an immediate duplicate upload.
- If a draft exists, edit or resume that draft rather than creating another one.
- Keep the compliance attestations and final publish/submit click user-confirmed.

## Completion evidence

Report only visible evidence: plugin ID, version, submission ID, terminal scan status, issue list, and whether the final submission remains pending. If any of these are unavailable, say exactly which evidence is missing.
