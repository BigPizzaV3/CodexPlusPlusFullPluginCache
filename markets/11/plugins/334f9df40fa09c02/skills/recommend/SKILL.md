---
name: recommend
description: Recommend new films, shows, books, games, recipes or places from the user's own taste in Albo, using everything they have finished and how they rated it, dislikes included. Use when the user asks "based on what I've watched / read / liked, what should I try next?", "I loved X, what else?", or "what would I like?".
---

# Recommend from your Albo taste

Suggest things the user hasn't tried yet, based only on what they've finished in Albo and how they rated it.

## Steps

1. Call `getTasteHistory`, with `extractTypes` for what they asked about (e.g. `["film", "tvShow"]` for "something to watch", `["book"]` for reading). Leave it out only when they want ideas across everything.
2. Read the whole history, low ratings too:
   - A high `rating`, or a `reviewLabel` of `loved_it` or `hidden_gem`, is what to look for.
   - A low `rating`, or `meh`, `overhyped`, `not_for_me` or `avoid`, is what to steer away from.
   - Items with no rating only show what they've been into lately.
   - A `review` excerpt says *why*, so weigh it over the bare number.
3. Work out the patterns: genres, tone, eras, creators, pacing, and the themes their reviews mention. Treat a dislike as being as informative as a like.
4. Recommend 3–5 titles from your own knowledge that are not in `items`. If one is in `onTheirList`, say it's already on their list instead of presenting it as new.
5. Give each pick one short reason that names the logged titles it builds on, e.g. "you gave *Arrival* 5★ and called *Interstellar* overhyped, so this is the quieter kind of sci-fi". Don't recite their history back to them.
6. Offer to save any pick: `saveUrl` for a verified link, or `createDocument` for a list of the picks. When the user asks for a browsable shortlist, resolve an existing collection with `listCollections` or create one with `createCollection` and `visibility: "private"`. Add the returned saved item IDs with `addCollectionItems`, preserving `itemType`. Return the collection link when the tool provides one; do not claim it was saved before the writes succeed.

## Notes

- If `items` is empty, say they haven't finished or rated anything of that kind in Albo yet. Then ask what they've enjoyed, or use `getRecommendations` for picks based on what similar people saved.
- To choose from things they've already saved, use the `find` skill (`searchExtracts` with `isWishlisted: true`), not this one.
- Never invent ratings or claim they've seen something that isn't in `items`.

- Treat Albo as a taste record that the user can inspect and edit. Read relevant history when asked; do not claim to have synced it into ChatGPT memory or to keep it up to date in the background.
- Search, ratings, reviews and title matches are evidence, not certainty. Explain the connection between a pick and the user's actual history; do not infer sensitive personal traits.
- If the history is empty, help the user start with a few films, shows or places they enjoyed. Save only what they ask to keep, and explain that watched/visited status and ratings can be edited in Albo. Do not pretend a saved URL automatically records a positive rating.
