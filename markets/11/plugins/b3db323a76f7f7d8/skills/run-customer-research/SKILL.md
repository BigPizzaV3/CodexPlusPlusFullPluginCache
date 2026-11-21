---
name: run-customer-research
description: Use Askli when the user wants to validate a product idea, understand a customer audience, run customer interviews, prepare or continue an Askli study, check study progress, or review evidence-backed research findings. Do not use for generic factual research, writing help, or requests unrelated to customer and product decisions.
---

# Run customer research with Askli

Use Askli's MCP tools to turn the user's product decision into a customer interview study and carry it through to evidence-backed findings.

## Start or continue a study

- For a new study, pass the user's complete research request to `create_study` in their own words. Preserve material audience, product, market, behavior, geography, timing, buyer/user, and business constraints. Do not shorten, improve, broaden, or silently reinterpret the input.
- Present every Askli clarifying question exactly as returned. Never answer a clarification on the user's behalf. Send only the user's own answer with `answer_clarification`.
- When the user refers to an existing or latest study without an ID, use `list_studies` and `get_study_status` to identify it. If multiple studies plausibly match, ask the user which one they mean.

## Review and approve the plan

- Use `get_plan` to show the objective, audience, method, sample, material requirements, recruiting feasibility, and any limitations.
- Make explicit which audience requirements are supported, screened, inferred, unknown, or currently unsupported. Never weaken or broaden an audience to make recruiting appear possible.
- Use `update_plan` only for changes the user asks for.
- Use `confirm_plan` only after the user clearly approves the plan. Approval of an idea is not approval of a research plan.

## Participants and recruiting

- Use the plan's recruiting feasibility to explain what Askli can and cannot support. If Askli cannot recruit the exact audience, say so plainly and preserve the study setup. Do not manufacture an executable study or claim readiness.
- Participant setup, paid participant capacity, assisted recruiting, and checkout are unavailable through this plugin. Direct the user to the full Askli study link returned by Askli if they want to continue in the web app.
- Do not quote prices, promote paid services, return checkout links, or request participant names, email addresses, payment details, or authentication codes in chat.

## Progress and findings

- Studies are asynchronous. Use `get_study_status` once when asked, report the current state and next action, and do not poll.
- Use `get_findings` for a completed or partially analyzable study. Preserve Askli's qualitative counts, confidence, caveats, contradictions, unknowns, recruiting limitations, and evidence links. Do not add conclusions or raise confidence.
- Use `get_transcript` only when the user asks to inspect supporting or contradictory evidence. Quote only what Askli returns and retain the source link.
- Use `analyze_now` only when the user explicitly asks to analyze the evidence currently available. Repeat Askli's small-sample or incompleteness caveats.

Finish with the most useful next action and the Askli review or participant link returned by the tools when one is available.
