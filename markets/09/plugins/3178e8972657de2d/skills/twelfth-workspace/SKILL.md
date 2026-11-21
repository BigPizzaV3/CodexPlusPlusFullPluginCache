---
name: twelfth-workspace
description: Answer questions about a Twelfth retail workspace (products, suppliers, sales, inventory, pricing, projects, members and open actions) using the Twelfth MCP tools. Use when the user mentions Twelfth, their workspace, or asks about their own retail or category data.
license: MIT
metadata:
  author: Twelfth
  version: "1.0.0"
  tier: twelfth
---

# Working with a Twelfth workspace

Twelfth is a commercial workspace for retail and category teams. The Twelfth MCP
server connects to **one** workspace, as the person who approved the connection,
with the tools they chose on the consent screen.

## Start with context

1. Call `twelfth_get_workspace` first to learn which workspace is connected and
   what it has switched on. Name that workspace in your answer.
2. If `twelfth_get_preferences` is offered, read it before formatting money,
   dates or units, so the answer follows the workspace's own settings rather
   than a guess.
3. The tool list differs between workspaces and connections. Use what is
   offered. If a needed tool is missing, say which one and that it can be
   approved by reconnecting from **Settings → AI & agents** in Twelfth.

## Read carefully

- **Reads by default; changes only when allowed.** The write tools
  (`twelfth_create_action`, `twelfth_complete_action`, `twelfth_snooze_action`,
  `twelfth_run_routine`) are offered only if the person ticked **Allow changes**
  when connecting, and act only on their own actions and routines. Call one only
  when the user asks for that change, then say what changed. Never claim a
  change no tool made. No tool raises an order or changes a price. When a write
  tool isn't offered, tell the user where to make the change in the Twelfth
  app, or that they can reconnect with **Allow changes** ticked.
- **An empty result is not proof of absence.** It can mean the person lacks
  access to that part of the workspace (a category, remit or capability), or
  that a filter was too narrow. Say which you can't rule out, instead of saying
  "there are none".
- **One workspace only.** Don't speculate about other workspaces or other
  companies' data.
- Quote names, SKUs, dates and owners as returned. Don't invent people,
  products, prices or figures, and label any calculation you do yourself.

## Shape the answer

- Lead with the answer, then the evidence: which tool, which records.
- For actions, include the due date and assignee when present, and say when an
  action has no assignee.
- For pricing and stock, give the as-of time the tool returned. Competitor
  prices are last-seen observations, not live quotes.

More: https://twelfth.ai/developers/mcp
