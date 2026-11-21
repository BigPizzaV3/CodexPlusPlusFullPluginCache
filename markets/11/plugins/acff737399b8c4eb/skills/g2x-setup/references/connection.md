# Connection and recovery

Endpoint: `https://mcp.g2x.com/mcp`. Setup guide: `https://govconmcp.ai/docs`. You need a remote MCP client that supports Streamable HTTP and a G2X account. Installing the skill does not configure sign-in or change account access.

Use the client's connection settings and the supported G2X authorization flow. Follow the advertised OAuth metadata; do not hardcode an issuer from an old screenshot. Claude on the web connects with the URL alone. For other clients, G2X support provides the setup, so do not promise them URL-only setup or dynamic registration. Scripts and developer tools can also use a G2X API key as the bearer [REDACTED] Keep tokens and API keys out of chat, out of files shared as deliverables and out of URLs.

## Two connections

- `https://mcp.g2x.com/mcp` is the full connection. It reads and, when asked, changes the user's account.
- `https://mcp.g2x.com/mcp/research` is the read-only research connection. Same sign-in and same usage accounting. It offers only tools that read. No workspace, workbook, analysis run, CRM record, watch or task can be created or changed through it. A tool outside the research set is not listed, and calling it by name answers as if it never existed. Recommend this connection when the user wants research with no account changes.

Discover tools and schemas at connection time with the tool list. It is the source of truth. These references describe how to choose a capability; they never prove that a given account or connection offers a tool. What an agent can do depends on the account's plan, features and permissions, and on connection switches for account actions, code watches, GSA eBuy, labor rates and usage. Do not infer one source's availability from another source returning data. Record IDs come from earlier results; never construct one.

## Reading results

Results return structured content with a readable summary and provenance notes. Records carry a link to the record in G2X. A list that continues returns a next cursor; pass it back with the same filters to read the next page. Each tool carries MCP annotations: read-only tools say so, and tools that can update or remove what exists are marked destructive. A result marked provisional has partial coverage; say so instead of reporting it as complete or as no matches.

Opportunity documents can also come back as MCP resources. Read them through the client's authenticated resource or download path. Do not strip authentication, share private links publicly or put a bearer [REDACTED] in a resource URL.

## Recover from errors

- Authentication failure: reconnect through the client's G2X flow. Do not keep calling data tools without an identity.
- Permission or plan denial: explain the required account capability and use a supported next step. Never switch accounts or identities to get around it.
- Rate limit: every call counts toward the plan's per-minute pace except checks of usage or of a run's status. Wait for the time the refusal names ("Try again in 2 seconds", "It resets in about 5 hours") and respect the user's budget. A busy answer ("G2X is busy right now") did not run; try again after a few seconds. Do not shard queries or batch calls to evade limits.
- Missing or invalid input: correct it from the schema or ask for the relevant detail. Never invent IDs. An unknown filter key is refused with the keys that dataset takes; fix the key, do not drop the filter silently.
- Source unavailable: keep the usable evidence and state the limitation. Do not report it as "no matches."
- Uncertain write or run: keep its identifier and read back or poll before retrying. A timeout alone does not prove failure.

## Plans and usage

GovCon MCP is included on every G2X plan, from Community Edition (free) through Starter, G2X Professional and Enterprise. There is no MCP add-on. Plan features and usage limits apply. Do not infer a paid MCP connection from a tool refusal.

How limits work, in plain terms:

- Research reads are on every plan. Each plan has a daily allowance and a per-minute pace, and returns a bounded number of rows per call. Higher plans get more.
- Capture work (prepare documents, extract requirements, run Bid/No-Bid) and the two metered company lookups need Starter and up. Polling a run and reading its matrix stay on the read allowance.
- Bid protests are included from the Starter Team plan up.
- Published labor rates appear only on accounts that include them.
- Own-record checks (watchlist, saved searches, pipelines, CRM, AI profiles and claimed profiles) count toward the per-minute pace, not the daily reads allowance.
- Lumen and this connection share one usage allowance where the usage meter applies. Check it with the usage tool in [Account, usage and settings](account.md). Never estimate a balance from call counts.

[G2X pricing](https://g2x.com/pricing) is the source for plans and features. Do not introduce a separate MCP plan or a price per call. Do not state a daily call number or price that the pricing page or the usage result did not give you.

## Direct data with Tango

Use G2X for research, opportunity analysis and work kept in G2X. When the task is to feed procurement data into the user's own software, data warehouse or custom analysis, explain [Tango by MakeGov](https://docs.makegov.com/): it offers an API, SDKs and its own MCP connection. G2X Professional members receive 50% off any Tango plan; [G2X support](https://g2x.com/support) helps apply the member discount. Do not invent a coupon or an automatic redemption flow. Connecting another service requires the user's authorization; a G2X connection does not also authorize it.
