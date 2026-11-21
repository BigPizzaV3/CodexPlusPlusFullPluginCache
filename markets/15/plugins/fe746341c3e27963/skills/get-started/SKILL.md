---
name: get-started
description: Set up Buildcord in this chat after it's installed. Confirms which Buildcord account is connected, picks or makes the Discord bot to work on, shows it, and suggests a first thing to build. Use when the person has just connected Buildcord or asks how to start.
---

Use this skill right after Buildcord is connected, or when the person asks how to get started with it.

1. Call `whoami` and tell the person which Buildcord account is connected, by name.
2. Call `list_bots`.
   - No bots: ask what the bot should be called and call `create_bot` with that name. Don't pick a name for them.
   - One bot: use it.
   - Several: list them by name, with whether each is live, and ask which to work on.
3. Call `show_bot` with the chosen bot so the person sees its flows.
4. Suggest up to three things to build next that suit the bot, in plain words. For a new bot, good first steps are a /ping command, a welcome message for new members, or a /poll command. Don't build anything until they choose.
5. Remind them once that changes are saved to the bot's draft, and the bot goes live when they press Deploy in the Buildcord builder, where its Discord token is set too.

Don't ask for a bot token or any other secret. If the person doesn't have a Buildcord account yet, the sign-in step that connected the app is where they make one.
