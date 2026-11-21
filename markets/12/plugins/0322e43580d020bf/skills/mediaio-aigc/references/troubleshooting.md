# Errors

| Code | Response |
| --- | --- |
| `AUTH_REQUIRED`, `AUTH_EXPIRED`, `AUTH_UPSTREAM_EXPIRED` | Resolve authorization before continuing |
| `AUTH_FORBIDDEN` | Stop access to this resource; another user's task or file is not allowed |
| `INVALID_PARAMETER` | Follow the current tool schema; unknown fields and out-of-range settings are rejected |
| `CAPABILITY_NOT_FOUND` | The selected release-declared model may be unavailable or its contract may have drifted; do not dynamically discover a substitute |
| `CREDIT_INSUFFICIENT`, `PLAN_REQUIRED` | Explain current unavailability neutrally and stop; no transaction suggestions or automatic fallback |
| `CREDIT_CHANGED` | A user-requested optional amount guard no longer matches; do not replace it and retry silently |
| `REQUEST_IN_FLIGHT` | Keep the same identifier and inputs; do not initiate another task |
| `RESULT_UNKNOWN` | Never resubmit automatically. Inspect recent task pages and timestamps with `list_generations`; if inconclusive, report uncertainty |
| `UPLOAD_NOT_READY` | Verify that the bytes arrived via the required PUT before completing |
| `UPLOAD_EXPIRED` | A new upload ticket may be needed; do not reuse an expired signature |
| `RATE_LIMITED`, `UPSTREAM_UNAVAILABLE` | Follow retryability while preserving task idempotency and avoiding additional submissions |

A failing terminal task is not evidence of a refund. Do not promise zero cost or a refund without a verified settlement record. Do not expose internal tokens, signed upload URLs or unrelated account data in diagnostics. Refresh an expired result through task lookup; never hand-edit signatures.
