---
name: horoscope-action-plan
description: Turn a daily, weekly, monthly, or yearly horoscope into a practical reflection plan. Use when the user asks to plan, reflect, set intentions, or choose grounded next steps from their horoscope. Call the horoscope app when the requested view is not already present, and never claim access to its private horoscope sections.
---

# Horoscope Action Plan

Use the `horoscope` tool to show the requested horoscope, then build a plan only from themes the user chooses or shares.

## Inputs

Resolve these inputs from the conversation:

- the user's star sign
- the requested period: daily, weekly, monthly, or yearly
- an optional focus such as work, relationships, energy, or social life
- any horoscope wording the user has quoted or paraphrased

If the user provides only a birthday, derive or confirm the standard Western tropical star sign. Always pass `starSign`; the tool does not infer it from `dateOfBirth`.

## Workflow

1. Ask only for a missing star sign or a materially ambiguous period. Treat “today” as daily, “this week” as weekly, “this month” as monthly, and “this year” as yearly.
2. Map the period to its exact route:
   - daily: `horoscope/daily`
   - weekly: `horoscope/weekly`
   - monthly: `horoscope/monthly`
   - yearly: `horoscope/yearly`
3. If the requested horoscope is not already displayed, call `horoscope` with the resolved `starSign`, route, and a concise `reason`. Include `dateOfBirth` only when the user supplied a complete valid `YYYY-MM-DD` date.
4. Explain that the widget contains Love, Work, Energy, and Social panels. Ask the user which panel or message they want to act on and have them quote or paraphrase it. Skip this question when they already supplied the relevant wording.
5. Convert only the user-provided theme into:
   - one grounded intention
   - one small next action
   - one boundary or condition that keeps the action realistic
   - one later check-in question
6. Keep the plan proportional to the requested period. A daily plan should be immediately actionable; longer periods may use milestones.

## Output

Return a compact plan with the sign and period, the user-selected focus, the next action, the boundary, and the check-in question. Clearly distinguish the user's horoscope theme from your planning suggestions.

## Boundaries

- The model-visible tool output contains the selected sign and route, not the horoscope prose. Never invent, quote, summarize, or imply access to the private panel text.
- Treat astrology as a reflection prompt, not a factual prediction or a basis for medical, legal, financial, or safety-critical decisions.
- Do not call the app merely for general planning advice when the user does not want a horoscope-based workflow.
