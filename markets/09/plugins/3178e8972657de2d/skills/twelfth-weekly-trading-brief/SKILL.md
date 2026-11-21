---
name: twelfth-weekly-trading-brief
description: Write a one-page weekly trading brief from a Twelfth workspace using the Twelfth MCP tools - overdue and due actions with owners, the suppliers with the most open recommendations, stock and cover pressure, where prices sit against competitors and this week's market moves, ending with the three things to do first. Use when someone asks for "the weekly brief", "Monday trading update", "what needs my attention this week", "trading summary", "week in review" or a brief focused on one category, supplier or remit. Needs the Twelfth MCP server connected.
license: MIT
metadata:
  author: Twelfth
  version: "1.0.0"
  tier: twelfth
---

# Weekly trading brief

A brief a category manager can read in two minutes on Monday: what is due, where
the pressure is, what moved in the market, and what to do first. Every figure
comes from a Twelfth tool, with the tool and as-of date stated.

For first-time setup and general workspace questions, see the `twelfth-workspace`
skill. This skill is the brief only.

## Before you start

- **The tool list varies by workspace and connection.** Use what is offered.
  If a step's tool is missing, skip the section and say which tool was not
  available, rather than filling it from memory.
- **An empty result can mean no access**, not nothing there. A connection reads
  only its remits. Say "none visible to this connection", not "none".
- **Whole-business tools vs snapshot tools.** `twelfth_list_products`,
  `twelfth_get_products`, `search_catalogue` and `find_supplier` read the
  workspace within the connection's remits. The `get_*` snapshot tools
  (`get_sales_metrics`, `get_inventory_position`, `get_product_ranking` and the
  rest) read only the open work unit. Do not present a snapshot ranking as the
  top of the business.
- **No week-on-week series.** Product figures are current (for example units
  last four weeks), not a weekly history. For a change on last week, read last
  week's brief with `list_reports` / `read_report`. Otherwise do not claim a
  movement.

## Steps

### 1. Frame the week

Call `twelfth_get_workspace` for the name, timezone and currency. State the week
as dates in that timezone (for example "Mon 19 Oct to Sun 25 Oct 2026, AEDT").
Format money in the workspace currency. If `twelfth_get_preferences` is offered,
read display defaults before formatting.

If a **focus** is given (category, supplier or remit), resolve it first:
category with `twelfth_list_category_settings`, supplier with `find_supplier`.
Use the resolved names and IDs as filters in every later step.

### 2. Actions due

Call `twelfth_list_open_actions`. Split into **overdue** and **due this week**,
each with owner and due date. Call out actions with no assignee. Group by owner
if there are many. The list is capped at 100; say so if it comes back full.

### 3. Suppliers awaiting action

Call `find_supplier` with `order_by: "open_recommendations"` and `limit: 5`.
Give each supplier's open recommendation count and catalogue size. For the top
one, `search_catalogue` with `supplier_name` and `only_recommended: true` shows
which lines.

### 4. Stock and cover pressure

Use `twelfth_list_products` (filtered by the focus if given):

- `sort: "cover", dir: "asc"` for the lowest cover. Lines with null cover are
  unmeasured, not zero; leave them out of the ranking and say how many.
- `sort: "units_l4w", dir: "desc"` for the top sellers. Flag any top seller with
  low cover and nothing on order.
- `sort: "days_since_sold", dir: "desc"` for slow lines holding stock, if the
  brief is meant to cover aged stock.

Keep it to the five most material lines per list.

### 5. Market and pricing

If `price_intel_summary` is offered, call it (window 4 unless asked) for the
price index by competitor. Index is our price ÷ theirs × 100: 100 is parity,
above 100 we are dearer. Then call `price_intel_observations` for this week's
detected moves. Prices are observed, not live: give the as-of date and say a
large single-retailer drop may be a listing error until another retailer
follows. For deeper pricing work use the `twelfth-competitor-pricing` skill.

### 6. Optional sections

Add only if the tool is offered and the section has something in it:

- **Projects:** `twelfth_list_projects` ordered by overdue tasks.
- **Routines:** `twelfth_list_routines` for last runs. A shadow routine
  publishes nothing; do not report its output as raised tasks.
- **Calendar:** `get_planning_calendar` for promotions or key dates in the next
  two to four weeks (it needs one remit).
- **Last week:** `list_reports` then `read_report` to carry open actions forward
  and compare figures.

### 7. Three things first

Close with three actions, each tied to a figure above and an owner where known.
Rank by money or customer impact, not by the order the tools were called.

The layout is in `references/brief-template.md`.

## Answer shape

1. **Headline.** One or two sentences: the week's main call.
2. **Sections** in the order above, each short, each with its source line
   (`Source: twelfth_list_open_actions, as of 19 Oct 2026 09:10 AEDT`).
3. **Unknowns.** Tools not offered, sections skipped, figures that are null, and
   anything the connection may not see.
4. **Three things first.**

Quote names, SKUs and owners as returned. Label any arithmetic you did yourself.

## Making changes

Write tools appear only if the person ticked **Allow changes** when connecting,
and they act only as that person. Use them only when asked:

- `twelfth_create_action` to log a follow-up from the brief (each call makes a
  new action; do not retry by calling again).
- `twelfth_snooze_action` to push an action to tomorrow or next week.
- `twelfth_complete_action` to mark an action done.
- `twelfth_run_routine` to run one of their own routines now.

Never claim a change no tool made. No tool raises an order or changes a price;
those happen in the Twelfth app.

More: https://twelfth.ai/developers/mcp
