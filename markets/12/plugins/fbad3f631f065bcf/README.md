# VanReceipts plugin

One package for a remote MCP server and two skills.

- `skills/ai-estimates` drafts an estimate, quote, or invoice. The server checks every price source and computes the total.
- `skills/before-and-after` shows a slider for two photos the user already has. The server does not generate images.
- `server` is the Streamable HTTP MCP server. See `server/README.md` to run it and to deploy it.

The server URL in `mcp.json` and `.mcp.json` is the local address used for development. Replace it with the deployed https URL before a directory submission. Steps for the owner are in the build report.

No hooks, no commands, and no userConfig. Skills carry the workflow.

## How to use it

Describe a job and ask for an estimate, a quote, or an invoice. Answer one short round of questions. VanReceipts checks every price line and computes the total, then the document viewer lets you edit the lines and download a PDF. For two photos you already have, ask for a before and after slider. The share link opens the same slider. The plugin does not generate images.

## Data

The document tools receive the business name, client name, dates, and lines you choose to print. Those fields are checked and returned. They are not stored. A slider stores the two photos until the delete link is opened or 30 days pass. A counter stores only the tool name, the trade, the document kind, and the day. There is no account and no card data. The draft privacy note is `PRIVACY.md`.
