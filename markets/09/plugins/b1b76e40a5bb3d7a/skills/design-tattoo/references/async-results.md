# Asynchronous result handling

`start_tattoo_session` creates a guest session with `sessionKey` and `expiresAt` without login. Reuse a valid session in the current task; it expires after seven days. `generate_tattoo_design` returns a durable snapshot. `get_tattoo_generation` reads it; the status tool does not finalize artwork. Keep the original session key, job ID, and request key in the current task so retries, refinements, and resumes target the same session and attempt. A session key grants access to that session's private artwork; pass it only in tool arguments, never in prose, links, or telemetry.

| State | User-visible meaning | Action |
| --- | --- | --- |
| `queued` | Waiting to begin | Bounded status reads or actual continuation page |
| `processing` | Creating the concept | Bounded status reads or actual continuation page |
| `preparing` | Preparing the result | Bounded status reads or actual continuation page |
| `ready` with asset | Artwork available | Present real asset and continuation |
| `ready` without asset | Incomplete result | Say artwork could not be retrieved; do not claim completion |
| `failed` | Attempt stopped | Report supplied error, stop polling; do not automatically start another job |

In a headless conversation, perform at most three status reads per response and spend at most 30 seconds waiting. If the client supports waiting, respect `retryAfterMs` and increasing backoff; if waiting is unavailable or the bound would be exceeded, return the pending state instead of immediate repeated calls. Stop on a terminal state or a non-transient error. Do not use shell or networking helpers to work around unavailable MCP tools.

If pending, show the actual returned `continuationUrl`, describe its actual state (waiting, creating, or preparing), and explain that the user can open the page or ask to check this concept again. Do not promise an unsolicited completion notification. A later check resumes `get_tattoo_generation` with the existing `jobId` and its original `sessionKey`; if context no longer has either value, explain that the original session cannot be resumed rather than guessing or starting a fresh job.

On a missing, expired, or invalid session, report the actual error. A new session cannot recover the prior session's private jobs or designs, and a status check never starts another session or generation. A later explicit request for a new concept may start a new session after the prior one expires. On an idempotency conflict, do not replace the request key to force the same attempt through; resolve the mismatched inputs. Report service limits or safety failures as returned. The continuation capability is functional access: keep it out of analytics, unrelated URLs, and external messages.
