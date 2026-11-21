---
name: secret-santa
description: Draw names for a Secret Santa or holiday gift exchange with couples and exclusions, and give each person a private page with their match, the budget, the date and wishlists, using create_secret_santa, show_secret_santa_status and redraw_secret_santa.
---

# Zovo Secret Santa

Use `create_secret_santa` when someone wants to draw names for a gift exchange.

1. Pass `participants` as a list with one person per item (3 to 60 unique first names or nicknames), for example `["Ana","Bo","Cy"]`. A comma inside an item stays part of that name. If two people share a name, ask for a last initial.
2. Put couples or households who must not draw each other in `couples`, for example `[["Ana","Bo"]]`. Put one-way rules, such as last year's match, in `exclusions`.
3. Add `budget`, `exchange_date` (YYYY-MM-DD; work out "next Friday" first; pages last at most 120 days, so the exchange must be within about 16 weeks), `event_name` and a short `note` when the user gives them. Links are not allowed in any text.
4. If the request already has the names, call the tool right away. Ask one short question only when the names are missing.

After the tool returns:
- Give each person's private link with their name, and tell the organizer to send each person only their own link.
- Give the organizer link separately and say to keep it private.
- The draw itself is never in the result. Do not guess, state or ask who buys for whom.
- If the tool says no draw is possible, repeat its reason and suggest the change it names.

Use `show_secret_santa_status` with the organizer link (it contains `/m/`) when the organizer asks who opened their link, who added a wishlist, or wants the links again.

Use `redraw_secret_santa` with the organizer link only when the organizer asks for a new draw. It works only while nobody has opened a link. It keeps the same links and wishlists.

Do not use this skill for White Elephant games, raffles, picking one winner, or gift ideas.
