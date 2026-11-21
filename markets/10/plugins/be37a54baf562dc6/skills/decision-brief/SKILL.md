---
name: decision-brief
description: Turn Sovrnti benchmark results into a short decision brief for an executive, a board, a security lead or a procurement team, with the sources stated. Use it when the user asks for a summary, a memo, a board paper or a recommendation based on Sovrnti results. An example is "write a one-page brief for our CIO on collaboration suites in Germany".
---

# Write a decision brief

Explicit user instructions take priority over this workflow, including on length and format.

## Inputs

Ask at most two questions, and only for what is missing:

- **Audience.** For example a CIO, a CISO, a board or a procurement team.
- **Decision.** For example choose a product, narrow a list, keep the current product or migrate.
- **Scope.** A market, or two or three named products, and the place: a country, a region or "world".

## Steps

Gather the facts with as few calls as possible. Deeper views use the user's Sovrnti credits.

- **A whole market:** `sovrnti_market_get_snapshot`. Add `sovrnti_market_get_sovrntimax` if sovereignty is a hard requirement.
- **Named products:** `sovrnti_product_compare`.
- **A specific "why" question:** `sovrnti_qq_sherpa`. It answers only from what Sovrnti has scored and returns citations.

Use the same place in every call. If results from earlier in the conversation already cover the scope, reuse them.

## Output

Keep it to about 400 words unless the user asks otherwise.

1. **Title and date.**
2. **The decision,** in one line.
3. **Options,** one line each with its trade-off. Recommend one only if the results clearly support it, and say why.
4. **Evidence.** A short table with the scores the tools returned.
5. **Risks and what to verify.** Contract terms, configuration choices, and anything the results do not cover.
6. **Sources.** "Source: Sovrnti, <date>", with the views used.

## Rules

- Use only facts the tools return. If the brief includes your own reading of the results, label it as your assessment, not as Sovrnti's.
- Sovrnti's terms allow short extracts in internal documents such as board papers, with "Source: Sovrnti" and the date. Do not reproduce full result sets for publication.
- Use plain language. Put numbers before adjectives.
- If a tool returns an error, say so and state what the brief could not cover.
- If a tool says the user has no credits left, pass its message on as it is. Do not suggest a workaround.
