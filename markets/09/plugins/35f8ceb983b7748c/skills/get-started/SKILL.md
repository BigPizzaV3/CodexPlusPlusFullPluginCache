---
name: get-started
description: How to answer engineering-leadership questions with Codiedev Reports — which tool to call, how to scope to a team, and how to state confidence.
---

# Codiedev Reports

Codiedev Reports is read-only. It answers questions from the connected company's Codiedev reporting. It can't change anything, and it never returns individual session transcripts.

## Who is asking

Call `list_teams` first when the user names a team, or when you need to know their access:

- `access: "company_admin"` means the user sees the whole company and may pass any `teamId` from the list.
- `access: "team_manager"` means the user sees only their own team. `canSeeSpend` is false, so don't call `get_finance` or `get_finance_detail`. Say spend is limited to company admins.

## Pick the tool

| Question | Tool |
| --- | --- |
| "How is engineering doing?" or another broad health check | `get_overview` (trim with `sections`) |
| "Is AI making us faster?" | `get_ai_impact` |
| "Are we shipping faster or slower?" or a repo slowing down | `get_velocity` |
| "When will we finish?" or predictability | `get_throughput_forecast` |
| Usage patterns or hitting limits | `get_activity` |
| Which models, errors or rate limits | `get_model_usage` |
| Rollout or who is using it | `get_adoption` (`team_status`, `signals`, `skills`) |
| How complete the data is | `get_capture_coverage` |
| Spend, ROI or waste (admins) | `get_finance` |
| Cost per merge, savings, what-if, seats, spend forecast (admins) | `get_finance_detail` |

`windowDays` accepts 30 (the default), 60 or 90.

## Answering

- Use only the numbers the tools return. When a field is null, missing, or `reason: "no_rollup_yet"`, say the data isn't available yet. Never fill in zeros.
- For AI impact, quote `classificationCoveragePct`. For broad claims, quote capture coverage from `get_capture_coverage`. Every metric only counts captured sessions.
- Durations are in milliseconds (`*Ms`). Convert them to hours or days for the reader.
- Money is in USD.
