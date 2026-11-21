# Binto Operations

Read your Binto Operations records from Claude. Ask what needs attention across your Locations, find a license, permit or lease by a Location's name or address and see when it expires, look up when a piece of equipment was last serviced and what it cost, find a supplier or service provider's contact details, and review tasks, procedures and inspection reports.

- **Read-only.** Claude can read records. It cannot add, change or delete anything in Binto.
- **Your access, nothing more.** You sign in to Binto in your browser and approve the connection. Claude sees only the Organizations, Locations and records your own Binto account can open.
- **No passwords or keys to copy.** Sign-in uses OAuth. Disconnect at any time.

## What this plugin contains

- A connection to one remote MCP server, `https://binto.ai/api/mcp` (Streamable HTTP, OAuth). This is the only place the plugin sends or fetches anything.
- Three skills that tell Claude which Binto tools to use:
  - `attention-across-locations`: what needs attention across your Locations
  - `find-document-or-permit`: find a document or permit at a Location by address or name
  - `equipment-service-history`: when equipment was serviced, what was done and what it cost

The plugin runs no code on your computer: it has no hooks, scripts or commands.

## What you need

A Binto account that belongs to an Operations Organization with Ask Binto turned on. Create an account at https://binto.ai.

## Install

In Claude Code:

```text
/plugin install binto-operations --marketplace binto-app/binto-plugins
```

## Connect

In Claude Code, after installing the plugin, run `/mcp`, choose `binto`, then **Authenticate**. Your browser opens Binto. Sign in and choose **Continue**.

## Try it

- "What needs attention across my Locations this week?"
- "Find the health permit for the Main Street Location. When does it expire?"
- "When was the walk-in cooler at Maple Street Market last serviced, and what did it cost?"

If your account belongs to more than one Organization, Claude asks which one you mean.

## Privacy

What you ask is sent to Binto as tool calls, and the matching records come back to Claude so it can answer. Binto records which tool was called, by which assistant, and whether it worked. It does not record what you asked or what was returned. See the [Privacy Policy](https://binto.ai/privacy) and [Terms of Service](https://binto.ai/terms).

## Help

https://binto.ai/contact

## License

MIT. See `LICENSE`.
