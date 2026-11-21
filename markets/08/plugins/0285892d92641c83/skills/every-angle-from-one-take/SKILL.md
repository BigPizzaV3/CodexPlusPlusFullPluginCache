---
name: every-angle-from-one-take
description: Use this when someone has one steady video take, filmed from a single fixed camera, and wants it as other camera angles, such as a close up, a wide, a top down view or a slow push in, all in sync over the original sound, or wants a highlight edit that cuts between angles. Trigger on multicam, more angles, coverage, another angle of this, make it look like it was shot with several cameras. Do not use it to change what happens in a clip or to change its look.
---

# Every angle from one take

Multicam turns one steady take into the camera angles the person picks, each one a clip as long as the take and in sync over its own sound, plus a highlight edit that cuts between them.

## When to trigger

Trigger on "give me more angles of this", "make this look like a multicam shoot", "I only had one camera", "can I get a close up of this take", "cut a highlight between angles".

Do not trigger when the person wants the action, the subject or the setting changed (use remake-a-clip), only the look changed (use grade-my-footage), or a new shot made from a brief (use make-a-video).

## Ask for this first

Ask once, bundled:

1. Which take: a clip already in their NOLGIA library, or one they will add there first. It must be one fixed camera and at most 2 minutes long.
2. What it is for, if they want a ready-made set: a music video, scene coverage, an ad, a fashion film, a performance or dance, or an interview.
3. Any angle they already know they want, in their own words if it is not a standard one.

## Steps

1. Find the take with `nolgia_list_assets` filtered to video. Where the host shows this server's cards, let the person point at it rather than reciting ids.
2. Call `nolgia_multicam_plan` with the take, plus the pack or angles they asked for. It is free and renders nothing. Where the host shows this server's cards the plan appears as a picker with the price, so do not read the angle list back; say in one sentence what the take is and what the plan suggests.
3. If they change their choice, call `nolgia_multicam_plan` again with the new choice so the price shown is the price they will pay.
4. Only when the person has chosen the angles and agreed to the price, call `nolgia_multicam_start` with exactly the same take, pack, angles, custom angles, quality and notes as the plan they agreed to. Never start a job they have not agreed to.
5. The job keeps running after the chat moves on. Check it with `nolgia_multicam_run` about every half minute while it is running, not in a tight loop, and tell the person roughly how long it takes.
6. When angles are finished, offer everything in one file with `nolgia_multicam_download`. Give the link exactly as returned.
7. If they ask to stop, call `nolgia_multicam_cancel` after confirming, and tell them what the result says about finished angles and credits.

## What to return

The finished angles and the highlight edit, each named by angle, and the one download link when they want the files together. Offer one next step: another angle, or the highlight edit cut to a different length in the NOLGIA editor.

Never name a model, and never promise a refund or a price the tool result does not show.

## When to stop or decline

- No take, or a take that moves the camera or cuts between shots: explain that Multicam needs one steady shot from a single camera and ask for one.
- A take longer than 2 minutes: ask them to trim it first.
- The plan hides an angle because there is no clear person in the take: say so plainly and offer the angles the plan does show.
- The balance does not cover the price: say so and stop; nothing starts.
