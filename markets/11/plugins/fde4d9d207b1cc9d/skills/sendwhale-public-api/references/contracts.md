# Current integration contracts

Hosted remote MCP is `https://www.gosendwhale.com/mcp`, Streamable HTTP with browser OAuth. Grants bind one workspace, expire and can be revoked. The Node SDK accepts an already acquired hosted access token; it does not handle login or refresh.

`sendwhale_save_email_drafts` accepts `title`, one to twelve `emails` with `name`, `subject`, `html`, an optional short `brief`, optional existing `conversation_id`, and required `idempotency_key`. Its result contains individual campaign `id` values, editor/review URLs, a shared `canvas_url`, `conversation_id`, `status: draft` and `mail_sent: false`. HTML is sanitized on the server. Unknown write outcomes require reconciliation, not a new creation key.

Local Deno MCP uses `SENDWHALE_SUPABASE_URL`, `SENDWHALE_PUBLISHABLE_KEY`, `SENDWHALE_ACCESS_TOKEN` (real user's Supabase session), `SENDWHALE_WORKSPACE_ID`, optional `SENDWHALE_APP_URL`. See repository `mcp/README.md`; hosted opaque OAuth access tokens do not authenticate this adapter.

Transactional HTTP: POST `${SENDWHALE_SUPABASE_URL}/functions/v1/transactional-send`, `Authorization: Bearer` using a server-held workspace API key with `email:send`. Body fields: `to`, `subject`, `html` and/or `text`, required stable `idempotency_key`, optional `workspace_id`, `reply_to`, `from_email`, `from_name`, and `category` (`transactional`, `security`, `system`). The authenticated workspace sender is still checked; arbitrary From does not bypass it. There is no recipient array, template ID expansion or marketing category. Store the returned `operation_id` and status. A 202 pending result or timeout is not a confirmed failure.

The local Node package `packages/sendwhale-sdk` offers `SendWhale` for drafts and `SendWhaleTransactional` for product messages. Its README and TypeScript declarations are authoritative for this release. It is not yet published to npm. Keep unrelated SDK methods from other products out of SendWhale integrations.

## Resolve identifiers and revisions

`get_campaign({campaign_id})` returns `{campaign, html, review_url}`. `update_campaign_draft` takes `campaign_id`, `expected_updated_at`, `subject` and `html`; read `campaign.updated_at` immediately before replacing content. A conflict requires a reread, not an unconditional overwrite. Use a new draft for a sent or locked campaign.

`sendwhale_get_context` returns the brand revision as its top-level `updated_at`. `remember_brand_fact` takes `title`, `detail`, `category` and `expected_updated_at`; valid categories are Brand, Design, Tone, Content, Product, Audience and Company. Its result includes the new memory `id` and revision. It requires owner/admin brand access and is not a safe blind retry. Read context again to confirm the memory before reporting persistence. This operation does not favorite an email.

`list_campaigns`, `list_templates` and `list_audiences` accept `offset` and `limit`; inspect `next_offset` rather than assuming the first page is complete. Audience discovery exposes group descriptions, not subscriber addresses. `create_audience` creates an empty group; it imports and subscribes nobody.

## Workflow surfaces

| Request | Actual SendWhale path |
| --- | --- |
| Generate one email or a series | The assistant authors HTML, then calls `sendwhale_save_email_drafts` once. There is no asynchronous generation endpoint to poll. |
| Bring existing HTML into a draft | Save supplied HTML through the same draft tool; server sanitization may change unsupported markup. |
| Continue an existing series | Read the same user's saved conversation and campaigns; edit individual campaign IDs with their current revisions. |
| Save a lasting brand preference | Use revision-checked brand memory or explicitly requested standing instructions; no favorite API exists. |
| Marketing send, test or schedule | Return native review with `sendwhale_prepare_publish`; the hosted MCP cannot perform these delivery actions. |
| Campaign results | `get_campaign` exposes lifecycle status. Detailed delivery/engagement results live in native campaign reports and Analytics. |
| Subscriber CSV import | Use the native audience import flow, preserving consent and suppression. No hosted contact-import tool exists. |
| Export email HTML to a file | Read `get_campaign` and write its returned HTML to the user's requested local file. This does not upload to a provider or create PNG/PDF screenshots. |
| DNS, domains, provider export or webhooks | Inspect the real app/provider setup and current documented contract. Do not manufacture a tool, public package or REST endpoint. |

Hosted grants use SendWhale's discovered scopes and one approved workspace. Do not request another product's `project:write` or `campaign:write` scopes, or treat the separate transactional `email:send` credential as permission to deliver marketing campaigns through MCP.
