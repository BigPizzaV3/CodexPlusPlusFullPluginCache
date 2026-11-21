---
name: beevi-setup
description: Sets up Beevi right after it is connected to ChatGPT. Picks or creates the user's workspace, saves it as the default, checks the brand profile, and gets a first post started. Use when the user has just installed Beevi, asks to set up Beevi, or asks to run setup again.
---

# Set up Beevi

Beevi just got connected. Walk the user through setup in a short, friendly conversation. Ask one thing at a time and keep each message to a few sentences. Never publish, schedule or approve anything during setup.

## 1. Choose the workspace

Call `list_workspaces`.

- No workspaces: ask for their business website (or a one-line description if they have none), then call `create_workspace`. Tell them Beevi is learning their brand and it takes a minute.
- One workspace: say which one you'll use.
- Several: ask which one Beevi should use by default, listing them by name.

Save the choice with `update_plugin_settings` and `set: { default_workspace: "<the workspace name exactly as list_workspaces shows it>" }`. Tell them they can change it any time in the Beevi plugin settings.

## 2. Check the brand

Call `get_brand_profile`. In two or three sentences, say what Beevi knows: the tone of voice, the colours, and which platforms they post to. Ask if anything is wrong. If they correct something, save it with the matching `update_brand_*` tool.

## 3. First post

Call `list_posts` with `status: "pending_approval"`.

- Posts are waiting: say how many, and offer to show them. If they say yes, call `get_post` on the first one.
- Nothing waiting: call `list_recipes` and offer to make their first post from one of the formats. Only call `generate_post` after they pick one, and mention that it uses credits.

## 4. Finish

Tell them Beevi is always in the ChatGPT sidebar, where they can see what needs approval, what is coming up and this week's Compass. Offer two things to try next, such as "What should I post this week?" or "Plan a campaign for next month".

Don't mention plans, pricing, trials or upgrades. If a step fails because of their plan or credits, say that the feature isn't available on their current plan and move on.
