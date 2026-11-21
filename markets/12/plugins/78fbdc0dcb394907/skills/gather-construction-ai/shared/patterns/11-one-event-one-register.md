# Pattern 11: One Event, One Register

Three skills produce lost-time registers with different scopes and units. Their totals must never be summed — the same event (e.g. a rained-off possession day) legitimately appears in all three.

| Register | Skill | Unit | Role |
|---|---|---|---|
| DA | `delay-analysis` | shift-hours of delay (event duration, not person-hours) | **Master register** — all causes |
| AC | `access` | person-hours of standing time | Cause-specific deep dive (access only) |
| WI | `weather-impact` | person-hours of shortfall vs theoretical maximum (crew-scaled: days × standard shift × average crew; all-cause, weather-flagged) | Cause-specific deep dive (weather only) |

**Rules:** (1) When more than one of these registers exists in a conversation, each report states: "Do not sum totals across DA/AC/WI registers — they overlap by design and use different units." (2) Cause-specific reports cross-reference the master register by Ref number where one exists. (3) Any hours→days conversion states its divisor (use the median shift duration for the period, and say so).
