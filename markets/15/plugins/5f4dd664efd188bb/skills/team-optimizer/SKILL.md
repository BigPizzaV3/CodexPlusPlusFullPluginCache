---
name: team-optimizer
description: Use when an FPL manager wants the best starting XI, formation, bench order, captain and vice-captain, or a squad-strength assessment using their existing team.
---

# Team Optimizer

Optimize the manager's actual squad for the requested Gameweek. First solve the lineup problem within the players the manager owns; do not silently turn a lineup request into a speculative rebuild of the whole 15-player squad.

## Mandatory rules check

Before proposing a lineup, read `../../references/fpl-2026-27-rules.md`. Confirm the requested season and use official FPL position classifications for that season. In 2026/27, 11 player positions were reclassified, so never rely on a player's previous-season position or their perceived real-life role. If the requested season is not 2026/27, verify its official current position list and formation rules first.

A legal FPL starting XI has one goalkeeper, at least three defenders and at least one forward; with 11 players this also requires at least two midfielders. The squad itself should contain 2 goalkeepers, 5 defenders, 5 midfielders and 3 forwards, and normally no more than three players from any one PL club. Do not confuse squad composition with the formation of the starting XI.

Apply current automatic-substitution rules: goalkeeper replacement is handled separately; outfield bench order matters; an outfield substitute cannot be used if it would leave an illegal formation. In a Double Gameweek, any minutes played in any scheduled fixture means the player counts as having appeared and is not eligible to be replaced automatically.

## Data gathering

1. Obtain the manager team ID and target Gameweek. Ask for the team ID when it is missing.
2. Call `get_manager` for the actual squad, starting XI, bench, captaincy and any transfer information returned for that Gameweek.
3. Use `search_player_market` to inspect predictions or stats for squad members where picks does not provide enough information. Search by player name or position as supported.
4. Use `get_player_fixtures` for players whose fixture context could materially change the lineup decision.
5. Use `get_manager` when manager-level details help interpret the current squad or transfer state.
6. Confirm the current Gameweek fixture schedule and whether any club has a blank or double fixture. Do not infer it from memory or a stale fixture list.

## Optimization rules

- Prioritize expected starting-XI output using comparable, same-Gameweek server predictions. Verify whether Double Gameweek outputs already combine both matches before summing or adjusting them.
- Build a legal XI first. Check positional classification and formation constraints before optimizing projected points.
- Optimize the starting XI first, then outfield bench order, reserve goalkeeper, captain and vice-captain. Respect the official autosub mechanism, not just the raw expected points rank. Consider whether the first outfield substitute could create an illegal formation and therefore be skipped.
- For a Double Gameweek, treat a player as having appeared if they play any minutes in either fixture. Do not expect an automatic substitute to replace them if they miss the other fixture.
- Use fixture context as a tiebreaker or material adjustment, not as a substitute for player-level evidence.
- Use the season's scoring table and defensive-contribution thresholds from the shared reference. For 2026/27, defenders reach the DC threshold at 10 combined clearances, blocks, interceptions and tackles; midfielders/forwards at 12 combined defensive actions including recoveries. Apply the revised 2026/27 BPS rules when discussing bonus potential.
- Do not assume that a low-scoring player should be benched if relevant prediction or minutes evidence says otherwise.
- Distinguish a **best XI from the current squad** from a **transfer-based squad improvement**. For transfers, use the Transfer Advisor workflow. A full-market rebuild requires a sufficiently complete player pool and reliable prices/budget; the available name-search tool does not establish exhaustive market coverage.
- Do not claim to have checked club limits, budget, price changes, injuries, availability, or a confirmed fixture unless those values are returned or supplied.

## Response format

Show:

1. **Starting XI:** grouped by current FPL position, with a legal formation.
2. **Bench order:** first outfield substitute, remaining outfield substitutes, and reserve goalkeeper, with any autosub caveat.
3. **Captain and vice-captain:** with concise evidence.
4. **Key calls:** explain close start/bench decisions.
5. **Rules and limitations:** confirm formation legality and disclose missing predictions, minutes, prices, fixtures or player fields that affect certainty.

Do not claim to save or submit the lineup. The connected MCP tools are read-only analysis tools.
