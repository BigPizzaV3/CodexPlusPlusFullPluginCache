---
name: name-wheel
description: Spin a name wheel (wheel spinner, random name picker, yes or no wheel), split people into random teams (sizes differ by at most one), or pick random numbers with the spin_wheel, make_teams, and pick_random_number tools. For fun, classroom, and team decisions only.
---

# Zovo Name Wheel

Use these tools for everyday random choices: "spin the wheel", "wheel spinner with names", "random name picker", "split us into teams", "random number from 1 to 30".

1. `spin_wheel`: pass every option as `entries` (2-200). Repeat an entry, or pass `weights`, only when the user wants some options more likely. Use `count` for several different winners and `remove_winners: true` when each person should be picked once (classroom cold-calling, presentation order). For a yes/no wheel use `["Yes", "No"]`. For the next spin, pass the returned `remaining` list.
2. `make_teams`: pass all `names` and either `team_count` or `team_size` (not both). Add `keep_apart` pairs or `keep_together` groups only when the user asks for them. Sizes always differ by at most 1; assignment is random, not skill-balanced.
3. `pick_random_number`: `min`, `max` (inclusive), `count`, and `unique` (default true).

After a tool returns, state the winner(s), teams, or numbers in one or two lines; the widget shows the animated wheel and lets the user spin again, remove the winner, edit, or shuffle.

Do not use these tools for lottery or Powerball numbers, betting or gambling, raffles or prize draws with legal requirements, login credentials or security codes, or buying wheel parts. Do not invent winners yourself; always use the tool result.
