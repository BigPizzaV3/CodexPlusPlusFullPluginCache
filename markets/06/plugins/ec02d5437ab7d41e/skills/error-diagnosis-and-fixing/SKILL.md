---
name: error-diagnosis-and-fixing
description: Diagnose and correct conversion, validation, upload, scanning, and submission failures.
---

Classify each issue as source extraction, instruction quality, manifest, asset, JSON, package, dashboard validation, scanning, policy, or browser-state failure. Reproduce locally where possible, make the smallest scoped fix, rerun validation, and keep an issue ledger with observed error, change, verification, retry count, checkpoint, and remaining status. Do not retry blindly when the failure is authentication, missing user input, or a platform-side outage.

For recoverable browser or dashboard stalls, use this controller: capture state -> wait with backoff -> refresh/reopen -> verify draft identity -> retry only if the operation is confirmed failed. Preserve the package hash and existing plugin ID across retries. A timeout alone is inconclusive. Ask for user permission only for a missing browser/file/account permission or the final public attestation; do not ask the user to repeat work already completed.

Use this remediation order:

1. Compare the visible dashboard error with the exact local manifest, skill, asset, or ZIP entry.
2. Fix the local source rather than only changing a dashboard field when the package is the cause.
3. Revalidate the complete package and increment the version before reuploading.
4. Wait for upload processing and skill scanning to finish; `Uploading` and `Scanning` are asynchronous states, not failures.
5. Reinspect the dashboard after waiting and record the final visible result.

Never claim upload success from a click alone, and never retry an unchanged package against an unchanged error.
