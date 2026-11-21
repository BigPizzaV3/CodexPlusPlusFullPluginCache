---
name: get-started
description: How to help a user run their social media with SociaHive from ChatGPT: DM automations, scheduled posts and results.
---

# Working with SociaHive

SociaHive runs DM automations ("flows") and schedules posts for the user's connected social accounts.

- Start with `list_accounts` if you don't know which account the user means.
- To build an automation, call `generate_flow` with the user's description. It is created as a draft; tell the user to review it and turn it on in SociaHive, or call `activate_flow` only when they ask.
- To schedule a post, use `schedule_post` with the text, platforms and time. Confirm the time zone with the user if it is unclear.
- For results, use `get_analytics_overview`, `get_post_analytics`, `get_flow_stats` or `get_content_insights`.
- Deleting something, or publishing a post right away, returns a confirmation step. Ask the user before confirming.
- If a tool says the account's plan doesn't include connecting AI apps, tell the user that and stop; do not retry.
