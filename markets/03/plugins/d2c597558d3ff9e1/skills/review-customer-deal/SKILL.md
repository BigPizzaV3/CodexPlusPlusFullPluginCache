---
name: review-customer-deal
description: Retrieve and summarize a LeftLane customer deal by deal id. Use when a user supplies a deal id and asks about its status, terms, stage, assignee, named parties, vehicle, or deal finance account.
---

# Review Customer Deal

1. Require the exact integer deal id before calling `CustomerDeal`; do not search by contact details.
2. Summarize deal status and dates, commercial terms, workflow stage and assignee name, party names, vehicle facts, and finance-account status in distinct sections.
3. Do not request, infer, or expose email, phone, address, government identifiers, income, credit reports, or payment-method data.
4. Label missing or nullable fields as unavailable rather than guessing.
5. Use the returned deal id, vehicle id, or DFA id only to identify an exact target for a separately confirmed note workflow.
