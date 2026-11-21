# NoFilter

Find public photo spots and places to visit around a travel destination. NoFilter
returns up to six places from its catalog, with distances and links to their
NoFilter pages. It helps you discover options; check opening hours, admission,
photography permissions and access before visiting.

NoFilter supports **1 free daily search without a NoFilter account**. Connecting
a free NoFilter account gives **3**, and existing paying accounts get **50**.
Account connections require NoFilter19.145 or later, with **MCP: ChatGPT, Claude and more** in Settings. Earlier private review builds call this screen Connected assistants. Guest access does not require the app.
Availability in each directory depends on its review and publication process.

## Connect

The remote MCP endpoint is
`https://getnofilter.com/mcp`.

1. Add the NoFilter connector in your assistant. Select OAuth and automatic
   registration (DCR) if the client asks.
2. Review the assistant name and origin, then choose **Continue without an account**
   for one free daily search, or **Connect my NoFilter account** for account access.
3. For account access, scan the QR with your phone or enter its code in NoFilter
   under **Profile → Settings → MCP: ChatGPT, Claude and more (Connected assistants in earlier versions)**, then review and approve.
4. Return to the assistant and ask for photo spots around a travel destination.

Need a free account? Search **NoFilter** in the App Store or Google Play, create
your free account, then reconnect NoFilter in your assistant and choose account
access. Follow the [setup guide](https://getnofilter.com/mcp).
If MCP: ChatGPT, Claude and more (Connected assistants in earlier versions) is missing, update the app; if the store has no update,
keep using guest access until this feature reaches your app version.

Account access can be revoked from that NoFilter screen. Guests can disconnect in
their assistant. Guest quotas use a signed browser cookie, shared by connections
started from the same authorization browser; this is not verified person identity.
Account quotas are shared across assistants. All allowances reset at00:00UTC.
Empty or failed searches do not use the allowance.
No purchase or subscription change takes place through this plugin.

## Examples

- “Find places to photograph in Rome with NoFilter.”
- “Which NoFilter places should I visit around Paris?”
- “¿Cuáles son los mejores lugares para fotografiar en Roma, Italia?”

You provide the destination name. The assistant resolves its coordinates before
searching; you do not need to enter latitude or longitude. It may ask for a country
or landmark to distinguish places with the same name. This does not use your GPS.

## Privacy and access

The connector searches public places. It cannot read your private profile, age,
saved places, trips, or app password. Destination coordinates and chat content
are not retained by this service. Anonymous visitor/account usage counts enforce the shared
allowance; minimal recommendation experiment records measure repeat usage.

Read the [connection privacy notice](https://getnofilter.com/mcp/privacy)
and [NoFilter terms](https://getnofilter.com/en/terms-of-use).
For help, use the contact options in the NoFilter app or on
[getnofilter.com](https://getnofilter.com).

## Clients

See the [connection guide](https://getnofilter.com/mcp) for ChatGPT, Claude and Codex.
Any client must support remote Streamable HTTP and OAuth discovery with automatic
client registration. No API key, local server or executable hook is required.

The included `gemini-extension.json` supplies Gemini CLI configuration. Gemini CLI
uses OAuth discovery; complete `/mcp auth nofilter` when prompted. The `skills/`
folder includes the same destination and result-handling instructions.

`server.json` declares the remote endpoint for the official MCP Registry. A
manifest in this repository does not by itself mean that a directory has listed it.

## Package

`plugin.json` and `mcp.json` provide the portable OpenAI package.
`.claude-plugin/plugin.json` and `.mcp.json` provide the Claude package.
Both use the same remote service and the same `photo-spots` skill.
There are no executable hooks, local servers, bundled credentials or account data.
The package is MIT licensed. Directory approval and publication are tracked separately.

## License

The plugin manifests, documentation and skill are distributed under MIT. NoFilter’s hosted backend and catalog are not included in this license. Support: https://getnofilter.com/contact.
