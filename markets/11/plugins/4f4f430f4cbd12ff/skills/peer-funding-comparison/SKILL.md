---
name: peer-funding-comparison
description: Compare observed funders across explicitly selected nonprofit peers and a focal organization in Azimuth. Use for peer-funder overlap or gap questions, not for unverified peer discovery or prospect recommendations.
---

# Peer Funding Comparison

Read [shared evidence rules](../azimuth-research/references/evidence-rules.md). For cohort choice or earned-revenue comparables read [peer design](references/peer-design.md); propose source-checked candidates, then obtain a selected set before running this comparison.

Resolve the focal organization and each chosen peer with `search` and `fetch`. Use `find_peer_funders` only when the user named the peers or they were clearly selected earlier in the conversation. If the user has only a strategy or a vague “organizations like us,” ask for the peer set or explain that this version cannot yet verify a comparable cohort. Keep close operating peers distinct from broader reference models when the user supplied both; do not imply they are equivalent.

Classify each named entity's role before interpreting a result. A peer nonprofit is an organization doing comparable work; do not evaluate it as a prospective funder, ask for its application rules, or call its incoming supporters its own grants to others. Some peers also make grants, but that requires separate outgoing-grant evidence. If the focal organization has few or no observed inbound edges, compare two already selected peers with visible histories and state that the focal organization's coverage is thin. Absence of an FCC-style focal edge is a data-coverage limit, not a failed overlap test or evidence that the organization lacks supporters.

`find_peer_funders` takes nonprofit EINs and reports funders observed for the selected peers. It does not directly compare two foundations' grantee portfolios. For a request to compare two funders, resolve and classify those funders first; inspect each one's outgoing records through a supported read path if available, with its caps and source limits. Never pass two foundation EINs as focal and peer merely to force a result from this tool.

Read the comparison as historical grant observations. Report the selected peers, observed years, overlapping funders, and whether a focal edge was observed. “Not observed here” means only that the selected warehouse path did not return that edge. The recorded funder role can include an operating partner or intermediary. Linked filings are examples for a pair and do not validate the aggregate total.

Treat a missing `funder_type` as an unresolved role. Warehouse year and example filing year are separate; a mismatch cannot verify aggregate amount/recency. Use native primary sources to check pass-through or donation roles. For retain requests follow [connection boundaries](../azimuth-research/references/connection-boundaries.md); an unavailable save becomes a conversation review note, not a claimed graph update.

Do not turn a peer-connected funder into a prospect recommendation without separate current fit, instrument, eligibility, application route, and access evidence. Keep grants separate from debt, equity equivalents, recoverable capital, and partnership routes. The current peer tool covers grant aggregates, not those other instruments. If the user asks for a shortlist, offer a clearly labeled research queue with the missing checks instead of a ranked recommendation.

If the user wants to investigate one of those funders further, use the host assistant's web search when available to inspect the funder's current official pages for program scope, eligibility, and application route. The peer table supplies names and historical leads; it does not confirm a current opportunity. Cite the pages actually checked and keep unresolved checks in the research queue.

The peer table helps inspect rows and sources. In prose, include the strongest observed patterns and the coverage limit even when the widget renders.

## In ChatGPT

GrantData is used through the Apps connection; users mention @GrantData in a conversation. Treat the selected public connection as the scope of a GrantData answer. Every public tool is read-only. Do not use private mail, file, or consulting-source connectors to answer a GrantData-scoped request, even when the host account has access to them. If the user wants separate private-source research, distinguish that work and its source from GrantData's public evidence.

Use ChatGPT's native web search for currentness checks and original sources, and cite the page actually checked.

Routine lookups return text-first results. The peer-funder comparison can render a table component when the host supports app views; still summarize the strongest patterns and the coverage limit in prose.

The guides are available as plugin skills and through `list_research_workflows` and `get_research_workflow`.

Use ChatGPT's document abilities for a packet when the user asks, and state that nothing was saved to GrantData. The owner connection may expose a save tool, but it is outside the public plugin's capability. Never switch to it to satisfy a public connection save request or represent a needs-review candidate as graph publication or permanent strategy memory.

The public connection cannot email a funder or submit an application. If asked, state this limit and offer a draft after verifying the intended funder and opportunity. Historical grant observations alone do not establish a live application route.

When the table component renders, keep the written answer complete on its own: selected peers, observed years, overlapping funders, focal status and one coverage limit. Lead with what the two peer organizations have in common; do not turn either peer into an applicant-facing funder evaluation. Put application-route checks only in a separate funder review when the user asks for one.
