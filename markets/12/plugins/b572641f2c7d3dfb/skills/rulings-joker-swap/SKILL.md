---
name: rulings-joker-swap
description: "Rule on an American mahjong joker swap with Jokerly. Use when the user asks whether they may swap (exchange, redeem) a tile for a joker, take a joker from their own or someone else's exposure, or when a joker swap is allowed."
---

Use this skill when the user asks whether a joker swap is allowed at their American mahjong table. The user's explicit instructions always come first.

## Flow

1. `check_joker_swap` takes the exposure with the joker, the tile offered, whose turn it is (`timing`) and where the joker is (`joker_from`).
2. It checks the standard American mahjong rules: the joker sits in an exposure on the table, it is the user's turn after drawing or calling, and the tile offered is the natural tile the joker stands for. The result names the rule that decided.
3. With the user's rack in `tiles`, it also says whether the swap brings the rack closer to a hand on the user's card.

## Scope

- House rules at the user's table win over the standard rules Jokerly checks.
- American mahjong only; Riichi, Chinese and other styles are ChatGPT's own job.
