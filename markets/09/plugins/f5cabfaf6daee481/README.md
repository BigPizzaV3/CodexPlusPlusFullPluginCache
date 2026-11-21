# Saleio

Review cold outreach on X, Telegram and LinkedIn. With draft access,
prepare unsent X or Telegram campaigns from existing Saleio lists. This plugin pairs Saleio's authenticated MCP connector with two skills:
`review-campaigns` and `create-and-resume`. A Saleio account is required. Your
existing Saleio plan and credit limits apply. Connecting the assistant does not
connect a sender.

## Connect

The production server URL is `https://api.saliobackend.com/mcp`. Sign in to Saleio
in the browser, verify the account and requested permissions, and return to your
assistant. OAuth uses PKCE and renewable, revocable grants; never paste credentials
or tokens into chat. Each user connects their own Saleio account.

For Claude, upload the Claude ZIP under Customize > Plugins > Add > Upload
plugin, then open its Connectors tab and connect Saleio. Custom connectors may
require an eligible plan or administrator permission. Claude Code can load the
unpacked plugin with `claude --plugin-dir /absolute/path/to/saleio` and authenticate
through `/mcp`. For Grok Bot, install the marketplace listing once published or
ask your bot to add a custom remote MCP server named Saleio using the server URL
above. Choose Connect on the returned connection card and complete sign-in.
Availability
in a public directory is separate from installing these package files.

## Try it

- "Show my LinkedIn campaigns and which ones need attention."
- "Summarize my campaigns with lifetime reply rates and their underlying counts."
- "Prepare an unsent Telegram campaign from my existing Saleio list."
- "Continue my saved Saleio task. Reuse anything already completed."

For LinkedIn, use the returned Saleio link to connect a sender, import profiles,
create campaigns and review messages.

For X and Telegram, the assistant saves your goal and proposed message before channel setup. Open
the returned Saleio task link to connect X or Telegram securely, then resume the
same task. Inspect import validation and enrichment costs before approving an
import. X enrichment can spend existing credits and can trigger an already
enabled automatic top-up. A saved draft is not launched or necessarily ready
to send. Review and launch remain in Saleio.

Reporting access does not authorize saving tasks, contacts or drafts. Authorize
additional scopes only when needed. If a host cannot complete a permission
upgrade, use the returned Saleio link; never repeat imports or drafts to work
around authentication. Tool availability varies by deployment and host review.
Optional campaign pause requires its own scope and explicit request, and is not
part of default draft access. The connector cannot send, launch, approve, resume
sending, enroll recipients, export inbox conversations, discover recipients or
purchase credits. Cards enhance the experience where supported; plain text and
Saleio task links remain usable.

Disconnect in Saleio Settings > AI connections. This invalidates access and
refresh tokens immediately. Removing a plugin from the host alone is not a
substitute for revoking the Saleio connection.

[Support](https://saleio.ai/integrations) · [Privacy](https://saleio.ai/privacy) ·
[Terms](https://saleio.ai/terms). Contact help@saleio.ai.

## Package license

The MIT license in this folder covers only the plugin files, skills and assets.
It does not license the Saleio application, backend, service or other repository
contents. Use of the hosted service remains subject to Saleio's terms.
