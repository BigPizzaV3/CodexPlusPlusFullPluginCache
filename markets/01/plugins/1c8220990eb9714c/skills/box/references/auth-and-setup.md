# Auth and Setup

## MCP server auth

### Preferred: official Box plugin

Use the official Box plugin from the product's plugin or connector marketplace by default. Do not ask the user to create an OAuth app or provide a client ID and secret for this path.

1. Follow the official setup guide for the product:
   - [ChatGPT](https://docs.box.com/en/box-mcp/configuring-box-mcp-server/chatgpt)
   - [Codex](https://developer.box.com/guides/box-mcp/integrations/codex)
2. Install or connect Box through that product's app or plugin marketplace.
3. Complete the Box sign-in and authorization flow.
4. Call `who_am_i` to confirm the connection and acting Box user.

If MCP tools do not appear or `who_am_i` fails:

1. Check whether the official Box plugin shows as connected.
2. Use the product's authenticate or reconnect action, then retry `who_am_i`.
3. Confirm third-party plugins or connectors are enabled and that the Box administrator allows the integration.
4. Restart the session only as a last resort.

Do not switch to custom MCP setup merely because the official plugin fails. Continue troubleshooting the plugin unless the user explicitly asks to configure a custom MCP connection.

### Custom MCP with a Box OAuth app

Use this path only when the user explicitly requests a custom MCP connection. Do not offer it as the routine alternative to the official Box plugin.

#### Use an existing OAuth app

If the user already has a Box OAuth 2.0 app:

1. Open it in the [Box Developer Console](https://app.box.com/developers/console).
2. On the **Configuration** tab, retrieve the **Client ID** and **Client Secret**.
3. Add the exact redirect URI shown by the OpenAI product's custom MCP setup screen, then save the app.

Never ask the user to paste credentials into the conversation or store them in a repository.

#### Create an OAuth app

If the user explicitly requested custom MCP and does not have an OAuth app:

1. Open the [Box Developer Console](https://app.box.com/developers/console).
2. Select **Create New App** → **Custom App**.
3. Select **User Authentication (OAuth 2.0)**.
4. Name and create the app.
5. Add the exact redirect URI shown by the OpenAI product's custom MCP setup screen.
6. Save the app and retrieve its **Client ID** and **Client Secret**.

If the enterprise requires app approval, authorize the app through the Box Admin Console before continuing.

#### Configure and authenticate the custom connection

1. Add `https://mcp.box.com` through the OpenAI product's custom MCP settings.
2. Enter the client ID and client secret through the product's protected credential fields.
3. Start the product's OAuth authentication flow and authorize the Box app.
4. Call `who_am_i` to verify the connection and acting user.

## Actor selection checklist

Choose the acting identity before you choose endpoints or debug errors:

- Connected user: use when the product acts on behalf of an end user who linked their Box account.
- Enterprise service account: use when the backend runs unattended against enterprise-managed content.
- App user: use when the product provisions managed Box identities per tenant or workflow.
- Existing token from the platform: use when the surrounding app already resolved auth and passes the token into the Box layer.

Always capture which actor you are using in logs, test output, and the final answer. Many Box bugs are actually actor mismatches.

## Codex-only CLI and REST authentication

This section applies only in Codex. In ChatGPT, use Box MCP and do not check or configure CLI or REST.

For a local smoke test, quick inspection, or one-off verification in Codex, prefer Box CLI before raw REST if `box` is already installed and authenticated.

- Check CLI auth safely with `box users:get me --json`.
- If CLI auth is missing:
  - Fastest OAuth path: `box login -d`
  - Use your own Box app: `box login --platform-app`
  - Use an app config file: `box configure:environments:add PATH`
- Use `--as-user <id>` when you need to verify behavior as a managed user or another actor allowed by the current Box environment.
- Use `-t <token>` only when the task explicitly requires a direct bearer token instead of the current CLI environment.
- For CLI auth guardrails (safe checks, commands to avoid), see `references/box-cli.md`.
- For token-first REST verification, prefer environment-based auth (for example `BOX_ACCESS_TOKEN`) and pass the token via `Authorization: Bearer ...` headers. Avoid printing or echoing token values in logs or command output.

## Codex per-path authentication

Path selection is governed by the `Route The Request` section of `SKILL.md`. This section covers only the authentication work each path needs.

- If MCP auth fails, reconnect the official Box plugin and retry. Use the custom OAuth app path only when the user explicitly requests custom MCP.
- If CLI is needed, guide the user through CLI login and verify with `box users:get me --json` before shifting tools.
- For REST, prefer obtaining a fresh access token from configured Box app credentials/OAuth flow over relying on manually copied short-lived developer tokens. The REST fallback approval gate is in `references/rest-calls.md`.
- Reuse the repository's existing Box auth flow if one already exists.
- Use a user-auth flow when end users connect their own Box accounts and the app acts as that user.
- Use the enterprise or server-side pattern already approved for the Box app when the backend runs unattended or manages enterprise content.
- Treat impersonation, app-user usage, token exchange, or downscoping as advanced changes. Add them only when the product requirements clearly demand them.
- Verify the exact flow against the current auth guides before introducing a new auth path or changing scopes.

## Choosing SDK vs REST

- Use an official Box SDK when the target language already has one in the codebase or the team prefers SDK-managed models and pagination.
- Use direct REST calls when the project already centers on a generic HTTP client, only a few endpoints are needed, or SDK support does not match the feature set.
- In agent-driven operations, direct REST is a fallback path. Do not use it by default when MCP or CLI can be set up.
- Avoid mixing SDK abstractions and handwritten REST calls for the same feature unless there is a clear gap.
- Preserve the project's existing retry, logging, and error-normalization patterns.

## Inspecting an existing codebase

Search for:

- `box`
- `BOX_`
- `client_id`
- `client_secret`
- `enterprise`
- `shared_link`
- `webhook`
- `metadata`

Confirm:

- Where access tokens are issued, refreshed, or injected
- Whether requests are user-scoped, service-account-scoped, or app-user-scoped
- Whether the codebase already has pagination, retry, and rate-limit helpers
- Whether webhook verification already exists
- Whether file and folder IDs are persisted in a database, config, or user settings

## Common secrets and config

- Client ID and client secret
- Private key material or app config used by the approved Box auth flow
- Enterprise ID, user ID, or app-user identifiers when relevant
- Webhook signing secrets
- Default folder IDs
- Metadata template identifiers and field names
- Shared link defaults such as access level or expiration policy
- Box CLI environment names or `--as-user` conventions when the team uses CLI-based operations

## Official Box starting points

- Developer guides: https://developer.box.com/guides
- API reference root: https://developer.box.com/reference
- SDK overview: https://developer.box.com/guides/tooling/sdks/
- Authentication guides: https://developer.box.com/guides/authentication/
- CLI guides: https://developer.box.com/guides/cli
- CLI OAuth quick start: https://developer.box.com/guides/cli/quick-start

Check the current Box docs before introducing a new auth model, changing scopes, or changing Box AI behavior, because auth guidance and SDK coverage can evolve independently from the content endpoints.