---
name: get-started
description: Set up eRank in ChatGPT. Confirms the eRank connection, shows the current and connected Etsy shops, lets the user choose the active shop, and summarizes account usage limits. Use when the user is getting started with eRank, asks what eRank can do, or wants to check or change their selected shop.
---

# Get started with eRank

Help the user confirm that eRank is connected and ready to use. Keep onboarding short.

The user's explicit instructions take priority over this workflow. If they ask to skip a step, use a different order, or get a different format, do that. Stop once they have what they asked for.

## Workflow

1. Check the shop setup with `get_current_shop` and `list_user_shops`.
   - `list_user_shops` returns the Etsy shops connected to the eRank account and marks the current one.
   - `get_current_shop` returns the current shop's profile and sales ranks. It returns an error if no shop is selected or the shop needs to be reconnected in eRank.

2. Report what you found:
   - **No connected shops:** say that no Etsy shop is connected to this eRank account and that shops are connected in eRank. Don't describe connection steps you can't verify, and don't say a shop was connected.
   - **One shop:** name it and say whether it is the current shop.
   - **Several shops:** name the current shop. If no shop is selected, or the user wants a different one, open the shop switcher with `open_shop_switcher` so they can choose. If the switcher isn't shown, ask which shop to use.

3. Change the active shop only when the user chooses one.
   - Call `set_current_shop` only with a shop the user picked by name or ID. Never pick a shop for them.
   - This changes the active shop in eRank only. It changes nothing on Etsy.
   - After a change, call `get_current_shop` to confirm it. If the change fails, say so, then check the active shop with `get_current_shop` and report it. If that also fails, say the active shop is unknown and suggest trying again.

4. Call `get_account_limits` and summarize it in one or two sentences: the plan name, remaining daily keyword and shop searches, and any feature that isn't available. If a feature isn't included in the current plan, say so plainly. Don't recommend upgrading or describe plans or prices.

5. Finish with a short "You're ready" summary:
   - The current shop, if one is selected
   - Any limits that affect what the user can do today
   - Three example requests, such as:
     - "Research the keyword personalized wedding gift."
     - "Audit one of my listings and analyze its tags."
     - "Summarize recent sales for the shops I track."

## Boundaries

- Don't start keyword, listing, or competitor research during onboarding unless the user asks for it.
- eRank reads research and account data and can change the active eRank shop. It can't create, edit, publish, or delete Etsy listings or change Etsy shop settings.
- Report only what the tools return. If a tool fails or the connection needs attention, say so plainly. Don't claim you fixed it.
- Don't promise search rankings, traffic, views, or sales.
