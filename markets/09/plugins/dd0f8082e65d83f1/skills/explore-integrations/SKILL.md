---
name: explore-integrations
description: Answer questions about what CRM Connector connects before anything is set up. Use it when a person asks which systems CRM Connector supports, what two systems can sync, whether a particular field goes across, or how to connect a system.
---

# Explore what CRM Connector connects

This belongs to part 2 of the plugin, **Integrations between two systems**. None of these questions needs a CRM Connector account. Answer from the tools, then offer the next step.

## Which systems CRM Connector connects

- "Which integrations do you have?", "What can CRM Connector connect?", "Do you support Keap?"
- Call `get_integration_options` without a system. It returns the systems CRM Connector connects as one plain list.
- Answer in two or three sentences: what an integration does and that list. Then ask which two systems they want in sync.
- When they name them, call `get_integration_options` with both. Available: offer to plan it and ask what should travel. Not available: offer `send_request`, which is free.
- Do not call `list_integrations` for this: that tool is only about the integrations a customer has set up.

## What two systems can sync

- "Can I sync Pipedrive with Xero?", "What goes across between HubSpot and QuickBooks Online?"
- Call `get_integration_options` with both systems.
- Say per record type:
  - in which direction it travels, one way or both ways
  - at which moment a record can travel, for example once an invoice is paid or a quote is accepted
  - which filters apply, for example tags, pipeline stages or a minimum amount

## Whether a field goes across

- "Does the phone number go across?", "Is the due date carried?", "Do the line items come along?"
- Call `get_integration_fields` with the two systems and the record type key.
- Say plainly whether that field travels and how:
  - **always**: it always goes across
  - **needed**: the sync needs it, so it cannot be switched off
  - **switchable**: the person can switch it off in the setup
- Pass on notes such as "only when the record is created" and name what does not travel.

## How to connect a system

- "How do I connect Xero?", "What do I need for GoHighLevel?", "Where do I find my token?"
- Call `get_connection_guide` with the system.
- Give the steps in CRM Connector and, for each field it asks for, where to find it in that system.

## Next step

- Every answer from these tools carries a setup link: share it, so the person can start right away.
- When they describe what should happen, for example "when a deal is won, make an invoice", continue with the plan-an-integration skill and make a plan.
- When a system or combination is not offered, say so and share the request an integration link the tool gives.

## Rules

- Only describe what the tools return. Never promise a record type, direction, field or system the tools did not confirm.
- Do not discuss prices, plans, trials or discounts.
- Never ask for passwords, API keys or tokens. Systems are connected inside the CRM Connector app, never in the conversation.
