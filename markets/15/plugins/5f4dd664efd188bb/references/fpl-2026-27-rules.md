# FPL rules reference — 2026/27

**Reference status:** season-specific baseline reviewed on 1 November 2026. This file is not a substitute for the live official rules. Re-check the official FPL rules and help pages whenever a recommendation depends on a rule, chip availability, a deadline, or a season boundary. The Premier League can amend rules during a season.

## Authority and freshness

Use sources in this order:

1. The live [official FPL Rules page](https://fantasy.premierleague.com/en/help/rules) supplied by the manager.
2. The official [FPL Help and FAQs](https://fantasy.premierleague.com/help/faqs).
3. Current-season official Premier League/FPL announcements, particularly the [2026/27 changes](https://www.premierleague.com/en/news/4679873), [2026/27 chip guide](https://www.premierleague.com/en/news/4679879/whats-happening-with-fpl-chips-in-202627), and [2026/27 scoring guide](https://www.premierleague.com/en/news/2174909/fpl-basics-scoring).

If the current season is not 2026/27, do not apply the season-specific values below without checking the new season's official rules. If the rules page cannot be reached, disclose that fact, use this dated baseline only where appropriate, and avoid a definitive recommendation for any unresolved rule-dependent choice. Do not use old-season memory as evidence.

## Squad and lineup constraints

- The initial squad budget is **£100.0m** for **15 players**.
- The squad composition is **2 goalkeepers, 5 defenders, 5 midfielders and 3 forwards**.
- The normal maximum is **3 players from one Premier League club**. The official FAQ describes a temporary exception when a real-life transfer between Premier League clubs causes a squad to exceed the limit; the manager must return below the limit when making the next transfer.
- A legal starting XI contains **1 goalkeeper**, at least **3 defenders**, and at least **1 forward**. With 11 players, that also leaves at least 2 midfielders. Use the official FPL position classification for this season, not a player's real-world role or an older-season position.
- FPL changed the classifications of 11 players for 2026/27. Never carry a player's previous-season FPL position into a legality check.
- The 2026/27 official help describes FDR as a 1–5 opponent-difficulty indicator that is reviewed weekly. Treat it as context, not as a points projection or a permanent rating.

## Transfers, free transfers and deadlines

- The normal allowance is **1 free transfer per Gameweek**. An unused free transfer rolls forward; managers may bank up to **5 free transfers**.
- Each transfer beyond the available free-transfer allowance normally costs **4 points** in that Gameweek.
- A **Wildcard** permits unlimited free transfers for the Gameweek and removes transfer-point deductions incurred earlier in that same Gameweek. It is permanent, and the manager must stay within the available budget. Saved free transfers from earlier Gameweeks are retained; the free transfer earned for the Gameweek in which the chip is played is consumed by activating it.
- A **Free Hit** permits unlimited free transfers for one Gameweek only. The squad and bank are restored at the next deadline to their previous state, with price changes during that Gameweek reflected. Changes to the bank while the Free Hit is active are lost. The free transfer earned for that Gameweek is consumed; previously banked free transfers remain.
- If a player rises in price after the manager bought them, the selling price includes half the rise, rounded down to the nearest £0.1m. Prefer the live selling price shown by FPL over a manual calculation.
- The official 2026/27 help says player prices can change by £0.1m at 00:00 UK time. The price predictor is an indication, not a guarantee. Do not treat a predicted rise or fall as certain.
- The Gameweek deadline is normally **90 minutes before the first kick-off** in that Gameweek. Check the live deadline; schedules can change. Changes made after the deadline apply to the following Gameweek. Confirmed transfers cannot be reversed.
- In a transfer comparison, calculate the hit only after verifying the manager's actual available free transfers, active chip, bank, selling prices and deadline. If any of these are absent from the connected server's output, request or label the missing information rather than guessing.

## Chips in 2026/27

- There are **two sets** of the four chips — Wildcard, Free Hit, Bench Boost and Triple Captain — for a total of **eight chips**.
- One set belongs to the first half, up to the Gameweek 19 deadline. The second set becomes available from Gameweek 20. The first-half set cannot be carried into the second half; unused first-half chips are lost. Use the live official schedule for the exact Gameweek 19 deadline. Check the live official schedule for the GW19 deadline; the date may change.
- Only **one chip may be active in a Gameweek**.
- The first Bench Boost and Triple Captain are available from the start of the season. The first Wildcard and Free Hit become available after Gameweek 1; neither is available for Gameweek 1, when unlimited transfers are already provided.
- **Wildcard:** unlimited permanent transfers within budget. Transfers already made in the Gameweek are covered. Saved free transfers are retained; the free transfer for the chip Gameweek is consumed. Once activated/confirmed, it cannot be reversed. Follow the live UI state for pending-versus-active cancellation details.
- **Free Hit:** unlimited transfers for one Gameweek; the normal squad and bank return at the following deadline. It cannot be used in Gameweek 1 or in consecutive Gameweeks. Once confirmed, it cannot be cancelled.
- **Bench Boost:** points from all substitutes count toward the Gameweek total. It is selected/saved on the Pick Team page and may be cancelled before the deadline.
- **Triple Captain:** the captain's points are tripled rather than doubled. The triple-captain benefit passes to the vice-captain if the captain plays no minutes in the entire Gameweek. If neither plays, the chip is spent and the bonus is lost. It is selected/saved on the Pick Team page and may be cancelled before the deadline.
- Verify chip inventory, whether a chip is already pending/active, and the half-season set before recommending use. The connected MCP tools may not expose the full chip ledger; do not infer availability from the calendar alone.

## Captaincy, automatic substitutions and blank/double Gameweeks

- The captain scores **double** points. The vice-captain becomes captain only if the captain plays **zero minutes** in the entire Gameweek.
- In a Double Gameweek, a player who appears for any minutes in any scheduled match counts as having played for captain and automatic-substitution purposes. Do not expect the vice-captain or an automatic substitute to replace a player who appeared in one of the matches but missed another.
- Automatic substitutions are processed after the Gameweek. The lineup must remain legal: 1 goalkeeper, at least 3 defenders and at least 1 forward. The reserve goalkeeper is considered separately; outfield bench order matters, but an outfield substitute may be bypassed if using them would create an illegal formation.
- In a Blank Gameweek, players whose clubs have no fixture score zero for that Gameweek. In a Double Gameweek, players can earn points from both fixtures. Use confirmed official fixtures and rescheduling notices; do not infer blanks or doubles from rumours or historic schedules.

## 2026/27 scoring baseline

Use the official current scoring table if it changes. The 2026/27 baseline is:

| Action | FPL points |
|---|---:|
| Appearance, up to 60 minutes | 1 |
| Appearance, 60 minutes or more (stoppage time excluded) | 2 |
| Goal — goalkeeper / defender / midfielder / forward | 10 / 6 / 5 / 4 |
| Assist | 3 |
| Clean sheet — goalkeeper or defender / midfielder | 4 / 1 |
| Every 3 goalkeeper saves | 1 |
| Penalty save | 5 |
| Penalty miss | -2 |
| Defensive contribution — defender at 10 combined clearances, blocks, interceptions and tackles | 2 |
| Defensive contribution — midfielder or forward at 12 combined clearances, blocks, interceptions, tackles and recoveries | 2 |
| Every 2 goals conceded by a goalkeeper or defender | -1 |
| Yellow card / red card / own goal | -1 / -3 / -2 |
| Match bonus points | 1–3 for the top BPS performers |

Defensive-contribution thresholds award **one 2-point return per player per match**, not repeated awards for multiples of the threshold. For a Double Gameweek, evaluate each match separately.

A player must record at least 60 minutes, excluding stoppage time, to qualify for a clean sheet or the 2-point appearance award. If substituted after reaching 60 minutes before a goal is conceded, the player retains clean-sheet points under the official help explanation.

### 2026/27 Bonus Points System changes

BPS determines the additional 1–3 bonus points; do not confuse BPS values with FPL points in the scoring table.

- All players gain **1 BPS for every 3 clearances, blocks and interceptions (CBI)**, rather than every 2 in 2025/26.
- Goalkeepers gain **2 BPS for any save**, plus **1 BPS** for a save from inside the box and **1 BPS** for a save from a Big Chance. The separate BPS metric for saves from outside the box was removed. A penalty save is worth **7 BPS** under the revised calculation.
- The **-1 BPS for being tackled was removed**.
- Projected bonus points are shown live after 20 minutes and can change. For 2026/27, the Gameweek score lock is scheduled for **09:00 UK time on the day after the final match** of the Gameweek so post-match Opta review can be reflected. Treat live totals and projected bonus as provisional until finalisation.

## Connected server implementation limits

The connected MCP tools are read-only analysis tools:

- `get_manager`: manager/team summary.
- `get_team_picks`: manager squad, picks, captaincy and some transfer fields.
- `search_player_market`: player-name/position search with returned stats and model predictions; it is not proof of exhaustive market coverage.
- `get_player_fixtures`: recent four played matches and next four scheduled fixtures for a player.

Do not claim these tools expose every required FPL field. In particular, inspect returned data before relying on current bank/sell prices, banked free-transfer count, active chip inventory/history, exact deadline, confirmed blank/double schedule, injury status, minutes likelihood, ownership or full-market coverage. Ask for missing information or explicitly qualify the recommendation. Never claim to submit transfers, change captaincy, set a lineup or activate a chip.

## Official source links

- [Official FPL Rules](https://fantasy.premierleague.com/en/help/rules)
- [Official FPL Help and FAQs](https://fantasy.premierleague.com/help/faqs)
- [2026/27 season changes](https://www.premierleague.com/en/news/4679873)
- [2026/27 chip rules and strategy](https://www.premierleague.com/en/news/4679879/whats-happening-with-fpl-chips-in-202627)
- [Official squad composition guide](https://www.premierleague.com/en/news/2174419)
- [Official scoring guide](https://www.premierleague.com/en/news/2174909/fpl-basics-scoring)
