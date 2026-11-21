---
name: mahjong-helper
description: Check an American mahjong (mah jongg) rack against the hands on the user's own card, choose a Charleston pass, or rule on a joker swap with Jokerly. Use when the user shares a rack photo or typed tiles, asks how many tiles away they are or which line on their card to go for, what to pass in the Charleston, or whether they can take a joker from an exposure.
---

Jokerly is a helper for American mahjong at the table. A rules engine on Jokerly's server does the counting: tiles away for every hand, the Charleston pass search and joker rulings. The user's explicit instructions always come first.

## The card

Jokerly ships no league's card. The hands come from the card the user's table plays: the user types the lines or sends a photo of the card, and each line is written in Jokerly notation (groups separated by spaces, 14 tiles, a suit letter a, b or c per color, for example FF 2222a 4444b 6666c). save_card_hands keeps them privately for this user; show_card_hands lists them with a #; remove_card_hands removes some or all of them. Until the user saves hands, Jokerly uses its own practice hands and says so.

## Flow

1. Rack photos are read into tile codes before a call: 1B-9B Bams, 1C-9C Craks, 1D-9D Dots, N E W S, RD GD WD (WD is Soap), F, J, and ? for a tile that can't be read. Groups already laid face up go in exposed.
2. check_rack counts how many tiles away the rack is from every hand on the user's card and returns the closest, with the tiles each still needs and where jokers can stand in.
3. suggest_charleston_pass takes the whole rack and the pass (first right, across, left; second left, across, right; courtesy) and returns the three tiles that keep the rack closest to the user's hands, jokers kept, with a blind-pass hint on the first left and second right.
4. check_joker_swap takes the exposure with the joker, the tile offered, whose turn it is and where the joker is, and says whether the swap is legal under the standard rules and which rule decided.
5. Each result ends with a short summary suitable to show the user; the card shows every hand and tile, and the user can tap a misread tile to fix it.

## Scope

- American mahjong only (jokers, the Charleston, a yearly card). Riichi, Chinese and other styles are ChatGPT's own job.
- Jokerly keeps no score and handles no money. House rules at the user's table win over the standard rules Jokerly checks.
- Saved hands are kept under ChatGPT's anonymous ID for this user, shared with nobody, and deleted on "Delete my Jokerly card" or after 12 months without use.
