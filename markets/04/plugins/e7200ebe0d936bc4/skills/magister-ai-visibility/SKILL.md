---
name: magister-ai-visibility
description: Track and report how a brand appears in AI-generated answers — ChatGPT, Claude, Gemini, Perplexity, and Google AI Overviews — using Magister AI-visibility prompt sets. Use when the user asks about AI visibility, GEO, generative engine optimization, whether AI assistants mention or recommend their brand, or wants to run or read a visibility report.
---

# Magister AI visibility (GEO)

An **AI-visibility set** is a group of tracked prompts — the questions a brand's
buyers actually ask. Magister runs each prompt against several AI answer engines
and scores how the brand appears. Each execution of a set is a **round**, and
comparing rounds over time is the point of the product.

Resolve `project_id` from `list_projects` first; never guess one.

## Reading existing visibility

1. `list_ai_visibility_sets` — the project's tracked sets.
2. `get_ai_visibility_set` — one set's prompts, rounds, and latest scores.
3. `render_ai_visibility_report` — a readable score summary plus an interactive
   report with the trend across rounds, scores by AI model, and per-prompt
   detail.

Prefer `render_ai_visibility_report` when the user wants to *see* how they are
doing. Call it once; it needs no polling and performs no network fetches of its
own.

## Rounds that are not comparable are deliberately excluded

The trend only charts rounds measured the same way. A round that was scored
against a different set of models, or that failed to measure enough of its
prompts, is **left out of the trend on purpose** rather than averaged in.

So the chart can legitimately show fewer points than the raw round count. That
is correct behavior, not missing data. Do not describe it as an error, and do
not try to reconstruct the excluded rounds.

## Running a new round costs credits

`run_ai_visibility_set`, `create_ai_visibility_set`, and
`suggest_ai_visibility_prompts` all **spend the organization's credits**.

Before starting one, tell the user it is a metered run. If they only want to
know their current standing, read the existing set instead — reads are free.
`get_credit_balance` reports the balance and whether metered tools are currently
blocked.

## Rounds are asynchronous

`run_ai_visibility_set` starts a round; it does not return scores. Poll
`get_ai_visibility_set` until the round reaches a terminal state.

Never start a second round because the first has not finished — that spends
credits again for the same answer. Rounds take minutes, not seconds; tell the
user it is running rather than waiting silently.

## Creating a new set

Use `suggest_ai_visibility_prompts` to generate site-grounded prompt candidates,
show them to the user, and create the set only from prompts they accept.
`create_ai_visibility_set` can start the set's first round immediately, so say
that before calling it.

Write prompts the way a buyer would ask them — a category question the brand
should win, not the brand's own name alone.

## Do not infer

- Never state a visibility score, a change, or a model's answer the tools did
  not return.
- Never claim a brand is or is not mentioned by an AI assistant without a round
  that measured it.
- If a tool reports the organization is out of credits, say plainly that they
  need to upgrade, and stop. Do not retry and do not reach for another metered
  tool.
