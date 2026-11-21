---
name: write-app-ad
description: Write a video ad script for the user's mobile app on the structure of a real ad that kept running, from Clonerrr's ad library. Use when the user asks for an ad script, ad concepts, hooks, a creative brief or a UGC brief for their own app or product.
---

# Write an app ad on a structure that already worked

The fastest way to a good ad is to rebuild one that held up: keep its scenes, pacing and the move its hook makes, and put the user's product in it with new words.

What the user asks for comes first. If they name the ad to build on, the length or the tone, follow that.

## Steps

1. **Know the product.** With an App Store or Google Play link, call `find_ad_templates_for_app` with `store_url`. Without one, ask once what the app does, who it is for and its category, then call it with `app_name`, `category` and `description`. Do not guess a store link from a name.
2. **Pick the ads.** Read each candidate's `why_it_works`: it says what a product needs for the structure to fit. Offer two or three whose every scene this product can fill truthfully, one line each on why, with its `url`. Skip this when the user already chose an ad.
3. **Read the ad.** Call `get_ad_template` for the chosen `id`.
4. **Write the script** as a table with one row per scene of the original, in the same order and at about the same length:

   | Time | What we see | On-screen text | Voiceover |
   |---|---|---|---|

   - Replace everything in `specific_to_this_app` with the user's product: its screens, its result, its name. Keep what is in `carries_over`.
   - The hook makes the same move as the original's (a question, a bold claim, a live demonstration) in new words about this product.
   - A voice says about 2.5 words a second, so a 4-second scene has room for about 10 spoken words. Keep each caption to about 7 words.
   - Name and show the app by the middle of the ad. End on one plain call to action.
5. **Add what makes it shootable:** two alternative hooks, and a shot list of what to screen-record or film for the scenes that show the product.
6. Link the ad the script is built on.

## What not to do

- Do not copy the original's lines, or name or show the original app. Its structure is reused; its words and brand are not.
- Make only the claims the store listing or the user supports. No invented numbers, ratings, awards or testimonials.
- Do not promise results. A structure that ran a long time for one app is a good bet for another, not a guarantee.
- If no candidate fits, say so and say which scenes break, rather than forcing the product into one.
