---
name: sendwhale-public-api
description: Integrate SendWhale from server code using the repository Node SDK, hosted MCP, local Deno adapter or existing transactional-send endpoint, with real current authentication and idempotency contracts.
---

Choose the integration around the actual task:

- An AI client drafting branded emails: hosted MCP at `https://www.gosendwhale.com/mcp`, with browser OAuth and workspace-scoped draft permissions.
- Node/TypeScript backend: the repository `packages/sendwhale-sdk` package builds ESM/CommonJS and declarations. It is not yet an npm-published package. Install its reviewed local archive only when needed and authorized.
- Command-based MCP clients: the repository `mcp/` Deno adapter. Read its README and use a real Supabase user session and publishable key. It has a different credential from hosted OAuth. Do not invent `sendwhale login` or `npx @sendwhale/mcp`.
- Authorized transactional product triggers: POST the project's `/functions/v1/transactional-send` using a purpose-bound workspace `email:send` key. Marketing campaigns use the native campaign review flow.

Read [API contracts](references/contracts.md) before coding. Verify current schemas through the hosted tool catalog, repository SDK types and `https://www.gosendwhale.com/docs/mcp-setup.md`. This skill is not a new endpoint specification. There is no implied `/v1/projects/emails/generate`, claim-code auth, local OAuth CLI, managed-domain purchase or provider export API.

Keep credentials and sends server-side. Preserve tenant scope and consent/suppression status. Add a stable idempotency key for draft saves and transactional delivery. Never automatically repeat an uncertain send with a new key. The SDK returns `{data,error}`; local invalid configuration throws. SMTP acceptance, remote delivery and inbox placement are separate outcomes.

For operating drafts use `sendwhale`. For auditing an existing app's triggers and wiring its backend use `sendwhale-setup`. Report changed files, chosen surface, actual IDs, test results and any unsupported operation clearly.
