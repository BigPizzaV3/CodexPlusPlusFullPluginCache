---
name: bingo-cards
description: Make sets of different printable bingo cards from the user's words (or classic 1-75 and UK 90-ball numbers) with a caller sheet, run the game with random draws and claim checks, and design a personal goal bingo card for the year.
---

# Zovo Bingo Card Maker

Tools: `generate_bingo_cards`, `show_bingo_caller`, `generate_goal_bingo`.

1. **Party, classroom, shower or meeting cards** -> `generate_bingo_cards`. Pass the user's words as `items` (one per entry), `card_count` (default 30), and any title, colour, grid size (3, 4, 5), centre-square label, paper and cards per page. For number bingo use `mode: "numbers_75"` (US, 5x5) or `"numbers_90"` (UK tickets). A 5x5 card with a centre square needs 24 different items; if there are too few, relay the tool's message (add items or use a smaller grid). Do not invent extra words unless the user asks you to.
2. Share the summary, card 1, the balance line and all three download links (cards PDF, caller sheet PDF, CSV). Mention the set number: it rebuilds the same cards later.
3. **Running the game** -> `show_bingo_caller` with the same `items` in the same order and the `caller_args` from step 1 (mode, grid_size, free_space, card_count, seed, unique_lines, list_code), plus every item called so far in order as `called`. `action: "draw"` calls the next item; `action: "check"` with `card_number` verifies a claim; `action: "winners"` lists every card that has the pattern. The tool keeps no state: always send the full called list.
4. **Goal bingo** (new year, resolutions, bucket list) -> `generate_goal_bingo` with exactly one goal per square (24 for 5x5 with a centre square). Pass `year`, `completed` goals and colour when given. Share the PNG, SVG and PDF links.
5. If the user asks for `unique_lines` and the tool says it is not possible, explain the limit it gives and offer more items, fewer cards, or turning it off.

Do not use these tools for prize, cash or betting games, for crosswords or word searches, or for questions about bingo history and rules.
