---
name: start-sit
description: Decide weekly lineup starts and sits with FantasyPros data. Use when the user asks who to start, whether to start player A or player B this week, whether to add and start a free agent over one of their players, or for help setting their lineup.
---
<!-- ChatGPT plugin fork of agentic-coach/strands-backend/src/app/agent/skills/start-sit/SKILL.md (DATA-696). Keep workflow changes in sync. -->
# Start/sit

Workflow for weekly lineup decisions.

**Inputs:** optionally the specific players or lineup slots in question.

**Which week? Check this first.** `start_sit_assistant` always covers the league's *current* matchup week, which its result reports as `nfl_week`. A user can ask about a later week ("Week 6" while `nfl_week` is 5, e.g. on the Monday or Tuesday before the week rolls over, or when planning ahead). In that case:
- You MUST say that the assistant's lineup is for the current week, and you MUST NOT present that week's results, scores, byes, or win odds as the later week's.
- Build the later week's lineup from `get_projections` with `projection_type="weekly"`, `week` set to that week, and `fp_ids` set to the `player_id` values from the start/sit result. For byes, call `get_schedule_and_strength` with the teams of the players involved: each team's `bye_week` says whether it is off that week. If a team has no `bye_week`, say you could not confirm its bye; do not assume.
- Injury news can be stale for a week that hasn't started. Say that the recommendation should be re-checked once that week's practice reports are out.

0. **Are the named players on the user's roster?** `start_sit_assistant` only evaluates players already on the user's roster. A free agent or another team's player never appears in it, and a rostered player's expert-start percentage there is NOT a comparison against him. So when the user names specific players, first find where each one is: call `get_roster` with `all_teams=true` and the selected `league_key` (the entry with `is_user_team: true` is the user's). A player on no team's roster is unrostered — a free agent or on waivers. If any team comes back with an empty roster, the league's roster data is incomplete: say the player does not appear on any synced roster rather than stating he is available.
   - If any named player is not on the user's roster, you MUST call `get_player_comparisons` with `comparison_type="weekly"`, the selected `league_key`, and all the named players, and base the verdict on that result. You MUST NOT use `start_sit_assistant` for that decision or quote its expert-start percentage for the rostered player. State where the player is as a fact — "Shipley is unrostered in your league, so you'd add him first" or "Shipley is on Spirited Misconduct, so this would take a trade" (do not call that an add) — never "if he's available". Only call `start_sit_assistant` as well if the user also asks about the rest of their lineup.
   - Each compared player carries `kickoff`, `game_started`, and `on_bye` for this week. State them as facts, never "before his game begins": if the unrostered player's game has started, he cannot score for the user this week, so say so instead of recommending the add-and-start; if the rostered player's game has started, he is already locked where he is. If the result lists a limitation saying game status could not be checked, say that you could not confirm whether the games have started.
   - If every named player is on the user's roster, continue with step 1.
1. **Get recommendations.** When the players in question are all on the user's roster, or the user wants help with their whole lineup, you MUST call `start_sit_assistant` for the lineup recommendation against the user's league.
2. **Check bye weeks.** You MUST check the current starters and proposed replacements for byes in the week being discussed. Use `get_roster` if the current lineup is not available, and `get_schedule_and_strength` for their teams when the tool results do not establish bye status. Do not infer a bye from missing projections or rankings. Explicitly call out each current starter on bye: "Bench X — his team is on bye this week," and name an eligible replacement from the assistant's recommendations whose game has not started and who is not on bye. If no suitable bench replacement exists, flag the slot that needs a waiver pickup and use the waiver-wire workflow. Benching for a bye does not mean dropping the player. If bye status cannot be verified, disclose that instead of guessing.
3. **Check injuries.** You MUST call `injury_status` for any recommended starter flagged questionable or worse, and adjust the recommendation if their status is in doubt.
4. **Matchup context.** You SHOULD call `matchup_analyzer` when the user asks about their weekly matchup outlook or when a start/sit call is close enough that win probability context would change the advice (e.g. favoring a high-floor player when favored, high-ceiling when an underdog).
5. **Flex swaps for later kickoffs.** The assistant can return a swap that puts one starter in FLEX "instead of" another "due to later kickoff". This is NOT a start/sit call. Both players start. The later-game player moves to FLEX so the FLEX slot stays unlocked longest, and the user can still pivot there if late news hits. Projected points do not change. You MUST describe it that way: "Both X and Y start; move X (later game) to FLEX." You MUST NOT say one player starts "over" the other, call it close, or list the pair as a decision.
6. **Answer.** You MUST present clear start/sit verdicts with a confidence level and the single biggest deciding factor for each call. For game-time decisions you MUST flag the risk and name the contingency pivot if the player is ruled out.


## Account access and subscription limits

Apply this section before the workflow's tool requirements. It takes precedence when a requested tool or league is unavailable to the current account.

- OAuth sign-in is available to free and paid FantasyPros accounts. Use tool descriptions and current responses as the authority for access. If the host exposes `ff://user/entitlements`, it can establish the current user's tool access; do not assume that resource is exposed or callable.
- Only bring up a subscription restriction when it is relevant to the user's request. If a tool returns `status="premium_required"`, relay `required_user_disclosure` once, including the supplied informational link, and follow its access-related guidance. Do not promote upgrades, describe plans or prices, or encourage subscribing. Never replace the informational link with a pricing or checkout link.
- Do not treat a gated result as empty successful data, repeat the same denied call, or retry with a different identity or league to bypass access controls. Do not claim the gated tool ran or invent its results.
- Continue helping with tools the account includes when their returned data supports an answer. Clearly distinguish any alternative analysis from the unavailable assistant, finder, or analyzer result. If available tools cannot answer the request, state the limitation.
- `get_leagues` may return `locked_leagues` without a `league_key`. Do not guess or construct keys for them. If the selected league is locked, disclose the returned restriction once and offer an accessible league or general research using available tools. If the user has multiple accessible leagues and none is selected, ask which league to use. Pass the selected accessible `league_key` explicitly on every league-scoped call; the server is stateless.

## Data sources
- Rankings, projections, start/sit verdicts, injury designations, byes, and roster facts MUST come from the FantasyPros tools above. Do not web-search to check or supplement them, and never let a web result override them.
- Say how current the data is when it matters: results carry `data_as_of` (date, season, week), and `injury_status` news items carry `published`.
- For anything the tools do not cover (for example why a player's role changed), you MAY search the web: prefer fantasypros.com and the most recent sources, skip anything from a previous season, and say where the information came from and when it was published.
