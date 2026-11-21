---
name: make-a-comic
description: Make a short personalized comic starring real people from their photos (a cover, a complete two-page story and a back cover) with the PersonalizedComics tools. Use when someone wants a comic of themselves, family or friends, for a birthday, anniversary, holiday or just for fun, or wants to see, redraw or reopen a short comic they made.
---

Use this skill with the PersonalizedComics tools. What the customer asks for always comes first; these steps are the default way through.

## 1. Gather what the comic needs

- **Who is in it:** a name for each person, up to four people.
- **A photo of each person** (best). With no photo, a one-sentence description of how they look, and only when the customer is happy to go without a photo. Never invent how a real person looks.
- **What happens:** the story idea in the customer's words, and the occasion if there is one.
- Optional: an art style (graphic novel, American classic, manga, noir, watercolor, cyberpunk, retro pop, fantasy, lifestyle) and a title.

Ask one short question when something essential is missing. Do not ask about things that have defaults.

## 2. Start it once

Call `create_comic` once per comic, with each attached photo in its own `photo_N` slot and `people[].photo` saying whose photo it is. Do not call it again for the same request.

If the answer says the photo did not arrive and gives a temporary upload address (apps that cannot hand a file to a tool, such as Codex), upload the photo file to that address with the command it gives, then call `create_comic` again with the photo slot it returns.

## 3. Let the customer check the cast

About a minute later the cast is ready: each person drawn as a comic character.

- Where the PersonalizedComics card is shown, it updates by itself. Do not poll, and do not repeat the pictures the card shows.
- Where no card is shown, call `get_comic` with `wait: true` until the status changes, and show the picture links it returns.

Ask the customer to check the likeness. If someone looks wrong, call `redraw_character` with what should change (each character can be redrawn twice); `restore_character` puts an earlier drawing back. Call `approve_cast` only when the customer says the cast looks right.

## 4. The finished comic

The cover, the two pages and the back cover take about two more minutes. The short comic is complete as it is: nothing in it is locked and nothing is sold in the conversation.

- `list_my_comics` shows the customer's short comics; `get_comic` reopens one.
- Mention `full_comic_link` only when the customer asks for more pages or a printed copy. It opens the PersonalizedComics website, where a longer comic is made and ordered as a printed book. Never quote prices, take payment details or offer upgrades here.

## Limits and refusals

- Each customer can make five short comics a day. When the tool says the limit is reached, pass on when the next one opens.
- Pages of a finished comic are not redrawn. To tell a different story, start a new comic.
- Only use photos the customer has the right to share, of people who would be happy to be in a comic. Do not make explicit, hateful or graphic comics.
- The plugin cannot delete comics. For deletion, the customer can email help@personalizedcomics.com.
