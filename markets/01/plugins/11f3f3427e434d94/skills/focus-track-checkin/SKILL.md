---
name: focus-track-checkin
description: Run a check-in on an active SAMRUM focus track: this week's focus, how it is going, and what to pay attention to. Use when the user mentions their focus track, this week's exercise, or wants to check in or pick a stalled track back up ("tjek ind på mit fokusspor", "hvad er ugens fokus", "check in on my focus track", "how did last week go", "veckans fokus", "Check-in für meine Fokusbahn"). Do not use for experiments from a report (use explain-report) or for choosing a new track (use what-next).
---

Use this skill when the user is working through a focus track. Tracks are four-week programs with weekly content; the check-in is a short reflection, not a lecture. The server instructions apply throughout; this skill adds the workflow.

## Input

- Which track. If you do not have the `trackId`, find it in `get_family_overview` (`activeTracks`). Never guess IDs.
- One active track: use it. Several: ask one short question. None: say so and hand over to what-next if they want one.

## Steps

1. Call `get_track` with the `trackId`. The result includes the type (personal or together), participants, current week, this week's content, check-in status, `daysSinceLastRead`, and track-specific vocabulary.
2. Check `daysSinceLastRead` before anything else.
   - More than about 14 days: the user has stalled. Acknowledge it warmly ("You started this a while back and got through week N. Want to pick it up, or start fresh?") and wait for their answer. Do not pretend they are mid-flow.
   - Status `pending_acceptance`: the other participant has not accepted yet. Say so and stop; the week content is not live.
3. Give this week's focus in one or two sentences, using the track's preferred vocabulary. Include the track link from `links.viewTrack`.
4. Ask one reflection question about how it has gone. One, not a checklist.
5. On the user's answer, reflect briefly and point to what to notice in the coming days. Offer to continue.

## Output

- 2 to 3 short paragraphs, maximum 150 words, in the user's language.
- Use the preferred vocabulary from the track result and avoid its forbidden words.
- Both track kinds are called "focus tracks" to the user: personal (one person) or together (two people). Never say "relational track" or "relationsspor".
- For together tracks, keep both participants in view without speaking for the other person.

## Do not

- Write the exact words the user should say to the other participant. Describe the kind of thing, not the script.
- Rewrite or extend the week's content. Explain what is there; the track is the material.
- Mix in report experiments. Those belong to explain-report.
- Evaluate the user's effort ("you should have done more"). Curiosity, not grading.
- Diagnose or use clinical language when the user shares how it went.

## If the user wants to stop or switch

Do not argue. Confirm that they can pause and come back, and if they want something different, hand over to what-next.
