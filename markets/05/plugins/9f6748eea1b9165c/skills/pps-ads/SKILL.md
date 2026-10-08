---
name: pps-ads
description: Make a finished 15, 30 or 60 second ad with motion graphics through the Pray Production Studio connector. Use when someone asks for an ad, promo or spot for a product, event, series, app or ministry.
---

# PPS Ads

You direct; PPS renders. This skill is the connector's "make-an-ad" recipe with one extra: on a
machine that can run Node, you may render the same composition locally to tinker with it.

For a cinematic or product demo / hype trailer, use `pps_get_workflow` with `make-a-trailer`, which offers those two modes and score-first direction.

## Run the recipe

1. Read the recipe: `pps_get_workflow` with workflow `make-an-ad`, and follow it with the person in
   this conversation. It asks, one question per message and never repeating anything already said:
   "What is the ad about?", "Anything from PPS you want in it?", "How long?" (15, 30 or 60),
   "Logo and brand color?", and, only when the blueprint has voiceover, "Which voice?" (the voice card
   plays samples). Before (4), the logo question, read `pps_get_brand_kit`. When it has a color or a logo,
   say "Using your saved brand: <name>, <color>, logo on file" (leave out whatever is not saved) and skip (4).
   If they say change it, ask (4) and use the answer for this ad only (set `brand.useBrandKit` false when they
   want none of the saved values); then offer "Replace your saved brand kit with this?" and call
   `pps_save_brand_kit` only on a yes. When nothing is saved, ask (4); after an answer with a logo or a color,
   offer once "Save this as your brand kit for next time?" and call `pps_save_brand_kit` only on a yes. Never
   overwrite a kit the person did not ask to change.
   Decide the format from the answer to the first question and never ask it: `demo` for an app, software,
   a service or a connector (the interface carries the ad: a prompt typing in, the agent working, results
   filling a grid, a device, an approve button); `promo` for a series, an event, a film, a ministry or a
   product that is not software (footage carries it); `spokesperson` for a person talking to camera
   (captions on every footage beat). State it in one line before drafting so it can be corrected, and set
   it as `format` on the blueprint.
2. The thesis: this is a dynamic motion-graphics piece that shows off the best motion design you have,
   like a resume showreel. Go all out. Every canvas beat moves, text lands on the music, the brand color
   cuts through, and the generated clips are footage inside that piece, not the piece itself. Draft the
   blueprint from the grammar in `pps_plan_ad`'s description, check it with `pps_plan_ad`, show it, and
   ask whether to change anything before it is priced. Storyboard every canvas beat (the prompt text, agent
   steps, results tiles from the person's own generations, the pick, the numbers that count up); `pps_plan_ad`
   answers one motion line per beat, so show that storyboard with the blueprint. Bounds: 6 to 24 words of
   prompt text in the person's words, 2 to 5 agent steps of at most 6 words, 3 to 6 tiles from the person's own
   generations (find them with `pps_search_assets` or `pps_get_project`; the ad's own clips are the fallback),
   and `captionAccent` words on captioned footage beats.
3. Build the ad as a Director Mode project with `pps_director_start_film` (shape "9:16", or "16:9"
   when asked): one shot per clip `pps_plan_ad` listed, in beat order, each shot's action being that beat's
   shotPrompt. Footage beat N is shot N; graphics beats are not shots. A shotPrompt names a cast
   character by the exact character name used in the script; that name binds the actor's portrait.
4. Price one kind "take" per shot at the seconds `pps_plan_ad` gave, each take with `prompt` set to
   that beat's shotPrompt word for word (the script is rewritten into slates, so the prompt is what
   carries the checked camera move and action) with audio left ON, the default (the clip's own sound
   plays under the music; never `audio: false` unless the person explicitly asked for silent clips,
   because a silent clip is credits spent on footage they cannot use anywhere else), plus the music (`musicTempo` on the blueprint matches the tempo word in the music prompt)
   and one
   voiceover take for the whole ad, in ONE `pps_quote_batch` (more than 12 items go in a second
   batch); after approval follow the set with `pps_wait_jobs`.
5. Render with `pps_render_ad` (free), each finished take's video id as that beat's
   clipVideoId; follow with `pps_wait_job`, and hand over the Save link.

## Optional: render locally

Rendering on PPS is the default and needs nothing installed. To iterate on the composition itself:

1. Unzip this skill; `packages/remotion-kit` is inside it. `cd packages/remotion-kit && npm install`.
2. Save each finished asset with `pps_get_download` and put its URL into a copy of
   `src/fixtures/ad-15.json` (clipUrl, musicUrl, voiceoverUrl, logoUrl) with your blueprint's beats.
3. `npx remotion render src/index.ts AdComposition out/ad.mp4 --props=<your json>`.
   `npx remotion studio src/index.ts` previews it live.
4. A blueprint edited locally still renders on PPS: hand it back to `pps_render_ad` with the asset ids.

Never roll again, re-render or re-price anything the person did not ask for.
