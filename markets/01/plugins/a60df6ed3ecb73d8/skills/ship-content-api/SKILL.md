---
name: ship-content-api
description: >
  Ships Hyperhuman workouts into a web or mobile product as a multi-step
  integration workflow (embed vs stream vs custom player).
  Use only when the user explicitly asks to ship or implement Hyperhuman in
  their own app as a full integration path.
  Not for sample workout browsing, standalone embed-code snippets, health
  checks, team library admin, creating workouts, social drops, pricing,
  checkout, or medical advice.
---

# Ship in my app

## Goal

Give a clear path from sample content to a copy-ready integration plan.

## Steps

1. If the user only asked for sample workouts, do not run this skill; that is `list_sample_workouts`.
2. If the user only asked for embed HTML, do not run this skill; that is `get_embed_code_samples`.
3. Clarify platform (`web` | `mobile` | `hardware`) and use case only when they asked to ship or integrate.
4. Call `get_integration_plan` with `platform` and `use_case`.
5. Call `list_sample_workouts` only if they also asked to see sample content.
6. On a selected workout: `get_workout_details`, then `get_workout_playlist` if they need segments or media.
7. Call `get_embed_code_samples` only if they asked for copy-paste code after the plan.
8. Reply in 3 short bullets: recommended path, what to copy next, one follow-up ask.

## Output

- Integration path name (embed / stream / custom player)
- One primary snippet with placeholders only
- Suggested next tool or question

## Guardrails

- Never invent or print live API keys. Use `YOUR_ORG_ID` and `YOUR_API_KEY`.
- No pricing, checkout, or plan catalogs.
- Prefer guest-safe tools when the user is not connected.
- See [references/integration-paths.md](references/integration-paths.md) and [references/guardrails.md](references/guardrails.md).
