---
name: chip-strategy
description: Use when an FPL manager asks whether or when to play Wildcard, Free Hit, Bench Boost, or Triple Captain, or wants a chip plan across upcoming Gameweeks.
---

# Chip Strategy

Treat a chip as a limited resource: using it now should solve a meaningful problem or capture a clearly evidenced opportunity that is better than keeping it for later. Do not recommend a chip simply because the next Gameweek looks interesting.

## Mandatory rules check

Before evaluating a chip, read `../../references/fpl-2026-27-rules.md` and verify the current season's official rules, chip inventory and target Gameweek. Do not rely on a previous season's number of chips, reset date, eligibility or Free Hit restrictions. If the live rules or chip ledger cannot be verified, state the uncertainty and do not give a definitive activation instruction.

For 2026/27 there are two sets of Wildcard, Free Hit, Bench Boost and Triple Captain — eight chips total. The first set must be used before the Gameweek 19 deadline; the second set is available from Gameweek 20. Unused first-half chips do not carry over. Only one chip can be active in a Gameweek. The first Wildcard and Free Hit are unavailable in Gameweek 1; the first Bench Boost and Triple Captain are available from the start. Free Hit cannot be used in consecutive Gameweeks.

Understand the operational differences: Wildcard is permanent and stays within budget; Free Hit changes the team for one Gameweek and restores the previous squad/bank at the next deadline; Bench Boost includes bench points; Triple Captain triples the captain's points. Apply the transfer/free-transfer side effects in the shared rule reference as well.

## Data gathering

1. Obtain the manager team ID and Gameweek range being considered. Ask for the team ID if missing.
2. Call `get_manager` for each relevant Gameweek to inspect manager and squad information.
3. Check returned information for chip availability/history, pending or active chip, transfer state, bank, squad depth and Gameweek. The current server tools may not expose the full chip ledger; if it is absent, ask the manager for the chip-status screen or state that availability cannot be verified.
4. Use `search_player_market` for relevant squad players and `get_player_fixtures` for player-level fixture context when evaluating captaincy or bench strength.
5. Verify confirmed blank/double Gameweeks, deadlines and the applicable half-season window from official current fixtures/rules. Do not infer them from rumour, old schedules or an incomplete player-fixture subset.

## Chip-by-chip assessment

- **Wildcard:** consider whether several squad changes are needed, structural problems, current injuries/suspensions/rotation backed by reliable information, and a multi-Gameweek plan. The final 15 must obey the current squad composition, club limit and budget. Wildcard transfers are permanent; saved free transfers are retained, while the free transfer earned in the chip Gameweek is consumed. A Wildcard removes point deductions from other transfers already made in that Gameweek. Do not claim an optimized rebuild without a complete player pool, prices, bank and constraints.
- **Free Hit:** consider whether the normal squad is poorly positioned for a specific Gameweek, especially a confirmed Blank Gameweek, and whether a temporary squad materially improves expected returns. It lasts one Gameweek, then the previous squad and bank return at the next deadline, subject to player price changes. It cannot be used in Gameweek 1 or consecutive Gameweeks. The free transfer earned in that Gameweek is consumed; saved prior transfers remain.
- **Bench Boost:** assess all four substitutes, not just the starting XI. Consider credible expected minutes and useful confirmed fixtures for each bench player. In a Double Gameweek, a player who appears in either match counts as having played for automatic-substitution purposes. Verify the chip is available and that no other chip is active.
- **Triple Captain:** compare the captain's target-Gameweek projection, minutes/appearance risk and confirmed fixtures against the value of saving the chip. In a Double Gameweek, confirm whether the connected server's model prediction covers both fixtures before combining or multiplying projections. The triple benefit passes to the vice-captain only if the captain plays zero minutes in the entire Gameweek; if neither appears, the chip is spent and the benefit is lost.

## Decision process

- Confirm the correct first-half/second-half chip set, current availability, eligibility and that no other chip is active for the same Gameweek.
- Compare **use now**, **save**, and where relevant **use a different chip**. State the opportunity cost.
- Check the live Gameweek deadline. For 2026/27, the first set expires at the GW19 deadline and cannot be carried into GW20; do not hardcode a date if the official fixture schedule changes.
- Base recommendations on confirmed fixtures and the manager's actual squad. Never invent a blank, double, fixture swing, deadline, chip reset, chip-use restriction or chip inventory.
- Treat points projections as estimates. Do not promise a rank gain or a particular points return.

## Response format

Provide:

1. **Recommendation:** play or save the chip, and target Gameweek if known.
2. **Eligibility check:** which half-season chip, remaining availability, one-chip-per-Gameweek and other restrictions — only if verified.
3. **Why:** squad or fixture evidence supporting the decision.
4. **Opportunity cost:** what the manager gives up by using it now.
5. **What would change the decision:** specific missing facts or future conditions to monitor.
6. **Confidence:** high, medium or low, based on data completeness.

Do not activate chips or claim account changes. The connected server's available tools are for analysis and do not expose chip-write actions.
