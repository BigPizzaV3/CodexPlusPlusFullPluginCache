# GreenOnion Product Images

Plugin package for GreenOnion's Amazon listing-image workflow. GreenOnion is an
independent service and is not affiliated with or endorsed by Amazon.

The deployed MCP endpoint is:

`https://api.greenonion.ai/plugins/amazon-listing/mcp`

The MCP surface exposes read-only requirements and server-authoritative credit
estimation. Its OAuth-protected tools create a nine-slot draft and attach
one to five ChatGPT-provided product photos to that draft. Files are fetched
server-side, size-limited, content-validated, and deduplicated before they enter
the same project storage used by the main Amazon listing UI. Storage URLs are
never returned through the MCP tool result.

New conversations create drafts with `create_amazon_listing_draft_v2`; the
unversioned draft tool remains temporarily available for conversations holding
an older cached schema. That compatibility tool preserves any supplied facts and
preferences, fills omitted fields with AI choices, and normalizes cached quality
settings to fixed 2K without forcing the user to restart the conversation. The
plugin reuses photos, product facts, and preferences already supplied in the
conversation. English and all nine slots are used by default unless the user
requests another language or fewer images.

Analysis produces the complete Product Analysis, exact Design System, and all
nine image slots with image type, full feature list, and enabled state in one
review. The user may revise any value or slot and then confirm the updated
version. After confirmation, the plugin asks one optional open-ended question
for image-specific direction such as exact wording, scene, layout, or visual
direction. It saves only supplied specifics; omitted slots and fields remain AI
choices. Image prompts are generated internally and final image generation
starts without a separate prompt-review or approval turn. Durable request IDs
replay retries without generating or charging twice. Credit details stay out of
the normal workflow and are only mentioned when the connected account cannot
afford the next operation.

Final generation is dispatched as a durable selected-slot job. Separate
read-only tools expose resumable drafts, recent jobs, job progress, a protected
GreenOnion project link, and an eligible short-lived ZIP download; they never
return original upload or storage URLs.

## OAuth resource-server configuration

Production requires all of:

- `CHATGPT_OAUTH_ISSUER`
- `CHATGPT_OAUTH_AUDIENCE`
- `CHATGPT_OAUTH_JWKS_URL`

`CHATGPT_MCP_RESOURCE_URL` optionally overrides the canonical MCP resource URL.
The authorization provider must issue asymmetric JWT access tokens with the
configured issuer and audience and both `amazon_listing:read` and
`amazon_listing:write` scopes. By default, a verified email links an existing
active GreenOnion account or provisions a new Firebase-backed Starter account.
The stable issuer/subject mapping prevents reconnects from granting credits
again. Set
`CHATGPT_OAUTH_USER_ID_CLAIM` when the provider places the Firebase UID in a
namespaced custom claim instead.

See [`docs/CHATGPT_AMAZON_AUTH0.md`](../../docs/CHATGPT_AMAZON_AUTH0.md) for the
Auth0 setup and account-linking runbook.

See [`docs/CHATGPT_AMAZON_CLOUD_TASKS.md`](../../docs/CHATGPT_AMAZON_CLOUD_TASKS.md)
for the durable final-image worker setup.

See [`SUBMISSION.md`](./SUBMISSION.md) for the marketplace listing copy, review
tests, demo-recording script, annotation justifications, and launch gate.

See [`LEGAL_REVIEW.md`](./LEGAL_REVIEW.md) for the counsel-review draft covering
plugin-specific privacy disclosures, terms, and unresolved legal decisions.

See [`PRE_SUBMISSION_AUDIT.md`](./PRE_SUBMISSION_AUDIT.md) for the latest
production, account-access, IAM, and legal-readiness evidence.

For local development, run the GreenOnion backend and connect ChatGPT developer
mode to:

`http://localhost:8000/plugins/amazon-listing/mcp`
