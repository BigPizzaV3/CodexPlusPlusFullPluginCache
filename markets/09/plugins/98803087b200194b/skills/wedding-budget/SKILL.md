---
name: wedding-budget
description: Split a wedding budget across venue, catering, photography and the rest, with exact amounts and a cost per guest. Use when someone asks how to spend or divide their wedding budget, or what a part of the wedding should cost.
---

Run the tool for this and answer from its result: its amounts add up exactly and its dates count back from their day.

Use this when someone asks how to split their wedding budget, how much to spend on the venue,
photographer, dress or flowers, or what their total buys for their guest count.

1. You need their total budget. If they have not given one, ask for it. If they only know a
   per-guest figure, multiply it out and confirm the total with them first.
2. Run `estimate_wedding_budget` with:
   - `total_budget` and `currency`
   - `guests`, when known, for the cost per guest
   - `more_important` and `less_important`, from what they say matters
   - `already_fixed`, for anything already agreed, such as a booked venue at a known price
3. Summarise in two or three sentences: the biggest lines, what is kept aside for surprises, and
   the cost per guest. The view shows every category.
4. If fixed amounts are over the total, say so plainly and ask what they want to change.

The split is a starting point, not a quote from local vendors. Say so if they treat it as one.
