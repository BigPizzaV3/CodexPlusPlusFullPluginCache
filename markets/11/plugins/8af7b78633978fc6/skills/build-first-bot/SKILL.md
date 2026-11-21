---
name: build-first-bot
description: Build a first Discord bot with camelBots from a plain-language description, publish it and add it to a server. Use when someone wants to make, build or set up a Discord bot, or asks how to get started with camelBots.
---

Help the person get a working Discord bot in a few steps. Their explicit instructions take priority over this
workflow: skip or change steps when they ask.

1. Work out what the bot should do. If the request doesn't say, ask one short question, such as "What should your bot
   do, and in which server?". Don't ask for anything else up front.
2. Call `create_bot` with what the bot should do, in the person's words, and a short name (lowercase letters, digits,
   `-` and `_`, such as `dice-roller`) and one emoji when they suggest them. Call `list_bots` first when they may have
   a bot by that name already.
3. camel-builder builds it: its turns take a minute or more. While the answer says `status: "working"`, tell the
   person it is still building and call `get_builder_reply` with its `requestId`. Show camel-builder's reply as it
   wrote it: never invent what the bot does.
   - `needs_you` with a question: ask the person, then send their answer with `message_builder`.
   - `needs_you` asking to publish: publish only if the person wants the bot live (`publish_bot`).
   - `failed`: show the error, and offer to try again.
4. For changes, call `message_builder` with the bot's name and the person's words, and follow the reply as above.
5. When they are happy, call `publish_bot`, then `get_install_link` (or show the bot card from `publish_bot`): the
   link opens Discord's own screen, where they pick a server they manage and a channel. It is valid for 30 minutes.
6. Finish with how to keep going: ask for changes here, or open the bot's page in camelBots
   (https://bots.camelai.com) to try it in its test channel, see its logs and versions, or delete it.

Rules:

- Never ask for, repeat or pass on a Discord bot token, client secret or other credential. If the person pastes one,
  don't use it; suggest they reset it in Discord's developer portal, and point them to the bot's settings in
  camelBots, which asks for it on its own page.
- Only act on the connected account. You can't see or change anyone else's bots.
