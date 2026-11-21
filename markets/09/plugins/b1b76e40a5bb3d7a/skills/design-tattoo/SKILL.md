---
name: design-tattoo
description: Generate and refine original tattoo concepts with Tatty without signing in, preserve private design versions, and preview or download the completed artwork.
---

Create an original tattoo concept from the user's brief or refine their own Tatty concept. Explicit user instructions take priority. Do not activate this workflow for inspiration alone, unrelated images, tattoo health questions, or artist bookings.

Use the supplied theme, style, placement, and size in a short editable brief. Ask only when a missing detail changes the requested result. Proceed directly when the user already knows what they want; discovery is optional. Read the live tool schema for accepted settings. Do not imply artist-approved tattooability or ready-made stencil quality.

No plugin workflow requires an account or sign-in. Before the first generation, call `start_tattoo_session` automatically unless this task already has a valid returned guest session. Retain its `sessionKey` and `expiresAt`; the session lasts seven days. Pass that same `sessionKey` in `generate_tattoo_design`, `get_tattoo_generation`, and any `get_tattoo_design` call for artwork created in that session. Public discovery needs no session. Keep the key only in tool arguments and task context: never expose it in prose, code blocks, links, external messages, or telemetry, and never ask the user to enter it.

Use `generate_tattoo_design` for each requested concept. A direct request to generate authorizes that private generation. The server scopes results to the guest session and enforces its limits. Report session, moderation, or service-limit failures as returned; do not replace a session to evade a limit or suggest buying upgrades.

Assign one unique `requestKey` to each new requested output and retain it with the canonical inputs and original `sessionKey`. Retry the same attempt at most once for a transient transport failure, using both of those keys and identical inputs. A user-requested new variation uses a new request key within the same session. To refine, use the returned session-owned `designId` as `parentDesignId`, preserve the prior version, and carry forward the settings the user keeps. If the intended parent has a known pending `jobId`, check that job using its original session and wait for a ready design ID before refining; keep the requested edit in context without starting a substitute job. If no parent ID or job is available, retrieve or clarify the intended concept; do not invent an ID.

Retain the returned `jobId` with its original `sessionKey` and use `get_tattoo_generation` to check that job. A status request or resume never creates another session or generation. Follow [asynchronous result handling](references/async-results.md) for states, bounded polling, and failures.

Show the artwork only when the service reports `ready` with a real image asset. Return the editable brief, actual result image or supported image content, and the actual continuation URL. Call the result an original digital concept for a tattoo artist to refine. Browser preview and artwork download work without signing in; preserve the returned options and offer the Tatty app download route when useful. Do not claim automatic guest import into the current app, fabricate download links or deferred install behavior, or claim successful try-on. Keep pending results useful with their real status and continuation page.

Generation remains private to its guest session. A generation or refinement request does not authorize public posting, community submission, sharing a session key, arbitrary uploads, or use of body photographs.
