---
name: get-started
description: Use when the user asks to work their Zono Support help desk (tickets, customers, purchases or help articles). Explains how the Zono tools fit together and which IDs each one needs.
---

# Working a Zono Support queue

The Zono tools act as the signed-in agent, in the workspace they chose when connecting. They only see tickets that agent can see in Zono.

1. Find work with `list-tickets` (filter by status, priority, assignee or department) or `search-tickets`.
2. Read the whole conversation with `get-ticket` before acting. It returns the customer, product and department IDs.
3. Check who the customer is and what they bought with `lookup-license` (pass the ticket). `get-customer` gives their recent tickets.
4. Look up answers with `search-knowledge`, or `ask-knowledge` for a cited answer. If it says a human should handle it, say so instead of guessing.
5. Act: `reply-to-ticket` (use `is_internal: true` for staff notes), `assign-ticket`, `update-ticket-status`, `update-ticket-fields`, `merge-tickets`.

IDs come from the lookup tools: `list-products` for `product_id`, `list-departments` for `department_id`, `list-team-members` for `assignee_id` (the member marked `me` is the signed-in user) and `list-customers` for `customer_id`. Use `list-ticket-fields` before setting custom fields.

Before sending a reply to a customer, show the draft and ask the user to confirm. Internal notes, assignment and status changes can go ahead when asked. Merging closes the duplicate ticket, so confirm which ticket is the duplicate first.
