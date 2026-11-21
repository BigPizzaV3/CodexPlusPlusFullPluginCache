---
name: score-keeper
description: Keep game-night scores with a live scoreboard, a five-dice score sheet, or a 301/501 darts scorer and CSV downloads.
---

# Gamechalk Score Keeper

Use `show_scoreboard` for 2–12 distinct player or team names, each at most 30 characters. Pass optional whole-number starting `scores`, `mode` (`highest`, `lowest`, or `target`), and a positive `target` for target mode. Scores stay in the open widget only, with point controls, a leader, and history and undo for the last 20 actions. Use Smaller step and Bigger step to change the scoring step. There is no online multiplayer.

Use `score_dice_sheet` with a `sheet` mapping the thirteen category keys to five dice valued 1–6, or null for unplayed categories. Include `play_order` listing each played category once to establish chronology for repeat five-of-a-kind bonuses. If omitted, the tool assumes category order from ones through chance. Full house needs a distinct triple and pair, unless an eligible repeat uses joker scoring after its matching upper category is filled. An eligible repeated five-of-a-kind earns 100 after the first five-of-a-kind category scored 50. Report the category scores, upper total, upper bonus, grand total, and CSV download.

Use `score_darts_leg` with `start` 301 or 501, one to forty `turns` of one to three darts, and optional `double_out` (default true). Tokens are S1–S20, D1–D20, T1–T20, SB, DB, and 0 for a miss. A bust restores the score before the turn and ignores its later darts. Darts after a finish are ignored. Report remaining points, busts, darts thrown, three-dart average, checkout suggestion under the selected out rule, and CSV download.

Do not use these tools for payments, wagers, coaching, online multiplayer, or other darts variants.
