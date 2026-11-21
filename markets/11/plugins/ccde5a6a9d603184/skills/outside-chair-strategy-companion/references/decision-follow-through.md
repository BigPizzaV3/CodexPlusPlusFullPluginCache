# Decisions and follow-through

## Confirm a decision

1. Retrieve current context once and select exact relevant versions silently.
2. Present a compact draft containing decision, rationale, date, reconsideration condition, outcome-review date, actions, owners, deadlines and named context relationships.
3. Internally use only `relies_on` for assumptions, `considers` for observations and `affects` for initiatives. Other relevant context may be frozen without a relationship. Present the meaning, not these internal labels.
4. Obtain the first explicit confirmation before calling `prepare_decision_confirmation` because that call stores a proposal.
5. Show the returned exact summary, proposal hash and expiry. Obtain a second confirmation tied to that hash.
6. Call `confirm_decision`, then read back the approved snapshot and current actions.

## Update an action

Show the new status and completion details in one sentence, obtain one confirmation, call `update_action`, then read back current context.

## Record an outcome

Present expected and observed results, assessment, reconsideration requirement, lessons, causal limitations, considered observations and any accepted evidence attachments. Obtain one confirmation, call `record_decision_outcome`, then read back current context. Never imply causation beyond the confirmed assessment.
