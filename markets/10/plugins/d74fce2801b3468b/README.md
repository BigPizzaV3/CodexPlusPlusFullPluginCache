# Lezonder 1.0.11

Six read-only tools at https://www.lezonder.com/mcp (AI connector v2, Release A, live on the server
since 2026-11-03): `get_latest_result`, `get_sleep_trend`, `get_sleep_history` (up to 30 days of
nightly detail), `get_tonight_target`, `get_account_status` and `explain_lezonder`. The detail tools
need the new `lezonder:mcp:details:read` permission. `get_monthly_progress` (draw standing) is not
listed until Release B turns on `draw_progress`. Same MCP key (`lezonder-sleep`), server and OAuth
client. Plan: `docs/ai-connector-v2-plan.md`.

Previous README (1.0.10) follows.

Two read-only sleep tools at https://www.lezonder.com/mcp: the latest dated Lezonder Sleep Score
and dated scores for the last one to seven days. Same MCP key (`lezonder-sleep`), server, tools,
OAuth client and review cases as the published 1.0.7.

Available in every country ChatGPT supports (`publication.countries: []`, since 1.0.8). Any
existing Lezonder account can connect (owner decision 2026-10-15). Scores from Apple Health and
WHOOP are shared, including Oura data that reaches Lezonder through Apple Health. Scores whose
month touches data from a direct Oura connection are refused with `oura_sharing_not_allowed`,
because Oura's API Agreement forbids sharing them with AI apps (live since 2026-10-31; see
`../../README.md`, Oura rule). Reviewer credentials stay outside the ZIP.

Changes in 1.0.10: `longDescription` adds the sentence "Scores calculated from a direct Oura
connection can't be shared, because Oura's developer rules don't allow it. Oura data synced
through Apple Health works." The subtitle "See if your sleep is improving" is from 1.0.9. No
tool, schema, OAuth or review case changes.
