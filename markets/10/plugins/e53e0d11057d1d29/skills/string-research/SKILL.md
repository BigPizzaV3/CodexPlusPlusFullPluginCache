---
name: string-research
description: Answer tennis string questions with the StringSpec tools - look up one string, compare two or three, recommend strings for a player's needs and racquet, and search or sort the database - and report the numbers honestly (measurements versus estimates, what a percentile means, which way is better for each metric, dated prices). Use whenever the user asks about tennis strings, restringing, string tension, string stiffness or comfort, spin strings, polyester versus multifilament or gut, or strings for tennis elbow or arm pain.
---

# Tennis string research with StringSpec

The `stringspec` MCP server gives read-only access to lab measurements of nearly 800 tennis strings, kept by stringspec.com. Every string was measured on the same machine under the same protocol, so the numbers compare fairly between strings. This skill is about choosing the right tool and reporting what it says honestly.

## Pick the tool

- **One named string** ("how does Hyper-G play?"): `get_string` with the name as the user wrote it. Misspellings and missing gauges are fine. If the answer lists `other_matches`, say which variant you used and offer the others.
- **Two or three named strings**: `compare_strings`. Give the `comparison_url` when there are two.
- **The player describes what they want** ("more spin", "my elbow hurts", "too much power"): `recommend_strings`. Map the request to `need`:
  - spin, shape, topspin: `spin`
  - arm, elbow or wrist pain, comfort, softer: `comfort`
  - control, launching the ball, too much power: `control`
  - power, depth, a short ball: `power`
  - strings going dead, tension loss: `hold`
  - breaking strings often: `durable`
  - touch, feel, volleys: `feel`
  Add `also` for a second wish. Ask about the racquet only if it changes the answer: string pattern (`open` or `dense`), head size (`small`, `mid`, `large`), frame feel (`flex`, `avg`, `stiff`). Use `avoid` when the player rules out gut (`gut`), polyester (`poly`) or wants polyester only (`polyonly`). For arm pain, `comfort` plus `frame` when known, and suggest `avoid: "poly"` if they have not tried non-polyester strings.
- **Filtering or ranking** ("softest polyesters", "cheapest Babolat", "17 gauge multis"): `search_strings` with `material`, `gauge`, `brand`, `query`, `max_price_usd` and `sort`. It returns at most 10 rows; narrow the filters instead of asking for more.

## Read the numbers correctly

- **Direction differs by metric.** Lower `stiffness_lb_in` is softer and kinder on the arm. Lower `tension_loss_pct` holds tension longer. Higher `energy_return_pct` is livelier. Higher `spin_potential` and higher `ball_bite_cof` help spin; lower `string_friction_cof` means the strings slide and snap back more freely.
- **A percentile is the share of measured strings with a lower value**, whichever direction is better. A stiffness percentile of 10 means softer than about 90% of strings. Translate it into plain words ("softer than 90% of the database") rather than quoting the raw percentile.
- **Measurements versus estimates.** Everything under `measured` and `elongation_pct` is a lab measurement. `playable_life_hours`, `tension_advice` and `fit` are estimates derived from those measurements. Say so when you use them.
- **The numbers compare strings with each other, not a strung racquet.** Racquet, tension and swing still decide how a string feels. Do not promise an outcome ("this will cure your elbow").
- **Prices are a retailer's set price on `price_checked`, not live.** When `buy_note` says there was no exact match, the link opens a search. Never invent a price for a string without `price_usd`.

## Good answers look like this

Placeholders in angle brackets stand for values from the tool results.

- "<string> measures <stiffness> lb/in, softer than <100 - percentile>% of the strings tested, and loses <tension_loss>% of its tension under the test, which is <better or worse> than most. StringSpec estimates about <hours> hours of play before it goes dead; that is an estimate, not a measurement."
- "For a stiff frame and a sore elbow, StringSpec's finder ranks <string> first (fit <fit>/100): it is among the softest beds tested and holds tension well. The finder removed the firmest quarter of the database because a stiff frame and a stiff string add up at the elbow."
- Link the string's `url` on stringspec.com when the user wants the full charts.
