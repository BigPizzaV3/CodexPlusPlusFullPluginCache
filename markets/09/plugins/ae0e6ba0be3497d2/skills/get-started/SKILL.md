---
name: get-started
description: Set up Hermoso for a new user. Use right after the plugin is installed, or when the user asks how to start, what Hermoso can do, or to set up their brand. Checks for a saved brand profile, drafts one from the user's website or description if there is none, shows which accounts are connected, and suggests a first task.
---

# Get started with Hermoso

Use this skill to get a new user from "just installed" to a first useful result in a few messages.
Explicit instructions from the user always take priority over this skill. If they already know what they want
("show me my competitors' ads", "make an ad"), skip the setup and do that instead.

## What you need from the user
- Nothing to begin with. Ask for their website (or a one-line description of the brand) only if no brand is saved.

## Steps
1. Call `get_brand`. It is free and changes nothing.
   - If a brand is saved, greet the user by the brand name, summarise in two or three lines what Hermoso knows
     (what it sells, main products, positioning), and go to step 3.
   - If no brand is saved, go to step 2.
2. Ask for the brand's website. If they have none, ask for a short description of what they sell and who it is for.
   Call `draft_brand` with the domain (or the description) and `save` set to false.
   - Show the user the drafted name and summary and ask whether it is the right company. A domain can resolve to a
     different business with a similar name; never assume it matched.
   - When the user confirms, call `draft_brand` again with `save` set to true. If they say it is wrong, ask for the
     correct website or a description and draft again.
3. Call `list_connectors` to see which social and ad accounts are connected to this workspace.
   - List the connected ones by name. If none are connected, say that posting and campaign reviews need an account
     connected in the Hermoso app (Connectors, in the sidebar), and that research and creating ads work
     without one.
   - Never ask the user for a password or an access token in the chat. Accounts are connected in Hermoso itself.
4. If there are several brands on the account, call `list_brands` and ask which one to work on, then `use_brand`
   with the brand the user picks. Skip this when there is only one brand.
5. Offer three first tasks, matched to what is set up, and let the user pick:
   - "Show me the ads my competitors are running" (research, works with no connected account).
   - "Make an Instagram ad for <brand>" (create, uses the saved brand).
   - "What's scheduled this week?" or "Which of my posts did best?" (only if a social account is connected).

## Output
A short welcome: the brand Hermoso will work on, what is connected, and three suggested next steps as plain
sentences the user can send back. Keep it under ten lines.

## Do not
- Do not invent brand details. Only repeat what `get_brand` or `draft_brand` returned.
- Do not save a drafted brand before the user confirms it is the right company.
- Do not start research or create anything during setup unless the user asks. Those use credits from the user's
  Hermoso account.
- Do not discuss plans, prices or purchases. If the user asks about their credit balance, `hermoso_credits`
  reports it; plans and billing are managed in their Hermoso account outside ChatGPT.
