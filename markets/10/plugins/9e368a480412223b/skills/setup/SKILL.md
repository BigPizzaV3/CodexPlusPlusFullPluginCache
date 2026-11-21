---
name: setup
description: Set up Exayard in this chat. Use right after the plugin is installed, or when the customer says "set up Exayard", "connect Exayard", "get started" or asks how to begin.
---

# Set up Exayard

The goal: the customer is signed in, their company is set up the way Exayard's own setup does it (company name,
trades, pricing location), and they know how to start. Keep it to a few short messages.

## Steps

1. **Connect.** Call `get_profile`. If the customer is not signed in yet, tell them to connect their Exayard
   account when asked, then call `get_profile` again.
2. **Show the company setup.** Call `get_company_setup`. It shows a card with the company's setup, the same
   settings Exayard's web app has, and the customer makes every change in that card:
   - **No company yet:** ask what the company is called; they type it in the card and press Create.
   - **Trades:** ask them to tick the kinds of work they do.
   - **Pricing location:** ask them to search for their city, region or country, so prices match where they work.
     Units and currency sit in the same card if they want to change them.
   - **Several companies:** the card lists their companies. Ask which one this chat should work in; they pick it
     in the card, or you call `choose_company` with the name they say. Then show the setup again.
   - **Not an admin:** the card shows the settings without editing. Say only an admin of the company can change
     them, then go on to step 3.
   Read back what the card's summary says in one short list and ask "Is this right?" Never change a setting
   yourself and never ask for or pass a company id.
3. **Start.** Say "Add a plan set to start." and call `add_plan_set` so the upload card is ready.

## Rules

- Ask only for what the setup does not already answer. If everything is already set, skip to step 3.
- Do not talk about Exayard plans, prices, credits, trials or upgrades.
- Plain words to the customer: no record ids and no tool names.
