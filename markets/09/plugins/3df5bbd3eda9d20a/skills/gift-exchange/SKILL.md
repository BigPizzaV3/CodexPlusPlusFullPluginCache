---
name: gift-exchange
description: Run a private Secret Santa or gift exchange name draw with exclusions (couples, households, one-way rules, last year's pairs), budget, date and wish lists, giving each person a sealed reveal link; or plan a White Elephant / Yankee Swap game with a fair turn order, steal-limit rules and a printable PDF.
---

# Secret Santa and White Elephant

## When to use
- "Draw names for Secret Santa", "secret santa generator no email", "gift exchange with exclusions", "couples can't draw each other", "with wish lists": call `plan_gift_exchange`.
- "White Elephant", "Yankee Swap", "Dirty Santa" turn order or rules: call `plan_white_elephant`.
- Not for picking one random winner, raffles, or buying gifts.

## How to call `plan_gift_exchange`
- `participants`: every name (3 to 60), unique. If two people share a name, ask for a last initial.
- Couples or households who must not draw each other go in `households` (both directions). One-way rules ("Ana can't draw Cy", last year's pairs) go in `exclusions`.
- Set `no_two_person_loops: true` only when the user asks that nobody draws the person who drew them.
- Pass `budget` as written ("$30"), `exchange_date` as YYYY-MM-DD, optional `event_name`, `wish_lists`, `organizer_note`, and `language` (en, es, fr, de, pl, pt, ja) for the reveal pages.
- Set `include_organizer_list: true` only if the organizer explicitly asks to see every pairing; say that it spoils the surprise.

## After the call
- Share each person's link with their name and tell the organizer to send every person only their own link (the widget has Copy message buttons).
- The pairings are encrypted inside the links. Never guess, invent, or state who drew whom, and do not open the links.
- If the tool explains that no valid draw exists, relay the reason and suggest the exclusion to remove.
- A redraw makes new links with a new draw code; everyone needs the new link.

## How to call `plan_white_elephant`
- `participants` (3 to 60), optional `steal_limit` (default 3, 0 = no stealing), `max_steals_per_turn`, `first_player_final_swap`, `no_immediate_steal_back`, `budget`, `party_date` (YYYY-MM-DD), `event_name`, `paper` (letter or a4).
- Show the turn order and rules, and offer the PDF and printable page links.
