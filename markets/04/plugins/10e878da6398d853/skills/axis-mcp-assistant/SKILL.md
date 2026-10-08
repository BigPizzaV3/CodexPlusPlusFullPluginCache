---
name: axis-mcp-assistant
description: Use when a user asks an AI assistant to read, create, update, organize, analyze, or delete data in Axis through its MCP connection.
---

# Axis MCP Assistant

Use Axis as a personal operating system. Work only with the signed-in user's
data and only within the five Modules: Finance, Network, Knowledge, Habits,
and Focus.

## Operating rules

- Identify Module and requested operation before calling a tool.
- Use read tools first when an ID, current value, or existing record is needed.
- Use exact values supplied by the user. Never invent amounts, dates, names,
  categories, or progress.
- Pass IDs returned by earlier calls into dependent calls; do not guess IDs.
- Keep multi-step requests ordered: create parent, then create dependent data;
  read after mutation when user asks to verify.
- Treat each tool's `result` field as authoritative. MCP results use the shape
  `{ "result": ... }`.
- Explain validation, permission, Free-plan, or Pro-plan errors in plain
  language. Do not retry a rejected mutation with altered user data.
- Never infer or expose data belonging to another individual account.
- Never request, store, or repeat passwords, payment-card data, OAuth tokens,
  or secrets.

## Module routing

| User intent | Module |
| --- | --- |
| Income, expenses, investments, budgets, savings, portfolio | Finance |
| People, relationships, interactions, contact history | Network |
| Books, articles, courses, sources, reading sessions, progress | Knowledge |
| Habits, completions, streaks, consistency, trends | Habits |
| Focus categories, tasks, sessions, pomodoros, heatmaps | Focus |

If intent spans Modules, complete each Module's calls separately and label
results clearly.

## Mutation guidance

- Create: validate required fields from the tool schema; report returned ID.
- Update: read the target when necessary, send only requested changes, then
  report the resulting record or acknowledgement.
- Single delete: perform only for the explicitly identified record; report what
  was removed.
- Bulk replace/delete: summarize target and scope before calling; never widen
  the selection beyond the user's request.
- Analytics: state date/range filters and distinguish zero from missing data.
- Investment actions: preserve ticker, asset class, action, quantity, price,
  currency, FX rate, fees, brokerage, and notes exactly as supplied.

## Good interaction pattern

1. Restate requested change briefly, including Module and target.
2. Read current data if needed to resolve IDs or ambiguity.
3. Call smallest complete sequence of tools.
4. Summarize created/updated/deleted records and any returned IDs.

Ask one concise clarification when required input is genuinely ambiguous.
Do not ask for confirmation for routine reads or single-record edits/deletes
that user explicitly requested.
