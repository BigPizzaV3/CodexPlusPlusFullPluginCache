---
name: find-amavie-characters
description: Find Amavie AI characters, chat with them and play ready-made scenes with them right here. Use when someone wants an AI character to talk to, or a roleplay scene, interactive story or text adventure to play.
---

Use this skill when the person wants to meet or chat with an AI character or play a scene on Amavie.

1. To find characters, call `search_characters` with what the person described: a name, personality, occupation, place or mood. When they gave no description, call it with an empty query to show featured characters.
2. When the person names one character, or gives an @handle or an amavie.ai link, call `get_character`.
3. To find a scene, call `search_scenes` with the theme, and pass `genre` when they name a genre.
4. When the person wants to play a scene from the cards, call `start_scene` with its id. The player opens here, and the person types their moves in it.
5. When the person wants to talk with one character right here, call `start_chat` with that character's @handle from a card or their link. The chat window opens here, and the person types their messages in it.
6. Let the cards show the results. Add one short line at most, and don't repeat the names and links that are already on the cards.
7. When nothing is found, say so and suggest other words. Don't invent characters, scenes or links.

Amavie’s engine plays the scene in the player and answers in the chat window. Don’t write a character’s messages or play a scene yourself, and don’t retell the moves or the messages. Don’t offer to change anything in an Amavie account: these tools have no access to it.
