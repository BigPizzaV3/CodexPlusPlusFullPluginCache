---
name: fundraising-strategy-process
description: Guide a nonprofit fundraising strategy conversation from its current question to a defensible next decision. Use for goals, peers, benchmarks, funding routes, prospect priorities, program cases, proposals, or strategy refresh; use the focused lookup skills for a simple entity or funding-history question.
---

# Fundraising Strategy Process

Read [shared evidence rules](../azimuth-research/references/evidence-rules.md). This is the portable research/decision method, not the Azimuth strategy application itself. Use the focused issue, program-evidence, funder-review and research-packet skills for their stage artifacts.

Use the Azimuth fundraising method as a guide, not a required wizard. People may enter through a full strategy, landscape or benchmark, prospect expansion, program or project case, live proposal, or execution and refresh. Begin with the user's question. Identify the decision, organization, scope, market, time horizon, and useful output; carry forward what the user already decided. Ask a focused question only when the answer would materially change the next move. Give a useful provisional answer while evidence is incomplete.

The method has eleven connected stages. Read the reference for the part of the process the user needs; for an end-to-end strategy, use all three as the work progresses:

- [Position, peers, and benchmark](references/position-and-benchmark.md): stages 1–4, from the ask to a fair financial diagnosis and planning goal.
- [Evidence, case, and opportunities](references/case-and-opportunities.md): stages 5–8, from program analogs and costs to funding routes and qualified prospects.
- [Portfolio, roadmap, and refresh](references/portfolio-and-roadmap.md): stages 9–11, from choices and channel goals to an owned plan, board memo, and subsequent revisions.

## Use the strategy prompt library

Read the [strategy prompt library](references/strategy-prompts/index.md) when drafting or improving a strategy. It carries the Azimuth Strategy Framework's stage profiles, reusable prompt modules, shared strategy context, fast-intake prompts, and six section helpers. Select the relevant stage and linked task module; for a first strategy use shared context plus fast intake, and for a chapter revision use the matching section helper. Use available evidence and accepted user decisions to fill context; leave unavailable inputs as explicit gaps. Never paste unresolved app placeholders into the deliverable.

Apply the Host/MCP adaptation at the top of each reference. These are research and drafting methods, not access to the strategy application, its database or its stored reviews. Put copy-ready organizational prose in the draft, and show provisional candidates, limitations and source checks separately in the conversation. Do not conceal uncertainty merely because the method keeps review metadata outside the document. Respect this connection's actual capabilities and existing goal-calibration rules.

For any numeric goal, portfolio or staffing recommendation, read [Goal calibration](references/goal-calibration.md). Keep peer ambition, solicitation volume, commitments and in-horizon cash separate; construct a conditional first-year scenario from access, workload and payment timing. When renewal cash, access and capacity are unknown, do not recommend a numeric first-year goal, even under the label provisional or planning case. Recommend the initial work and the decision date instead. A numeric scenario requires an explicit ask/conversion/payment construction; historical contributions are not confirmed next-year cash.

Start at the relevant stage and surface consequential upstream gaps. When new peers, sources, or decisions change an earlier premise, revisit the affected downstream conclusions. Produce the useful stage artifact, not merely a list of research that someone else should do.

## Work with the evidence available here

Use the bound Azimuth app and its actual catalog. Follow [connection boundaries](../azimuth-research/references/connection-boundaries.md) for availability and any explicitly requested saving. Do not switch connections or claim hosted persistence from another app's result.

- Resolve a named organization with `search` and `fetch` before relying on its profile. Use the focused `entity-evidence` workflow for ambiguous names or a deep profile question. Treat Azimuth facts and graph paths as dated evidence or research leads within their stated coverage.
- Separate peer roles: operating and financial peers support financial benchmarks; funding-market peers reveal possible doors; program analogs inform the case; capital-stack neighbors reveal instruments and partners. Explain why each suggested peer belongs. Use `compare_org_financials` when available for selected EINs and filing years; it returns filing metrics and coverage, not an approved cohort or fundraising target. If it is unavailable or incomplete, inspect primary filings with the host assistant's native tools. Do not create a target or peer band from grant-edge totals.
- Use `find_peer_funders` only for peers the user has named or selected. Its output is historical grant observation and a discovery lead. Follow `peer-funding-comparison` for that narrow step. Keep operating grants, public funding, bank support, project capital, intermediaries, and donor channels in separate lanes.
- For current eligibility, program fit, application route, dates, people, and recent deals, use the host assistant's native web search when available. Inspect official or other primary sources and cite the page actually checked. An old filing, graph edge, or generated search summary does not establish a current opening or warm introduction.
- A peer-only grantor is a lead to investigate, not a ranked prospect. Before ordering outreach or recommending an application, verify the funding instrument, current program and geography, application or relationship route, and fit with the organization's specific case on primary sources. If those checks are missing, rank the *research checks* instead. Do not label a warehouse grant edge as project capital or an operating grant without instrument evidence.

## Help the user make the next decision

At each turn, give the strongest supportable working position, the source or assumption behind it, the viable choices and tradeoffs, and one useful next decision or research check. Distinguish observed facts, user statements, inference, recommendations, and unresolved gaps. A peer benchmark informs a goal; the user chooses the goal and route mix. A prospect list is not the strategy until fit, access, effort, capacity, and timing have been considered.

Use Azimuth to augment the evidence, and use the host assistant's own research and document abilities for sources outside its coverage. Retrieve public information before asking the user to find it. Ask the user for private capacity, costs, relationships, or judgments that materially change the plan. When asked for recommendations, make a provisional choice with a reason and assumptions; do not end with an unchosen menu. Mark decisions as accepted only when the user accepts them.

Keep accepted peers, set-asides, chosen lanes, and reasons legible so follow-ups can revise them. Follow connection boundaries rather than assuming a workspace/inbox exists. Private strategic decisions stay in the requested artifact/conversation; label their provenance and keep them out of public graph claims.

## In ChatGPT

GrantData is used through the Apps connection; users mention @GrantData in a conversation. Treat the selected public connection as the scope of a GrantData answer. Every public tool is read-only. Do not use private mail, file, or consulting-source connectors to answer a GrantData-scoped request, even when the host account has access to them. If the user wants separate private-source research, distinguish that work and its source from GrantData's public evidence.

Use ChatGPT's native web search for currentness checks and original sources, and cite the page actually checked.

Routine lookups return text-first results. The peer-funder comparison can render a table component when the host supports app views; still summarize the strongest patterns and the coverage limit in prose.

The guides are available as plugin skills and through `list_research_workflows` and `get_research_workflow`.

Use ChatGPT's document abilities for a packet when the user asks, and state that nothing was saved to GrantData. The owner connection may expose a save tool, but it is outside the public plugin's capability. Never switch to it to satisfy a public connection save request or represent a needs-review candidate as graph publication or permanent strategy memory.

The public connection cannot email a funder or submit an application. If asked, state this limit and offer a draft after verifying the intended funder and opportunity. Historical grant observations alone do not establish a live application route.
