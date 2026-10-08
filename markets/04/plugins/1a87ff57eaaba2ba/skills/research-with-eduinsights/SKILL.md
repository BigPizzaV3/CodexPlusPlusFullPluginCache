---
name: research-with-eduinsights
description: Research U.S. colleges, reported fields and credentials, enrollment, completions, outcomes, accreditation, careers, occupational tasks, pay, outlook, and observed AI use with the EduInsights MCP tools. Use for factual questions, rankings, comparisons, and program-to-career questions that need public evidence. Also use when deciding which EduInsights tool should answer a question. Do not claim current catalog courses or requirements from this data.
---

# Research with EduInsights

Answer the person's question with the smallest suitable read-only tool path. Keep every claim connected to its source, period, and level of detail.

## Start with the question

Identify these parts before calling a tool:

- the named college, field, credential, occupation, task, or place;
- the measure the person means;
- the requested period or whether current accepted evidence is enough;
- whether the task is a focused lookup, comparison, grouped result, history, or source check.

If a named entity is ambiguous, resolve it. Ask the person only when ranked candidates remain genuinely ambiguous.

## Route the work

Read [tool-routing.md](references/tool-routing.md) before the first tool call in a conversation. Follow its focused-tool-first route.

For a cross-domain question or any question about what the evidence can establish, also read [question-to-evidence.md](references/question-to-evidence.md).

For SQL or a complex aggregation not covered by a focused tool, read [query-recipes.md](references/query-recipes.md) before calling `edu_run_sql`.

## Preserve meaning

- Keep the person's ordinary concept as the target. Do not rename an AI question into a Claude-only question.
- When Anthropic is the only relevant empirical source, use it as the best available AI-use evidence. State the product, population, period, and release.
- Treat reported degrees as historical reporting evidence, not proof of a currently offered named program.
- Treat field-to-career links as preparation paths, not observed graduate destinations.
- Treat observed AI use as behavior evidence, not a forecast of job loss, productivity, or wages.
- Treat broader field or national evidence as context for a narrower question. Label that broader fit instead of presenting it as direct evidence.
- Never turn a blank into zero. Use the supplied coverage reason.

## Verify before answering

Check that:

1. every name was resolved to a canonical identifier before filtering;
2. every figure retains its period and source or release;
3. compared figures use compatible measures, populations, places, and periods;
4. sums use additive measures only;
5. medians, wages, rates, scores, years, and overlapping source packages were not summed;
6. the answer states important boundaries once, close to the affected claim.

## Write the answer

Read [answer-contract.md](references/answer-contract.md) before producing the final response.

Lead with the answer. Use readable names rather than internal relation names. Show identifiers only when requested or needed for disambiguation. Pair every shown identifier with its label.

Finish only when the result includes the finding, the relevant year or period, the source scope, and the limit that would change a decision.
