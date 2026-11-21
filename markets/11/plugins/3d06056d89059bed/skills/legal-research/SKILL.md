---
name: legal-research
description: Use Jus Mundi's legal research tool for questions about international law, arbitration, treaties, institutional rules, national laws, and scholarly publications.
---

# Jus Mundi legal research

For legal research questions about international arbitration, investment law, and related areas of international law, use the `jusmundi_legal_research` MCP server's `legal_research` tool. If the question is ambiguous, ask one focused clarifying question first. Pass the user's question in the `query` field.

Ground the answer in the returned research. Preserve its numbered citation links, and include the source titles and links from `citations`, with excerpts when provided. Briefly explain why the most relevant sources matter. Do not answer legal questions from model knowledge alone, and do not invent authorities, treaty articles, or citation details. Treat `reasoning_steps` as a summary of the research process, not as legal conclusions. If the tool returns no relevant source or an error, say so clearly.
