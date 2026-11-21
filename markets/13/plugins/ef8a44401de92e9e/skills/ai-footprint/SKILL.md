---
name: ai-footprint
description: Answer questions about the environmental impact of AI with sourced figures from EcoGPT's tools. Use when the user asks how much electricity, carbon or water AI prompts use, how AI compares with everyday activities, or asks about EcoGPT itself, such as how it plants trees or whether it is legitimate.
---

Explicit user instructions have priority over this skill.

## Estimate a person's AI use

1. Call `estimate_ai_footprint` when the user gives a number of AI text prompts. Pass `prompts_per_day` and the `period` that the user asks for: `day`, `month` or `year`. Pass `grid` only when the user names a grid that the tool lists.
2. If the user does not give a number, ask how many prompts they send on a typical day. Do not guess it.
3. Give the low-to-high ranges for energy, carbon and water that the tool returns. Say that they are estimates between two published figures, and name the sources.

## Answer from the guides

1. Call `search_ai_environment_guides` with the words of the topic.
2. Before you quote a figure, call `read_ai_environment_guide` with the `url` of the best match.
3. Answer with the figures in the guide. Name the guide, its sources and the date it was updated.
4. If no guide is about the question, say so.

## Limits

- Use only figures that a tool returns.
- `estimate_ai_footprint` is for AI text prompts only. Do not use it for flights, cars, images, video or reasoning modes.
- The tools read no account and change nothing. Do not say that a tree was planted or funded for the user, and do not give a tree count for an account.
