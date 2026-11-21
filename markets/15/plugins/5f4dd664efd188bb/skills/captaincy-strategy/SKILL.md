---
name: captaincy-strategy
description: Use when an FPL manager asks who to captain or vice-captain, wants a captaincy comparison, or is considering Triple Captain.
---

# Captaincy Strategy

Choose the captain by comparing the strongest evidence for expected returns, not by selecting the biggest name or the easiest-looking fixture. The captain's points are doubled under the game rules; the vice-captain is the fallback only if the captain plays zero minutes in the entire Gameweek.

## Mandatory rules check

Before recommending captaincy or Triple Captain, read `../../references/fpl-2026-27-rules.md`. Confirm the requested season and verify current official rules if the season differs from 2026/27 or if a rule/deadline may have changed. Do not use old-season scoring, FPL positions, or chip assumptions.

For a Double Gameweek, a captain who appears for any minutes in either fixture is treated as having played, so the vice-captain will not take over just because the captain misses the other fixture. Triple Captain makes the captain's score triple rather than double; if the captain plays zero minutes, the triple-captain benefit passes to the vice-captain. If neither appears, the benefit is lost and the chip is spent. Check the chip inventory and eligibility before suggesting activation.

## Data gathering

1. Obtain the manager team ID and target Gameweek. Ask for the team ID if it is not available; do not guess.
2. Call `get_manager` to identify the actual squad and current captain/vice-captain for that Gameweek.
3. Use `search_player_market` for leading captaincy candidates from the manager's squad. Do not recommend an out-of-squad player as captain unless the user explicitly asks for a transfer-plus-captain scenario.
4. Use `get_player_fixtures` for leading candidates to review returned recent matches and next scheduled fixtures.
5. Use the manager summary returned by `get_manager` when manager-level information is relevant.
6. Check current FPL positions and the current Gameweek's confirmed fixtures. In a Double Gameweek, assess each fixture and total Gameweek projection separately.

## Evaluation

- Start with the connected server's returned model prediction for the target Gameweek, comparing candidates on the same basis and for the same Gameweek. Confirm whether the model's output already includes both fixtures for a Double Gameweek; never double it again unless the model definition confirms it is a per-match prediction.
- Use returned fixture information and recent matches as context. Do not treat recent returns as a guarantee of future points.
- Consider minutes or appearance risk, penalties, set pieces, role, rotation, and injury only if reliable current data for those factors is present. Never infer them from reputation.
- Prefer the player with the strongest expected return after accounting for appearance risk. Explain close calls rather than presenting false precision.
- Select a vice-captain who is a credible alternative and likely to feature, based only on available evidence. Remember that vice-captaincy activates only when the captain records zero minutes across the whole Gameweek.
- For Triple Captain, verify that the correct half-season chip is available, not already used/active, and permitted in the target Gameweek. Compare using it now with preserving it for a better evidenced opportunity. If chip inventory or future fixtures are unknown, say so and do not assert availability.
- Use the current-season scoring and BPS reference when evaluating player profiles. For 2026/27, include defensive-contribution scoring where relevant and use the revised BPS rules; do not rely on 2025/26 BPS weights.

## Response format

Provide:

1. **Captain:** name and strongest evidence for the choice.
2. **Vice-captain:** name and fallback rationale.
3. **Close alternatives:** briefly compare the next one or two candidates.
4. **Risk check:** note evidenced minutes, rotation, fixture or data-quality concerns; otherwise say the information was not available.
5. **Triple Captain view:** include only when asked or clearly relevant, and only after chip eligibility is verified.

Do not change the manager's captaincy or claim that a chip has been activated. The connected server's available tools provide analysis, not FPL account write access.
