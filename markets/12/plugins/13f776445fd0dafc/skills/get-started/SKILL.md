---
name: get-started
description: First steps after connecting Better Email. Confirms which organization is connected, shows its design systems and recent campaigns, and offers to build a first campaign.
---

Help the user take their first look at Better Email from this chat.

1. Call `get_guidelines` and follow what it returns for the rest of the conversation.
2. Call `get_organization_profile` and tell the user which organization they are connected to. If it is the wrong one, they can disconnect Better Email in ChatGPT's settings and sign in again, picking the right organization.
3. Call `list_design_systems` and `list_campaigns`. Show the design systems by name and the five most recent campaigns, each with its link.
4. Offer two next steps: build a new campaign from one of the design systems, or open one of the recent campaigns and work on it. Wait for the user to pick. Don't create anything yet.
