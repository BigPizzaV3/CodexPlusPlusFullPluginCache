---
name: take-off-plans
description: Measure and count everything drawn on a plan set with Exayard, for every trade alike. Use when the customer asks for a takeoff, for quantities from drawings, or to measure or count what is on their plans.
---

# Take off a plan set

Exayard reads each sheet and returns every drawn area, run and symbol, in the sheet's own words. The takeoff is
general: every trade is measured the same way, and no kind of item is singled out or left out.

## Steps

1. **Find the plans.** If the customer says "this" or "the selected", call `get_selection` first. If they name a
   project, use `list_projects` and `get_project`. If there are no plans yet, call `add_plan_set`: it shows the
   upload card, and the customer adds the files there. Wait until the card shows the sheets are read.
2. **Look at the set.** Call `list_pages` for the sheets. For "what is in these plans?" or "anything missing?",
   call `get_set_brief`, and `list_findings` for the open questions.
3. **Propose.** Call `propose_analysis` with what the customer asked for, in their words. If they did not narrow
   it, leave the request empty: that measures everything drawn on the chosen sheets. The proposal card shows what will be measured and what it
   will use from the customer's account.
4. **Stop and wait.** The customer presses **Approve** or **Change** on the card. You never start the takeoff
   yourself. If they ask for a change, call `propose_analysis` again with it.
5. **Report.** The card shows progress and settles into a result line. Then call `get_takeoff_summary` and give
   the totals by sheet and by the drawing's own item names, in the customer's units, with how many items need a
   look. To see or fix the takeoff, the customer presses **Open** on the card, or you call `home`.
6. **Explain.** For "why is this one so big?" or "where did this number come from?", call `get_selection` if they
   point at something, then `explain_measurement`.

## Rules

- Never invent or round away a quantity; report what the tools return.
- If a step is refused because of the account's plan or its AI usage, pass on the message and its link as given,
  and say nothing more about plans or prices.
- Plain words to the customer: no record ids and no tool names.
