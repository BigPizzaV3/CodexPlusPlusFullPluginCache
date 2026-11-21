---
name: get-started
description: How to help someone use MBX Reach from ChatGPT for the first time.
---

# Getting started with MBX Reach

1. Call `get_workspace` first to learn the workspace name, plan and sender domains.
2. Call `list_lists` before adding contacts or writing a campaign, so you use a list that exists.
3. Only add people who asked to hear from the sender. Never import bought or scraped addresses.
4. Campaigns are saved as drafts with `create_campaign`. There is no send tool: when the person wants to send, run `campaign_readiness` and tell them to press Send inside MBX Reach.
5. There is no tool to delete contacts, lists or campaigns. If asked, say so plainly.
