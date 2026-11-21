---
name: get-started
description: First steps with Adspirer. Use when the user has just installed Adspirer, asks what it can do, or has no ad account connected yet.
---

# Get started with Adspirer

1. Call `get_connections_status` to see which ad accounts are connected: Meta Ads (Facebook and
   Instagram) and TikTok Ads. It is free.
2. If no ad account is connected, tell the user to connect one at https://adspirer.ai/connections,
   then come back. Don't call platform tools until an account is connected.
3. If the user has more than one account on a platform, ask which one to work on before running
   anything account-specific.
4. Offer three first tasks, using the platforms they actually connected:
   - Show performance for the last 30 days, by campaign.
   - Find wasted spend and creative fatigue.
   - Show what a competitor is advertising right now, next to their own account.

For how to call the tools after this, follow the `adspirer-mcp` skill.
