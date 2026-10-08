---
name: tossups
description: Use when the user asks which 2026 US Senate or House races are competitive, close, in play, battlegrounds, or toss-ups. Lists them with list_races_by_rating and reports the true total, not just the races the tool happened to name.
---

# List the races in play

Call `list_races_by_rating` with `rating: "competitive"`, which spans Lean D, Toss-up and
Lean R together. That is what "in play", "close" and "competitive" mean; `tossup` alone is
narrower than the question almost anyone is asking.

- If the user specifically asks for toss-ups only, call it with `rating: "tossup"` and say
  which of the two you are showing.
- If the user does not say which chamber, use the Senate and say that you did. Offer the
  House if it seems wanted.

## Reporting the result

- The **true total** the tool returns, not the number of races it named. The list can be
  capped; the total never is.
- The date the ratings were published.

A rating is a forecaster's opinion about a race that has not happened. Never phrase it as
though something has occurred in that state or district.
