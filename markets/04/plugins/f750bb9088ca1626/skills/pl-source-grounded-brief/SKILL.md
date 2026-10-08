---
name: pl-source-grounded-brief
description: Produce concise source-grounded briefs, memos, and partner/customer prep notes from Partnership Leaders MCP findings with clear evidence, caveats, and follow-up questions.
---

# Partnership Leaders Source-Grounded Brief

Use this skill when a user asks for a brief, memo, customer prep note, executive summary, or point of view based on Partnership Leaders research. Assume the reader is a senior partnership leader who wants a judgment they can act on or put in a slide, backed by named companies, dates, and figures.

Briefing rules:

- Use the MCP server to gather evidence before drafting.
- Prioritize high-signal findings by tier, recency, and relevance to the user's question.
- Lead with the judgment a partner executive would repeat, not a description of what the brief covers.
- Surface notable companies, competitors, and adjacent ecosystem players when the user asks a broad question.
- If the prompt names a company, center that company and use one or two named peers only when evidence supports the comparison.
- Treat `insight_si`, `ec75`, and `aip` as internal routing only. Do not expose dataset names, significance labels, cadence, coverage notes, or provenance footers in the final answer unless the user asks an admin/testing question.
- Use finding ids and source URLs to verify claims before writing.
- Keep recommendations clearly labeled as interpretation.
- Preserve uncertainty when evidence is mixed or limited.
- Copy program names, dates, and figures from returned records; do not rely on memory.
- Use day-level dates only when the returned records carry them.
- Include cross-company synthesis when supported, but make every count auditable by naming each company in the count.
- Count vendors and programs separately, and do not include announced future programs in counts of completed changes.
- Cover what got harder or was tightened, not only what launched.

Suggested brief structure:

- Start with the executive judgment.
- Explain why it matters for partner strategy.
- Support the judgment with named companies, dates, and figures.
- Include competitive or ecosystem implications when evidence supports them.
- Close with a specific action for the reader.

Style:

- Write continuous analyst prose and format sparingly.
- Use bullets only for four or more genuinely parallel items.
- Avoid bolded label ladders, formula closers, numbered signposts, and generic consulting language such as "robust", "seamless", "landscape", "leverage", and "game-changing".
- Do not invent prior rules or prior regimes just to make a change look bigger.
- Use at most one superlative per answer, and only when the evidence names what it beats.

Security and privacy:

- Never ask the user to paste secrets, API keys, OAuth tokens, or private partner records into chat.
- Treat access control as server-side. The MCP server decides which rows the user can see.
- If a requested answer appears to require data outside the user's entitled scope, state that the server did not return enough evidence.
