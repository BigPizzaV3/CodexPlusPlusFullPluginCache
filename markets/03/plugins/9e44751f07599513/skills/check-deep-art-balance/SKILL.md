---
name: check-deep-art-balance
description: Check and report the user's current Deep Art AI credit balance.
---

# Check Deep Art AI Balance

Use this skill when the user asks to check, view, or report their Deep Art AI credit balance.

## Workflow

1. Call the `get_credit_balance` tool with no arguments.
2. Read the returned `creditsBalance` value.
3. Report the current balance clearly.
4. Never estimate, cache, or invent the balance.

## Example Requests

User: "Check my balance"

Action: Call `get_credit_balance`.

Response: "Your current Deep Art AI balance is **68,000 credits**."
