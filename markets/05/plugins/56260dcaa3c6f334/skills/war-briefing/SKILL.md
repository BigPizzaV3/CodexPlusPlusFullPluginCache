---
name: war-briefing
description: Brief the user on the Iran–US war from World War Watcher's curated, sourced data, with a citation for every claim. Use when the user asks what is happening in the war, for a daily or weekly briefing, or how the war is affecting oil, shipping, cloud infrastructure or weapon stocks. The user's own instructions about scope, length or format take precedence over this skill.
---

# War briefing

World War Watcher publishes daily dispatches, a dated event timeline, a graded source registry, a
0–1 escalation score, US oil supply, Gulf cloud and connectivity status, submarine-cable status and
curated weapon stockpiles. Day 1 of the war is 2026-02-28; war day N is 2026-02-28 plus N−1 days.

The user's instructions override this skill whenever they differ.

## "Brief me on the war today"

1. `get_dispatch` with no day: the latest dispatch and its sections.
2. `search_timeline` with `from` set two days before today: the newest dated events.
3. `get_escalation_score` with `history_days: 7`: the score, its factors and the week's trend.
4. `get_oil_supply`, when the briefing should cover energy.
5. Optionally `render_situation_card`, when a visual helps.

Lead with events, not the score. When the score appears, say it measures current intensity and is
not a forecast. Cite each claim with the `url` of the result it came from.

## "How is X affecting Y"

1. Map Y to its data tool: oil → `get_oil_supply`; cloud, internet or cables →
   `get_infrastructure_status`; interceptors or missiles → `get_weapon_stockpiles`.
2. `search` for "X Y", then `fetch` the two most relevant passages.
3. `search_timeline` for X to date the events.

Keep correlation and attribution apart: a movement in the data that coincides with an event is not
evidence the event caused it unless a passage says so, with its source.

## Rules

- Report not-found as not-found. A day without a dispatch, or a passage id that does not exist, is
  absent, not pending.
- Flag stale data: when a result has `stale: true`, say how old `asOf` is.
- Attribute: timeline events carry `source_attribution`, and `quoted_text` is the quoted party's own
  words. Present claims as the source's, not as settled fact.
- Stockpile counts are curated estimates with a confidence grade and an assessment date; a null
  count is not assessed, never zero.
- Decline trading advice and forecasts of strikes, targets or casualties. For casualty totals, point
  to the UN OCHA and UCDP datasets rather than estimating.
- World War Watcher's data is CC BY-NC 4.0: cite it and do not present it as your own.
