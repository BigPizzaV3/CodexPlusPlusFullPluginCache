# Costs, credit balance, and agency end customers

## Billing

`get_monthly_costs(timezone=...)` provides month-to-date spend including call costs and phone number costs. `get_credits()` provides current remaining euro credit. They are **not** interchangeable: remaining credit is not revenue, a withdrawal amount, or the price of the next call. Use returned values and current month/time zone. If a tool provides no currency field, only describe the credit balance in EUR, as documented. Don't invent tax treatment, future bills or refund eligibility.

## Agency and multi-client views

`list_clients()` lists end customers only for partner-agency accounts, with their `client_id`. If it returns permission errors for a regular account, explain the partner-only feature rather than treating the account as broken.

Partner filters:
- `list_agents(client_id=...)` lists agents belonging to one authorized end customer.
- `list_calls(client_id=...)` lists that customer's call records (also supports direction, status, dates, pagination).
- Do not use `get_call_stats(agent_id=...)` as if it directly supports a `client_id` filter. Resolve permitted agent IDs first and aggregate only where data completeness can be guaranteed. Do not assume agency access gives universal tenant access.

Always state whose workspace/client the report covers, and never combine client call records in a way that reveals data to another customer. If the user requests aggregate agency metrics beyond the existing filters and the tools cannot deliver accurate totals within pagination/limits, state the limitation.
