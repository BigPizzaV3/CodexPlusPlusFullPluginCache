---
name: entity-evidence
description: Resolve a named nonprofit or funder to the right EIN and summarize its available Azimuth profile and source-backed funding signals. Use when identity, aliases, or observed organization evidence matter.
---

# Entity Evidence

Read [shared evidence rules](../azimuth-research/references/evidence-rules.md). Use `funder-review` for current qualification and `program-evidence` for an intervention/program case; this workflow resolves identity and observed records.

Search the name or EIN, inspect the candidate cards, and fetch the selected `org:<EIN>` result. If two plausible entities remain, present their names and EINs and ask which one the user means. Do not silently choose by a similar name or location.

Lead with the resolved legal entity and EIN. Give only the profile fields and funding observations returned by `fetch`; keep an unknown field unknown. The entity profile is an identity link, not proof of every funding amount. A linked IRS filing is an example for a funder-recipient pair, not a citation for the full aggregate. State when the result has only a warehouse aggregate and when the latest observed year is missing.

Separate three questions when they arise: who the organization is, what funding was observed, and whether a funder is a current prospect. The present tools answer the first two within their coverage. An observed edge does not establish an open application, current fit, or an introduction. If the user asks about grants versus loans or investments, do not infer the instrument from a grant aggregate; request or inspect an instrument-specific source before classifying it.

The current profile does not supply mission or program evidence. Do not label an organization as primarily focused on a population, or claim it runs an embedded program, from its name, NTEE, website URL, or grant rows alone. When the host assistant's web search is available, use the resolved name, EIN, and website as search leads; inspect an official program or mission page before making that classification. Cite the inspected page and its date or currentness. If web search is unavailable or the source remains unclear, mark the classification unverified.

For current prospects, applications, investments, or staff, use native web search to inspect the funder's own current pages or primary transaction documents when available. Do not upgrade a historical grant edge or a search-summary lead into a current claim. Keep what Azimuth observed separate from what the web source confirms.

The organization evidence card is a compact way to inspect the result. Keep the written answer useful if the card is unavailable, with the EIN, relevant years, available source links, and one material coverage limit.

## In ChatGPT

GrantData is used through the Apps connection; users mention @GrantData in a conversation. Treat the selected public connection as the scope of a GrantData answer. Every public tool is read-only. Do not use private mail, file, or consulting-source connectors to answer a GrantData-scoped request, even when the host account has access to them. If the user wants separate private-source research, distinguish that work and its source from GrantData's public evidence.

Use ChatGPT's native web search for currentness checks and original sources, and cite the page actually checked.

Routine lookups return text-first results. The peer-funder comparison can render a table component when the host supports app views; still summarize the strongest patterns and the coverage limit in prose.

The guides are available as plugin skills and through `list_research_workflows` and `get_research_workflow`.

Use ChatGPT's document abilities for a packet when the user asks, and state that nothing was saved to GrantData. The owner connection may expose a save tool, but it is outside the public plugin's capability. Never switch to it to satisfy a public connection save request or represent a needs-review candidate as graph publication or permanent strategy memory.

The public connection cannot email a funder or submit an application. If asked, state this limit and offer a draft after verifying the intended funder and opportunity. Historical grant observations alone do not establish a live application route.
