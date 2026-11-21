# Prompt Prospect for ChatGPT, Claude and other assistants

Get the attendee list for any conference, expo or trade show. Prompt Prospect finds who is speaking, exhibiting, sponsoring and attending an event (with each person's company and the evidence that puts them there), checks everyone against your target customer, and knows which other events a company or speaker goes to, so you know who to meet before you go. This plugin connects an assistant to your Prompt Prospect workspace through the Prompt Prospect MCP server and teaches it four workflows:

- **Plan a conference**: find events near a place or in an industry from the curated catalog, save one, and start its research.
- **Find people at an event**: who is going and why, filtered by role, company, fit or relationship (speakers, sponsors, exhibitors, engaged attendees), with the evidence behind each name and who matches your target customer.
- **Trace across events**: the other conferences a company, speaker, exhibitor or sponsor is listed at, across the catalog and your workspace.
- **Keep track of people**: save or dismiss people, keep notes, record meetings on the event calendar and mark outcomes.

Your target customer is set in the Prompt Prospect app (Settings → Target customer); once it is, every researched event is checked against it automatically and the assistant reads the result. When none is set, the assistant says so and shows the unfiltered list.

## What it connects to

One remote MCP server, `https://www.promptprospect.ai/api/mcp`, over Streamable HTTP with OAuth 2.1 (dynamic client registration and PKCE). There is no API key to paste: the assistant sends you to Prompt Prospect to sign in, choose a workspace and approve the scopes it asks for. Read scopes list events, people and companies with their evidence, fit and other events; write scopes add events, save people, and keep notes, meetings and outcomes. Everything goes through the same code and limits as the Prompt Prospect app.

The plugin runs no local code, installs nothing and reads nothing from your machine. It contains only these skill files, the manifests and the icons.

## Install

**Claude Code**

```
claude plugin marketplace add AdamScholes/prompt-prospect-plugins
claude plugin install prompt-prospect@prompt-prospect-plugins
```

Then run `/mcp` once to sign in to Prompt Prospect.

**Claude (claude.ai and desktop)**: add Prompt Prospect from the directory, or Settings → Connectors → Add custom connector with the URL above.

**ChatGPT**: add Prompt Prospect from the plugin directory. Or, with developer mode on, add the MCP server URL above as a connection.

## Privacy

The server returns only data from your own workspace and the public event catalog: event details, people connected with an event (name, headline, company, LinkedIn profile URL and the evidence that puts them there), companies, fit verdicts, the other events a person or company is listed at, and your own notes. It never returns email addresses, phone numbers or payment details. The full policy is at https://www.promptprospect.ai/privacy and the terms at https://www.promptprospect.ai/terms. Support: chris@promptprospect.ai.

## Documentation

This README is the documentation. Product help and answers to common questions: https://www.promptprospect.ai/faq
