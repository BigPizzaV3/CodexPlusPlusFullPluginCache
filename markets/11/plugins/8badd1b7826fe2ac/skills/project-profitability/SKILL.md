---
name: project-profitability
description: Project profitability and risk from Hubity. Use when someone asks which projects are losing money, which are at risk, or how profitable a project is. Reads only.
---

# Project profitability

Shows revenue, cost and margin per project, worst first, and ties it to project health.

## Steps

1. For at-risk questions, call `list_projects` with `status` `active` and `limit` 50, and keep the projects whose `health` is `yellow` (at risk) or `red` (critical); `green` is on track. If 50 projects come back, say the answer covers the 50 most recently updated active projects.
2. Call `get_project_profitability`. Pass `projectId` for one project, and `from` and `to` as `YYYY-MM-DD` when the person names a period; otherwise it covers each project's life so far. It returns every project, so for an at-risk question keep only the rows whose `projectId` matches an `id` kept in step 1.
3. Answer with:
   - For an at-risk question, every project kept in step 1, with its health, revenue, cost and margin.
   - Projects losing money, worst first, with revenue, cost and margin.
   - Thin margins, under 15 percent, to watch.
   - What to check for each loss. Name a cause only when the figures show it, such as cost with nothing billed yet; otherwise offer the usual ones to look into: time not yet billed, or a fixed fee that has run over.
   - What to do this week.

## Rules

- Revenue is what was billed. Cost is logged time at each person's cost rate, or the bill rate where no cost rate is set. Say so when it matters.
- Never invent figures. If a tool is refused for the person's role, say so.
