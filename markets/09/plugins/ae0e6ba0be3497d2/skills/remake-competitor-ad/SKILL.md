---
name: remake-competitor-ad
description: Find a competitor's strongest ads and remake one for the user's own brand. Use when the user asks to copy, clone, remake or do their own version of a competitor's ad or of any ad, video or post they link to, or asks to see what a named competitor is running and then make something like the best one for their brand.
---

# Remake a competitor's ad for your brand

Use this skill to go from "what is my competitor running?" to an on-brand version of their strongest ad. The remake
keeps the structure, layout and pacing and swaps in the user's own product, brand and words; nothing of the other
brand stays in it. Explicit instructions from the user always take priority over this skill, including which ad to
remake and what to change.

## What you need from the user
- The competitor's name, and their website if the name is ambiguous.
- A saved brand of their own. Call `get_brand` first; if none is saved, ask for the website and set one up with
  `draft_brand` before remaking anything.

## Steps
1. Call `pull_competitor_ads` with the competitor's name (and `domain` if the user gave one). The ads come back
   sorted with the longest-running first; a long run is the usual sign an ad is working.
2. Show the top few with what each one does: the format, the opening hook, the offer and how long it has run. If
   the library returned no ads, say so plainly and suggest checking the spelling or the website; a brand can run no
   ads on Meta.
3. Optional, when the user wants the reasoning: call `competitor_teardown` with those ads for the hook mix, the
   themes and the gaps nobody in the set covers.
4. Ask the user which ad to remake, and what to change if anything.
5. Remake it:
   - An image ad: call `clone_static` with the ad's image link as `imageUrl`.
   - A video ad: call `plan_video_remake` with the ad's link as `url`, then pass its plan to `render_ad` as
     `creative`. Ask for a yes before rendering, since rendering uses credits.
   - A video takes a few minutes; call `get_job` until it is done, without asking the user to wait.
6. Show the original and the remake side by side with one line on what was kept and what was changed.

## Output
The chosen original, the finished remake with its link, and two next steps as plain sentences, for example "Make
two more hook variations" or "Schedule it for Friday".

## Do not
- Do not copy the competitor's logo, name, people, slogans or claims into the remake.
- Do not invent results for a competitor's ad. The ad library shows what ran and for how long, not its sales; say
  that when the user asks how well an ad did.
- Do not remake more than one ad unless the user asked for several.
