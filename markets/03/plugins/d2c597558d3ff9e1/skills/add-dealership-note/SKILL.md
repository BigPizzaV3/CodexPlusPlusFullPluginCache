---
name: add-dealership-note
description: Add one confirmed private note to an exact LeftLane vehicle, customer deal, or deal finance account with CreateComment. Use when a user asks to record, add, attach, or save a dealership note or comment.
---

# Add Dealership Note

Treat `CreateComment` as a non-idempotent write. Follow this sequence exactly:

1. Discover the target with a read tool before preparing the write, even when the user supplies an id. Use `ActiveVehicles` for a vehicle, `CustomerDeal` for a customer deal, or `DealFinanceAccounts` for a finance account.
2. Resolve exactly one returned record and retain its integer id. If the read returns no match or multiple plausible matches, do not prepare the write; refine the search or ask the user to choose.
3. Obtain the complete note body. Do not silently rewrite material facts; show any cleanup to the user.
4. Display the target type, target id, identifying facts from the discovery result, and exact note body. Ask for explicit confirmation to create that one comment.
5. Call `CreateComment` exactly once only after the user confirms the displayed target and body.
6. Report the returned comment id, timestamp, and target relationship.

Never call the tool when discovery, an exact target, the body, or confirmation is missing. Never guess between multiple targets. If the response is ambiguous, times out, or fails after dispatch, do not retry automatically because a retry can create a duplicate note; inspect state or ask the user how to proceed.
