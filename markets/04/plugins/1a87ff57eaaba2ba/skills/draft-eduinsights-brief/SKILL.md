---
name: draft-eduinsights-brief
description: Turn EduInsights college, field, career, workforce, accreditation, or AI-use research into a concise decision brief for a provost, dean, workforce leader, policymaker, or advisor. Use when the person asks for a briefing, memo, recommendation, comparison summary, or decision-ready synthesis rather than a raw data answer.
---

# Draft an EduInsights brief

Build the brief from verified evidence. If the provided research lacks a material measure, source, period, or comparison, use the EduInsights tools to fill that gap before drafting.

## Set the decision

Identify:

- who will use the brief;
- the decision they need to make;
- the options or entities under consideration;
- the period and geography;
- the evidence that would change the decision.

Ask a question only when the missing choice would materially change the recommendation.

## Research proportionately

Use `edu_resolve_entity` for names. Prefer `edu_get_institution`, `edu_get_program`, `edu_get_occupation`, `edu_compare`, and `edu_aggregate`. Use `edu_get_sources` to verify releases. Use SQL only for a necessary question the focused tools cannot answer.

Do not fill gaps with assumptions. Mark an important unanswered part as an evidence gap and explain what source would resolve it.

## Draft the brief

Read [brief-template.md](references/brief-template.md). Use only the sections that help the decision.

Lead with the decision and the strongest supporting finding. Keep findings separate from judgment. Tie every figure to a year and source. Translate internal data terms into ordinary language.

Do not show codes, relation names, or SQL unless the audience needs a reproducible appendix.

## Check the result

Before finishing:

1. confirm the recommendation follows from the cited evidence;
2. confirm comparisons use aligned periods and measures;
3. state the strongest alternative explanation or limit;
4. distinguish reported degrees from current catalog programs;
5. distinguish related careers from graduate destinations;
6. distinguish observed AI use from employment forecasts;
7. make the next action specific and proportionate to the evidence.
