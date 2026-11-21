---
name: setup
description: "Set up thott.bot for a WoW Forever player after they install it: offer to link their Battle.net characters, then show how well you now know those characters."
---

Use this skill when the player runs setup for thott.bot.

Linking Battle.net lets you give personalized answers about the characters
this player actually plays: their gear, talents, stats, professions and
recipes, quests, reputations, achievements, mounts, pets, transmog, raid
progress and PvP. Once linked, every character on their account stays fresh:
its data updates each time they log out. It is free forever, and looking up
their own characters never counts toward their usage limit. thott.bot
receives nothing from Battle.net beyond their WoW characters and BattleTag.

Linking isn't required to use thott.bot. Without it, you just can't give
personalized answers about their characters beyond what they tell you.

1. Call `show` with `{ "type": "characters" }`. This draws the My characters
   card, where they link Battle.net. Contextualize what linking gives them
   in terms of what this player cares about, if you know it.

2. When the player says their characters are linked, fetch "my characters",
   then the sheet of each character that bears on what this player cares
   about ("character: <name>").

3. Show them you know their characters. Connect what you see to what they
   care about in the game, from this chat or from what you remember about
   them, so it's clear you now have a lasting, up-to-date awareness of their
   characters. Don't recite numbers for their own sake. Then offer a few
   topics you think they'd find interesting, as options they can pick from
   if you can.

The player's own instructions come before this skill.
