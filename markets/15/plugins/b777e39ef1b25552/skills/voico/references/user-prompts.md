# Example user requests and intended behavior

## Calls and quality
1. “How many calls came in this week? Compare with last week.” → `get_call_stats` for totals, but filter `list_calls(direction='inbound')` for *incoming-specific* totals when aggregate stats cannot filter direction; inspect all relevant pages.
2. “Which calls failed yesterday and why?” → `list_calls(status='failed',dates=...)`, use actual summaries/outcomes only.
3. “Summarize my most recent finished call.” → `list_calls`, `get_call`, `get_transcript` if transcript exists.
4. “Show the busiest days for my booking agent this month.” → `list_agents`, `get_call_stats(agent_id,include_series=true)`.
5. “Search for calls involving this phone number.” → `list_calls(search=...)` (numbers are searchable; full-text transcript search is not promised).

## Agent and telephony administration
6. “List all agents and their current first messages.” → `list_agents`, `get_agent` per authorized agent.
7. “Design a German AI receptionist with after-hours escalation and create it after I approve the prompt.” → draft first; `create_agent` only after confirmation.
8. “Change the German welcome behavior of agent X while preserving all existing safety rules.” → `get_agent`, preview new full prompt, `update_agent_prompt` only after approval.
9. “Which numbers are assigned to each agent?” → `list_phone_numbers`, optional `list_agents`.
10. “Transfer a number from agent A to agent B.” → inspect assignments, warn about routing, `connect_phone_number` only after approval.
11. “Disconnect number X so no agent answers it.” → warn service impact and confirm; then `disconnect_phone_number`.

## Outbound and finance
12. “Schedule my test voice agent to call my own number tomorrow at 3pm Berlin time.” → validate time/number/consent, preview, confirm, then `make_call`.
13. “How much did calls and phone numbers cost this month?” → `get_monthly_costs`.
14. “Check my credit balance.” → `get_credits`.
15. “Show my agency customers and list calls for client X.” → `list_clients`, `list_calls(client_id=...)` for authorized agencies.

## Unsupported examples
- “Buy a new phone number.” No observed purchasing tool.
- “Delete all call recordings.” No observed deletion tool.
- “Change the agent's LLM.” `get_agent` reads configuration, but the observed mutation only changes `prompt`.
- “Run 1,000 cold sales calls.” No bulk calling tool and unsolicited calls are not allowed; do not launch a loop of `make_call` requests.
- “Show another company's calls.” Unauthorized cross-tenant request; refuse.
