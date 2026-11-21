---
name: compare-revisions
description: Compare two revisions of a plan set in Exayard and show which sheets changed and what measured items moved. Use when new drawings arrive, for "what changed in revision B", "check the addendum" or "which sheets are different".
---

# Compare two revisions

## Steps

1. **Find the project.** If the customer says "this" or "the selected", call `get_selection` first. Otherwise
   use `list_projects` and `get_project`.
2. **Get the new drawings in.** If the newer revision is not in the project yet, call `add_plan_set`: the
   customer adds the files on the upload card. Wait until the card shows the sheets are read.
3. **Compare.** Call `compare_drawing_revisions`. It matches sheets by sheet number and reports each one as new,
   unchanged, changed or not checked, with the measured items on the changed sheets.
4. **Report.** Lead with the count of changed sheets, then list them by sheet number and title. Name the measured
   items that sit on changed sheets, since their quantities may need a new takeoff. To see the changes drawn on
   the sheets, the customer presses **Open**, or you call `home`.
5. **Next step.** If quantities may have changed, offer a new takeoff of the changed sheets. That goes through
   the proposal card and the customer's **Approve**, as every takeoff does.

## Rules

- Report "not checked" sheets as not checked; never call them unchanged.
- Plain words to the customer: no record ids and no tool names.
