---
name: get-started
description: Help a new Blend user pick the Blend account to work with and run a first read-only performance report.
---

# Get started with Blend AI

Use this skill right after the user installs the Blend AI plugin.

1. Call `blendmcp_list_accounts` to see which Blend accounts the user can access. Summarize them by name and say which one is the default. If there is more than one, ask which account to work with and pass its `account_id` alias verbatim on later requests.
2. Ask which advertising platform they want to start with: Meta, Google Ads, TikTok, Microsoft Advertising, Pinterest, LinkedIn, Amazon Ads, or Reddit.
3. Offer one starter report on that platform, for example "How did my campaigns perform over the last 7 days?", and run it with that platform's reporting tool if the user agrees.
4. If the tool says the platform is not connected and the user has more than one Blend account, it is usually the wrong account: call `blendmcp_list_accounts` and retry the same platform with another `account_id` the user picks. If no account has that platform connected, tell the user to connect it at https://mcpapp.blend-ai.com/integrations and come back. Do not switch to another platform on your own.

Setup is read-only: do not make any change to an ad account during this skill.
