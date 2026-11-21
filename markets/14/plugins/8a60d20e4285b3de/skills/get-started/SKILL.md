---
name: get-started
description: Help a nonprofit operator connect their Better Giving account and try the first tasks, such as listing campaigns, checking fundraising results and creating a draft campaign.
---

# Get started with Better Giving

Use this when someone has just installed Better Giving or asks what it can do.

1. If the Better Giving tools are not connected yet, ask the user to connect and sign in with their Better Giving account.
2. Call `list_campaigns` and show their campaigns with status and public link.
3. Offer next steps: check results with `get_results`, look up donors with `list_donors`, or create a draft campaign with `create_campaign`.

Rules:
- The connector moves no money. It cannot charge a card, refund a gift, change a monthly gift or pay out funds. Say so if asked.
- Act only on the connected account.
- Before `publish_campaign`, ask where the gifts go and wait for an explicit yes.
- Before `end_campaign`, confirm with the user and wait for an explicit yes.
