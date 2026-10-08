---
name: find-inventory
description: Page through and summarize active LeftLane dealership inventory with the ActiveVehicles tool. Use when a user asks to audit, review, list, compare, or analyze in-stock vehicles by stock number, VIN, make, model, price, stage, branch, or other returned inventory facts.
---

# Find Inventory

Use `ActiveVehicles` for inventory audit and analytic reads. Do not treat this skill as free-text vehicle search; a dedicated search skill will cover that later.

1. Request a modest `take` and `skip: 0`. Use `sortBy` only when an ordering was requested.
2. Report both the returned rows and total count.
3. Continue with `skip + take` only when the user asks for more or the request requires exhausting inventory pages. Never imply the first page is the complete result when `count` is larger.
4. Summarize operational facts (for example counts by stage or branch, price ranges, or aging signals from returned fields) without inventing availability, pricing, or condition details that the tool did not return.
5. Retain a vehicle `id` only when it is needed to identify an exact record for a follow-up action such as a confirmed note.
