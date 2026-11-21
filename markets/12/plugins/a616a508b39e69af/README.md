# EQUIRE plugin

[EQUIRE](https://www.equire.ai) is a governed commercial real estate deal workspace for acquisitions and investment teams, built by [Agentic Assets](https://agenticassets.ai). When the offering memorandum, rent roll, and T-12 disagree, the team needs to know which figure to trust before investment committee, not during it. This plugin connects a compatible AI assistant (Claude, ChatGPT, Codex, or Cursor) to your EQUIRE account and adds skills for deal briefings, portfolio triage, underwriting what-ifs, listing screening, market research, and diligence. The skills instruct the assistant to use only what EQUIRE returns from the deals, documents, valuation models, listings, and research you can access, and to state each figure's source and release basis. It requires an EQUIRE account.

## Skills

Where the host exposes skill commands, use the names below; elsewhere, ask for the workflow by name.

- `/equire:onboarding`: connect EQUIRE, choose an organization, and learn what the assistant can and cannot change.
- `/equire:deal-briefing`: an investment-committee-style briefing on one deal, with cited source excerpts.
- `/equire:portfolio-triage`: what needs attention across the portfolio, ranked by open risk, with side-by-side deal comparisons.
- `/equire:underwriting-what-if`: read-only sensitivities through a deal's saved valuation model; nothing is saved unless you ask for a proposal and confirm it.
- `/equire:listing-screening`: search EQUIRE's market listing index, inspect offering memorandum facts with their caveats, and queue a listing for screening after you confirm.
- `/equire:market-research`: broker reports, supply, comparable sales, and metro trends for a deal, run only from a plan you approve.
- `/equire:investment-workflow`: document evidence across deals, deal notes, diligence items, review-item proposals, and the interactive EQUIRE workspace.

## Connect

The EQUIRE server URL is `https://www.equire.ai/mcp`. You sign in with your EQUIRE account; the plugin never asks for a password or key.

- **Claude (web, desktop, Cowork):** once EQUIRE is listed in the Claude directory, install the plugin, open its Connectors tab, connect EQUIRE, and sign in. Until then, or without the plugin, add EQUIRE as a custom connector with the server URL where your Claude plan allows custom connectors.
- **Claude Code:** run `claude mcp add --transport http equire https://www.equire.ai/mcp`, or install the plugin from a marketplace that lists it, then run `/mcp` and sign in to the EQUIRE server.
- **ChatGPT:** install EQUIRE where your workspace lists it, or, where your account allows developer connectors, add a connector with the server URL and sign in. A direct connector reaches EQUIRE's tools but not this plugin's skills.
- **Codex and Cursor:** install the plugin where your client lists it, or add the server URL in the client's MCP settings, then sign in when prompted.

EQUIRE shows its own consent screen during sign-in. You choose which organizations to share, which permissions to grant, and a write level: Read Only, Reads & Staged Changes, Deal Intake, or, when the consent screen offers it, Routine Workflow Updates. Review or revoke the connection at any time in EQUIRE Settings. Connect EQUIRE once per assistant; a second connection to the same server shows every tool twice.

If a client requests Organization Website Search, you can choose it separately on the consent screen. EQUIRE stores your current session access token encrypted on its server to search retained website evidence under your existing access. Search uses your current organization even if the connection includes others. It expires with that session token, so reconnect to search again even if the assistant connection is still active. EQUIRE does not store a refresh token for this search. Search and source-detail retrieval require the separate Organization Website Knowledge permission. Select both permissions to enable search. An existing client registration may not offer the search permission yet.

## What the assistant can change

The assistant reads only the organizations and permissions you grant. With Reads & Staged Changes, it can stage valuation and review proposals that a person on your team approves in EQUIRE. With Deal Intake, it can create a deal and attach transferable documents and property photos to a permitted deal after confirmation. When authorization scopes are omitted, consent requests default to deal reads and intake permissions within the registered ceiling; existing grants stay unchanged. With Routine Workflow Updates, while EQUIRE offers that level, it can also add deal notes, create or update diligence items, queue a listing for screening under one of your Investment Mandates, attach report links you supply to a deal, and start market research from a plan you approved. The skills instruct the assistant to state each change and wait for your confirmation first, and your assistant may also ask you to approve each write. File attachment supports downloadable originals and a private upload handoff for sandbox files. Validated in ChatGPT and Claude with test files; host settings and file access still determine whether bytes can transfer; sandbox network policy may require allowing the storage domain. If the host cannot transfer bytes, upload through the deal's Documents page or photo gallery in EQUIRE. EQUIRE's tools cannot delete deals, approve or release data, make investment committee decisions, convert a listing into a deal, or create share links. What your assistant does with returned data in the conversation, including through other connectors you have enabled, is governed by your assistant and its settings.

## Data and privacy

This package contains connector configuration and skill instructions only. It runs no hooks, scripts, or local servers, and it reads no files on your machine. When you use it, your requests and the EQUIRE data they return pass between your AI assistant and one server, `https://www.equire.ai/mcp`, operated by Agentic Assets, under the permissions you granted. Market research runs, attached report links, and listing photo lookups fetch public web pages from EQUIRE's servers, not from your machine. A research run sends search queries to web search providers, built from the deal's market scope (metro, submarket, and property type) and, for a custom search, the request text you approve. EQUIRE processes your data as described in its privacy policy and records each tool call in your organization's audit log. EQUIRE data your assistant receives is then handled under your AI provider's terms and your organization's settings for that assistant. Privacy policy: https://www.equire.ai/privacy

## Scope and limits

EQUIRE supports investment analysis and decision workflows. It is not investment, legal, tax, or appraisal advice, and it does not replace your team's review. Coverage depends on the documents and data in your workspace, and the skills disclose thin evidence, permission limits, and preliminary figures rather than filling gaps. Write actions need a write level that allows them, an organization role that can edit, and an organization billing status that allows writes, and market research uses your organization's metered research allowance. Host support and your account permissions determine which features are available.

## Support and license

Support: [contact EQUIRE](https://www.equire.ai/contact). Security reports: see SECURITY.md. Files in this repository are MIT licensed; the EQUIRE service is governed by the [terms of service](https://www.equire.ai/terms).

## Source

Published from internal source. Each release replaces this repository's contents. Issues are welcome; changes arrive in the next release.
