---
name: doubles-mixer
description: Plan a social doubles mixer with rotating partners, balanced rests, printable score sheets, and individual standings.
---
# Pairloop Doubles Mixer

Use for a pickleball mixer, tennis mixer schedule, rotating partners schedule, padel americano, or badminton social play with individual players.

Call `generate_mixer_schedule` with 4–48 distinct names, 1–12 courts, 1–24 rounds, and optional seed (default 1). Change the seed to remix. Optional `group_a` and `group_b` must partition the player list; partners cross groups. Unequal groups are refused when balanced rests are impossible. `paper` is `letter` or `a4`.

The same seed reproduces the schedule. Different seeds can coincide because the rotation space is finite. For four players and one round without groups, seeds 0 through 23 enumerate the 24 ordered team representations; the sequence repeats modulo 24. There are three distinct sporting matchups when player and team order are ignored. With two groups of two, the corresponding counts are 16 ordered representations and two sporting matchups. State the small-space notice returned in the fairness summary.

Report courts used, partner repeats and their counting lower bound, highest opponent count, and sit-out range. General bounded optimization may not reach the lower bound. Without group constraints, full courts for 8, 12, 16 or 20 players avoid partner repeats through player-count-minus-one rounds.

The result includes `details.schedule_request`: reuse it as `schedule` for `score_mixer_standings`, together with scores `{round,court,score_a,score_b}`. The JSON download also contains the full indexed schedule (indexes refer to the player list). Partial scores leave games pending; tied games count as draws. State the returned tie-break order. Show the leading standings and link the full CSV.

Call `check_mixer_fairness` with names, courts and rounds when the user wants feasibility before scheduling. The repeat count is a lower bound, not a promise of an optimum.

Offer PDF, CSV and JSON links from the result. PDF names are transliterated and numbered; digital names remain intact. Download links carry the settings and should be shared with intended participants. For social play; no rating or skill balancing, fixed-team brackets, or official tournament rules.
