---
name: deep-research
description: Run a CitedEvidence Deep Research report and bring its findings into the conversation. Use only when the user explicitly asks for in-depth research, a research report or a literature review that needs many sources.
---

# Deep Research

Deep Research takes several minutes and uses credits from the user's CitedEvidence account. Don't start it for questions a few `search_papers` calls can answer.

1. Agree the question and scope with the user (population, time frame, region, outcome) in one short exchange if it is vague.
2. Call `start_research` with the full question and `depth: "standard"`. Use `"deep"` only if the user wants a broader, longer study.
3. Tell the user it has started, roughly how long it takes, and that the card shows progress. They can keep chatting.
4. When the user asks, or later in the conversation, call `get_research` with the `research_id`. If it's still running, report the progress. When it's finished, summarise the key findings with their citations and link the full report.
5. If the account doesn't have enough credits, state that plainly. Don't suggest buying credits or upgrading.

`list_my_research` shows earlier reports from the user's History.
