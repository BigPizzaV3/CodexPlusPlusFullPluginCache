---
name: ai-visibility-audit
description: Audit how AI answers talk about the user's brand, using Proofsource data. Use when the user asks whether AI mentions their brand, who AI recommends instead of them, which sources AI cites, or what changed in their AI visibility.
---

# AI visibility audit

Answer with Proofsource's measured data only. Never guess a number. Every claim names the tool result it came from.

## Steps

1. **Pick the brand.** Call `list_brands`. One brand: use it. Several: ask which one, unless the user already named it.
2. **Visibility.** Call `get_visibility` with `by: "engine"` (default 30-day window). Note the overall mention rate, each engine's rate and the change against the previous period.
3. **Competitors.** Call `get_competitors`. Note the top 3 by share of voice and any that gained since the last period.
4. **Sources.** Call `get_citations`. Note the domains AI cites most for this brand's questions, and whether the brand's own site is among them.
5. **Changes.** Call `get_changes`. Note the visibility trend over the window, meaningful changes on competitors' websites and new pages about the category.
6. **Weak questions.** When visibility is low on an engine, call `get_visibility` with `by: "question"` and name the 3 questions where the brand is missing.

## Report

Write a short report in this order:

- **Headline:** one sentence with the overall mention rate and its change.
- **By engine:** a small table (engine, mention rate, change).
- **Competitors AI recommends instead:** top 3 with their share of voice.
- **Sources AI trusts:** top 5 cited domains.
- **What changed:** up to 3 bullet points.
- **Proof:** for each number, the tool and window it came from (for example "get_visibility, last 30 days"). Link the `open_url` from the results so the user can check every answer in Proofsource.

End by offering the fix-plan skill: "Want a prioritized plan to close these gaps?"

## Rules

- Say "competitors", never "rivals".
- No prices, plan names or upgrade links.
- If a tool says the workspace has no data yet, say so plainly and stop. Do not fill gaps with estimates.
