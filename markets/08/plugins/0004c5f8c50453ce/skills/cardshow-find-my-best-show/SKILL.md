---
name: cardshow-find-my-best-show
description: Compare upcoming CardShow events against a collector's dates, place, saved plans, seller-declared coverage, and optional connected HobbyWise Hunt List. Use when a user asks which card show to attend, wants events near a place or during a date range, asks where they are most likely to find their targets, or wants a transparent shortlist instead of a generic directory search.
---

# Find the best CardShow event

Recommend events from CardShow evidence and the collector's own priorities. Keep the ranking explainable and never turn seller declarations into inventory guarantees.

## Establish the search

1. Resolve the intended place and date range. State exact dates when the user uses relative language such as “this weekend.”
2. Ask a follow-up only when the missing place or date would materially change the result.
3. Use `cardshow_get_my_planning` when signed-in saves or existing plans are relevant.
4. Use `cardshow_find_events` for the bounded public candidate set.
5. When the customer has the required CardShow access and approved HobbyWise connection, use `cardshow_recommend_events_for_my_hunt_list` for the same place and dates.
6. If Hunt List access is unavailable, continue with public CardShow discovery and user-stated priorities. Do not infer or request private HobbyWise fields.

## Compare the evidence

- Use `cardshow_get_show_supply` for a selected event or a small set of serious candidates when the Hunt List recommendation did not already provide enough seller evidence.
- Separate exact seller-listed item matches, strong category matches, and general leads.
- Consider date and place fit, current saved/planned state, matched targets, declared category coverage, and how complete the seller information is.
- Do not invent distance, travel time, admission cost, vendor count, inventory, verification, or availability when CardShow did not return it.
- Do not rank an event first merely because it appears first in a tool result.

## Present the shortlist

Return a compact comparison with:

1. the best one to three events for the stated goal;
2. the evidence supporting each choice;
3. the important tradeoffs or missing information;
4. unmatched Hunt List targets when available; and
5. the CardShow notice that seller declarations are planning leads, not guarantees or reservations.

If no event has meaningful evidence, say so and show the best directory candidates without pretending they match.

## Save only after confirmation

Do not save, unsave, or change attendance during comparison. If the user asks to save or set attendance, refresh the exact show and current planning state, preview the exact final state, ask for explicit confirmation, use the matching final-state tool, and verify with a fresh read. Never apply a bulk action to multiple shows under vague confirmation.
