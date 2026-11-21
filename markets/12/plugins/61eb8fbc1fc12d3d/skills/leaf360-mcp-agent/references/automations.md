# Automation Builder

Automation creation is high leverage. Always use the contract before building.

## Required Flow

1. Call `leaf360_automation_capabilities_get`.
2. Read trigger types, action types, condition operators, metadata fields, response behavior options, stage/status values, and builder guidance.
3. Confirm the user's business goal, target audience, trigger, conditions, timing, and intended actions.
4. Build fully configured nodes only.
5. Use configured status/stage values from capabilities, not guessed slugs.
6. Call `leaf360_automation_create` or `leaf360_automation_update`.
7. Tell the user the automation is a draft for review, not live.

## Never Do This

- Do not call create/update before reading capabilities.
- Do not persist trigger-only drafts.
- Do not leave nodes unconfigured.
- Do not guess config field names such as `taskTitle`, `selectedStatuses`, response behavior, stage slugs, or action config shapes.
- Do not activate automations through MCP unless a future tool explicitly supports a safe activation flow.

## Good Automation Brief

Before creating an automation, gather:

- Record type: lead, loan, partner/contact, webhook, or workflow context
- Trigger
- Conditions
- Timing delay
- Action sequence
- Exit conditions
- Owner or assignment behavior
- Whether communication actions should draft, send after approval, or create tasks only

## Safer Defaults

- Prefer task creation or note creation when the user is exploring a workflow.
- Prefer draft communication steps when consent or message content is not final.
- If statuses/stages are involved, use the exact configured values returned by capabilities.
- Include clear names and descriptions so the draft is easy to review in Leaf360.
