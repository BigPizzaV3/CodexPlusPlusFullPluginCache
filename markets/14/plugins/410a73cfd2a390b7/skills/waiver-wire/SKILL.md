---
name: waiver-wire
description: Recommend waiver-wire pickups and evaluate specific waiver moves with FantasyPros data. Use when the user asks about free agents, waiver targets, pickups, who to add, who to drop, or whether a particular add/drop is worth making.
---
<!-- ChatGPT plugin fork of agentic-coach/strands-backend/src/app/agent/skills/waiver-wire/SKILL.md (DATA-696). Differs only where Coach uses tools the public MCP server lacks (get_roster_with_rankings) and Coach-only visual cards. Keep workflow changes in sync. -->
# Waiver wire

Workflow for recommending waiver adds and the drops to make room for them, and for evaluating a waiver move the user already has in mind.

**Inputs:** optional position of interest, and/or specific player(s) the user wants to add or drop.

1. **Pick the right tool.** Read what the user actually asked for and route accordingly — this choice is not optional:
   - **The user names the player(s) they are considering adding** ("should I pick up X?", "is X worth a claim?", "add X and drop Y?", "X or Y off waivers?"): you MUST call `waiver_analyzer` with `coach_adds` set to the named player(s), and `coach_drops` set to the drop they named if they named one. You MUST NOT call `waiver_finder` to answer this — it returns a generic list and ignores the move the user asked about. When the user is weighing two alternative adds against each other, call `waiver_analyzer` once per candidate and compare the results; only pass multiple names in a single `coach_adds` when they are adding all of them together.
   - **The user asks open-endedly who to add** ("who should I pick up?", "best waiver targets", "any RBs available?"): you MUST call `waiver_finder` (with the `position` filter when the user names one).
   - **The user names only the player they want to drop** ("any moves with dropping X?", "who can I pick up for X?", "I want to cut X, who replaces him?"): call `waiver_finder` (with the `position` filter when the user names one) only to find candidate adds. Its suggestions pair each add with a drop that it picks itself, which is often NOT the player the user named. Then call `waiver_analyzer` once per top candidate (up to three), with `coach_adds` set to that candidate and `coach_drops` set to the player the user named, and base your answer on those results. You MUST NOT present `waiver_finder`'s own add/drop pairings for this request, because they show a different drop than the one you recommend. You MUST NOT state the named drop's rank or value unless a tool result reports it.
   - **The user asks only who to drop** ("who should I cut?"): find the lowest-ranked players on the user's roster at a position where they have other depth, using the roster and rankings from step 2.
   - **The user asks whether to add AND start a player over one of their own** ("should I add and start X over Y?"): use `waiver_analyzer` for the add as above, and `get_player_comparisons` with `comparison_type="weekly"` and the selected `league_key` for the start. You MUST NOT use `start_sit_assistant` for the start — it only sees the user's roster, so it never evaluates X and its expert-start percentage for Y is not a head-to-head.
   - If the user names a player but `waiver_analyzer` reports them unavailable or unrostered in a way that blocks the analysis, you SHOULD then fall back to `waiver_finder` for alternatives and say why.
2. **Evaluate against the user's lineup, not a league grade.** You MUST weigh the move or the candidates against the user's actual roster and starting lineup:
   - Call `get_roster` for the user's players by position, `get_current_starters` for who is in the lineup now, and `get_league_settings` for the starting slots (`roster_positions`: how many QB/RB/WR/TE, and which positions each FLEX slot accepts). Do not guess the slot counts.
   - For the positions involved, call `get_ecr` with `ranking_type="ROS"` and that position to get each player's rest-of-season rank. Do not rank players from memory.
   - A candidate helps only in one of two ways. Say which one applies: (a) **Starter upgrade** — his rank beats the user's worst current starter at a slot he can fill, FLEX included; or (b) **Contingent value** — he backs up a starter and would become a weekly starter if that starter got hurt. A player who is neither is a low-ceiling bench add; say so plainly.
   - `league_analyzer` positional grades are league-relative context only. A low grade at a position does NOT by itself mean the user needs a player there, and a high grade does not mean they don't. Check the actual starters first. You MUST NOT name a position as the user's weakness while citing a grade that ranks it among the league's best.
   - In shallow leagues (8–10 teams), weekly starters on the wire are common, so favor candidates with a real path to starter-level points over low-upside depth.
3. **Schedule context.** You SHOULD call `get_schedule_and_strength` to compare upcoming schedules (including fantasy playoff weeks) when two candidates are otherwise close, or when judging whether a named add upgrades the user's rest-of-season outlook.
4. **Drops — only when a roster spot is needed.**
   - When a waiver tool returns `open_roster_slots` greater than 0, or the user says they have an open spot, the add needs no drop. You MUST NOT suggest a drop, name a player to cut, or add "if you later need room" advice.
   - Only when the roster is full and the user has not named a drop SHOULD you identify the best drop candidate from the user's bench and say why they are expendable. Compare the add against the players you would cut, using their ranks. Never propose cutting a player who ranks clearly above the add.
   - When the user did name a drop, you MUST say whether that drop is the right one or another bench player is more expendable.
5. **Players whose game has started.** Waiver results mark each candidate with `game_started` and list started players under `game_already_started`. You MUST NOT recommend a player whose game has started as a pickup for this week. If you mention one, say that his game has already been played. If a result says it could not check game status, say so before recommending a pickup for this week.
6. **Answer.** For a specific move, lead with a clear verdict (make the move or not) and the single biggest reason. For an open-ended request, present a ranked list of adds with a one-line rationale each, and say for each one whether it is a starter upgrade or contingent value. When league settings indicate FAAB or waiver priority, you SHOULD include bid-size or priority guidance proportional to the player's expected impact.
7. **Stay on one verdict.** Once you have recommended an add, keep that recommendation unless new data changes it. When the user pushes back, re-check with the tools, then either hold your position with the reason or say what new fact changed it. Do not recommend leaving an open roster spot empty; fill it with the best available option.


## Account access and subscription limits

Apply this section before the workflow's tool requirements. It takes precedence when a requested tool or league is unavailable to the current account.

- OAuth sign-in is available to free and paid FantasyPros accounts. Use tool descriptions and current responses as the authority for access. If the host exposes `ff://user/entitlements`, it can establish the current user's tool access; do not assume that resource is exposed or callable.
- Only bring up a subscription restriction when it is relevant to the user's request. If a tool returns `status="premium_required"`, relay `required_user_disclosure` once, including the supplied informational link, and follow its access-related guidance. Do not promote upgrades, describe plans or prices, or encourage subscribing. Never replace the informational link with a pricing or checkout link.
- Do not treat a gated result as empty successful data, repeat the same denied call, or retry with a different identity or league to bypass access controls. Do not claim the gated tool ran or invent its results.
- Continue helping with tools the account includes when their returned data supports an answer. Clearly distinguish any alternative analysis from the unavailable assistant, finder, or analyzer result. If available tools cannot answer the request, state the limitation.
- `get_leagues` may return `locked_leagues` without a `league_key`. Do not guess or construct keys for them. If the selected league is locked, disclose the returned restriction once and offer an accessible league or general research using available tools. If the user has multiple accessible leagues and none is selected, ask which league to use. Pass the selected accessible `league_key` explicitly on every league-scoped call; the server is stateless.

## Data sources
- Rankings, projections, waiver recommendations, injury designations, and roster facts MUST come from the FantasyPros tools above. Do not web-search to check or supplement them, and never let a web result override them.
- Say how current the data is when it matters: results carry `data_as_of` (date, season, week), and `injury_status` news items carry `published`.
- For anything the tools do not cover (for example why a player's role changed), you MAY search the web: prefer fantasypros.com and the most recent sources, skip anything from a previous season, and say where the information came from and when it was published.


## Waiver bid limitations
If waiver_finder returns data_source=waiverFinder, relay its limitations and do not quote or estimate a FAAB bid: that path has no bid data. Quote bid guidance only when the result supplies it.
