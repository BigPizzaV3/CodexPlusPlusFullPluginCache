---
name: build-discord-bot
description: Build or change a Discord bot in Buildcord from a description, such as slash commands, replies to things that happen in a server, schedules, buttons, forms, embeds and saved data. Use when the person asks for something their Discord bot should do, wants to change how it behaves, or asks what's wrong with a bot and to fix it.
---

Use this skill when the person wants their Discord bot to do something new or different, or wants a bot's problems fixed. Buildcord's tools change the bot's draft; nothing goes live until the person deploys it from the Buildcord builder.

## Workflow

1. Find the bot. Call `list_bots`. If the person names a bot, use it. If they have exactly one, use that. If there are several and it isn't clear which, ask. If they have none, offer to make one with `create_bot`, using the name they give.
2. Read before changing. Call `get_bot` for the bot's outline, and `read_flow` or `read_item` for anything you're about to change.
3. Learn the steps. Call `read_step_catalogue` once per conversation before building or changing flows. Use only the step kinds, settings, outputs and `{tokens}` it describes. Never invent them.
4. Build.
   - A new command, event reply or schedule is `create_flow`, then `edit_flow` to add and wire its steps. Add and wire many steps in one `edit_flow` call, giving new steps a ref so later operations in the same call can use them.
   - A message design is `save_embed`, buttons and menus are `save_components`, a form is `save_modal`, and stored data is `save_variable` or `save_collection`. Create what a flow needs if it doesn't exist; reuse what exists when it fits.
5. Check. `edit_flow` returns the flow's remaining problems. Fix the ones your change caused. Mention, without fixing unasked, problems that were there before.
6. Show. Call `show_bot` with the bot and the flow you built so the person sees the diagram.
7. Reply in plain words: what the bot now does, anything the person must still do, and that it goes live when they press Deploy in the builder. Give the builder link from the tool result.

## Ask, stop or decline

- Ask when a wrong guess would be costly or can't be undone: which bot, which channel or role when several fit, or what a message should say when it matters to them.
- Before `delete_item`, say exactly what will be deleted and wait for the person to confirm.
- Don't accept bot tokens, passwords or other secrets in the chat, and don't repeat them. Secrets and the bot's token are set in the builder. If someone pastes a token, tell them to reset it in Discord's developer portal.
- You can't deploy, see secrets, or act in a Discord server directly (ban someone, post a message now). Say so, and offer to build a flow that does it instead.
- If a tool fails, read its error, correct the call and try again. If it still fails, tell the person what didn't work.

## Don't

- Don't describe a flow instead of building it when the person asked for it to be built.
- Don't report ids, JSON or step kinds to the person. Name things the way the builder does: the /ping command, the welcome embed.
- Don't claim something is live, or that a command works in Discord, before it's deployed.
