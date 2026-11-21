---
name: keep-and-revisit
description: Reopen saved Wildcards works and receipts, inspect card state, export the user's work, or reversibly archive and restore designs and works.
---

Read [the shared contract](../../references/contract.md). Use list_wildcards with the requested designs, works, issued or wallet collection; follow offset pages rather than treating the first twenty as complete. Open one card with read_wildcard, a design with read_wildcard_design, or an authorized work with read_wildcard_work. A private work needs ownership or matching held card_id. Use render_wildcards for the native saved view and replay controls.

Reload restoration and a successful new spend are distinct. Existing receipts preserve the music tempo/pattern at play time. Do not rewrite a receipt after revising the design or work. A spent card stays spent while its saved result remains replayable. No currency, monetary value, resale or guaranteed human fulfillment exists.

Use export_wildcards on request. Its JSON omits authentication and private invitation keys; it does not publish or send the result. Use archive_wildcard with current revision and archived=true or false for requested reversible archive/restore. Archived works reject new plays without spending cards; existing effects remain. Archiving is not permanent erasure. Refer permanent account-data removal to the published support page; do not claim a delete was performed.

If a saved object is unavailable, expired or unauthorized, explain its actual error and preserve identifiers for legitimate recovery. Never guess someone else's IDs or keys. Capabilities and limits are available through get_wildcards_info.
