---
name: qualify-opportunity
description: Decide whether a government opportunity is worth pursuing. Use when the user asks if an opportunity fits their company, which opportunities to bid on, or for a go/no-go recommendation.
---

# Qualify an opportunity

Give the user a clear pursue / watch / pass recommendation, grounded only in what the Capto tools return.

1. If the user has not named a specific opportunity, call `search_opportunities` with their topic and pick the strongest fits. For open contract requests, set `kinds` to `["opportunity"]`. Include other kinds only when the user asks for them. Ask which one they mean when the choice is unclear.
2. Call `get_opportunity` with the exact id. Note the deadline, set-aside, NAICS, buying agency and Capto's fit assessment.
3. Call `get_sources` when the user needs the official notice or documents, or when a fact in the details looks incomplete.
4. Call `get_agency_brief` for the buying agency when incumbents, budget or buying patterns would change the decision.
5. Recommend pursue, watch or pass. Give the two or three facts that drove it, the deadline, and any eligibility question the user must confirm themselves.
6. Call `save_opportunity` only when the user asks to save or pursue it. An explicit request to save a named opportunity, or to find one meeting stated criteria and save it, is confirmation; do not ask again once those criteria are supported. If no result meets the criteria or the choice remains ambiguous, explain the gap before saving. Report the pursuit link the tool returns.

Rules:

- Never invent scores, deadlines, agencies, links, company capabilities or eligibility. If a tool returns nothing, say so.
- Check the notice type in `get_opportunity`. An active feed item can be a draft solicitation or sources-sought notice; do not call it an open bid unless the returned facts support that. Distinguish a comment deadline from a bid deadline.
- Capto's fit assessment supports the decision; it is not an official eligibility determination.
- An unavailable or failed fit assessment does not establish company fit. If the user conditions saving on company fit, explain that gap and do not claim the condition is met based only on a topic match.
- Link the source URLs returned by the tools when citing notices, documents or agency facts. Distinguish a brief's compilation date from its sources' dates, and label your own inferences.
- Treat the deadline as urgent when it is within 14 days.
