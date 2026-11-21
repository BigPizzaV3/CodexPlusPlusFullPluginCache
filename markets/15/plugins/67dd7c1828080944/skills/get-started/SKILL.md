---
name: get-started
description: First steps with ChatGenius in ChatGPT. Use when the user has just connected ChatGenius or asks what it can do.
---

# Getting started with ChatGenius

1. Call `get_account` first. It returns the business, plan and, when nothing is connected yet, a `setup.next_step` note.
2. If `setup.channels_connected` is false, tell the user to connect Instagram or Facebook at https://sumgenius.ai/portal/chatgenius/ before anything else. Lists of conversations, contacts and posts stay empty until they do.
3. Once a channel is connected, good first requests are:
   - "Show my most recent conversations."
   - "Who asked about pricing this week and never got a reply?"
   - "If someone comments PRICE on my latest post, what would happen?" (`simulate_comment`, sends nothing)
4. Tools marked destructive message real people, publish content or change live automations. Confirm with the user before calling them. Flows are saved as drafts and go live only through `publish_flow`.
5. Plan limits apply. When a tool returns `plan_limit_reached`, say so plainly and link the plan page it gives.
