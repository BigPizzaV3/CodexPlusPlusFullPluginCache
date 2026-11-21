# Scoreboard MCP annotation justifications — 21 October 2026

Generated from the same explicit boolean descriptors and justifications served by tools/list. All 17 tools set readOnlyHint, destructiveHint, idempotentHint and openWorldHint. No hints are null or inferred from omitted properties.

This revision corrects destructiveHint for recording scores, undoing scores and accepting scorer invitations. Their descriptions now disclose overwritten state and irreversible side effects. Scoring/undo/round/clock operations remain confined to a bounded private game. Creating a share is open-world because its bearer capability can expose data outside the connected account.

Sources: [OpenAI annotation guidelines](https://developers.openai.com/plugins/plugin-guidelines#correct-annotation) and [remote MCP review requirements](https://developers.openai.com/plugins/deploy/app-review). The rejection email requests justifications; this document supplies them even though the current guidelines no longer universally require them.

Implementation: src/lib/mcp/tools.ts and src/lib/sessions/service.ts. Role, scope, version/round and retry guards are enforced by the server, not by annotations. Idempotent means no additional intended operation effects for the same inputs/account, not identical response data or guaranteed success after permissions change.

## open_scoreboard

- **readOnlyHint: true** — Returns a connection prompt, the caller's saved-session list, or an authorized game's current view. Opening the dashboard creates no game and performs no write.
- **destructiveHint: false** — Only reads existing game data; does not change scores, membership, history or access.
- **idempotentHint: true** — Repeated calls have no additional state effects; displayed data can reflect changes made by other members.
- **openWorldHint: false** — Confined to the connected account's owned or joined games. The UI is a static server resource and does not fetch arbitrary destinations.

## get_scoreboard_presets

- **readOnlyHint: true** — Computes a response from the built-in scoring preset catalog and team limit without writing data.
- **destructiveHint: false** — No state change, deletion or external action occurs.
- **idempotentHint: true** — Repeated calls return the same configured catalog without side effects.
- **openWorldHint: false** — Uses a fixed application catalog, with no web search or external destination.

## list_scoreboard_sessions

- **readOnlyHint: true** — Queries games where the authenticated account is a member; pagination only reads the authorized cursor and next page.
- **destructiveHint: false** — Does not create, update, delete or publish any session.
- **idempotentHint: true** — Repeated reads have no state effects; results may reflect other members' changes.
- **openWorldHint: false** — The query is bounded by the caller's membership in this application's private game store.

## create_scoreboard_session

- **readOnlyHint: false** — Persists a new private game and its initial history entry, with the caller as owner.
- **destructiveHint: false** — Purely additive: creates a new game without replacing any existing game, changing existing access, sending messages or publishing data. A conflicting operation ID is rejected rather than overwritten.
- **idempotentHint: true** — The account ID and operationId deterministically identify the game. Identical retries return it without creating another game or history entry; different arguments with the same ID are rejected.
- **openWorldHint: false** — Creates only a private game for the connected account. No external recipient, destination or public link is created.

## get_scoreboard_session

- **readOnlyHint: true** — Reads an existing game after checking the caller's current membership and returns its filtered view.
- **destructiveHint: false** — Does not mutate the game, clock, history or membership.
- **idempotentHint: true** — Repeated reads do not change state; other members can independently update the returned view.
- **openWorldHint: false** — Limited to a specifically authorized private Scoreboard game in this application's database. No arbitrary URL, recipient, external service or device can be targeted.

## update_scoreboard_team

- **readOnlyHint: false** — Adds, removes or updates a team and records the operation in game history.
- **destructiveHint: true** — Remove permanently deletes a roster entry with no restore operation; update overwrites name/color. Owner-only, current-version guarded, with add/remove prohibited after scoring starts or the first round closes. Adding a team alone is additive, but the same tool exposes destructive modes.
- **idempotentHint: true** — For the same authenticated account, identical arguments and operationId reuse an atomic operation receipt without repeating the change. Reusing the ID with different arguments is rejected. Authorization is rechecked; a retry after access removal can fail without a further write. A fresh operationId requests a new action.
- **openWorldHint: false** — Limited to a specifically authorized private Scoreboard game in this application's database. No arbitrary URL, recipient, external service or device can be targeted.

## record_scoreboard_score

- **readOnlyHint: false** — Updates a team's current score, permanently sets the roster lock and appends a score action and retry receipt.
- **destructiveHint: true** — Overwrites the current score and can subtract points. The first successful score permanently prevents roster additions/removals; undo does not clear this lock. Owner/editor only, expected-round guarded, with score bounds checked atomically. Point compensation alone does not make the operation non-destructive.
- **idempotentHint: true** — For the same authenticated account, identical arguments and operationId reuse an atomic operation receipt without repeating the change. Reusing the ID with different arguments is rejected. Authorization is rechecked; a retry after access removal can fail without a further write. A fresh operationId requests a new action.
- **openWorldHint: false** — Limited to a specifically authorized private Scoreboard game in this application's database. No arbitrary URL, recipient, external service or device can be targeted.

## undo_scoreboard_score

- **readOnlyHint: false** — Changes the team score, updates the original score action's undoneBy marker and appends a compensating history action.
- **destructiveHint: true** — Overwrites the current score and permanently marks the selected action as undone. No operation restores that action's undo eligibility; the roster remains locked. Only an un-reversed score in the current active round can be targeted, with owner/editor authorization, current-version and score-range checks.
- **idempotentHint: true** — For the same authenticated account, identical arguments and operationId reuse an atomic operation receipt without repeating the change. Reusing the ID with different arguments is rejected. Authorization is rechecked; a retry after access removal can fail without a further write. A fresh operationId requests a new action.
- **openWorldHint: false** — Limited to a specifically authorized private Scoreboard game in this application's database. No arbitrary URL, recipient, external service or device can be targeted.

## finish_scoreboard_round

- **readOnlyHint: false** — Banks scores, updates cumulative totals and round wins, pauses the stored clock, then advances the round or finishes the game.
- **destructiveHint: true** — Permanently closes the round against further scoring/undo; intermediate rounds reset current scores and the final round closes the game. No reopen operation exists. Requires owner/editor access and the current version; instructions require explicit intent to close the round.
- **idempotentHint: true** — For the same authenticated account, identical arguments and operationId reuse an atomic operation receipt without repeating the change. Reusing the ID with different arguments is rejected. Authorization is rechecked; a retry after access removal can fail without a further write. A fresh operationId requests a new action.
- **openWorldHint: false** — Limited to a specifically authorized private Scoreboard game in this application's database. No arbitrary URL, recipient, external service or device can be targeted.

## get_scoreboard_results

- **readOnlyHint: true** — Reads the authorized game and computes standings from stored current and completed-round scores.
- **destructiveHint: false** — No scores, results or history are changed by computing the view.
- **idempotentHint: true** — Repeated reads have no additional effects; totals may reflect independent game updates.
- **openWorldHint: false** — Limited to a specifically authorized private Scoreboard game in this application's database. No arbitrary URL, recipient, external service or device can be targeted.

## get_scoreboard_history

- **readOnlyHint: true** — Checks game membership, then reads existing action records in pages of 50. Cursor validation is read-only.
- **destructiveHint: false** — Does not remove, mark or update any history record.
- **idempotentHint: true** — Repeated pagination reads have no state effects.
- **openWorldHint: false** — Limited to a specifically authorized private Scoreboard game in this application's database. No arbitrary URL, recipient, external service or device can be targeted.

## create_scoreboard_share

- **readOnlyHint: false** — Adds an expiring spectator capability or single-use scorer invitation and a history/receipt record.
- **destructiveHint: false** — Additive creation of a new revocable capability; it does not revoke/overwrite existing links or members, send a message, or submit data to a recipient. The owner can revoke an unused invitation or spectator link. The subsequent join operation is separately marked destructive.
- **idempotentHint: true** — An atomic operation receipt preserves the first generated token and link. Same-account retries with identical operationId and arguments return that original capability, not an additional link. Different arguments with the same ID are rejected.
- **openWorldHint: true** — True because a spectator bearer link can disclose game details to anyone holding it outside the connected account, and an invitation can admit another authenticated account. No message is sent automatically. Owner-only creation; links expire and can be revoked.

## get_scoreboard_access

- **readOnlyHint: true** — Owner-only read of existing member roles and link metadata; never returns credentials or stored link tokens.
- **destructiveHint: false** — Listing access does not grant, revoke or alter access.
- **idempotentHint: true** — Repeated reads have no state effects; the owner can independently change access.
- **openWorldHint: false** — Limited to a specifically authorized private Scoreboard game in this application's database. No arbitrary URL, recipient, external service or device can be targeted.

## revoke_scoreboard_share

- **readOnlyHint: false** — Marks an existing game link revoked and appends an access history action and receipt.
- **destructiveHint: true** — Permanently invalidates the selected spectator link or unused scorer invitation, with no un-revoke operation. Owner-only and link-to-game matching enforced. Revoking a claimed invitation does not remove its existing member; member removal is a separate tool.
- **idempotentHint: true** — For the same authenticated account, identical arguments and operationId reuse an atomic operation receipt without repeating the change. Reusing the ID with different arguments is rejected. Authorization is rechecked; a retry after access removal can fail without a further write. A fresh operationId requests a new action.
- **openWorldHint: false** — Limited to existing capability records for one owner-authorized game. It cannot target arbitrary external links, recipients or services; it only withdraws access in this application's store.

## update_scoreboard_member

- **readOnlyHint: false** — Overwrites a non-owner member's role or removes membership and records the change.
- **destructiveHint: true** — Can revoke editing permission or all game access. Removing a joined scorer does not restore their consumed invitation. Owner-only, current-version guarded, and cannot change/remove the owner.
- **idempotentHint: true** — For the same authenticated account, identical arguments and operationId reuse an atomic operation receipt without repeating the change. Reusing the ID with different arguments is rejected. Authorization is rechecked; a retry after access removal can fail without a further write. A fresh operationId requests a new action.
- **openWorldHint: false** — Only changes an existing member in the owner's bounded private game; cannot invite arbitrary new recipients or change permissions in another service.

## join_scoreboard_session

- **readOnlyHint: false** — For a new member, adds the authenticated account as an editor of the invitation's game, records history and marks the invitation claimed.
- **destructiveHint: true** — Permanently consumes a single-use invitation. Removing the joined member does not make the token usable again. Validity, expiry, revocation and a 32-member limit are enforced; existing members return without consuming a new invitation.
- **idempotentHint: true** — The token's claimedBy marker is an atomic retry guard. Repeating with the same token/account while still a member returns duplicate without another membership/history write. After removal, expiry or revocation it fails without a write; another account cannot reclaim it.
- **openWorldHint: false** — Accepts only an application-issued capability for one specific private game. It cannot access public/open-ended entities, invite an arbitrary third party or target an external service.

## control_scoreboard_timer

- **readOnlyHint: false** — Updates elapsedMs and runningSince fields in the saved game and appends an operation history entry/receipt.
- **destructiveHint: true** — Reset permanently discards elapsed time; no restore action exists. Start/pause also overwrite clock state. Requires owner/editor membership, an active game and the current version.
- **idempotentHint: true** — For the same authenticated account, identical arguments and operationId reuse an atomic operation receipt without repeating the change. Reusing the ID with different arguments is rejected. Authorization is rechecked; a retry after access removal can fail without a further write. A fresh operationId requests a new action.
- **openWorldHint: false** — False: this is only timestamp/elapsed-millisecond bookkeeping in the bounded private game document. It controls no physical device, external clock service, scheduler, background job, message or arbitrary endpoint. Other members read the same stored fields.
