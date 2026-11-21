# Optional portfolio financial details

Use these fields only inside `payload.portfolio.portfolio_financials` when the user supplies or asks to include more than the required count, principal, and currency. All monetary amounts use that portfolio's currency and must be finite, nonnegative numbers. Do not guess missing amounts or require optional values before submission.

| Field | Meaning and omitted behavior |
| --- | --- |
| `interest` | Interest; defaults to zero. |
| `attorney_fees` | Attorney fees; defaults to zero. |
| `court_costs` | Court costs; defaults to zero. |
| `other_costs` | Other costs; defaults to zero. |
| `total` | Defaults to principal + interest + attorney fees + court costs + other costs when omitted. |
| `repaid_balance` | Amount repaid; defaults to zero. |
| `oustanding_balance` | Outstanding balance; defaults to `max(total - repaid_balance, 0)` when omitted. The API field intentionally has this spelling, with the missing "t". Do not send `outstanding_balance`. |
| `late_balance` | Overdue amount; defaults to zero. |

Omit unspecified optional amounts so the backend can apply its defaults; in particular, do not replace omitted `total` or `oustanding_balance` with zero. If supplied figures conflict, ask for clarification rather than silently changing them. Show friendly labels such as "outstanding balance" in the confirmation summary, keeping the API spelling internal.
