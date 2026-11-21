# Modern Performance: on-demand training report

Use this workflow when the user asks how their Modern results are developing, whether local results transfer to competitive events, which matchups matter, or requests the full Modern Performance report. Build a fresh report from Matchbook MCP data for the authenticated user. Present it in the conversation or in an artifact the user requested. Do not create or update a web dashboard as part of this workflow.

Read [tools.md](tools.md) for tool contracts. All numbers below must come from returned records, never from the illustrative examples in a prompt. Keep the selected player deck distinct from all-deck player history.

## Scope and retrieval

The analysis key is **tournament format + player deck ID + inclusive date range**. Also accept event tier/type, venue (and city/country when needed), and played-only versus all recorded match results.

- Default to `format: "Modern"`, the current calendar year (or the last 12 months when that better matches the user's stated period), the most recent identifiable deck with a played Modern match, all eligible Regular + Competitive events, and `resultTypes: ["played"]`. State the actual date bounds and selected deck. Preserve user-specified filters instead of applying defaults over them.
- Call `list_matches` with format/date/location filters, `limit: 100`, and follow `nextOffset` until `null`. Its pages are newest-first by tournament, not the chronological order needed for rolling rates. For played-only mode request `resultTypes: ["played"]`; for all recorded results omit `resultTypes`, then retain a played subset for matchups and game statistics.
- Fetch the **all-deck** rows in the selected format/period/location/tier to calculate player history, opponent distribution across the format, and deck consistency. Select the deck by `deckId` from those rows. Use `list_decks` if a name is ambiguous or the user wants to choose among registered decks. Do not combine similarly named deck IDs without evidence that they represent one deck. If the user explicitly selects “All decks,” label combined matchups as all-deck history, not current-deck matchups.
- Apply tier classification locally to each match using `eventType` and `tournamentName` as described below. The MCP analytics tools do not currently accept a tier filter. Use `get_stats` or `get_matchup_stats` as optional cross-checks only when their scope matches the report exactly; their default summaries can include tournament-level totals or excluded event types. Recompute tier-filtered figures from the fetched match rows.
- If any page fails or the retrieval is incomplete, do not present percentages as if they cover the full period. Report what was fetched and the limitation. Do not silently truncate at the first 50 or 100 rows.

`list_matches` contains match-level records. Explicit tournament W-L-D totals with no corresponding match rows cannot supply opponent, date order within an event, tiered matchups, or game scores. Keep them out of the training metrics, and disclose this coverage limit when relevant. A tournament has one `format` field; do not assign a mixed-format round to Modern when its format is unknown.

## Event tier classification

Classify from **both** recorded `eventType` and tournament name. Do not edit historical records just to make a report. Apply the following order so exclusions take precedence over competitive keywords:

1. **Separate / excluded by default:** Prerelease, Sealed, Booster Draft, Draft, Game Day, Store Championship. Also keep a genuinely unknown level separate rather than calling it competitive.
2. **Competitive:** RCQ, Regional Qualifier, PTQ, PPTQ, Championship Qualifier, Premium Event Qualifier, Mythic Championship Qualifier, Pro Tour Destination, Spotlight competitive event, Grand Prix main event, Nationals.
3. **Regular:** Friday Night Magic/FNM, weekly or local Modern, ordinary store event, other clearly recurring local constructed tournaments. A generic `Tournament` type alone is not proof of level; use the name and context. If still ambiguous, mark it Unclassified and show the count separately.

By default include only Regular and Competitive in performance metrics. A requested tier filter applies to every metric in the report; an unavailable side of the Regular vs Competitive comparison is shown as `—`. Include Separate/Unclassified only if the user explicitly requests them, and label the resulting scope. Never treat Prerelease or Limited results as competitive constructed performance.

## Metric contract

Use rows after format/date/location/tier filtering. When the user chooses all recorded results, non-played rows may enter **match-level** W-L-D, trend, and tier comparison. Matchup and game calculations remain played-only in every mode.

| Metric | Calculation and display |
| --- | --- |
| Match WR | `W / (W + L)` from decisive rows; draws are outside the denominator. Show W-L-D, total rows, and decisive count. Show `—` if `W + L = 0`. |
| Rolling 10 / 20 WR | Sort decisive rows by tournament date ascending, then `eventId`, `roundNumber`, and `matchId`; use the latest 10 or 20 at each point. Show the available count and `Partial` until the window fills. |
| Cumulative WR | For each chronological decisive match, wins so far / decisive matches so far. Reference 45%, 50%, 55% visually without skill labels. |
| Competitive gap | `Competitive WR - Regular WR` in percentage points for the same deck and period. Show `—` unless both sides have decisive matches, and show both sample sizes. |
| Game WR | Sum `playerGamesWon` / (sum of both players' games) only where `resultType=played` **and both game scores are known**. Missing scores, byes, technical results, concessions, and no-shows contribute no games. Show scored-match count. |
| Loss contribution | Played losses against an exact opponent archetype / all played losses for the selected deck and scope. Show `—` when no played losses exist. |
| Field share | Played matches against an exact opponent archetype / all played matches for the selected deck and scope. Keep `Unknown` as its own group. |
| Deck consistency | Among the latest 20 and latest 50 played matches across **all decks** in the filtered format/period/tier/location, report the most-played deck share and selected-deck share. Show available counts when fewer than 20 or 50 exist. |

Use tournament date, not import or update time. Several tournaments on one date may lack their true time order; `eventId` is only a stable tie-breaker. If the data is sparse, say so rather than drawing a trend conclusion.

Matchup maturity by played match count: 1–4 **Insufficient**, 5–9 **Tentative**, 10–19 **Useful**, 20–29 **Strong**, 30+ **Mature**. Deck-level sample maturity: under 20 **Early**, 20–49 **Developing**, 50–99 **Useful**, 100+ **Mature**. These labels describe sample size, not player skill. Display `N / 50` for the selected deck and `N / 10` for relevant exact matchups. Do not use strong favorable/unfavorable coloring or claims below 10 matchup matches.

Normalize only case and whitespace variants already treated as one exact archetype by Matchbook. Do **not** merge labels such as `UG Oculus`, `WUG Oculus`, and `UG Cascade Oculus` into a family without an explicit family mapping. Use the most recent recorded spelling for display if variants differ. Unknown opponent names do not prevent archetype analysis; unknown archetypes remain `Unknown`.

## Report shape

Adapt length to the user's question. For the full report, use this order and keep every rate adjacent to its sample size:

1. **Context and current performance:** format, selected deck, period, tier, venue, result scope; Match WR, Rolling 20 WR, Competitive WR, Game WR, deck sample progress. Mark fewer than 20 decisive matches as partial and fewer than five total matches as highly uncertain.
2. **Win Rate Over Time:** rolling 10, rolling 20, cumulative WR by chronological match. Use a compact chart if the response medium supports it; otherwise a dated progression table or concise sequence. If interactive tooltips are available, include date, event, opponent, opponent archetype, result, and all three rates. Avoid hiding early partial windows.
3. **Regular vs Competitive:** both W-L-D records and WRs, sample counts, competitive gap, or a clear no-data state.
4. **Matchup matrix for the selected deck:** exact opponent archetype, matches, W-L-D, Match WR, Game WR with scored-match count, last played, and maturity. Sort by played match count descending, then latest date. If a sortable artifact is requested, also support Match WR, Game WR, loss contribution, and recency.
5. **Matchup detail on request:** chronological W/L/D sequence, dates, tournament names, opponents when known, scores when known, tier split, and aggregate rates. Do not invent game-one, post-board, play/draw, or sideboard statistics.
6. **Sample progress and encountered field:** selected deck `N / 50`; relevant matchups `N / 10`; opponent archetype frequency and field share. Prefer horizontal bars over a pie chart when visualizing many archetypes.
7. **Biggest Opportunities:** archetype, matches, W-L-D, WR, field share, losses, loss contribution, and maturity. Favor both actual losses and useful sample size; one 0–1 result is not a major training priority. A transparent priority sort is `losses × min(matches / 10, 1)`, with raw losses and sample count as tie-breakers. This priority score is only for ranking, never a win-rate estimate.
8. **Deck consistency and perspective:** latest-20 and latest-50 deck shares, and a separate all-deck Player History count. If play is fragmented, explain neutrally that selected-deck matchup samples accumulate more slowly.

Use `—` for unavailable rates, not `0%`. Show the observed result even for an insufficient matchup, but label its uncertainty. Distinguish measured facts from any training suggestion. Close with the largest data gaps or quality limits affecting the conclusions.
