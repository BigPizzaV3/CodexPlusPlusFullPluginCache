---
name: fair-draw
description: Run a verifiable prize draw on a hosted page (entrants add names from one link or the organizer adds a list), then draw winners and backups with a published SHA-256/HMAC method, using create_prize_draw, add_draw_entries, draw_winners and show_draw_results.
---

# Zovo Fair Draw

Use `create_prize_draw` when someone wants a fair random pick of winners from a group: a giveaway, door prize, team voucher, classroom pick.

1. Pass `title`, optional `prize`, `winners` (1-20, default 1) and `backups` (0-10). Pass `free_entry: true` only when nobody pays to enter (ask if unsure). If the user gives names, pass them in `names` as a list, one person per item. Set `public_entry: false` when only the organizer adds names.
2. After the tool returns, give the public link to share and say plainly that the organizer link is private. Mention that the page shows a commitment (SHA-256 of a secret seed) from the start.
3. To add names later, call `add_draw_entries` with the organizer link (contains `/m/`), up to 100 names per call; send longer lists in several calls. Duplicates are skipped and reported.
4. When the user is ready, call `draw_winners` with the organizer link. It closes entries and the result is final. Report the winners and backups in the returned order. Do not pick winners yourself.
5. `show_draw_results` reads the state (entries, commitment, and after the draw the winners and proof values).

For free draws only: the organizer confirms nobody pays to enter. Do not use it for paid raffles, ticket sales, betting or anything that handles money. One entry per name; it does not check identities.
