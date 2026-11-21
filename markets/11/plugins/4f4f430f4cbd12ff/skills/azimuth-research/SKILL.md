---
name: azimuth-research
description: Search Azimuth nonprofit intelligence for a research topic or source and give a concise evidence-backed answer. Use for open-ended corpus lookup; use the focused entity or peer-funding skills for those workflows.
---

# Azimuth Research

Read [shared evidence rules](references/evidence-rules.md). Use Azimuth `search` and `fetch` for name/EIN and paper-title discovery. Inspect the chosen result before making claims; clarify plausible identity matches. Use the discovered catalog for actual tool availability.

Explain the evidence at the same level the tool supports:

- A warehouse aggregate is an observed funding signal. The organization profile URL identifies the entity but does not validate the aggregate amount. A linked IRS filing is an example for that funder-recipient pair, not proof of the whole aggregate.
- Grant history does not show an open application, a warm introduction, or current strategic fit. Say when those items need separate verification.
- A paper result identifies a source; inspect the linked paper before claiming a specific finding.

Give the user a concise answer, name the selected entities and years, link source-bearing records, and state the one or two material coverage limits. Do not use private files or infer private relationships from public graph paths.

This MCP search covers organization names and paper titles. If a longer phrase returns no match, retry the core entity name. Use the MCP result to identify the entity, known relationships, source links, and exact coverage gap. It is a starting point for research, not the only source the host assistant may use.

When the user asks about mission, programs, current status, or another claim that `fetch` cannot establish, use the host assistant's own web search if it is available. Search with the resolved legal name and EIN, then inspect an official organization or funder page, filing, or other primary source that speaks to the claim. A graph path, third-party discovery result, or website link can guide the query, but its summary is not confirmation. Cite the page actually checked, distinguish its date from historical MCP observations, and note any conflict. If web search is unavailable or no suitable source is found, give the useful MCP findings and mark the claim unverified.

For cohort or program-role questions, do not classify an organization from its name, NTEE, website URL, or grant rows alone. Check a program-specific source with native web search when possible; otherwise say the program evidence is missing.

Choose the focused workflow for the next job: `entity-evidence` for identity; `peer-funding-comparison` for selected peers/benchmarks; `issue-to-funding-map` for an issue landscape; `program-evidence` for studies and analogs; `funder-review` for current fit/access; `research-packet` for an artifact; `fundraising-strategy-process` for decisions across the whole process. The same guides are retrievable through `list_research_workflows` / `get_research_workflow` when exposed.

For conflicts, new discoveries and whole-org research use [research review](references/research-review.md). For any retain request follow [connection boundaries](references/connection-boundaries.md). Never assume a save or graph refresh happened from instructions alone.

## In ChatGPT

GrantData is used through the Apps connection; users mention @GrantData in a conversation. Treat the selected public connection as the scope of a GrantData answer. Every public tool is read-only. Do not use private mail, file, or consulting-source connectors to answer a GrantData-scoped request, even when the host account has access to them. If the user wants separate private-source research, distinguish that work and its source from GrantData's public evidence.

Use ChatGPT's native web search for currentness checks and original sources, and cite the page actually checked.

Routine lookups return text-first results. The peer-funder comparison can render a table component when the host supports app views; still summarize the strongest patterns and the coverage limit in prose.

The guides are available as plugin skills and through `list_research_workflows` and `get_research_workflow`.

Use ChatGPT's document abilities for a packet when the user asks, and state that nothing was saved to GrantData. The owner connection may expose a save tool, but it is outside the public plugin's capability. Never switch to it to satisfy a public connection save request or represent a needs-review candidate as graph publication or permanent strategy memory.

The public connection cannot email a funder or submit an application. If asked, state this limit and offer a draft after verifying the intended funder and opportunity. Historical grant observations alone do not establish a live application route.
