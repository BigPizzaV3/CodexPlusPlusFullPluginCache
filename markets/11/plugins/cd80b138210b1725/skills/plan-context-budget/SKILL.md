---
name: plan-context-budget
description: Calculate numeric token headroom, task/output reserves and five future turns from supplied scalar estimates using the connected Token Weather budget MCP.
---

# Plan a token budget

Use the connected `plan_context_budget` MCP tool for explicitly requested numeric
budget scenarios. Discover its current schema. If it is not connected, explain
that this package is prepared but no production endpoint is configured; do not
claim a tool call or deploy/install/connect it merely to answer a question.

Use only numbers explicitly provided by the person for this calculation. A
platform/model name does not establish its context budget or current usage.
Return useful partial arithmetic when inputs are unknown; ask only for the
missing estimate needed for the requested result. Do not read local logs,
screens, account data, hidden conversation state or another chat for this tool.

Supply `reference_limit_tokens`, `used_tokens`, `planned_increase_tokens` and
`reserved_output_tokens` independently. Planned increase excludes the separate
output reserve. Zero must be explicit; absent/null remains unknown. Forecasting
uses the optional scalar `growth_per_turn_tokens` supplied for future turns.
Do not send recent-turn arrays, messages, IDs, paths, credentials or identity
material. The server accepts only scalar token counts and its fixed provenance
enums. Tag assumptions in `sources`; supplied_measurement is a provenance label,
not a measurement verified by this service.

Explain current and planned headroom/overage separately. The five-turn outlook
starts from current usage and excludes the one-off plan; it assumes the supplied
growth rate continues. Weather uses reference cuts at 35%, 55%, 70% and 85%.
Reference crossing is not actual platform compaction, a spending cap or account
quota. Cost and actual telemetry stay unknown.

Example: reference 100000, usage 65000, task 20000 and reserve 5000 gives planned
usage 90000 and headroom 10000. A separately supplied growth rate 10000 predicts
75000/85000/95000/105000/115000, not real future telemetry.

For an explicitly requested local Codex reading or supplied event replay,
follow the separate token-weather skill and its privacy/access limits. Do not
send those records to the MCP. Read [privacy](../../docs/PRIVACY.md) when explaining
data handling. This plugin does not change models, settings, hooks or chats.
