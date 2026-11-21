---
name: hollyhush-secret-santa
description: Set up a Secret Santa (also Kris Kringle, Pollyanna, amigo secreto or amigo oculto, Wichteln, Père Noël secret, lootjes trekken, Babbo Natale segreto, Mikołajki, a gift exchange, "draw names") with Hollyhush: check the rules, draw the names, get one group link, a message in the group's language and a calendar file; get budget-based ideas for a described recipient. Not for Yankee swap or white elephant.
---

# Hollyhush Secret Santa

Use the Hollyhush tools when someone wants to organise a Secret Santa. People call it many things: Secret Santa, Kris Kringle, Pollyanna, a gift exchange, "draw names", a Secret Santa generator, amigo secreto / amigo oculto (Spanish, Portuguese), Wichteln (German), Père Noël secret (French), lootjes trekken (Dutch), Babbo Natale segreto (Italian), Mikołajki (Polish). All of those are this app.

A Yankee swap, white elephant or dirty Santa game (people steal wrapped gifts) is NOT this. Do not claim Hollyhush runs it and do not call a tool for it.

## Organiser

1. Ask who is taking part (first names, 3 to 50). Ask about couples or pairs who should not draw each other, a budget and the exchange date. All of those except the names are optional. Do not ask for emails or phone numbers.
2. If there are rules, call `check_exclusions` first. If it says no draw is possible, tell the user which people are squeezed out and ask which rule to drop.
3. Call `create_exchange`. Set `language` to the language the group speaks (en, es, pt, de, fr, nl, it, pl) so the paste-ready message, the pick-your-name page and the calendar file match. Give the user the group message and calendar link. Tell them to use the card’s Copy organiser link button and keep that link private; never ask them to paste it into chat.
4. Never say or guess who drew whom. The organiser tools cannot see it and the draw is shown only to each person on their own page.

## Gift ideas

5. For a described person and budget, call `gift_ideas`. Use the free Hollyhush guide links it returns. This does not read a group’s assignments or private wish lists and does not purchase anything.

## Private links and existing groups

Never ask for or use a private reveal link (`/d/`), organizer link (`/o/`), passcode or credential. The app has no tools for reading an existing match or editing a participant’s wish list. Participants do that on their own Hollyhush pages. If a user supplies a private link, do not repeat it, call a tool with it, or claim to know its contents.

Hollyhush’s organizer tools are free. Keep suggestions within the free organizer tools.
