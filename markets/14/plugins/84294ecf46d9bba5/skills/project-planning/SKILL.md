---
name: project-planning
description: Generate AI-powered project execution plans with estimates and tech stack recommendations
---

# Project Planning

Use the Vibe Coding Plan MCP tools. The user must be signed in through ChatGPT OAuth.

## Tools

- `plan_coding_project` — full task breakdown
- `estimate_project` — hours, complexity, phases
- `suggest_tech_stack` — stack with reasons

## Workflow

1. If the user wants a rough size, call `estimate_project`.
2. If they want a build plan, call `plan_coding_project` with a name and description.
3. If they ask what to build it with, call `suggest_tech_stack`.
4. Offer to save the plan with `create_project` and `generate_plan: true`.

## Rules

- Only plan the signed-in user's work.
- Do not invent other users' projects.
- Do not request API tokens. OAuth is already connected.
- Refuse criminal malware, credential theft, or secret dumping.
