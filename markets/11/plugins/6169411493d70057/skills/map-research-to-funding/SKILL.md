---
name: map-research-to-funding
description: Map a research topic to the DoD budget lines and organizations that fund similar work.
---

Use this when someone describes a research or technology area and wants to know where defense money for it sits.

1. Call `get_defense_budget` with `query` set to program title words from the topic (or a program element code) to find related RDT&E, procurement and O&M budget lines.
2. For each relevant line, report its title and program element exactly as the budget book prints it, the organization, and the dollars by fiscal year as labeled (request, enacted, actual). Say when a figure mixes reconciliation or mandatory money if the tool reports it.
3. The tool's growing/shrinking movers compare the enacted year with the latest request. Say so when you use them: an enacted figure can include congressional adds or reconciliation money, so where a line shows two requests, describe growth request to request instead.
4. Present the dollars as program-element totals, not money spent on the user's specific topic, and list the lines as candidates to investigate.
5. If the user names a company, use `get_budget_exposure` (account required) to see which of those accounts have funded its awards.
