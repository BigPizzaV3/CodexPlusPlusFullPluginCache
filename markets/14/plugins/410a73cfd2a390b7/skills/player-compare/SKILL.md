---
name: player-compare
description: Compare two to four NFL players for fantasy with FantasyPros expert data. Use when the user asks who is better, X vs Y, which player to prefer this week or for the rest of the season, or to rank a short list of named players.
---
# Player comparison

Workflow for head-to-head fantasy comparisons of named players. The verdict comes from FantasyPros expert consensus, not from web articles or memory.

**Inputs:** the 2–4 players being compared and the horizon (this week, rest of season, dynasty, or draft).

1. **Pick the horizon.** Map the question to `comparison_type`: "this week" or any start decision → `weekly`; "rest of season" or "going forward" → `ros`; keeper or long-term value → `dynasty`; draft prep → `draft`. If the user does not say, use `weekly` during the season and say that you did.
2. **Get the comparison.** You MUST call `get_player_comparisons` ONCE with every named player in `player_names`, the chosen `comparison_type`, and the user's `league_key` (from `get_leagues` if you do not have it), so the league's scoring is applied. More than four players → compare the four the user cares about most and say so.
   - If the result lists `unresolved_names`, retry with the full first and last names before answering. Never compare a player the tool did not resolve.
   - Base the verdict on `expert_consensus` (the share of experts who prefer each player) and each player's `position_ranking`, plus the projections the result includes. Cite those numbers.
3. **Roster context.** If the question is whether to start one of the user's players over another, this skill applies as is. If one of the players is not on the user's roster, follow the start-sit skill's step 0 and say whether he would be an add or a trade.
4. **Injuries.** For any compared player who is questionable or worse, or whom the user mentions as hurt, you MUST call `injury_status` (all such players in one call) and fold the designation into the verdict. State the date of the report or news you rely on.
5. **This week's games.** For a weekly comparison, each player carries `kickoff`, `game_started`, and `on_bye`. A player on bye or whose game has started cannot be started this week: say so as a fact, not a factor.
6. **Rest-of-season context.** For a `ros` comparison that is close, you SHOULD call `get_schedule_and_strength` for both players' teams and position, including the fantasy playoff weeks, and name the schedule edge if there is one.
7. **Answer.** Lead with the pick, a confidence level, and the single biggest reason, quoting the FantasyPros numbers it rests on (for example "62% of experts prefer X; he is WR14 vs WR22"). Then one line per other player. Keep it short unless the user asks for depth.


## Account access and subscription limits

Apply this section before the workflow's tool requirements. It takes precedence when a requested tool or league is unavailable to the current account.

- OAuth sign-in is available to free and paid FantasyPros accounts. Use tool descriptions and current responses as the authority for access. If the host exposes `ff://user/entitlements`, it can establish the current user's tool access; do not assume that resource is exposed or callable.
- Only bring up a subscription restriction when it is relevant to the user's request. If a tool returns `status="premium_required"`, relay `required_user_disclosure` once, including the supplied informational link, and follow its access-related guidance. Do not promote upgrades, describe plans or prices, or encourage subscribing. Never replace the informational link with a pricing or checkout link.
- Do not treat a gated result as empty successful data, repeat the same denied call, or retry with a different identity or league to bypass access controls. Do not claim the gated tool ran or invent its results.
- Continue helping with tools the account includes when their returned data supports an answer. Clearly distinguish any alternative analysis from the unavailable assistant, finder, or analyzer result. If available tools cannot answer the request, state the limitation.
- `get_leagues` may return `locked_leagues` without a `league_key`. Do not guess or construct keys for them. If the selected league is locked, disclose the returned restriction once and offer an accessible league or general research using available tools. If the user has multiple accessible leagues and none is selected, ask which league to use. Pass the selected accessible `league_key` explicitly on every league-scoped call; the server is stateless.

## Data sources
- Rankings, projections, expert consensus, injury designations, and byes MUST come from the FantasyPros tools above. Do not web-search for rankings, projections, or injury designations, and never let a web result override them.
- Say how current the data is when it matters: results carry `data_as_of` (date, season, week), and `injury_status` news items carry `published`.
- Web results MAY add news context the tools do not cover (for example a role change or a coach's comments): prefer fantasypros.com and the most recent sources, skip anything from a previous season, and say where the information came from and when it was published. News context never changes the FantasyPros-based pick on its own; if it seems to, say why.
