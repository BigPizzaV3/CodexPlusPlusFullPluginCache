---
name: place-cards
description: Turn a guest list into printable tent-fold place cards (name on both faces, back face rotated, fold lines and crop marks), flat escort cards and a table plan PDF.
---

# Zovo Place Card Maker

Use `generate_place_cards` for folded place cards or table name cards. Use `generate_escort_cards` for flat escort cards that tell guests their table, or when the user asks for a table plan list.

1. Convert the guest list (typed, pasted, a spreadsheet or a photo of a seating chart) into `guests`: one object per guest with `name`, and `table` and `meal` when given. Keep names exactly as written, in any script. Use `text` only when you cannot split the list.
2. Pass `event_title` when the user names the event. Pass `size` "a7" and `paper` "A4" for metric cards, `per_page` 6 only for 3.5 x 2 in cards on Letter.
3. Sorting defaults to by table when tables are given. Pass `sort` "alpha", "last" or "given" when asked.
4. After the tool returns, give the layout line, the number of pages, any warnings verbatim, and both download links. Remind the user to print at 100% (actual size).

Do not use this skill to decide who sits where, or for invitations and menus.
