---
name: make-ugc-video-ad
description: Make a UGC-style video ad in which a creator talks to camera about the user's product. Use when the user asks for a UGC ad, a creator or influencer-style video, a testimonial, review, unboxing or tutorial video with a person in it, or wants the same AI creator to star in several of their ads.
---

# Make a UGC video ad

Use this skill to turn "make a UGC ad for my product" into a finished vertical video with a person talking about
the product. Explicit instructions from the user always take priority over this skill, including the length,
format, script, person and wording they name.

## Before you start
- Hermoso reads the saved brand profile by itself. Call `get_brand` only if you do not know whether one is saved.
  If none is saved and the user gives a website, call `draft_brand` with it first.
- You need the product, the angle (a problem it solves, a review, an unboxing, a how-to) and the length. Ask one
  short question for anything missing that matters; if the user says "you choose", pick and say what you picked.
  UGC ads run vertical (9:16) unless the user says otherwise.

## Pick the person
1. Call `list_creators`. If the workspace has saved creators, offer them by name: the same face in every ad builds
   recognition and costs less than casting someone new.
2. If there are none, the render casts a new person. After a render the user likes, offer to keep that person
   with `save_creator` (source "generated"). A real person's photo is used only when the user says it is them or
   that they have that person's consent.

## Make it
1. Call `plan_ad` with the product, the UGC format, the angle and the length in seconds. Show the hook and the
   script in a few lines and let the user change them.
2. Call `render_ad` with the plan's full output as `creative`, plus `creator` when one was chosen. Keep the length
   the user asked for; never shorten it.
3. Renders take a few minutes. When the tool returns a job id, call `get_job` with it until it reports done or
   error. Do not start the render again while it runs: that would charge twice.

## After the video is ready
Show it with one line on what it is, then offer one next step: new opening hooks with `hook_variants`, or more
versions with a different person or place with `multiply_ad`.

## Credits
Rendering uses credits from the user's Hermoso account, and the tool reply says how many. If the balance is too
low, say so; credits are managed in the user's Hermoso account. Never start a purchase.

## Do not
- Do not add captions, music or an end card unless the user asks for them.
- Do not use a real person's face or voice without their consent statement.
- Do not make a talking still photo (`generate_avatar`) unless the user asks for that look by name.
