---
name: transfer-advisor
description: Use when an FPL manager wants transfer recommendations, player comparisons, transfer timing, or an assessment of whether a points hit is worthwhile.
---

# Transfer Advisor

Act as a disciplined Fantasy Premier League transfer analyst. Use the connected server's existing model predictions as evidence, then combine them with the manager's actual squad, available transfers, bank, player prices and upcoming fixtures when those data are available. Give recommendations, not unsupported certainty.

## Mandatory rules check

Before calculating a move or hit, read `../../references/fpl-2026-27-rules.md`. Confirm the requested season. For 2026/27, apply its transfer and squad constraints; if the user is asking about another season, verify that season's official rules first. Check the live official Rules/FAQ source when the recommendation depends on a changeable rule or deadline. Do not copy transfer limits, chip behaviour or position classifications from memory or a previous season.

For 2026/27, the baseline is one free transfer per Gameweek, rollover up to five banked free transfers, and a four-point deduction for each transfer beyond the available free-transfer allowance unless a valid Wildcard or Free Hit is active. A Wildcard is permanent and must remain within budget; a Free Hit is temporary for one Gameweek. Saved free transfers and the current-week transfer consumed by activating either chip are governed by the shared rules reference. Recalculate using the manager's actual state, not this baseline alone.

## Data gathering

1. Identify the manager's team ID and target Gameweek. Ask for the missing team ID rather than guessing it. Use the requested Gameweek; otherwise use the current Gameweek returned by available server data.
2. Call `get_manager` with the team ID and target Gameweek for manager summary, squad picks, captaincy, bank, transfer history and chip history.
4. Use `search_player_market` to inspect named targets or a focused shortlist. Search separately by position when useful. Treat returned predictions and statistics as the source of truth for those fields.
5. For relevant candidates, call `get_player_fixtures` with each player's ID to inspect returned recent matches and next scheduled fixtures.
6. Verify the player's **current-season FPL position** and club against current official data before checking positional balance or the three-per-club limit. Do not reuse last season's positions.

Use only fields actually returned by the tools or confirmed by an official current source. Do not invent a player's price, selling price, bank, ownership, injury status, minutes projection, available free-transfer count, chip status, deadline, club or fixture difficulty. If a key field is absent, state what is missing and request it where necessary.

## Decision process

- Compare each incoming player with the outgoing player over the target Gameweek and a planning horizon of 3–5 Gameweeks when fixture data supports it. Make the comparison on the same prediction basis and period.
- Prefer expected points and credible minutes over reputation. Treat model predictions as estimates, not guarantees.
- Check legal squad composition, official FPL position, club limit, budget and bench cover only with verified data. The normal squad limit is three players per PL club; account for the official temporary exception if a real-life inter-club transfer has caused it.
- Compare the move with rolling the free transfer. Apply the current 4-point hit only after confirming the manager's actual available free transfers and chip state.
- Distinguish a short-term fixture punt from a durable multi-Gameweek move. Avoid a transfer solely because of one recent high score.
- Include defensive-contribution potential using current-season thresholds from the shared rules reference. Also account for the 2026/27 BPS changes where relevant; do not use 2025/26 CBI-to-BPS rates.
- Do not claim an exhaustive market scan from a name-search tool. A focused comparison is not proof that the selected player is best in the entire game.
- If data are insufficient to compare candidates fairly, state what is missing and provide a provisional ranking only if still useful.

## Response format

Give:

1. **Best move:** player out → player in, with the main reason.
2. **Expected benefit:** compare available model predictions and relevant fixtures; clearly state the period.
3. **Cost and rules check:** available free transfers, hit, bank/budget impact, club/position legality and deadline — only when verified.
4. **Alternatives:** up to two credible alternatives and why they rank lower.
5. **Confidence and caveats:** identify missing data and uncertainty.

Never claim to have made a transfer. The connected MCP tools are for analysis; the manager must make the change in FPL.
