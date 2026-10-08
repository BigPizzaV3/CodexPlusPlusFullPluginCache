# Verification boundaries

The packaged unit tests prove local cache behavior with synthetic identities. They do not prove native voice, host permissions, screen visibility, user consent, or a public release.

A live acceptance run must:
1. Configure the real coordinator and an existing owner, each host-qualified.
2. Ingest a supported native wait snapshot, preserve the returned cursor, then observe unchanged message suppression.
3. Add one genuine decision with its source ID and exact scope. Reserve it once.
4. Promote its actual preview through the supported host tool in the coordinator conversation. Record queued placement separately from visible evidence.
5. Present the question and receive a genuine user message. Verify its source and scope; never use a fixture as an approval.
6. Ask the helper for a dispatch packet, send once to the stored owner, then record the actual send result. An uncertain result must be reconciled before retry.
7. Observe the correct owner's acknowledgment through changed native state. Reopen the cache and confirm a duplicate answer cannot resend.
8. Install the package in a fresh supported host context and confirm skill discovery without restarting an active voice conversation. The supported app-server `skills/list` method with `forceReload` verifies the native registry without a model call; a short model-facing catalog is weaker evidence.
9. Inspect a release archive's exact file list and scan for private state, credentials, personal paths, and user task identifiers. Confirm a real intended distribution destination before publishing.

No guarantee of exactly-once external execution is possible without host-supported idempotent sends. Unicycle favors withholding an uncertain retry over duplicate instructions. The durable cache records intent and receipts; it cannot authenticate the user or force native display.
