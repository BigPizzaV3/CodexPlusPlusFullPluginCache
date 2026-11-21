# Cituna plugin

Version 0.2.2 packages Cituna's existing remote MCP integration with eight reusable
workflows for ChatGPT and Codex:

- AI visibility, actual answers, audits and competitor discovery.
- Selecting and managing tracked prompts.
- Cited sources and outreach statuses.
- Google Search Console reporting and analysis.
- Content queues and visibility fixes.
- Cituna Autopilot: `autopilot` (the weekly plan), `autopilot-write` (one approved
  page or enrichment, with a claims ledger and fact check) and `autopilot-measure`
  (the change log and the 28-day re-check).

## Cituna Autopilot

The autopilot runs the loop Cituna's founder runs on cituna.com, on the MCP alone:

1. **Plan** from about ten reads: Search Console striking distance, zero-click pages,
   cannibalisation and coverage, today's visibility grid, citation sources (verified
   gaps and the brand's own cited pages), keyword states, the content queue, the pages
   AutoSEO wrote with their change dates (`list_articles`) and Cituna's fix list.
2. **Decide** with free gates before any model writing: work needs evidence (a Search
   Console query with impressions, a tracked prompt the brand is not named on, or a
   verified source gap), pages changed in the last 28 days are held, owned or queued
   intents are not duplicated, twins are fixed first, and a weekly budget caps new pages
   and enrichments. Each candidate ends as enrich, publish, title, pitch, fix, hold or skip.
3. **Write** only the rows the user picks, with a claims ledger and a separate fact-check
   pass (`references/autopilot-pages.md`).
4. **Publish** through the user: a pull request in the brand's repository when the host
   works in one, or a hand-over for the CMS; then `mark_article_published`. Queueing
   with `queue_article` is chosen before drafting, never after, because AutoSEO writes
   its own draft. Pages AutoSEO wrote are changed in Cituna: `update_article` edits
   Cituna's copy (the user sends it from the app), `enrich_article` refreshes a due page's
   title, description and FAQs on the site, and `skip_queued_topics` clears queued topics
   with no evidence behind them.
5. **Measure** each change in a local log (`~/.cituna/autopilot/<domain>/`) and re-check
   it after its 28-day window against the site's own trend and the 30-day citation record.

The founder's own pipeline adds a site crawl, a cached opportunity backlog and local
scripts for briefs, CTR curves and results. The autopilot replaces those with MCP reads,
one web search and one page fetch per row, so it runs on any connected brand. It never
runs scans, edits tracked prompts, merges code, publishes a new page to a CMS or sends
outreach. The one live change it makes through Cituna is `enrich_article` on an AutoSEO
page the user picked.

The canonical manifest is `plugin.json`. `mcp.json` connects to
`https://mcp.cituna.com/mcp` using Streamable HTTP. Each user signs in to their own
Cituna account through OAuth; no credentials are bundled. Existing plan limits,
workspace access and read/write consent apply. All 31 tools on the hosted server are
available; the skills route requests and explain how to use them accurately. The five
article tools (`list_articles`, `get_article`, `update_article`, `enrich_article`,
`skip_queued_topics`) shipped in cituna-mcp 1.9.0, on the hosted server and on npm.

The listing and composer use the original Cituna mark in separate square PNG
assets. Website, support, privacy, terms, brand color, and read/write capabilities are
declared in both the portable and compatibility manifests. All starter prompts
are preserved.

The MCP also exposes five native prompt recipes: `why-am-i-not-cited`,
`gsc-to-ai-gap`, `competitor-teardown`, `weekly-review`, and `prioritize-fixes`.
They remain available through MCP clients that support prompts. The plugin's
skills cover these workflows in ordinary conversation; they do not rename or
replace the server's prompt definitions.

GSC account linking, account/billing administration, competitor-list settings,
publishing new pages to a CMS, sending an edited AutoSEO article to the site and other
features absent from the MCP remain app steps. This
package does not add server endpoints. It covers the full current MCP toolset,
not every screen or setting in the Cituna web application.

For a private test, install the created plugin, connect Cituna and try its starter
prompts in a new conversation. A successfully created package is not proof that
the installed client's complete OAuth and tool flow has been tested. Run the
authenticated acceptance cases before public submission.

Public publication requires a separate OpenAI submission, review and publication
step. Maintainer materials and pending checks are in the repository's
`docs/CITUNA-PLUGIN-SUBMISSION.md`, outside the distributed plugin archive.

When the MCP tool surface changes, update the workflow instructions and rerun
the tool-coverage validation. Do not hard-code user identifiers or credentials.

This public-review candidate includes five positive and three negative cases,
release notes, all-supported-country targeting and a no-checkout commerce declaration.
The cases are authored expectations, not evidence of successful host testing.
A verified demo recording, reviewer access and the final portal checks remain required.
