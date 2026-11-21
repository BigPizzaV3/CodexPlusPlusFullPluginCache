---
name: setup
description: First-run setup for WOIII.me. Use when the user installs or sets up WOIII.me, asks how to start, or asks what WOIII.me can do.
---

# Set up WOIII.me

1. Call `auth_status`. If the Discogs account is linked, say only that it is linked: don't repeat the username or user id it returns. If it is not linked, explain that WOIII.me needs read-only access to their Discogs account and that the plugin's sign-in opens discogs.com to approve it. Never ask for a password or token in the conversation.
2. Once linked, say in two sentences what WOIII.me does: it judges vinyl pressings from Discogs evidence (mastering, stampers, plants, ratings, demand) on two lenses, sound and collector, and works with the user's own collection, wantlist, artist pages and collecting goals.
3. Call `open_home` (it makes no Discogs request) and branch on its `collection`:
   - **not loaded** (`loaded: false`): offer to load it, with its cost (about one Discogs request per 100 records, then free for four hours), and the three starters below meanwhile.
   - **empty** (`empty: true` or `size` 0): say plainly that there is nothing on the shelf yet, so there is no taste to read and no "fit" to show. Offer three starters that need no collection: a pasted release link, "which pressing of Blue Train?", "tell me about Alice Coltrane" (`get_artist_overview`). Then ask for up to three interests (jazz, soul-funk, electronic, hip-hop, rock-indie, psych-prog, folk-country, reggae-dub, classical, ambient-experimental, global, soundtracks-library), store them with `settings_update` (`interests`, comma-separated), call `goal_suggestions` and offer each canon with `goal_add`. Explain that WOIII.me reads what they add on Discogs and cannot add records itself.
   - **loaded**: the usual flow: the home's workflows for album surveys, comparisons, the wantlist and goals.
4. Offer three ways to start:
   - "Is this a good pressing? <paste a Discogs release link>"
   - "What's the best-sounding pressing of Kind of Blue?"
   - "Which albums on my wantlist should I buy first?" (needs records in the collection)
5. Mention settings (default lens, pressings checked per album, notes, interests) on the plugin page.
6. State plainly: read-only, no prices or cover images, data provided by Discogs, not affiliated with Discogs.
